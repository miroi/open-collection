#!/bin/bash
#SBATCH -J lammps

## max. execution time
##SBATCH -t 7-00:00:00
#SBATCH -t 0-08:00:00

# number of nodes
#SBATCH -N 1
##SBATCH --exclusive

##SBATCH --mem=120GB
##SBATCH --mem-per-cpu=28G # deactivated

## CPU count  - max. 40 per node ?
#SBATCH -n 8

##  partition (queue)
##SBATCH -p parallel
##SBATCH -p long
#SBATCH -p main

## stdout/stderr output file
#SBATCH -o log_slurm_job.%j.%N.std_out_err

## mail
#SBATCH --mail-user=M.Ilias@gsi.de 
#SBATCH --mail-type=ALL

 
echo -e "Kronos cluster - running on host `hostname`"
echo -e "Time is `date` \n"

echo -e "\nJob user is $SLURM_JOB_USER and his job $SLURM_JOB_NAME has assigned ID $SLURM_JOBID"
echo -e "This job was submitted from the computer $SLURM_SUBMIT_HOST"
echo -e "and from the home directory:\c" 
echo $SLURM_SUBMIT_DIR
echo -e "\nIt is running on the cluster compute node SLURM_CLUSTER_NAME=$SLURM_CLUSTER_NAME "
echo -e "Job is employing $SLURM_JOB_NUM_NODES node/nodes: $SLURM_JOB_NODELIST"
echo -e "\nJob partition is $SLURM_JOB_PARTITION \n"
echo -e "The job requests $SLURM_CPUS_ON_NODE CPU per task."

module use /cvmfs/it.gsi.de/modulefiles/
echo -e "All modules at disposal:"
module avail
echo -e "\n Loading openmpi/intel/4.0_intel17.4:"
module load openmpi/intel/4.0_intel17.4
echo -e ".... loaded modules:"
module list

# CPU model, total numer of CPUs, number of allocated CPUs
echo -e "The node's CPU \c"; cat /proc/cpuinfo | grep 'model name' | uniq
NPROCS=`cat /proc/cpuinfo | grep processor | wc -l`
#echo -e "This node has total $NPROCS CPUs available for EXCLUSIVE job."
echo "This node has $SLURM_CPUS_ON_NODE CPUs allocated for SLURM calculations."

echo -e "\n The total memory at the given node (in GB)"
free -t -g

## set internal OpenMP parallelization for MKL - Slurm CPU count
#export MKL_NUM_THREADS=$SLURM_CPUS_ON_NODE
#export MKL_NUM_THREADS=24
#export MKL_NUM_THREADS=$NPROCS
#echo -e  "\nInternal MKL parallelization MKL_NUM_THREADS=$MKL_NUM_THREADS\n"
export OMP_NUM_THREADS=1
export MKL_DYNAMIC="FALSE"
export OMP_DYNAMIC="FALSE"

##   My OpenMPI-Intel installation   ##
#export PATH=/lustre/nyx/ukt/milias/bin/openmpi-2.0.1-intel-17/bin:$PATH
#export LD_LIBRARY_PATH=/lustre/nyx/ukt/milias/bin/openmpi-2.0.1-intel-17/lib:$LD_LIBRARY_PATH
#export PATH=/lustre/nyx/ukt/milias/bin/openmpi-3.1.0-intel17-i8/bin:$PATH
#export LD_LIBRARY_PATH=/lustre/nyx/ukt/milias/bin/openmpi-3.1.0-intel17-i8/lib:$LD_LIBRARY_PATH
#

export LAMMPS_EXE=/lustre/nyx/ukt/milias/work/software/lammps/lammps_stable/src/lmp_icc_openmpi

echo -e "\nldd $LAMMPS_EXE:"
ldd $LAMMPS_EXE
echo -e "\n ifort -V: \c"; ifort -V

echo -e "\nMy PATH=$PATH\n"
echo -e "Python -v :\c"; python -V
#echo -e "cmake ? which cmake = \c"; which cmake
#echo -e "ctest ? which ctest = \c"; which ctest
#echo -e "ctest --version \c"; ctest --version
echo -e "\n mpirun ? \c"; which mpirun; mpirun --version

#echo -e "\n For comparison, /tmp local disk;  df -h /tmp/."; df -h /tmp

# for running jobs from your homedir
cd $SLURM_SUBMIT_DIR
echo -e "\n I am in SLURM_SUBMIT_DIR=$SLURM_SUBMIT_DIR"
echo -e "...for control, pwd=\c";pwd

echo -e "\nLaunching mpirun -np $SLURM_CPUS_ON_NODE $LAMMPS_EXE -in in.melt :"
mpirun -np $SLURM_CPUS_ON_NODE $LAMMPS_EXE -in in.melt

#
exit
