Quantum Espresso
================

milias@lxir127.gsi.de
---------------------

milias@lxir127.gsi.de:/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/../configure 
checking build system type... x86_64-pc-linux-gnu
checking ARCH... x86_64
checking setting AR... ... ar
checking setting ARFLAGS... ... ruv
checking for gfortran... gfortran
checking whether the Fortran compiler works... yes
checking for Fortran compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU Fortran compiler... yes
checking whether gfortran accepts -g... yes
checking for mpif90... mpif90
checking whether we are using the GNU Fortran compiler... no
checking whether mpif90 accepts -g... yes
checking version of mpif90... ifort 17
checking for Fortran flag to compile .f90 files... none
setting F90... ifort
setting MPIF90... mpif90
checking for icc... icc
checking whether we are using the GNU C compiler... yes
checking whether icc accepts -g... yes
checking for icc option to accept ISO C89... none needed
setting CC... icc
setting CFLAGS... -O3
checking for ifort... ifort
checking whether we are using the GNU Fortran 77 compiler... no
checking whether ifort accepts -g... yes
setting F77... ifort
using F90... ifort
setting FFLAGS... -O2 -assume byterecl -g -traceback
setting F90FLAGS... $(FFLAGS) -nomodule
setting FFLAGS_NOOPT... -O0 -assume byterecl -g -traceback
setting FFLAGS_NOMAIN... -nofor_main
setting CPP... cpp
setting CPPFLAGS... -P -traditional -Uvector
setting LD... mpif90
setting LDFLAGS...
checking whether make sets $(MAKE)... yes
checking whether Fortran files must be preprocessed... no
checking for library containing dgemm... -lmkl_intel_lp64
setting BLAS_LIBS... -lmkl_intel_lp64 -lmkl_sequential -lmkl_core
checking for library containing dspev... none required
checking FFT... 
checking MASS... 
checking for library containing mpi_init... none required
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... no
checking ELPA... 
checking for ranlib... ranlib
checking for wget... wget -O
setting WGET... wget -O
setting DFLAGS... -D__DFTI -D__MPI
setting IFLAGS... -I$(TOPDIR)/include -I$(TOPDIR)/FoX/finclude -I$(TOPDIR)/S3DE/iotk/include/ -I/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/include
configure: creating ./config.status
config.status: creating install/make_lapack.inc
config.status: creating include/configure.h
config.status: creating make.inc
config.status: creating configure.msg
config.status: creating install/make_wannier90.inc
config.status: creating include/c_defs.h
--------------------------------------------------------------------
ESPRESSO can take advantage of several optimized numerical libraries
(essl, fftw, mkl...).  This configure script attempts to find them,
but may fail if they have been installed in non-standard locations.
If a required library is not found, the local copy will be compiled.

The following libraries have been found:
  BLAS_LIBS=  -lmkl_intel_lp64  -lmkl_sequential -lmkl_core
  LAPACK_LIBS=
  FFT_LIBS=
  
  

Please check if this is what you expect.

If any libraries are missing, you may specify a list of directories
to search and retry, as follows:
  ./configure LIBDIRS="list of directories, separated by spaces"

Parallel environment detected successfully.\
Configured for compilation of parallel executables.

For more info, read the ESPRESSO User's Guide (Doc/users-guide.tex).
--------------------------------------------------------------------
configure: success




