#!/bin/bash

#PBS -S /bin/bash
#PBS -A UMB-ITMS-26110230082
#PBS -N VXnw

### Declare myprogram non-rerunable
#PBS -r n

##PBS -l nodes=1:ppn=12:old
##PBS -l nodes=1:ppn=32
#PBS -l nodes=1:ppn=8

##PBS -l walltime=100:00:00
#PBS -l walltime=24:00:00

##PBS -l mem=47g # max mem
##PBS -l mem=36g  # 12x3gb=36gb
##PBS -l mem=32g
#PBS -l mem=24g

#PBS -j oe

#PBS -q batch
##PBS -q debug

#PBS -M emacusova@studenti.umb.sk

echo -e "\nWorking host is: \c"; hostname -f

# Intel 2013 compilers
source /mnt/apps/intel/bin/compilervars.sh intel64
# Intel MKL 2013 math library
source /mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/bin/mklvars.sh intel64
echo -e "\n Intel Fortran/C/C++ commercial compilers 2013 with MKL library 2013 activated, PROD_DIR=$PROD_DIR, MKLROOT=$MKLROOT.\n"

source /mnt/apps/pgi/environment.sh
export LD_LIBRARY_PATH=/home/milias/bin/lib64_libnuma:$LD_LIBRARY_PATH  # libnumma for PGI

# provide OpenMPI-Intel local installation 
export PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/bin:$PATH
export LD_LIBRARY_PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib:$LD_LIBRARY_PATH
export PMIX_MCA_gds=hash
echo -e "PATH, LD_LIBRARY_PATH and PMIX_MCA_gds adjusted for /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++"

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
#DIRAC=/home/milias/Work/qch/software/dirac/dirac_production
#BUILD=build_openmpi_intel14_mkl_i8
export NWCHEM_EXECUTABLE=/home/milias/Work/qch/software/nwchem_suite/nwchem_master/bin/LINUX64/nwchem
echo -e "\nDIRAC executable linked libraries, ldd $NWCHEM_EXECUTABLE"
ldd $NWCHEM_EXECUTABLE

echo -e "\npython -V \c"; python -V
echo -e "mpif90 ? \c"; which mpif90; mpif90 --version
echo -e "mpicc ? \c"; which mpicc; mpicc --version
echo -e "mpirun ? \c"; which mpirun; mpirun --version
#echo -e "ctest ? \c";which ctest;ctest --version

### set local scratch directory for run
export TMPDIR=/mnt/local/$USER/$PBS_JOBID
echo -e "\n Local scratch directory, TMPDIR=$TMPDIR";
echo -e "Size of local scratch dir, df -h /mnt/local/$USER/:";df -h /mnt/local/$USER

mkdir $TMPDIR
cd $TMPDIR
echo -e "\nI am in TMPDIR=$TMPDIR"
echo -e "For control pwd=\c";pwd
echo -e "The local home directory with NWChem input file, PBS_O_WORKDIR=$PBS_O_WORKDIR"

#mpirun -np $NPROCS_PBS  $NWCHEM_EXECUTABLE  $PBS_O_WORKDIR/N2.scf_geomopt_sto2g.nw  > $PBS_O_WORKDIR/N2.scf_geomopt_sto2g.out
#mpirun -np $NPROCS_PBS  $NWCHEM_EXECUTABLE  $PBS_O_WORKDIR/N2.scf_geomopt.nw  > $PBS_O_WORKDIR/N2.scf_geomopt.out
#mpirun -np $NPROCS_PBS  $NWCHEM_EXECUTABLE  $PBS_O_WORKDIR/GB-conf36.nw  > $PBS_O_WORKDIR/GB-conf36.out
mpirun -np $NPROCS_PBS  $NWCHEM_EXECUTABLE  $PBS_O_WORKDIR/VX.b3lyp_3-21G_geopt_shield.nw  > $PBS_O_WORKDIR/VX.b3lyp_3-21G_geopt_shield.out

echo -e "\n Working files in scratch dir $TMPDIR:"
ls -lt $TMPDIR 
du -h -s $TMPDIR
cd .. ; echo -e "just for control -  pwd=\c";pwd
echo -e "\nDeleting scratch directory $TMPDIR: "; /bin/rm -r $TMPDIR
echo -e "\n Afterwards, content of ls -lt /mnt/local/$USER :"; ls -lt /mnt/local/$USER

echo -e "\n returning to $PBS_O_WORKDIR"
cd $PBS_O_WORKDIR


exit 0
