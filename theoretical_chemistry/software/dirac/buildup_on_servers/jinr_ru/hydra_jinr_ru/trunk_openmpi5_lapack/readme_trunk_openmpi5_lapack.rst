=============
DIRAC buildup
=============

module add Python/v3.10.2
module add CMake/v3.29.2
module add openmpi/v5.0.3_gcc1230
module add LAPACK/v3.12.0_gcc1230

module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1               3) Python/v3.10.2           5) gcc/v12.3.0              7) LAPACK/v3.12.0_gcc1230
  2) BASE/1.0                 4) CMake/v3.29.2            6) openmpi/v5.0.3_gcc1230


milias@hydra.jinr.ru:~/work/software/dirac/trunk/build_openmpi5_lapack/.which mpif90
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/openmpi/v5.0.3_gcc1230/bin/mpif90
milias@hydra.jinr.ru:~/work/software/dirac/trunk/build_openmpi5_lapack/.mpif90 --version
GNU Fortran (GCC) 12.3.0
Copyright (C) 2022 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

milias@hydra.jinr.ru:~/work/software/dirac/trunk/. ./setup --mpi --exatensor=OFF  --fc=mpif90 --cc=mpicc --cxx=mpicxx --blas=off --lapack=off  --explicit-libs="-L/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/LAPACK/v3.12.0_gcc1230/lib64 -llapack -lblas"  $BUILD

milias@hydra.jinr.ru:~/work/software/dirac/trunk/build_openmpi5_lapack_i4/cmake ..
milias@hydra.jinr.ru:~/work/software/dirac/trunk/build_openmpi5_lapack_i4/make -j4 


