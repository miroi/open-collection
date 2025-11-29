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

does not help

try: - does not help...
#SBATCH -N 1 -n 4
#SBATCH --oversubscribe

57% tests passed, 314 tests failed out of 726

try: 
~~~~
-DSIESTA_TESTS_MPI_MAX_NUMPROCS=1

... this works !!!
93% tests passed, 52 tests failed out of 725

