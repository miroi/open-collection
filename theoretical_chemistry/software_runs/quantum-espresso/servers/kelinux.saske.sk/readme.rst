QE on kelinux.saske.sk
======================

ilias@login1.kelinux.saske.sk:~/work/qch/software/quantum-espresso/.wget https://github.com/QEF/q-e/releases/download/qe-6.7.0/qe-6.7-ReleasePack.tgz

ilias@login1.kelinux.saske.sk:~/work/qch/software/quantum-espresso/.module list

Currently Loaded Modules:
  1) prun/1.3   2) gnu7/7.3.0   3) ohpc   4) openmpi3/3.1.0   5) openblas/0.2.20

ilias@login1.kelinux.saske.sk:~/work/qch/software/quantum-espresso/qe-6.7/../configure
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
checking for mpif90... mpif90
checking whether we are using the GNU Fortran compiler... yes
checking whether mpif90 accepts -g... yes
checking version of mpif90... gfortran 7.3
checking for Fortran flag to compile .f90 files... none
setting F90... gfortran
setting MPIF90... mpif90
checking for cc... cc
checking whether we are using the GNU C compiler... yes
checking whether cc accepts -g... yes
checking for cc option to accept ISO C89... none needed
setting CC... cc
setting CFLAGS... -O3
using F90... gfortran
setting FFLAGS... -O3 -g
setting F90FLAGS... $(FFLAGS) -cpp
setting FFLAGS_NOOPT... -O0 -g
setting CPP... cpp
setting CPPFLAGS... -P -traditional -Uvector
setting LD... mpif90
setting LDFLAGS... -g
checking whether make sets $(MAKE)... yes
checking whether Fortran files must be preprocessed... no
checking whether we are using the GNU Fortran 77 compiler... yes
checking whether gfortran accepts -g... yes
checking for library containing dgemm... -lmkl_gf_lp64
setting BLAS_LIBS... -lmkl_gf_lp64 -lmkl_sequential -lmkl_core
checking FFT...
checking MASS...
checking for library containing mpi_init... none required
checking for library containing pdgemr2d... no
checking for library containing pdgemr2d... -lmkl_scalapack_lp64
checking ELPA...
checking BEEF... -lbeef
setting BEEF_LIBS... $(TOPDIR)/LIBBEEF/libbeef.a
checking for ranlib... ranlib
checking for wget... wget -O
setting WGET... wget -O
setting DFLAGS... -D__DFTI -D__MPI -D__SCALAPACK
setting IFLAGS... -I$(TOPDIR)/include -I$(TOPDIR)/FoX/finclude -I/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/include
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
  BLAS_LIBS=  -lmkl_gf_lp64  -lmkl_sequential -lmkl_core
  LAPACK_LIBS=
  SCALAPACK_LIBS=-lmkl_scalapack_lp64 -lmkl_blacs_openmpi_lp64
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
ilias@login1.kelinux.saske.sk:~/work/qch/software/quantum-espresso/qe-6.7/.

make -j6 all


ilias@login1.kelinux.saske.sk:~/work/qch/software/quantum-espresso/qe-6.7/.ldd bin/pw.x
        linux-vdso.so.1 =>  (0x00007fffd99f1000)
        libmkl_scalapack_lp64.so => /lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_scalapack_lp64.so (0x00007ff4b56de000)
        libmkl_blacs_openmpi_lp64.so => /lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_blacs_openmpi_lp64.so (0x00007ff4b549b000)
        libmkl_gf_lp64.so => /lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_gf_lp64.so (0x00007ff4b49b6000)
        libmkl_sequential.so => /lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_sequential.so (0x00007ff4b35be000)
        libmkl_core.so => /lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_core.so (0x00007ff4af5b5000)
        libmpi_usempif08.so.40 => /opt/ohpc/pub/mpi/openmpi3-gnu7/3.1.0/lib/libmpi_usempif08.so.40 (0x00007ff4af384000)
        libmpi_usempi_ignore_tkr.so.40 => /opt/ohpc/pub/mpi/openmpi3-gnu7/3.1.0/lib/libmpi_usempi_ignore_tkr.so.40 (0x00007ff4af17d000)
        libmpi_mpifh.so.40 => /opt/ohpc/pub/mpi/openmpi3-gnu7/3.1.0/lib/libmpi_mpifh.so.40 (0x00007ff4aef27000)
        libmpi.so.40 => /opt/ohpc/pub/mpi/openmpi3-gnu7/3.1.0/lib/libmpi.so.40 (0x00007ff4aec10000)
        libgfortran.so.4 => /opt/ohpc/pub/compiler/gcc/7.3.0/lib64/libgfortran.so.4 (0x00007ff4ae83e000)
        libm.so.6 => /lib64/libm.so.6 (0x00007ff4ae53c000)
        libgcc_s.so.1 => /opt/ohpc/pub/compiler/gcc/7.3.0/lib64/libgcc_s.so.1 (0x00007ff4ae325000)
        libquadmath.so.0 => /opt/ohpc/pub/compiler/gcc/7.3.0/lib64/libquadmath.so.0 (0x00007ff4ae0e6000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007ff4adeca000)
        libc.so.6 => /lib64/libc.so.6 (0x00007ff4adafc000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007ff4ad8f8000)
        libopen-rte.so.40 => /opt/ohpc/pub/mpi/openmpi3-gnu7/3.1.0/lib/libopen-rte.so.40 (0x00007ff4ad645000)
        libopen-pal.so.40 => /opt/ohpc/pub/mpi/openmpi3-gnu7/3.1.0/lib/libopen-pal.so.40 (0x00007ff4ad339000)
        libnuma.so.1 => /lib64/libnuma.so.1 (0x00007ff4ad12d000)
        librt.so.1 => /lib64/librt.so.1 (0x00007ff4acf25000)
        libutil.so.1 => /lib64/libutil.so.1 (0x00007ff4acd22000)
        libz.so.1 => /lib64/libz.so.1 (0x00007ff4acb0c000)
        /lib64/ld-linux-x86-64.so.2 (0x00007ff4b5fde000)

