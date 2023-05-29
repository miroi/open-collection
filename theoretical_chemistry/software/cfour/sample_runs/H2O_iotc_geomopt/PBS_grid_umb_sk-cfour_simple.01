#!/bin/bash

#PBS -S /bin/bash
#PBS -A UMB-ITMS-26110230082
#PBS -N C4h2o

### Declare myprogram non-rerunable
#PBS -r n

##PBS -l nodes=1:ppn=12:old
#PBS -l nodes=1:ppn=4

#PBS -l walltime=5:00:00

##PBS -l mem=47g # max mem
##PBS -l mem=24g  # 12x2gb=24gb
##PBS -l mem=20g  # 10x2gb=20gb
#PBS -l mem=4g

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

# provide proper OpenMPI-Intel installation 
export PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/bin:$PATH
export LD_LIBRARY_PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib:$LD_LIBRARY_PATH
export PMIX_MCA_gds=hash
echo -e "\nPATH,LD_LIBRARY_PATH,PMIX_MCA_gds updated for OpenMPI, /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++"

echo -e "\nMy PATH=$PATH"
echo -e "My LD_LIBRARY_PATH=$LD_LIBRARY_PATH"
echo -e "\nRunning on host `hostname`"
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

echo -e "\n The memory at the node (in GB)"
free -t -g
echo

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

#DALTON=/home/milias/Work/qch/software/dalton_suite/dalton_master
#BUILD=build_intelmklpar_openmpi
#echo -e "\nDalton executable linked libraries, ldd $DALTON/$BUILD/dalton.x:"
#ldd $DALTON/$BUILD/dalton.x

#CFOUR=/home/milias/Work/qch/software/cfour/cfour-public-master-4567f08b44f7f255929f07cb843baf9a89d5c048
CFOUR=/home/milias/Work/qch/software/cfour/cfour-public_openmpi_intel_g++_mkl_i8
export PATH=$CFOUR/bin:$PATH

echo -e "\nCFOUR binaries in PATH, $CFOUR/bin:"; ls -lt $CFOUR/bin

echo -e "\nPython -V \c"; python -V
echo -e "mpif90 ? \c"; which mpif90; mpif90 --version
echo -e "mpicc ? \c"; which mpicc; mpicc --version
echo -e "mpicxx ? \c"; which mpicxx; mpicxx --version
echo -e "mpirun ? \c"; which mpirun; mpirun --version

export CFOUR_NUM_CORES=$NPROCS_PBS
echo -e "\n CFOUR_NUM_CORES=$CFOUR_NUM_CORES"

workdir=/mnt/local/$USER/$PBS_JOBID
mkdir $workdir
echo -e "\n Local scratch directory, workdir=$workdir";
echo -e "Size of local scratch dir, df -h $workdir:"; df -h $workdir

cd $workdir

### Link all files into scratch directory
ln -sf $CFOUR/basis/GENBAS .
#ln -sf $CFOUR/bin/x*       .
ln -sf $PBS_O_WORKDIR/ZMAT .
echo -e "\n I am in pwd=$PWD ; input files are linked, ls -lt:"; ls -lt
echo -e "\n Going to launch xcfour !!!! \n"
xcfour

echo -e "\n After the job, in pwd=$PWD see the content; ls -lt:"; ls -lt; du -h -s .

cd $PBS_O_WORKDIR
echo -e "\n...returning to homedir, PBS_O_WORKDIR=$PBS_O_WORKDIR"

echo -e "\ncontent of $workdir"
ls -lt  $workdir

echo -e "...deleting the $workdir"
/bin/rm -r $workdir

echo -e "\n remaining content of scratch.../mnt/local/$USER/"; hostname -f; ls -lt /mnt/local/$USER/

exit 0

