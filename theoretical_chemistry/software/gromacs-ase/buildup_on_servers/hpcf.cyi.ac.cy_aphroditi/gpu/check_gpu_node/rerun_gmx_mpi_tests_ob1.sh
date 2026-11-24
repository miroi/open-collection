#!/bin/bash -l
#SBATCH -A p326
#SBATCH --job-name=GMX_mpitests
#SBATCH --partition=rtx
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:1
#SBATCH --time=0:20:00
#SBATCH -o log_gmx_mpitests.%j.%N.std_out

# Re-runs the 6 GROMACS tests that crashed with UCX (no CUDA support), this time
# with OpenMPI's ob1 PML + smcuda BTL (CUDA IPC inside the node), bypassing UCX.
# Does not rebuild anything. Output goes to stdout.

module purge
module load Python CMake
module load GCC OpenMPI CUDA imkl

GMX_BUILD=${GMX_BUILD:-/nvme/h/ru26mi1/work/software/gromacs/gromacs_cloned/build-gpu_cuda_mpi}
cd "$GMX_BUILD" || exit 1

export OMPI_MCA_pml=ob1
export OMPI_MCA_btl=self,smcuda,tcp
export GTEST_COLOR=no

echo "OMPI_MCA_pml=$OMPI_MCA_pml  OMPI_MCA_btl=$OMPI_MCA_btl"
ctest -j 1 --output-on-failure \
      -R "DomDecMpiTests|GpuUtilsMpiTests|MdrunMpiTests|MdrunMultiSimTests|MdrunCoordinationBasicTests2Ranks|MdrunVirtualSiteTests"
rc=$?
echo "ctest exit status: $rc"
exit $rc
