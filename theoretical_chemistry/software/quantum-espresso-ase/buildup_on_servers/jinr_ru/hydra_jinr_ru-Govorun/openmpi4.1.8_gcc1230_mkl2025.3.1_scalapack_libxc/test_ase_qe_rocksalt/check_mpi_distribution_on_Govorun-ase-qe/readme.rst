=================
ASE rocksalt test
=================

N1,n4, noHT ... 32.27s WALL
N1,n4, noHT ..  33.26s WALL

espresso.err ...The error logs you're seeing show that your MPI ranks (specifically ranks 0 and 2) are being bound to the same set of physical cores (cores 19, 20, 21, 22), causing an overlap. This "over-binding" typically happens when the launcher (e.g., mpirun or srun) and the SLURM scheduler have conflicting ideas about the node's architecture or how to distribute tasks.


to fix..
