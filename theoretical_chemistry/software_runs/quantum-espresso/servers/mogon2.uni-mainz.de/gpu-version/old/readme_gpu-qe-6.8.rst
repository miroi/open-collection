============================
GPU version of QE on MogonII
============================

module purge
#module load system/CUDAcore/11.1.1
#module load compiler/PGI
module load compiler/NVHPC/21.7

mirilias@login22.mogon:~/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8/.module list

Currently Loaded Modules:
  1) system/CUDAcore/11.2.2   2) compiler/NVHPC/21.7


mirilias@login22.mogon:~/work/software/quantum_espresso/.wget https://github.com/QEF/q-e/archive/refs/tags/qe-6.8.zip
/home/mirilias/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8

Test of loaded modules
----------------------
mirilias@login22.mogon:~/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8/.echo $CUDA_HOME
/cluster/easybuild/broadwell/software/CUDAcore/11.2.2

mirilias@login22.mogon:~/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8/.echo $LD_LIBRARY_PATH
/cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib:/cluster/easybuild/broadwell/software/CUDAcore/11.2.2/nvvm/lib64:/cluster/easybuild/broadwell/software/CUDAcore/11.2.2/extras/CUPTI/lib64:/cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib

Configure 
---------
mirilias@login22.mogon:~/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8/../configure --with-cuda=yes --with-cuda-cc=60 --with-cuda-runtime=11.0
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
checking for mpiifort... no
checking for mpif90... no
checking for ifort... no
checking for nvfortran... nvfortran
checking whether we are using the GNU Fortran compiler... no
checking whether nvfortran accepts -g... yes
checking version of nvfortran... nvfortran 21.7-0
checking for Fortran flag to compile .f90 files... none
setting F90... nvfortran
setting MPIF90... nvfortran
checking for pgcc... pgcc
checking whether we are using the GNU C compiler... yes
checking whether pgcc accepts -g... yes
checking for pgcc option to accept ISO C89... none needed
setting CC... pgcc
setting CFLAGS... -fast -Mpreprocess
using F90... nvfortran
setting FFLAGS... -fast
setting F90FLAGS... -fast -Mcache_align -Mpreprocess -Mlarge_arrays
setting FFLAGS_NOOPT... -O0
setting FFLAGS_NOMAIN... -Mnomain
setting CPP... cpp
setting CPPFLAGS... -P -traditional -Uvector
setting LD... nvfortran
setting LDFLAGS...
checking for Fortran flag to compile .f90 files... (cached) none
checking whether Fortran compiler accepts -cuda -gpu=cuda11.0... yes
checking for /usr/local/cuda/... no
checking for /usr/local/cuda/include... no
checking for /usr/local/cuda/lib64... no
checking for nvcc... /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/bin/nvcc
checking whether nvcc works... no
checking for cusolverDnZhegvdx_bufferSize in -lcusolver... yes
checking whether make sets $(MAKE)... yes
checking whether Fortran files must be preprocessed... no
checking whether we are using the GNU Fortran 77 compiler... no
checking whether nvfortran accepts -g... yes
checking for library containing dgemm... no
MKL not found
in /opt/intel/mkl/lib/intel64: checking for library containing dgemm... no
MKL not found
in /cluster/easybuild/broadwell/software/Python/3.8.6-GCCcore-10.2.0/lib: checking for library containing dgemm... no
MKL not found
in /cluster/easybuild/broadwell/software/SQLite/3.33.0-GCCcore-10.2.0/lib: checking for library containing dgemm... no
MKL not found
in /cluster/easybuild/broadwell/software/GCCcore/10.2.0/lib64: checking for library containing dgemm... no
MKL not found
in /cluster/easybuild/broadwell/software/GCCcore/10.2.0/lib: checking for library containing dgemm... no
MKL not found
in /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib: checking for library containing dgemm... no
MKL not found
in /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/nvvm/lib64: checking for library containing dgemm... no
MKL not found
in /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/extras/CUPTI/lib64: checking for library containing dgemm... no
MKL not found
in /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib: checking for library containing dgemm... no
MKL not found
checking for library containing dgemm... no
in /usr/local/lib: checking for library containing dgemm... no
in /cluster/easybuild/broadwell/software/Python/3.8.6-GCCcore-10.2.0/lib: checking for library containing dgemm... no
in /cluster/easybuild/broadwell/software/SQLite/3.33.0-GCCcore-10.2.0/lib: checking for library containing dgemm... no
in /cluster/easybuild/broadwell/software/GCCcore/10.2.0/lib64: checking for library containing dgemm... no
in /cluster/easybuild/broadwell/software/GCCcore/10.2.0/lib: checking for library containing dgemm... no
in /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib: checking for library containing dgemm... no
in /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/nvvm/lib64: checking for library containing dgemm... no
in /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/extras/CUPTI/lib64: checking for library containing dgemm... no
in /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib: checking for library containing dgemm... no
checking for library containing dgemm... -lblas
setting BLAS_LIBS... -lblas
checking for library containing dspev... -llapack
in /usr/local/lib: checking for library containing dspev... -llapack
in /cluster/easybuild/broadwell/software/Python/3.8.6-GCCcore-10.2.0/lib: checking for library containing dspev... -llapack
in /cluster/easybuild/broadwell/software/SQLite/3.33.0-GCCcore-10.2.0/lib: checking for library containing dspev... -llapack
in /cluster/easybuild/broadwell/software/GCCcore/10.2.0/lib64: checking for library containing dspev... -llapack
in /cluster/easybuild/broadwell/software/GCCcore/10.2.0/lib: checking for library containing dspev... -llapack
in /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib: checking for library containing dspev... -llapack
in /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/nvvm/lib64: checking for library containing dspev... -llapack
in /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/extras/CUPTI/lib64: checking for library containing dspev... -llapack
in /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib: checking for library containing dspev... -llapack
checking FFT... checking for library containing dfftw_execute_dft... -lfftw3
 -lfftw3 
checking MASS... 
checking for library containing mpi_init... no
checking ELPA... 
checking for ranlib... ranlib
checking for wget... wget -O
setting WGET... wget -O
setting DFLAGS... -D__PGI -D__CUDA -D__USE_CUSOLVER -D__FFTW3
setting IFLAGS... -I$(TOPDIR)/include -I$(TOPDIR)/FoX/finclude
configure: creating ./config.status
config.status: creating install/make_lapack.inc
config.status: creating include/configure.h
config.status: creating make.inc
config.status: creating configure.msg
config.status: creating install/make_wannier90.inc
config.status: creating include/qe_cdefs.h

ESPRESSO can take advantage of several optimized numerical libraries
(essl, fftw, mkl...).  This configure script attempts to find them,
but may fail if they have been installed in non-standard locations.
If a required library is not found, the local copy will be compiled.

The following libraries have been found:
  BLAS_LIBS= -lblas 
  LAPACK_LIBS=-L/cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib -llapack  -lblas 
  FFT_LIBS= -lfftw3 
  
  

Please check if this is what you expect.

If any libraries are missing, you may specify a list of directories
to search and retry, as follows:
  ./configure LIBDIRS="list of directories, separated by spaces"

Parallel environment not detected \(is this a parallel machine?\).\
Configured for compilation of serial executables.

For more info, read the ESPRESSO User's Guide (Doc/users-guide.tex).

configure: success
mirilias@login22.mogon:~/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8/.


