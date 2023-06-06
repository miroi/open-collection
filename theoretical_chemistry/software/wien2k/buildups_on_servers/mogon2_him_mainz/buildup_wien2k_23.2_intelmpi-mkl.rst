=======================================
WIEN2k_23.2 buildup with IntelMPI + MKL
=======================================

Modules
-------
mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_openmpi-intel/.module load mpi/impi/2021.4.0-intel-compilers-2021.4.0
mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_openmpi-intel/.which ifort
/cluster/easybuild/broadwell/software/intel-compilers/2021.4.0/compiler/2021.4.0/linux/bin/intel64/ifort
mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_openmpi-intel/.which icc
/cluster/easybuild/broadwell/software/intel-compilers/2021.4.0/compiler/2021.4.0/linux/bin/intel64/icc

which mpiifort
/cluster/easybuild/broadwell/software/impi/2021.4.0-intel-compilers-2021.4.0/mpi/2021.4.0/bin/mpiifort

which mpirun
/cluster/easybuild/broadwell/software/impi/2021.4.0-intel-compilers-2021.4.0/mpi/2021.4.0/bin/mpirun

mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_openmpi-intel/.mpiifort --version
ifort (IFORT) 2021.4.0 20210910
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.

mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_openmpi-intel/.mpiicc --version
icc (ICC) 2021.4.0 20210910
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.

mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_openmpi-intel/.mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2021.4 Build 20210831 (id: 758087adf)

MKL library
~~~~~~~~~~~
module load numlib/imkl/2021.4.0 
emkl
Intel MKL library ? MKLROOT=/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0

see ls /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/ for blacs, scalapack etc

emkl
Intel MKL library ? MKLROOT=/cluster/easybuild/broadwell/software/imkl/2020.1.217-iimpi-2020a/mkl

ls /cluster/easybuild/broadwell/software/imkl/2020.1.217-iimpi-2020a/mkl/lib/intel64/


   *         ScaLAPACK Settings         *
   **************************************

   Your current ScaLAPACK options are:
   
   SCALAPACK_LIBS:             -L/cluster/easybuild/broadwell/software/imkl/2020.1.217-iimpi-2020a/mkl/lib/intel64 -lmkl_scalapack -L/cluster/easybuild/broadwell/software/imkl/2020.1.217-iimpi-2020a/mkl/lib/intel64 -lmkl_blacs_intelmpi_lp64
   
   which are derived from following settings:
   
   R   SCALAPACKROOT:          /cluster/easybuild/broadwell/software/imkl/2020.1.217-iimpi-2020a/mkl/lib/
   S   SCALAPACK_LIBNAME:      mkl_scalapack
   BR  BLACSROOT:              /cluster/easybuild/broadwell/software/imkl/2020.1.217-iimpi-2020a/mkl/lib/
   BL  BLACS_LIBNAME:          mkl_blacs_intelmpi_lp64
   M   MKL_TARGET_ARCH:        intel64

   RS  Reset complete ScaLAPACK setup
   X   Delete all settings
   
   B   Back to parallel options



Intel-built FFTW3
~~~~~~~~~~~~~~~~~~
module load numlib/FFTW/3.3.8-intel-2020a
module show numlib/FFTW/3.3.8-intel-2020a

ls /cluster/easybuild/broadwell/software/FFTW/3.3.8-intel-2020a/include/
ls /cluster/easybuild/broadwell/software/FFTW/3.3.8-intel-2020a/lib

 The OMP parallel version of your FFTW library will be used.

  Your FFTW_OPT are:   -DFFTW3 -DFFTW_OMP -I/cluster/easybuild/broadwell/software/FFTW/3.3.8-intel-2020a/include 
  Your FFTW_LIBS are:  -L/cluster/easybuild/broadwell/software/FFTW/3.3.8-intel-2020a/lib -lfftw3 -lfftw3_omp
  Your FFTW_PLIBS are: -lfftw3_mpi

  These options derive from your chosen settings:
   
  FFTWROOT:            /cluster/easybuild/broadwell/software/FFTW/3.3.8-intel-2020a/
  FFTW_VERSION:        FFTW3
  FFTW_LIB:            lib
  FFTW_LIBNAME:        fftw3
  Is this correct? (Y,n): Y


Intel-built ELPA
~~~~~~~~~~~~~~~~~~
ml load math/ELPA/2020.05.001-intel-2020a

The following have been reloaded with a version change:
  1) mpi/impi/2021.4.0-intel-compilers-2021.4.0 => mpi/impi/2019.7.217-iccifort-2020.1.217
  2) numlib/imkl/2021.4.0 => numlib/imkl/2020.1.217-iimpi-2020a
  3) toolchain/iimpi/2021b => toolchain/iimpi/2020a

module show math/ELPA/2020.05.001-intel-2020a 

ls /cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/lib/
libelpa.a    libelpa_openmp.a    libelpa_openmp.so@     libelpa_openmp.so.15.0.1*  libelpa.so.15@      pkgconfig/
libelpa.la*  libelpa_openmp.la*  libelpa_openmp.so.15@  libelpa.so@                libelpa.so.15.0.1*

   *                           ELPA Summary                           *    
  Your ELPA_OPT are:   -DELPA -I/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/include/elpa_openmp-2020.05.001/elpa 
                           -I/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/include/elpa_openmp-2020.05.001/modules 
  Your ELPA_LIBS are:  -lelpa_openmp -L/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/lib -Wl,rpath=/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/lib

  These options derive from your chosen Settings:
   
  ELPAROOT:            /cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/
  ELPA_VERSION:        2020.05.001
  ELPA_LIB:            lib
  ELPA_LIBNAME:        elpa_openmp
  Is this correct?  (Y,n): Y

   Your current ELPA options are:
   
   ELPA_OPT:             -DELPA -I/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/include/elpa_openmp-2020.05.001/elpa 
                  -I/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/include/elpa_openmp-2020.05.001/modules
   ELPA_LIBS:            -lelpa_openmp -L/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/lib -Wl,-rpath=/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/lib
   
   which are derived from following settings:
   
   R  ELPAROOT:          /cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/
   V  ELPA_VERSION:      2020.05.001
   L  ELPA_LIB:          lib
   N  ELPA_LIBNAME:      elpa_openmp
   
   RS Reset complete ELPA setup
   X  Delete all settings
   
   B  Back to parallel options

mirilias@login22.mogon:~/.ls /cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/
bin/  easybuild/  include/  lib/  lib64@  share/
mirilias@login22.mogon:~/.ls /cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/include/elpa_openmp-2020.05.001/elpa 
elpa_constants.h  elpa_generated_c_api.h  elpa_generated.h  elpa_generic.h  elpa.h  elpa_simd_constants.h  elpa_version.h
mirilias@login22.mogon:~/.ls /cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/include/elpa_openmp-2020.05.001/modules
elpa_api.mod  elpa_constants.mod  elpa.mod
mirilias@login22.mogon:~/.ls /cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/lib
libelpa.a    libelpa_openmp.a    libelpa_openmp.so@     libelpa_openmp.so.15.0.1*  libelpa.so.15@      pkgconfig/
libelpa.la*  libelpa_openmp.la*  libelpa_openmp.so.15@  libelpa.so@                libelpa.so.15.0.1*


List of all modules
~~~~~~~~~~~~~~~~~~~
module list
module unload compiler/GCCcore/9.3.0 lib/UCX/1.8.0-GCCcore-9.3.0 
module unload numlib/imkl-FFTW/2021.4.0-iimpi-2021b
module list

Currently Loaded Modules:
  1) compiler/intel-compilers/2021.4.0
  2) compiler/iccifort/2020.1.217
  3) mpi/impi/2019.7.217-iccifort-2020.1.217
  4) toolchain/intel/2020a
  5) math/ELPA/2020.05.001-intel-2020a
  6) numlib/FFTW/3.3.8-intel-2020a


Buildup
-------
LS
mpiifort
mpiicc
MKL_TARGET_ARCH was set to intel64


