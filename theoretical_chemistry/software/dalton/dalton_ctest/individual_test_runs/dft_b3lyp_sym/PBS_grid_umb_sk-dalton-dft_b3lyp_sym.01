#!/bin/bash

#PBS -S /bin/bash
#PBS -A UMB-ITMS-26110230082
#PBS -N DalTest
### Declare myprogram non-rerunable
#PBS -r n

##PBS -l nodes=1:ppn=12:old
#PBS -l nodes=1:ppn=4

#PBS -l walltime=2:00:00

##PBS -l mem=47g
##PBS -l mem=32g
#PBS -l mem=12g  # 4x3gb=12gb

#PBS -j oe

#PBS -q batch
##PBS -q debug

#PBS -M Miroslav.Ilias@umb.sk

echo -e "\nWorking host is: \c"; hostname -f

# Intel 2013 compilers
source /mnt/apps/intel/bin/compilervars.sh intel64
# Intel MKL 2013 math library
source /mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/bin/mklvars.sh intel64
echo -e "\n Intel Fortran/C/C++ commercial compilers 2013 with MKL library 2013 activated, PROD_DIR=$PROD_DIR, MKLROOT=$MKLROOT.\n"

source /mnt/apps/pgi/environment.sh
export LD_LIBRARY_PATH=/home/milias/bin/lib64_libnuma:$LD_LIBRARY_PATH  # libnumma for PGI

# provide OpenMPI-Intel - local installation for DIRAC
export PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/bin:$PATH
export LD_LIBRARY_PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib:$LD_LIBRARY_PATH
export PMIX_MCA_gds=hash
echo -e "\n PATH, LD_LIBRARY_PATH, PMIX_MCA_gds initialized for /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++"

echo -e "\nMy PATH=$PATH"
echo -e "My LD_LIBRARY_PATH=$LD_LIBRARY_PATH"
echo -e "Running on host `hostname`"
echo -e "Date & Time is `date`"
echo -e "Current directory is, pwd= `pwd`"
echo -e "This jobs runs on the following processors: \c "
echo `cat $PBS_NODEFILE`

UNIQUE_NODES="`cat $PBS_NODEFILE | sort | uniq`"
UNIQUE_NODES="`echo $UNIQUE_NODES | sed s/\ /,/g `"
echo -e "\nUnique nodes for parallel run:  $UNIQUE_NODES"

# Extract number of processors
NPROCS_PBS=`wc -l < $PBS_NODEFILE`
NPROCS=`cat /proc/cpuinfo | grep processor | wc -l`
echo -e "This node has $NPROCS CPUs."
echo -e "This node has $NPROCS_PBS CPUs allocated for PBS calculations."

#echo "PBS_SERVER=$PBS_SERVER"
echo "PBS_NODEFILE=$PBS_NODEFILE"
echo "PBS_O_QUEUE=$PBS_O_QUEUE"
echo "PBS_O_WORKDIR=$PBS_O_WORKDIR"
#

#export MKL_NUM_THREADS=$NPROCS
#echo "MKL_NUM_THREADS=$MKL_NUM_THREADS"
#export MKL_DOMAIN_NUM_THREADS="MKL_BLAS=$NPROCS"

export OMP_NUM_THREADS=1
export MKL_DYNAMIC="FALSE"
export OMP_DYNAMIC="FALSE"
# set MKL envirovariables
unset MKL_NUM_THREADS
export MKL_NUM_THREADS=1
echo -e "\nUpdated MKL_NUM_THREADS=$MKL_NUM_THREADS"
echo -e "MKL_DYNAMIC=$MKL_DYNAMIC"
echo -e "OMP_NUM_THREADS=$OMP_NUM_THREADS"
echo -e "OMP_DYNAMIC=$OMP_DYNAMIC"

DALTON=/home/milias/Work/qch/software/dalton_suite/dalton_master
BUILD=build_intelmklpar_openmpi
echo -e "\nDalton executable linked libraries, ldd $DALTON/$BUILD/dalton.x:"
ldd $DALTON/$BUILD/dalton.x

echo -e "\nPython -V \c"; python -V
echo -e  "ctest ? \c";which ctest;ctest --version
echo -e "mpirun ? \c"; which mpirun; mpirun --version
echo -e "mpif90 ? \c"; which mpif90; mpif90 --version
echo -e "ifort ? \c"; which ifort; ifort --version
echo -e "mpicc ? \c"; which mpicc; mpicc --version
echo -e "icc ? \c"; which icc; icc --version
echo -e "mpicxx ? \c"; which mpicxx; mpicxx --version
echo -e "icpc ? \c"; which icpc; icpc --version
echo -e "g++ ? \c"; which g++; g++ --version

# set local scratch directory for your runs 
export DALTON_TMPDIR=/mnt/local/$USER/$PBS_JOBID
echo -e "\n Local scratch directory, DALTON_TMPDIR=$DALTON_TMPDIR "
echo -e "Size of scratch dir; df -h /mnt/local/$USER/ :\c";df -h /mnt/local/$USER/

#export DALTON_NUM_MPI_PROCS=$NPROCS_PBS 
export DALTON_LAUNCHER="mpirun -np $NPROCS_PBS"
echo -e "DALTON parallel run with DALTON_LAUNCHER=$DALTON_LAUNCHER"

cd $DALTON/$BUILD
echo -e "\n I am in $DALTON/$BUILD for ctest "
echo -e "Running ctest -VV -R dft_b3lyp_sym"
ctest -VV -R dft_b3lyp_sym

cd $PBS_O_WORKDIR
echo -e "\n Now I am in PBS_O_WORKDIR=$PBS_O_WORKDIR ; pwd=\c";pwd

echo -e "\n Running $DALTON/DALTON/test/dft_b3lyp_sym:"
#$DALTON/$BUILD/dalton  -noarch  $DALTON/DALTON/test/dft_b3lyp_sym/dft_b3lyp_sym.dal   $DALTON/DALTON/test/dft_b3lyp_sym/H2O_intgrl.mol # does not work

ln -sf  $DALTON/DALTON/test/dft_b3lyp_sym/dft_b3lyp_sym.dal  $PBS_O_WORKDIR/.
ln -sf  $DALTON/DALTON/test/dft_b3lyp_sym/H2O_intgrl.mol  $PBS_O_WORKDIR/.
$DALTON/$BUILD/dalton  -noarch  dft_b3lyp_sym  H2O_intgrl
/bin/rm dft_b3lyp_sym.dal
/bin/rm H2O_intgrl.mol

exit 0
