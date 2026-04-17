Test MPI with GNU OpenMPI compilers
===================================

module add  openmpi/v4.1.8_gcc1230


##SBATCH --distribution=cyclic:cyclic
srun: warning: can't honor --ntasks-per-node set to 4 which doesn't match the requested tasks 8 and -mpack, which forces min number of nodes to 1

#SBATCH --nodes=2
##SBATCH --ntasks=8
#SBATCH --ntasks-per-node=4
#SBATCH --distribution=cyclic:cyclic


