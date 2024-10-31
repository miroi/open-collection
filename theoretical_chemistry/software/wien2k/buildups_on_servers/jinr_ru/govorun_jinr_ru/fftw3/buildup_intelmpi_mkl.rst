=======================
FFTW3 with IntelMPI+MKL
=======================

modules
~~~~~~~
milias@hydra.jinr.ru:~/work/software/fftw3/fftw-3.3.10/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1      2) intel/v2021.1   3) BASE/1.0        4) gcc/v10.2.0
milias@hydra.jinr.ru:~/work/software/fftw3/fftw-3.3.10/.

configure
~~~~~~~~~
CC=icc MPICC=mpiicc   FC=ifort   ./configure --prefix=$PWD  --enable-openmp --enable-mpi
.
.


compile
~~~~~~~



