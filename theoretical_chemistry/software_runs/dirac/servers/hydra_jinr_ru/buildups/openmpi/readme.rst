DIRAC-OpenMPI on hydra
======================

Own Intel-OpenMPI-i8
--------------------
   ## My Intel-OpenMPI-i8:
   # milias@hydra.jinr.ru:~/work/software/openmpi/openmpi-4.0.4-intel19.3-i8/../configure --prefix=$PWD  F77=ifort FC=ifort FFLAGS=-i8 FCFLAGS=-i8 CXX=icpc CC=icc
     extend_string PATH             /zfs/hybrilit.jinr.ru/user/m/milias/work/software/openmpi/openmpi-4.0.4-intel19.3-i8/bin          $PATH
     extend_string MANPATH          /zfs/hybrilit.jinr.ru/user/m/milias/work/software/openmpi/openmpi-4.0.4-intel19.3-i8/share/man    $MANPATH
     extend_string LD_LIBRARY_PATH  /zfs/hybrilit.jinr.ru/user/m/milias/work/software/openmpi/openmpi-4.0.4-intel19.3-i8/lib          $LD_LIBRARY_PATH

milias@hydra.jinr.ru:~/work/software/dirac/master_production/.mpif90 --version; mpicc --version; mpicxx --version
ifort (IFORT) 2021.1 Beta 20201112
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

icc (ICC) 2021.1 Beta 20201112
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

icpc (ICC) 2021.1 Beta 20201112
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

configuration
--------------
milias@hydra.jinr.ru:~/work/software/dirac/master_production/../setup --mpi --int64 --fc=mpif90  --cc=mpicc --cxx=mpicxx --mkl=parallel build_openmpi_intel_i8_mklpar


