==============
SIESTA buildup
==============

now GNU build of LIBXC 

but got GNU mpirun issue
https://gitlab.com/siesta-project/siesta/-/issues/567

-DSIESTA_TESTS_MPI_NUMPROCS=1 .. does not help !

try:
#SBATCH -N 1 -n 4
##SBATCH  --sockets-per-node=1

