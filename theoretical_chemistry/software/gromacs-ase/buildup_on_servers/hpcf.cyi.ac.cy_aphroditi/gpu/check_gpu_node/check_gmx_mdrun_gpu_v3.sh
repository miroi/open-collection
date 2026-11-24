#!/bin/bash -l
#SBATCH -A p326
#SBATCH --job-name=GMX_mdrun_chk
#SBATCH --partition=rtx
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:1
#SBATCH --time=0:30:00
#SBATCH -o log_gmx_mdrun_check.%j.%N.std_out

# Real mdrun check of the gmx_mpi + CUDA build, no input files needed:
# builds a ~7 nm SPC/E water box (~34k atoms) and runs 2000 steps in several modes:
#   A1 1 rank, nonbonded+PME on GPU (baseline);  A2 same + update on GPU
#   B  4 ranks (3 PP + 1 PME), direct GPU communication DISABLED (GMX_DISABLE_DIRECT_GPU_COMM=1,
#      i.e. real host staging of halo/PME data)
#   C  4 ranks, GROMACS default = direct GPU communication (GPU-aware MPI) ON
#   D  (optional, RUN_UCX_CONTROL=1) like C but with UCX instead of ob1: expected to crash
#   E  (optional, RUN_UCX_CONTROL=1) like B but with UCX: does disabling direct GPU comm alone
#      avoid the UCX crash?
# All ranks share the single GPU in B-E, so expect them to be much slower than A1/A2.
# Everything goes to stdout; the scratch dir is removed at the end.
#
# Usage: sbatch check_gmx_mdrun_gpu_v3.sh
#        RUN_UCX_CONTROL=1 sbatch --export=ALL check_gmx_mdrun_gpu_v3.sh

INSTALL_DIR=${INSTALL_DIR:-/nvme/h/ru26mi1/work/software/gromacs/install_build-gpu_cuda_mpi}
NSTEPS=${NSTEPS:-2000}
BOX=${BOX:-7}
RUN_UCX_CONTROL=${RUN_UCX_CONTROL:-0}

module purge
module load Python CMake
module load GCC OpenMPI CUDA imkl
source "$INSTALL_DIR/bin/GMXRC" || { echo "GMXRC not found in $INSTALL_DIR"; exit 1; }

# UCX in this stack has no CUDA support -> bypass it (CUDA IPC via smcuda inside the node)
export OMPI_MCA_pml=ob1
export OMPI_MCA_btl=self,smcuda,tcp

WORK=${SLURM_TMPDIR:-/tmp}/gmx_mdrun_check_$$
mkdir -p "$WORK" && cd "$WORK" || exit 1
declare -A VERDICT PERF

echo "== Environment"
hostname; date
nvidia-smi --query-gpu=name,compute_cap,driver_version --format=csv
which gmx_mpi mpirun
gmx_mpi --version 2>&1 | grep -E "GROMACS version|GPU support|MPI library|SIMD|CUDA targets"
echo "OMPI_MCA_pml=$OMPI_MCA_pml  OMPI_MCA_btl=$OMPI_MCA_btl"

# ---------------------------------------------------------------- input
echo; echo "== Building test system (${BOX} nm SPC/E water box)"
cat > topol.top << 'EOF'
#include "oplsaa.ff/forcefield.itp"
#include "oplsaa.ff/spce.itp"
[ system ]
water
[ molecules ]
EOF
cat > md.mdp << EOF
integrator     = md
dt             = 0.002
nsteps         = ${NSTEPS}
cutoff-scheme  = Verlet
coulombtype    = PME
rcoulomb       = 1.0
rvdw           = 1.0
constraints    = h-bonds
tcoupl         = v-rescale
tc-grps        = System
tau-t          = 0.1
ref-t          = 300
gen-vel        = yes
gen-temp       = 300
gen-seed       = 12345
nstcalcenergy  = 100
nstenergy      = 100
nstlog         = 500
EOF
mpirun -np 1 gmx_mpi solvate -cs spc216.gro -box $BOX $BOX $BOX -o water.gro -p topol.top > solvate.out 2>&1 \
    || { cat solvate.out; exit 1; }
tail -3 topol.top
mpirun -np 1 gmx_mpi grompp -f md.mdp -c water.gro -p topol.top -o md.tpr -maxwarn 1 > grompp.out 2>&1 \
    || { cat grompp.out; exit 1; }
grep -a -E "atoms|System has non-zero|WARNING" grompp.out | head -5

# ---------------------------------------------------------------- cases
# run_case NAME NRANKS ; uses arrays CASE_ENV (env settings) and MDRUN_ARGS
run_case() {
    local name="$1" np="$2"
    local d="$WORK/$name"; mkdir -p "$d"; cd "$d" || return
    echo; echo "------------------------------------------------------------"
    echo "--- CASE $name: $np rank(s)  env: ${CASE_ENV[*]:-none}  mdrun: ${MDRUN_ARGS[*]}"
    timeout 600 env X_DUMMY=1 "${CASE_ENV[@]}" \
        mpirun --bind-to none -np "$np" gmx_mpi mdrun -s ../md.tpr -deffnm md -pin off "${MDRUN_ARGS[@]}" > mdrun.out 2>&1
    local rc=$?
    echo "  mdrun exit code: $rc   (139 = segfault, 134 = abort, 124 = timeout)"
    if [ -f md.log ]; then
        echo "  --- GPU / communication lines from md.log"
        grep -a -i -E "GPU-aware|direct GPU|GPU halo|halo exchange|PME tasks|PME.*GPU|Mapping of GPU|will use [0-9]+ GPU|tasks will be" md.log | sort -u | head -8
        grep -a -E "^ *Performance:" md.log
        PERF[$name]=$(grep -a -E "^ *Performance:" md.log | awk '{print $2}')
        local fin; grep -a -q "Finished mdrun" md.log && fin=yes || fin=no
        local nan; nan=$(grep -a -c -i -w "nan" md.log)
        echo "  finished: $fin   'nan' lines in md.log: $nan"
        if [ -f md.edr ]; then
            echo "  --- average potential energy (kJ/mol)"
            echo "Potential" | mpirun -np 1 gmx_mpi energy -f md.edr 2>&1 | grep -a -E "^Potential"
        fi
        if [ "$rc" = 0 ] && [ "$fin" = yes ] && [ "$nan" = 0 ]; then VERDICT[$name]=PASS; else VERDICT[$name]="FAIL (rc=$rc)"; fi
    else
        VERDICT[$name]="FAIL (rc=$rc, no md.log)"
    fi
    if [ "${VERDICT[$name]}" != PASS ]; then
        echo "  --- GROMACS error message (from mdrun.out)"
        if grep -a -q "^Fatal error" mdrun.out; then
            grep -a -B9 -A10 "^Fatal error" mdrun.out | head -45 | cut -c1-200
        else
            echo "  (no 'Fatal error' block; first lines of mdrun.out without MPI stack frames)"
            grep -a -v -E "^\[.*\] \[ *[0-9]+\] |^$" mdrun.out | head -40 | cut -c1-200
        fi
        echo "  --- last lines of md.log"
        tail -8 md.log 2>/dev/null | cut -c1-200
    fi
    cd "$WORK"
}

CASE_ENV=();  MDRUN_ARGS=(-ntomp 8 -nb gpu -pme gpu)
run_case A1_1rank_nb_pme_gpu 1

CASE_ENV=();  MDRUN_ARGS=(-ntomp 8 -nb gpu -pme gpu -update gpu)
run_case A2_1rank_plus_update_gpu 1

CASE_ENV=(GMX_DISABLE_DIRECT_GPU_COMM=1);  MDRUN_ARGS=(-ntomp 2 -nb gpu -pme gpu -npme 1)
run_case B_4ranks_no_direct_gpu_comm 4

CASE_ENV=();  MDRUN_ARGS=(-ntomp 2 -nb gpu -pme gpu -npme 1)
run_case C_4ranks_direct_gpu_comm_default 4

if [ "$RUN_UCX_CONTROL" = 1 ]; then
    echo; echo "(controls: ob1 settings unset so OpenMPI falls back to UCX, which has no CUDA support)"
    unset OMPI_MCA_pml OMPI_MCA_btl
    CASE_ENV=();  MDRUN_ARGS=(-ntomp 2 -nb gpu -pme gpu -npme 1)
    run_case D_UCX_direct_gpu_comm_default 4
    CASE_ENV=(GMX_DISABLE_DIRECT_GPU_COMM=1);  MDRUN_ARGS=(-ntomp 2 -nb gpu -pme gpu -npme 1)
    run_case E_UCX_no_direct_gpu_comm 4
    export OMPI_MCA_pml=ob1 OMPI_MCA_btl=self,smcuda,tcp
fi

# ---------------------------------------------------------------- summary
echo; echo "=================================================================="
echo "== SUMMARY"
echo "=================================================================="
printf "%-42s %-14s %s\n" "case" "result" "speed"
for k in "${!VERDICT[@]}"; do printf "%-42s %-14s %s\n" "$k" "${VERDICT[$k]}" "${PERF[$k]:+${PERF[$k]} ns/day}"; done | sort
cat << 'EOF'

How to read this:
  * A1/A2 pass                -> the GPU build itself works.
  * B and C pass              -> multi-rank GPU runs work with ob1+smcuda, with and without direct
                                 GPU communication. Keep the two OMPI_MCA exports in production.
  * C fails, B passes         -> keep GMX_DISABLE_DIRECT_GPU_COMM=1 in multi-rank jobs.
  * D fails, E passes         -> with UCX (no CUDA) disabling direct GPU comm alone is enough; the
                                 ob1 exports would then not be needed for multi-rank runs.
  * D and E both fail         -> UCX is unusable for GPU runs here; keep the ob1 exports.
  * Average potential energies of the cases should agree within the error estimate.
  * Compare the ns/day column: several ranks sharing ONE GPU are normally much slower than one rank
    (earlier run: ~1550 vs ~80 ns/day). Use 1 rank per GPU; more ranks only with more GPUs.
EOF

cd /; rm -rf "$WORK"
failed=0; for k in "${!VERDICT[@]}"; do case $k in D_*|E_*) ;; *) [ "${VERDICT[$k]}" = PASS ] || failed=1;; esac; done
exit $failed
