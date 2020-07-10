Abinit on ADF2
==============


milias@adf2:~/work/software/abinit/abinit-8.10.3/../configure FC=mpif90 CC=mpicc  --prefix=$PWD --enable-mpi
 ==============================================================================
 === Final remarks                                                          ===
 ==============================================================================


Summary of important options:

  * C compiler      : gnu version 9.3
  * Fortran compiler: gnu version 9.3
  * architecture    : intel xeon (64 bits)

  * debugging       : basic
  * optimizations   : standard

  * OpenMP enabled  : no (collapse: ignored)
  * MPI    enabled  : yes
  * MPI-IO enabled  : auto
  * GPU    enabled  : no (flavor: none)

  * TRIO   flavor = none
  * TIMER  flavor = abinit (libs: ignored)
  * LINALG flavor = netlib (libs: auto-detected)
  * ALGO   flavor = none (libs: ignored)
  * FFT    flavor = none (libs: ignored)
  * MATH   flavor = none (libs: ignored)
  * DFT    flavor = none

Configuration complete.
You may now type "make" to build ABINIT.
(or, on a SMP machine, "make mj4", or "make multi multi_nprocs=<n>")

