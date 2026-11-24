#!/bin/bash -l
#SBATCH -A p326
#SBATCH --job-name=UCX_CUDA_chk
#SBATCH --partition=rtx
#SBATCH --nodes=1
#SBATCH --ntasks=2               # the MPI tests below use 2 ranks
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:1
#SBATCH --time=0:20:00
#SBATCH -o log_ucx_cuda_check.%j.%N.std_out

# Diagnoses whether UCX / OpenMPI can move GPU (device) memory through MPI.
# Everything goes to stdout. No 'set -e': every check must run even if one fails.
#
# Usage:
#   sbatch check_ucx_cuda.sh
#   EXTRA_MODULES="UCX-CUDA/<version>" sbatch --export=ALL check_ucx_cuda.sh
#       (loads additional/alternative modules after the default set, to test them)
#   GMX_BUILD=/path/to/gromacs/build-dir  (optional: also runs GROMACS' own
#       gpu_utils-mpi-test, the test that crashed, under each MPI configuration)

GMX_BUILD=${GMX_BUILD:-/nvme/h/ru26mi1/work/software/gromacs/gromacs_cloned/build-gpu_cuda_mpi}
WORKDIR=${SLURM_TMPDIR:-/tmp}/ucx_cuda_check_$$
mkdir -p "$WORKDIR" && cd "$WORKDIR" || exit 1

section() { echo; echo "=================================================================="; echo "== $*"; echo "=================================================================="; }
declare -A VERDICT

# ------------------------------------------------------------------ modules
section "Modules"
module purge
module load Python CMake
module load GCC OpenMPI CUDA imkl
if [ -n "${EXTRA_MODULES:-}" ]; then
    echo "Loading EXTRA_MODULES: $EXTRA_MODULES"
    module load $EXTRA_MODULES
fi
module list 2>&1

section "Which CUDA-enabled UCX modules exist on this cluster?"
for pat in UCX-CUDA UCX gdrcopy; do
    echo "--- module avail $pat"
    module avail "$pat" 2>&1 | grep -v '^$' | head -20
done
echo "--- module spider UCX-CUDA (Lmod only)"
module spider UCX-CUDA 2>&1 | head -30

# ------------------------------------------------------------------ node / GPU
section "Node and GPU"
hostname; date
nvidia-smi
echo "--- topology"
nvidia-smi topo -m 2>&1
echo "--- kernel modules relevant for GPUDirect (empty is OK, just informative)"
lsmod 2>/dev/null | grep -i -E "nvidia_peermem|nv_peer_mem|gdrdrv|nvidia_uvm" || echo "(none listed / lsmod unavailable)"
echo "--- environment"
env | grep -E '^(UCX|OMPI|PRTE|PMIX|CUDA|EBROOTUCX|EBROOTOPENMPI|EBROOTCUDA)' | sort

# ------------------------------------------------------------------ UCX
section "UCX installation"
UCX_INFO=$(command -v ucx_info)
echo "ucx_info: ${UCX_INFO:-NOT FOUND}"
if [ -n "$UCX_INFO" ]; then
    ucx_info -v
    echo
    echo "--- configure line (look for --with-cuda / --with-gdrcopy)"
    ucx_info -v | grep -i "configured with"
    if ucx_info -v | grep -i "configured with" | grep -q -i -- "with-cuda"; then
        VERDICT[ucx_configured_with_cuda]="YES"
    else
        VERDICT[ucx_configured_with_cuda]="NO"
    fi

    echo
    echo "--- UCX plugin libraries (libuct_cuda*.so must exist for CUDA support)"
    UCXLIBDIRS=$(ls -d ${EBROOTUCX:-/nonexistent}/lib*/ucx 2>/dev/null)
    echo "UCX plugin dirs: ${UCXLIBDIRS:-none found}"
    for d in $UCXLIBDIRS; do ls -l "$d" | grep -i -E "cuda|gdr|ze|rocm" ; done
    if ls ${EBROOTUCX:-/nonexistent}/lib*/ucx/libuct_cuda* >/dev/null 2>&1; then
        VERDICT[uct_cuda_plugin_present]="YES"
        for f in ${EBROOTUCX}/lib*/ucx/libuct_cuda.so*; do echo "--- ldd $f"; ldd "$f" 2>&1 | grep -i -E "cuda|not found"; done
    else
        VERDICT[uct_cuda_plugin_present]="NO"
    fi

    echo
    echo "--- transports and memory domains seen on this node"
    ucx_info -d | grep -E "Transport:|Memory domain:" | sort | uniq -c
    for t in cuda_copy cuda_ipc gdr_copy; do
        if ucx_info -d | grep -q -E "Transport: +$t"; then VERDICT[transport_$t]="YES"; else VERDICT[transport_$t]="NO"; fi
    done
    echo
    echo "--- all CUDA-related lines from ucx_info -d"
    ucx_info -d | grep -i -E "cuda|gdr" | head -40
else
    VERDICT[ucx_configured_with_cuda]="UNKNOWN (no ucx_info)"
fi

# ------------------------------------------------------------------ OpenMPI
section "OpenMPI"
which mpicc mpicxx mpirun ompi_info
ompi_info | head -12
echo "--- CUDA support flag"
ompi_info --parsable --all | grep -E "mpi_built_with_cuda_support:value"
echo "--- PML / BTL components (ucx pml and smcuda btl)"
ompi_info | grep -i -E "MCA pml|MCA btl|MCA accelerator|MCA opal.*cuda"
echo "--- UCX/CUDA related parameters"
ompi_info --all 2>/dev/null | grep -i -E "ucx.*(cuda|tls|devices)|accelerator" | head -20

# ------------------------------------------------------------------ functional test
section "Functional test: MPI send/recv of GPU memory, 2 ranks"
cat > mpi_cuda_test.cu << 'EOF'
#include <mpi.h>
#include <mpi-ext.h>
#include <cuda_runtime.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CK(x) do { cudaError_t e = (x); if (e != cudaSuccess) { \
    printf("CUDA error %s at line %d\n", cudaGetErrorString(e), __LINE__); fflush(stdout); MPI_Abort(MPI_COMM_WORLD, 2);} } while (0)

// mode 0: device -> device ; mode 1: pageable host -> device (as in GROMACS GpuUtilsMpiTests)
static int run(int rank, int n, int mode)
{
    size_t bytes = (size_t)n * sizeof(float);
    float *h = (float*)malloc(bytes), *d = nullptr;
    CK(cudaMalloc((void**)&d, bytes));
    int bad = 0;
    if (rank == 0) {
        for (int i = 0; i < n; i++) h[i] = 0.5f * i + 1.0f;
        float *src = h;
        if (mode == 0) { CK(cudaMemcpy(d, h, bytes, cudaMemcpyHostToDevice)); src = d; }
        printf("  [mode %d] n=%-8d sending...\n", mode, n); fflush(stdout);
        MPI_Send(src, n, MPI_FLOAT, 1, 7, MPI_COMM_WORLD);
    } else {
        CK(cudaMemset(d, 0, bytes));
        MPI_Recv(d, n, MPI_FLOAT, 0, 7, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        CK(cudaMemcpy(h, d, bytes, cudaMemcpyDeviceToHost));
        for (int i = 0; i < n; i++) if (h[i] != 0.5f * i + 1.0f) { bad++; }
        printf("  [mode %d] n=%-8d received: %s (%d mismatches)\n", mode, n, bad ? "MISMATCH" : "OK", bad); fflush(stdout);
    }
    cudaFree(d); free(h);
    return bad;
}

int main(int argc, char** argv)
{
    MPI_Init(&argc, &argv);
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (size != 2) { if (!rank) printf("need exactly 2 ranks\n"); MPI_Finalize(); return 3; }
    CK(cudaSetDevice(0));
    if (rank == 0) {
#if defined(MPIX_CUDA_AWARE_SUPPORT)
        printf("  MPIX_CUDA_AWARE_SUPPORT=%d, MPIX_Query_cuda_support()=%d\n", MPIX_CUDA_AWARE_SUPPORT, MPIX_Query_cuda_support());
#else
        printf("  MPIX_CUDA_AWARE_SUPPORT not defined in this MPI\n");
#endif
        fflush(stdout);
    }
    int sizes[] = {1, 256, 1 << 16, 1 << 22};   // eager and rendezvous protocols
    int total_bad = 0;
    for (int mode = 0; mode < 2; mode++)
        for (int k = 0; k < 4; k++) {
            total_bad += run(rank, sizes[k], mode);
            MPI_Barrier(MPI_COMM_WORLD);
        }
    if (rank == 1) printf("  RESULT: %s\n", total_bad ? "FAILED" : "ALL TRANSFERS OK");
    MPI_Finalize();
    return total_bad ? 1 : 0;
}
EOF

BUILD_OK=0
if nvcc -O1 -ccbin mpicxx -o mpi_cuda_test mpi_cuda_test.cu 2>build.err; then
    BUILD_OK=1
else
    echo "nvcc -ccbin mpicxx failed, trying explicit MPI flags:"; cat build.err
    if nvcc -O1 $(mpicxx --showme:compile | sed 's/-pthread//') -o mpi_cuda_test mpi_cuda_test.cu \
           $(mpicxx --showme:link | sed 's/-pthread//') 2>build.err; then BUILD_OK=1; else cat build.err; fi
fi
echo "test program built: $BUILD_OK"

# run_case NAME VAR=val ...   (runs the 2-rank test and optionally the GROMACS gpu test)
run_case() {
    local name="$1"; shift
    echo; echo "--- CASE: $name   [$*]"
    timeout 120 env MPI_DUMMY=1 "$@" mpirun -np 2 ./mpi_cuda_test 2>&1 | grep -v -E "^\[.*\] \[ *[0-9]+\] " | head -40
    local rc=${PIPESTATUS[0]}
    echo "  exit code: $rc   (139 / signal 11 = segmentation fault, 124 = timeout)"
    VERDICT["case: $name"]=$([ "$rc" = 0 ] && echo "PASS" || echo "FAIL (rc=$rc)")

    if [ -x "$GMX_BUILD/bin/gpu_utils-mpi-test" ]; then
        echo "  -- GROMACS gpu_utils-mpi-test under the same settings"
        timeout 120 env GTEST_COLOR=no "$@" mpirun -np 2 "$GMX_BUILD/bin/gpu_utils-mpi-test" 2>&1 \
            | grep -a -E "PASSED|FAILED|Segmentation|Signal:" | head -6
        local rc2=${PIPESTATUS[0]}
        echo "  gpu_utils-mpi-test exit code: $rc2"
        VERDICT["gmx gpu_utils-mpi-test: $name"]=$([ "$rc2" = 0 ] && echo "PASS" || echo "FAIL (rc=$rc2)")
    fi
}

if [ "$BUILD_OK" = 1 ]; then
    run_case "default (OpenMPI chooses; this is what GROMACS tests used)" X_NONE=1
    run_case "UCX with explicit CUDA transports"  UCX_TLS=self,sm,cuda_copy,cuda_ipc
    run_case "UCX host-only transports (expected to FAIL if UCX lacks CUDA)" UCX_TLS=self,sm
    run_case "bypass UCX: pml=ob1 + smcuda btl"   OMPI_MCA_pml=ob1 OMPI_MCA_btl=self,smcuda,tcp
    run_case "GROMACS side switch: GPU-aware MPI disabled (host staging)" GMX_DISABLE_GPU_AWARE_MPI=1
fi

# ------------------------------------------------------------------ summary
section "SUMMARY"
for k in "${!VERDICT[@]}"; do printf "%-70s %s\n" "$k" "${VERDICT[$k]}"; done | sort
cat << 'EOF'

How to read this:
  * ucx_configured_with_cuda = NO, uct_cuda_plugin_present = NO, no cuda_copy transport
        -> this UCX cannot handle GPU memory: ask for / load a UCX-CUDA module
           (see 'module avail UCX-CUDA' above), then rebuild nothing, just load it
           together with OpenMPI and re-run this script via EXTRA_MODULES.
  * the 'default' case FAILS but 'bypass UCX' PASSES
        -> run GROMACS with OMPI_MCA_pml=ob1 OMPI_MCA_btl=self,smcuda,tcp
  * only the 'GPU-aware MPI disabled' case works for the GROMACS test
        -> GPU-aware MPI is unusable here; run multi-rank jobs with that variable
           set (verify the variable name in the GROMACS docs for your version),
           or use a thread-MPI build on a single node.
  * default case PASSES
        -> UCX is fine; the GROMACS crashes then need a closer look (send me the log).
EOF

cd /; rm -rf "$WORKDIR"
exit 0
