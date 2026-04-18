=========
Elk tests
=========


/lustre/projects/m/milias/work/software/elk/intelmpi2023.1.0/elk-10.9.5/tests/.less test-mpi.sh
  OMP_NUM_THREADS=2 OMP_STACKSIZE=128M mpirun -n 4 ../../src/elk > test.log
