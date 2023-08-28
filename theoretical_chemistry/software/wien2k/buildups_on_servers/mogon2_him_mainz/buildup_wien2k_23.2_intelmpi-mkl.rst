=======================================
WIEN2k_23.2 buildup with IntelMPI + MKL
=======================================

Modules
-------
Currently Loaded Modules:
  1) compiler/intel-compilers/2021.4.0
  2) toolchain/intel/2020a
  3) math/ELPA/2020.05.001-intel-2020a
  4) numlib/FFTW/3.3.8-intel-2020a
  5) compiler/GCCcore/8.3.0
  6) compiler/iccifort/2019.5.281
  7) mpi/impi/2019.5.281-iccifort-2019.5.281
  8) toolchain/iimpi/2019b
  9) numlib/imkl/2019.5.281-iimpi-2019b

module load compiler/intel-compilers/2021.4.0 toolchain/intel/2020a math/ELPA/2020.05.001-intel-2020a numlib/FFTW/3.3.8-intel-2020a compiler/GCCcore/8.3.0 compiler/iccifort/2019.5.281 mpi/impi/2019.5.281-iccifort-2019.5.281 toolchain/iimpi/2019b numlib/imkl/2019.5.281-iimpi-2019 compiler/intel-compilers/2021.4.0 toolchain/intel/2020a math/ELPA/2020.05.001-intel-2020a numlib/FFTW/3.3.8-intel-2020a compiler/GCCcore/8.3.0 compiler/iccifort/2019.5.281 mpi/impi/2019.5.281-iccifort-2019.5.281 toolchain/iimpi/2019b numlib/imkl/2019.5.281-iimpi-2019b

Intel MKL library ? MKLROOT=/cluster/easybuild/broadwell/software/imkl/2019.5.281-iimpi-2019b/mkl

mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.which ifort
/cluster/easybuild/broadwell/software/iccifort/2019.5.281/compilers_and_libraries_2019.5.281/linux/bin/intel64/ifort
mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.which mpiifort
/cluster/easybuild/broadwell/software/impi/2019.5.281-iccifort-2019.5.281/intel64/bin/mpiifort
mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.mpiifort --version
ifort (IFORT) 19.0.5.281 20190815

mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.ifort --version
ifort (IFORT) 19.0.5.281 20190815

mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.which mpirun 
/cluster/easybuild/broadwell/software/impi/2019.5.281-iccifort-2019.5.281/intel64/bin/mpirun
mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2019 Update 5 Build 20190806 (id: 7e5a4f84c)
Copyright 2003-2019, Intel Corporation.

MKL library
~~~~~~~~~~~

module show numlib/imkl/2019.5.281-iimpi-2019b

ls /cluster/easybuild/broadwell/software/imkl/2019.5.281-iimpi-2019b/mkl/lib/intel64/*

  Your current ScaLAPACK options are:
   
   SCALAPACK_LIBS:             -L/cluster/easybuild/broadwell/software/imkl/2019.5.281-iimpi-2019b/mkl/lib/intel64 -lmkl_scalapack -L/cluster/easybuild/broadwell/software/imkl/2019.5.281-iimpi-2019b/mkl/lib/intel64 -lmkl_blacs_intelmpi_lp64
   
   which are derived from following settings:
   
   R   SCALAPACKROOT:          /cluster/easybuild/broadwell/software/imkl/2019.5.281-iimpi-2019b/mkl/lib/
   S   SCALAPACK_LIBNAME:      mkl_scalapack
   BR  BLACSROOT:              /cluster/easybuild/broadwell/software/imkl/2019.5.281-iimpi-2019b/mkl/lib/
   BL  BLACS_LIBNAME:          mkl_blacs_intelmpi_lp64
   M   MKL_TARGET_ARCH:        intel64


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

mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.ls /cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/include/elpa-2020.05.001/elpa/
elpa_constants.h  elpa_generated_c_api.h  elpa_generated.h  elpa_generic.h  elpa.h  elpa_simd_constants.h  elpa_version.h

mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.ls /cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/include/elpa-2020.05.001/modules
elpa_api.mod  elpa_constants.mod  elpa.mod

mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.ls /cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/lib
libelpa.a    libelpa_openmp.a    libelpa_openmp.so@     libelpa_openmp.so.15.0.1*  libelpa.so.15@      pkgconfig/
libelpa.la*  libelpa_openmp.la*  libelpa_openmp.so.15@  libelpa.so@                libelpa.so.15.0.1*

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

IntelMPI parallel
~~~~~~~~~~~~~~~~~~
mirilias@login22.mogon:~/work/software/wien2k/wien2k_23.2_intelmpi_mkl/.ls /cluster/easybuild/broadwell/software/impi/2019.5.281-iccifort-2019.5.281/intel64/lib/
debug/         libmpicxx.so.12@      libmpifort.so@         libmpi_ilp64.a*       libmpijava.so@             mpi.jar*
debug_mt/      libmpicxx.so.12.0@    libmpifort.so.12@      libmpi_ilp64.so@      libmpijava.so.1@           release/
libmpicxx.a*   libmpicxx.so.12.0.0*  libmpifort.so.12.0@    libmpi_ilp64.so.4@    libmpijava.so.1.0*         release_mt/
libmpicxx.so@  libmpifort.a*         libmpifort.so.12.0.0*  libmpi_ilp64.so.4.1*  libmpi_shm_heap_proxy.so*

   Your current parallel settings (options and libraries) are:
   
     C   Parallel Compiler:          mpiifort
     FP  Parallel Compiler Options:  -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I$(MKLROOT)/include
     MP  MPIRUN command:             srun -K -N_nodes_ -n_NP_ -r_offset_ _PINNING_ _EXEC_
     O   Parallel OpenMP switch:     -qopenmp

   Additional setting for SLURM batch systems (is set to 1 otherwise):
 
     CN  Number of Cores:            1

   Libraries:
 
     Sp  SCALAPACK:                   -L/cluster/easybuild/broadwell/software/imkl/2019.5.281-iimpi-2019b/mkl/lib/intel64 
                                                     -lmkl_scalapack 
                                                     -L/cluster/easybuild/broadwell/software/imkl/2019.5.281-iimpi-2019b/mkl/lib/intel64 -lmkl_blacs_intelmpi_lp64
     E   ELPA options:                -DELPA -I/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/include/elpa-2020.05.001/elpa 
                                                     -I/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/include/elpa-2020.05.001/modules
         ELPA-LIBS:                   -lelpa -L/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/lib -Wl,-rpath=/cluster/easybuild/broadwell/software/ELPA/2020.05.001-intel-2020a/lib

     RP  Parallel-Libs:      /cluster/easybuild/broadwell/software/impi/2019.5.281-iccifort-2019.5.281/intel64/lib


Buildup
-------
LS
mpiifort
mpiicc
MKL_TARGET_ARCH was set to intel64

 Since intel changes the name of the mkl-libraries from version to version,
 you may find the linking options for the most recent ifort version at
 http://software.intel.com/en-us/articles/intel-mkl-link-line-advisor/

 Recommended options for system linuxifs are:
      OpenMP switch:           -qopenmp
      Compiler options:        -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I$(MKLROOT)/include
      Linker Flags:            $(FOPT) -L$(MKLROOT)/lib/$(MKL_TARGET_ARCH) -lpthread -lm -ldl -liomp5
      Preprocessor flags:      '-DParallel'
      R_LIB (LAPACK+BLAS):     -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core

 Current settings:
  M   OpenMP switch:           -qopenmp
  O   Compiler options:        -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I$(MKLROOT)/include
  L   Linker Flags:            $(FOPT) -L$(MKLROOT)/lib/$(MKL_TARGET_ARCH) -lpthread -lm -ldl -liomp5
  P   Preprocessor flags       '-DParallel'
  R   R_LIBS (LAPACK+BLAS):    -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core
  F   FFTW options:            -DFFTW3 -DFFTW_OMP -I/cluster/easybuild/broadwell/software/FFTW/3.3.8-intel-2020a/include
      FFTW-LIBS:               -L/cluster/easybuild/broadwell/software/FFTW/3.3.8-intel-2020a/lib -lfftw3 -lfftw3_omp
      FFTW-PLIBS:              -lfftw3_mpi
  X   LIBX options:
      LIBXC-LIBS:

  PO  Parallel options

  S   Save and Quit
  Q   Quit and abandon changes

