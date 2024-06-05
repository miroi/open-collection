===================
QE 7.3.1 on Govorun
===================

download
~~~~~~~~

https://www.quantum-espresso.org/download-page/

wget https://www.quantum-espresso.org/rdm-download/488/v7-3-1/328289162201bd6a785ae7620be3eb71/qe-7.3.1-ReleasePack.tar.gz


modules
~~~~~~~

milias@hydra.jinr.ru:~/work/software/quantum-espresso/.module add intel/v2021.1

milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-7.3.1/.module list
milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-7.3.1/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1        2) BASE/1.0          3) Python/v3.10.13   4) intel/v2021.1
milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-7.3.1/.emkl
Intel MKL library ? MKLROOT=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest



milias@hydra.jinr.ru:~/work/software/quantum-espresso/.which mpirun
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/intelpython/latest/bin/mpirun
milias@hydra.jinr.ru:~/work/software/quantum-espresso/.mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2021.1 Build 20201112 (id: b9c9d2fc5)
Copyright 2003-2020, Intel Corporation.
milias@hydra.jinr.ru:~/work/software/quantum-espresso/.emkl
Intel MKL library ? MKLROOT=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest
milias@hydra.jinr.ru:~/work/software/quantum-espresso/.mpiifort --version
ifort (IFORT) 2021.1 Beta 20201112
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@hydra.jinr.ru:~/work/software/quantum-espresso/.which mpiicc
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1/bin/mpiicc

installation
~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-7.3.1/.
./configure --enable-parallel --enable-openmp --with-scalapack --prefix=/lustre/home/user/m/milias/work/software/quantum-espresso/qe-7.3.1/bin
.
.
configure: success

milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-7.3.1/.less install/config.log


milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-7.3.1/.FC=ifort CC=icc ./configure --enable-parallel --enable-openmp --with-scalapack --prefix=/lustre/home/user/m/milias/work/software/quantum-espresso/qe-7.3.1/bin

configure: success

m -j4 all




