#!/bin/bash

echo -e "\n DIRAC run "
echo -e "\nRunning on host `hostname`"
echo -e "Time is `date` \n"

spack load intel-parallel-studio@professional.2020.1
spack load intel-mkl@2020.4.304
#spack load cmake@3.21.4 target=$(spack arch -t)
 
echo -e "\n loaded modules:"; spack find --loaded

#set up Intel-OpenMPI-i8
export PATH=/u/milias/bin/openmpi-i8/bin:$PATH
export LD_LIBRARY_PATH=/u/milias/bin/openmpi-i8/lib:$LD_LIBRARY_PATH

# CPU model, total numer of CPUs, number of allocated CPUs
echo -e "The node's CPU \c"; cat /proc/cpuinfo | grep 'model name' | uniq
NPROCS=`cat /proc/cpuinfo | grep processor | wc -l`
echo "This node has total $NPROCS CPUs available for EXCLUSIVE job."

echo -e "\n the memory at the node (in GB)"
free -t -g
echo -e "\n"

## set internal OpenMP parallelization for MKL - Slurm CPU count
#export MKL_NUM_THREADS=$SLURM_CPUS_ON_NODE
#export MKL_NUM_THREADS=24
#export MKL_NUM_THREADS=$NPROCS
#echo -e  "\nInternal MKL parallelization MKL_NUM_THREADS=$MKL_NUM_THREADS\n"
export OMP_NUM_THREADS=1
export MKL_DYNAMIC="FALSE"
export OMP_DYNAMIC="FALSE"

echo -e "\n ifort -V: \c"; 
which ifort; ifort --version
which icc; icc --version

#echo -e "\nMy PATH=$PATH\n"
echo -e "Python -v :\c"; python -V
echo -e "cmake ? which cmake = \c"; which cmake
echo -e "ctest ? which ctest = \c"; which ctest
echo -e "ctest --version \c"; ctest --version
echo -e "\n mpirun ? \c"; which mpirun; mpirun --version
which mpif90; mpif90 --version

#
export DIRAC=/data.local1/milias/software/dirac/dirac-public
export DIRACBIN=$DIRAC/build_intelompi_mklpar_i8
export PAM=$DIRACBIN/pam
export BASDIR=$DIRAC/basis_dalton:$DIRAC/basis:$DIRAC/basis_ecp
echo -e "DIRAC=$DIRAC"
echo -e "DIRACBIN=$DIRACBIN"
echo -e "\nldd $DIRAC/dirac.x:"
ldd $DIRACBIN/dirac.x

export DIRAC_TMPDIR=/data.local1/milias/scratch/
echo -e "\nDIRAC scratch directory space, $DIRAC_TMPDIR"
df -h $DIRAC_TMPDIR/.
echo -e "\n For comparison, /tmp local disk;  df -h /tmp/."; df -h /tmp
echo -e "\n"

#let "NUMTHR=$NPROCS/$THISMPI"
#export MKL_NUM_THREADS=$NUMTHR
export MKL_NUM_THREADS=1
#echo -e "\nThis node has $NPROCS CPUs available for this EXCLUSIVE JOB and dirac.x is running via $THISMPI threads."
#echo -e "Therefore, for the MKL internal parallelization, number of calculated threads=$MKL_NUM_THREADS \n"

# set MPI launcher
unset DIRAC_MPI_COMMAND
export DIRAC_MPI_COMMAND="mpirun -np 2"
echo -e "\n Set DIRAC_MPI_COMMAND=$DIRAC_MPI_COMMAND"

cd $DIRACBIN
#ctest -j8 -L short
ctest -R ecp


#$PAM --noarch --mpi=4  --gb=1.89 --ag=1.99 --mol=CO.mol  --inp=ccsd.small.inp  --suffix=$SLURM_JOB_PARTITION-$SLURM_JOBID-out 
#$PAM --help

exit
