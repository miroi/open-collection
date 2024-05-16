Wien2k buildup
==============

module load  openmpi fftw ELPA

module list

Currently Loaded Modulefiles:
  1) GVR/v1.0-1
  2) BASE/1.0
  3) Python/v3.10.2
  4) gcc/v11.2.0
  5) openmpi/v4.1.1_gcc1120
  6) intel/v2018.1.163-9
  7) openmpi/v1.8.8-1
  8) Python/v3.6.5
  9) ELPA/v2020.05.001_intel2018_python365
 10) fftw/v3.3.7-5

milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.mpiifort --version
ifort (IFORT) 18.0.1 20171018
Copyright (C) 1985-2017 Intel Corporation.  All rights reserved.

milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.mpiicc --version
icc (ICC) 18.0.1 20171018
Copyright (C) 1985-2017 Intel Corporation.  All rights reserved.

milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.which mpirun
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/openmpi/v1.8.8-1/bin/mpirun

 System linuxifs selected.

mpiifort
mpiicc


You have the following mkl libraries in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64 :
MKL_TARGET_ARCH was set to intel64

FFTW3
~~~~~

/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/latest-release

Please specify the name of your FFTW library or accept present choice (enter): lib

  No OMP parallel version of your FFTW library could be found. Installing
  it would improve the performance of some programs (lapw0, lapw2, 3ddens).

  Your FFTW_OPT are:   -DFFTW3 -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/include
  Your FFTW_LIBS are:  -L/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5//cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/latest-release -llib

  These options derive from your chosen settings:

  FFTWROOT:            /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/
  FFTW_VERSION:        FFTW3
  FFTW_LIB:            /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/latest-release
  FFTW_LIBNAME:        lib

parallel
~~~~~~~~

   Do you have MPI, ScaLAPACK, ELPA, or MPI-parallel FFTW installed and intend
   to run finegrained parallel?

   This is useful only for BIG cases (50 atoms and more / unit cell)
   and your HARDWARE has at least 16 cores (or is a cluster with Infiniband)
   You need to KNOW details about your installed MPI, ELPA, and FFTW )

ScaLAPACK
~~~~~~~~~
  Your SCALAPACK_LIBS are:    -lmkl_scalapack_lp64 -lmkl_blacs_intelmpi_lp64

  These options derive from your chosen settings:

  SCALAPACKROOT:       $(MKLROOT)/lib/
  SCALAPACK_LIBNAME:   mkl_scalapack_lp64
  BLACSROOT:           $(MKLROOT)/lib/
  BLACS_LIBNAME:       mkl_blacs_intelmpi_lp64
  MKL_TARGET_ARCH:     intel64

ELPA
~~~~
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/ELPA/v2020.05.001_intel2018_python365

/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/ELPA/v2020.05.001_intel2018_python365/lib/

 Please specify the name of your installed ELPA library (e.g. elpa or elpa_openmp):
elpa


Configure parallel execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mpi/intel64/bin/mpirun

milias@hydra.jinr.ru:~/./cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mpi/intel64/bin/mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2018 Update 1 Build 20171011 (id: 17941)
Copyright (C) 2003-2017, Intel Corporation. All rights reserved.

   Please specify your MPIRUN command or accept the recommendations (Enter - default)!:
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mpi/intel64/bin/mpirun


   parallel execution:

         RP_LIBS                : $(R_LIBS)
!!!  WARNING:  No MPI version of the FFTW library found!
!!!  WARNING:  Please provide it before compiling MPI-parallel
!!!  WARNING:  programs (e.g. lapw0_mpi). Only the sequential
!!!  WARNING:  versions will be installed with the current settings.

Compilation of lapw0:
~~~~~~~~~~~~~~~~~~~~

xcpot1.o xcpot1Q.o xcpot3.o ykav.o ylm.o coulint.o c_alpha_m.o gaunt.o notri.o t3j0.o t3j.o ph.o finl_elect_str.o kahan_summ_gxyz.o stress_gga.o -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/include  -DFFTW3 -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/include  -qopenmp -L/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/ -lpthread -lm -ldl -liomp5 -L/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5//cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/latest-release -llib  -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core
ld: cannot find -llib
make[1]: *** [lapw0] Error 1


mpiifort -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/include  -DFFTW3 -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/include  -qopenmp -DParallel -c fft_modules.F
fft_modules.F(62): error #5102: Cannot open include file 'fftw3-mpi.f03'
        include 'fftw3-mpi.f03'


