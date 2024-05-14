==================
Wienk2k on Govorun
==================

Loading modules
---------------
milias@hydra.jinr.ru:~/work/software/wien2k/.module load openmpi intel fftw
milias@hydra.jinr.ru:~/work/software/wien2k/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1               4) gcc/v11.2.0              7) fftw/v3.3.7-5
  2) BASE/1.0                 5) openmpi/v4.1.1_gcc1120
  3) Python/v3.10.2           6) intel/v2021.1

milias@hydra.jinr.ru:~/work/software/wien2k/.which mpif90
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1/bin/mpif90
milias@hydra.jinr.ru:~/work/software/wien2k/.mpif90 --version
GNU Fortran (GCC) 11.2.0

milias@hydra.jinr.ru:~/work/software/wien2k/.emkl
Intel MKL library ? MKLROOT=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest

Wien2k unpacking
----------------
# in own directory:  tar xvf WIEN2k_23.2.tar
milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_openmpi_mkl/.
milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_openmpi_mkl/.gunzip *
milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_openmpi_mkl/.check_minimal_software_requirements.sh
milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_openmpi_mkl/../expand_lapw
.
.
python found at /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/intelpython/latest/bin/python.

WIEN is now expanded. The shell-script commands were copied and links created.
To configure your Fortran-executables run:

./siteconfig_lapw



Own compilation
----------------

mpif90
mpicc
MKL

FFTW3
~~~~~
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/lib/libfftw3_threads.so
lib64

  No OMP parallel version of your FFTW library could be found. Installing
  it would improve the performance of some programs (lapw0, lapw2, 3ddens).

  Your FFTW_OPT are:   -DFFTW3 -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/include
  Your FFTW_LIBS are:  -L/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/lib64 -lfftw3

  These options derive from your chosen settings:

  FFTWROOT:            /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/
  FFTW_VERSION:        FFTW3
  FFTW_LIB:            lib
  FFTW_LIBNAME:        fftw3
  Is this correct? (Y,n):

 ***********************************************************************
 *                     Compiler and linker options                     *
 ***********************************************************************

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
  F   FFTW options:            -DFFTW3 -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/include
      FFTW-LIBS:               -L/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/lib64 -lfftw3
  X   LIBX options:
      LIBXC-LIBS:

  S   Save and Quit

      To change an item select option.


Parallel
~~~~~~~~

mpiifort
mpirun

milias@hydra.jinr.ru:~/.mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2021.1 Build 20201112 (id: b9c9d2fc5)

ScaLAPACK
~~~~~~~~~~
  Your SCALAPACK_LIBS are:    -lmkl_scalapack_lp64 -lmkl_blacs_intelmpi_lp64

  These options derive from your chosen settings:

  SCALAPACKROOT:       $(MKLROOT)/lib/
  SCALAPACK_LIBNAME:   mkl_scalapack_lp64
  BLACSROOT:           $(MKLROOT)/lib/
  BLACS_LIBNAME:       mkl_blacs_intelmpi_lp64
  MKL_TARGET_ARCH:     intel64

Summary of parallel settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

!!!  WARNING:  No MPI version of the FFTW library found!
!!!  WARNING:  Please provide it before compiling MPI-parallel
!!!  WARNING:  programs (e.g. lapw0_mpi). Only the sequential
!!!  WARNING:  versions will be installed with the current settings.


