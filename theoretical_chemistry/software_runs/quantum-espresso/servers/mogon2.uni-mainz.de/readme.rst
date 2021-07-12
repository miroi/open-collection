============
QE on Mogon2
============

module purge
module load numlib/FFTW
module load chem/libxc/4.3.4-iccifort-2020.1.217

Having:
mirilias@login23.mogon:~/work/software/quantum_espresso/.module list
Currently Loaded Modulefiles:
 1) compiler/GCCcore/9.3.0         4) mpi/impi/2019.7.217-iccifort-2020.1.217   7) toolchain/intel/2020a                 
 2) compiler/iccifort/2020.1.217   5) toolchain/iimpi/2020a                     8) numlib/FFTW/3.3.8-intel-2020a         
 3) lib/UCX/1.8.0-GCCcore-9.3.0    6) numlib/imkl/2020.1.217-iimpi-2020a        9) chem/libxc/4.3.4-iccifort-2020.1.217  


./configure --with-scalapack --with-libxc  

mirilias@login23.mogon:~/work/software/quantum_espresso/qe-6.7/../configure --with-scalapack --with-libxc
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
checking for mpiifort... mpiifort
checking whether we are using the GNU Fortran compiler... no
checking whether mpiifort accepts -g... yes
checking version of mpiifort... ifort 19
checking for Fortran flag to compile .f90 files... none
setting F90... ifort
setting MPIF90... mpiifort
checking for icc... icc
checking whether we are using the GNU C compiler... yes
checking whether icc accepts -g... yes
checking for icc option to accept ISO C89... none needed
setting CC... icc
setting CFLAGS... -O3
using F90... ifort
setting FFLAGS... -O2 -assume byterecl -g -traceback
setting F90FLAGS... $(FFLAGS) -nomodule
setting FFLAGS_NOOPT... -O0 -assume byterecl -g -traceback
setting FFLAGS_NOMAIN... -nofor_main
setting CPP... cpp
setting CPPFLAGS... -P -traditional -Uvector
setting LD... mpiifort
setting LDFLAGS...
checking whether make sets $(MAKE)... yes
checking whether Fortran files must be preprocessed... no
checking whether we are using the GNU Fortran 77 compiler... no
checking whether ifort accepts -g... yes
checking for library containing dgemm... -lmkl_intel_lp64
setting BLAS_LIBS... -lmkl_intel_lp64 -lmkl_sequential -lmkl_core
checking FFT... 
checking for libxc... yes (-I/usr/include -lxcf03 -lxc)
checking MASS... 
checking for library containing mpi_init... none required
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... no
checking ELPA... 
checking BEEF... -lbeef
setting BEEF_LIBS... $(TOPDIR)/LIBBEEF/libbeef.a
checking for ranlib... ranlib
checking for wget... wget -O
setting WGET... wget -O
setting DFLAGS... -D__DFTI -D__LIBXC -D__MPI
setting IFLAGS... -I$(TOPDIR)/include -I$(TOPDIR)/FoX/finclude -I/cluster/easybuild/broadwell/software/imkl/2020.1.217-iimpi-2020a/mkl/include -I/usr/include
configure: creating ./config.status
config.status: creating install/make_lapack.inc
config.status: creating include/configure.h
config.status: creating make.inc
config.status: creating configure.msg
config.status: creating install/make_wannier90.inc
config.status: creating include/qe_cdefs.h
config.status: include/qe_cdefs.h is unchanged
--------------------------------------------------------------------
ESPRESSO can take advantage of several optimized numerical libraries
(essl, fftw, mkl...).  This configure script attempts to find them,
but may fail if they have been installed in non-standard locations.
If a required library is not found, the local copy will be compiled.

The following libraries have been found:
  BLAS_LIBS=  -lmkl_intel_lp64  -lmkl_sequential -lmkl_core
  LAPACK_LIBS=
  FFT_LIBS=
  
  LIBXC_LIBS= -lxcf03 -lxc

Please check if this is what you expect.

If any libraries are missing, you may specify a list of directories
to search and retry, as follows:
  ./configure LIBDIRS="list of directories, separated by spaces"

Parallel environment detected successfully.\
Configured for compilation of parallel executables.
.
.
.
configure: success



