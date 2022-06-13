#!/bin/bash

#SBATCH --job-name=Si

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4

##SBATCH --mem=50gb

#SBATCH --partition=short 

##SBATCH --time=1-00:10:00
#SBATCH --time=0-00:20:00

## memory per CPU ... is it working
##SBATCH --mem-per-cpu=8G

## stdout/stderr output file
#SBATCH -o log_slurm_job.%j.%N.std_out_err

## mail
#SBATCH --mail-user=Miroslav.Ilias@umb.sk

 
echo -e "Job user is SLURM_JOB_USER=$SLURM_JOB_USER"
echo -e "User's job is SLURM_JOB_NAME=$SLURM_JOB_NAME has assigned ID SLURM_JOBID=$SLURM_JOBID"
echo -e "This job was submitted from the computer SLURM_SUBMIT_HOST=$SLURM_SUBMIT_HOST"
echo -e "and from the home directory: SLURM_SUBMIT_DIR=$SLURM_SUBMIT_DIR"
echo -e "It is running on the cluster compute node: SLURM_CLUSTER_NAME=$SLURM_CLUSTER_NAME"
echo -e "Job  is employing SLURM_JOB_NUM_NODES=$SLURM_JOB_NUM_NODES node/nodes:"
echo -e "SLURM_JOB_NODELIST=$SLURM_JOB_NODELIST"
echo -e "The job requests SLURM_CPUS_ON_NODE=$SLURM_CPUS_ON_NODE CPU per task."

#module load git/2.8.0-foss-2016a
#module load intel/2016a
#module load imkl/11.3.1.150-iimpi-8.1.5-GCC-4.9.3-2.25
#module load OpenMPI/1.8.6-iccifort-2015.2.164-i8
#module load CMake/3.6.1-foss-2016a

#echo -e "\n Loadig module QuantumESPRESSO/6.5-foss-2019b:"
#module load QuantumESPRESSO/6.5-foss-2019b

module use /lustre/home/utils/easybuild_old/modules/all
module load impi/2021.2.0-intel-compilers-2021.2.0

echo -e "List of loaded modules:"
module list

#module unload OpenMPI/1.8.6-iccifort-2015.2.164-i8
#echo -e "\n Removed system provided module OpenMPI/1.8.6-iccifort-2015.2.164-i8"
# my openmpi installation
#export PATH=/home/f113112/work/qch/software/openmpi-2.1.1_intel-15/bin:$PATH
#export LD_LIBRARY_PATH=/home/f113112/work/qch/software/openmpi-2.1.1_intel-15/lib:$LD_LIBRARY_PATH

echo -e "\nRunning on host `hostname`"
echo -e "Time is `date` \n"
echo -e "\nMy PATH=$PATH\n"
echo -e "My LD_LIBRARY_PATH=$LD_LIBRARY_PATH\n"

# CPU model, total numer of CPUs, number of allocated CPUs
echo -e "The node's CPU \c"; cat /proc/cpuinfo | grep 'model name' | uniq
NPROCS=`cat /proc/cpuinfo | grep processor | wc -l`
echo "This node has $NPROCS CPUs available."
#
echo "(i) This node has SLURM_CPUS_ON_NODE=$SLURM_CPUS_ON_NODE CPUs allocated for SLURM calculations."

echo -e "\n The TOTAL memory at the node (in GB); free -t -g"
free -t -g
echo

## set internal OpenMP parallelization for MKL - Slurm CPU count
#export MKL_NUM_THREADS=$SLURM_CPUS_ON_NODE

# no OpenMP multithreading, use full OpenMPI for dirac.x
#export MKL_NUM_THREADS=1
#echo -e  "\nInternal MKL parallelization upon SLURM CPU count, MKL_NUM_THREADS=$MKL_NUM_THREADS\n"
#export OMP_NUM_THREADS=1
#export MKL_DYNAMIC="FALSE"
#export OMP_DYNAMIC="FALSE"

#export QE=/software/software/QuantumESPRESSO/6.5-foss-2019b/bin
export QE=/lustre/home/ilias/work/qch/software/quantum-espresso/qe-7.0/build_intelmpi/bin

echo -e "\n Dependencies of QE main executable, ldd $QE/pw.x:"
ldd $QE/pw.x
echo

echo -e "Python -v :\c"; python -V
#echo -e "cmake ? which cmake = \c"; which cmake
#echo -e "ctest ? which ctest = \c"; which ctest
#echo -e "ctest --version \c"; ctest --version
echo -e "mpirun ? which mpirun  = \c"; which mpirun
echo -e "mpirun --version \c"; mpirun --version

#export DIRAC_TMPDIR=/data
#export DIRAC_TMPDIR=/scratch
#echo -e "\nDIRAC scratch directory space, $DIRAC_TMPDIR"
#df -h $DIRAC_TMPDIR/.
#echo -e "For mere comparison, df -h /tmp/."; df -h /tmp

# for running jobs from your homedir, use ...
cd $SLURM_SUBMIT_DIR

echo -e "\n Current directory where this SLURM job is running `pwd`"
echo " It has the disk space of (df -h) :"
df -h .
echo

 #project=Si.scf
 project=Si.scf_k10x10x10
 inp=$project.in
 out=$project.$SLURM_CLUSTER_NAME.$SLURM_JOBID.out$SLURM_CPUS_ON_NODE
 mpirun -np $SLURM_CPUS_ON_NODE  $QE/pw.x < $inp > $out

exit
