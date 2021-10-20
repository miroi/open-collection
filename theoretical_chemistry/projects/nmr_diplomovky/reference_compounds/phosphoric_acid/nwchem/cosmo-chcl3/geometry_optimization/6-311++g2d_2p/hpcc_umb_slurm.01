#!/bin/bash

## job name
#SBATCH -J h3po4go1

##   number of nodes
#SBATCH -N 1

##SBATCH --nodelist=comp06

##   number of CPUs, max 12 on old nodes
#SBATCH -n 12

## partition
#SBATCH -p compute

## max. execution time
#SBATCH -t 0-10:00:00

# allocated total memory per this job
#SBATCH --mem=42GB

# do not restart in the case of nodefail!
#SBATCH --no-requeue
#SBATCH --no-kill

## logfile
#SBATCH -o log_slurm_job.%j.%N.std_out_err

## mail
#SBATCH --mail-user=Miroslav.Ilias@umb.sk
#SBATCH --mail-type=ALL

#echo -e "\nWorking host is: \c"; hostname -f
echo -e "\nRunning on host `hostname -f`"
echo -e "Time is `date` \n"

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

echo -e "\npython -V \c"; python -V
echo -e "mpif90 ? \c"; which mpif90; mpif90 --version
echo -e "mpicc ? \c"; which mpicc; mpicc --version
echo -e "mpirun ? \c"; which mpirun; mpirun --version

echo Job user is $SLURM_JOB_USER and his job $SLURM_JOB_NAME has assigned ID $SLURM_JOBID
echo This job was submitted from the computer $SLURM_SUBMIT_HOST
echo and from the home directory:
echo $SLURM_SUBMIT_DIR
echo
echo It is running on the cluster compute node:
echo $SLURM_CLUSTER_NAME
echo and is employing $SLURM_JOB_NUM_NODES node/nodes:
echo $SLURM_JOB_NODELIST
echo -e "  Job partition is $SLURM_JOB_PARTITION \n"

# CPU model, total numer of CPUs, number of allocated CPUs
echo -e "The node's CPU \c"; cat /proc/cpuinfo | grep 'model name' | uniq
NPROCS=`cat /proc/cpuinfo | grep processor | wc -l`
echo "This node has total $NPROCS CPUs available for an EXCLUSIVE job on this node."
echo "This node has $SLURM_CPUS_ON_NODE CPUs allocated for this SLURM job."
echo -e "\n The job requests SLURM_MEM_PER_NODE=$SLURM_MEM_PER_NODE memory."

echo -e "\n The total memory at the node (in GB)"
free -t -g
echo -e "\n"

echo -e "\nMy PATH=$PATH"
echo -e "My LD_LIBRARY_PATH=$LD_LIBRARY_PATH"

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

export NWCHEM_EXECUTABLE=/home/milias/Work/qch/software/nwchem_suite/nwchem_master/bin/LINUX64/nwchem
#export NWCHEM_EXECUTABLE=/home/milias/Work/qch/software/nwchem_suite/nwchem-7.0.2/bin/LINUX64/nwchem
echo -e "\nNWCHEM executable linked libraries, ldd $NWCHEM_EXECUTABLE"
ldd $NWCHEM_EXECUTABLE

### set local scratch directory for run
export TMPDIR=/mnt/local/$USER/SLURMjob-${SLURM_JOBID}
echo -e "\n Noide's local scratch directory, TMPDIR=$TMPDIR";
echo -e "Size of this local scratch dir, df -h /mnt/local/$USER/:";df -h /mnt/local/$USER

mkdir $TMPDIR
cd $TMPDIR
echo -e "\nI am in working dir, TMPDIR=$TMPDIR"
echo -e "For control pwd=\c";pwd
echo -e "The local home directory with NWChem input file, SLURM_SUBMIT_DIR=${SLURM_SUBMIT_DIR}"

# copy starting geometry to the workdir
#cp ${SLURM_SUBMIT_DIR}/VX.converged_geometry_blyp_tz2p-solvent-chcl3.xyz   $TMPDIR/.
cp ${SLURM_SUBMIT_DIR}/h3po4_startgeom.xyz   $TMPDIR/.

#project=der2.uhf_nmr_b3lyp_ccpvdz_cosmo-chcl3
#project=der2.odft_nmr_b3lyp_ccpvdz_cosmo-chcl3
#project=der2.odft_nmr_b3lyp_ccpvdz
project=h3po4.geopt_b3lyp_6-311++g2d_2p_cosmo-chcl3
echo -e "\n Launching NWChem run of project=$project"
mpirun -np  $SLURM_CPUS_ON_NODE $NWCHEM_EXECUTABLE  ${SLURM_SUBMIT_DIR}/$project.nw  > ${SLURM_SUBMIT_DIR}/$project.${SLURM_JOBID}.out

# save conveged geometry to homedir 
cp $TMPDIR/h3po4_geom_b3lyp*   ${SLURM_SUBMIT_DIR}/.

echo -e "\n Working files remained in scratch dir $TMPDIR:"
ls -lt $TMPDIR 
du -h -s $TMPDIR
cd .. ; echo -e "just for control -  pwd=\c";pwd
echo -e "\nDeleting scratch directory $TMPDIR: "; /bin/rm -r $TMPDIR
echo -e "\n Afterwards, content of ls -lt /mnt/local/$USER :"; ls -lt /mnt/local/$USER

echo -e "\n Time of finishing job is `date` \n"
echo -e "\n returning to ${SLURM_SUBMIT_DIR}"
cd ${SLURM_SUBMIT_DIR}
ls -lt

exit 0
