==============
QE on HPCC UMB
==============

milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-6.7/.which mpirun
/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/bin/mpirun
milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-6.7/.which ifort
/mnt/apps/intel/composer_xe_2013_sp1.1.106/bin/intel64/ifort
milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-6.7/.which mpirun
/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/bin/mpirun
milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-6.7/.mpif90 --version
ifort (IFORT) 14.0.1 20131008
Copyright (C) 1985-2013 Intel Corporation.  All rights reserved.

milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-6.7/../configure
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
checking whether we are using the GNU Fortran compiler... no
checking whether mpif90 accepts -g... yes
checking version of mpif90... ifort 14
checking for Fortran flag to compile .f90 files... none
setting F90... ifort
setting MPIF90... mpif90
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
setting LD... mpif90
setting LDFLAGS...
checking whether make sets $(MAKE)... yes
checking whether Fortran files must be preprocessed... no
checking whether we are using the GNU Fortran 77 compiler... no
checking whether ifort accepts -g... yes
checking for library containing dgemm... -lmkl_intel_lp64
setting BLAS_LIBS... -lmkl_intel_lp64 -lmkl_sequential -lmkl_core
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
setting IFLAGS... -I$(TOPDIR)/include -I$(TOPDIR)/FoX/finclude -I/mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/include
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


milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-6.7/.make -j6 all
.
.
milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-6.7/.ldd bin/pw.x
        linux-vdso.so.1 =>  (0x00007ffdce99d000)
        libmkl_scalapack_lp64.so => /mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64/libmkl_scalapack_lp64.so (0x00007efed944c000)
        libmkl_intel_lp64.so => /mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64/libmkl_intel_lp64.so (0x00007efed8d08000)
        libmkl_sequential.so => /mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64/libmkl_sequential.so (0x00007efed8645000)
        libmkl_core.so => /mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64/libmkl_core.so (0x00007efed6f87000)
        libmpi_usempif08.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib/libmpi_usempif08.so.40 (0x00007efed6d54000)
        libmpi_usempi_ignore_tkr.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib/libmpi_usempi_ignore_tkr.so.40 (0x00007efed6b49000)
        libmpi_mpifh.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib/libmpi_mpifh.so.40 (0x00007efed68e4000)
        libmpi.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib/libmpi.so.40 (0x00007efed6598000)
        libm.so.6 => /lib64/libm.so.6 (0x00007efed6296000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007efed607a000)
        libc.so.6 => /lib64/libc.so.6 (0x00007efed5cac000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007efed5a96000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007efed5892000)
        libopen-rte.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib/libopen-rte.so.40 (0x00007efed55b8000)
        libopen-pal.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib/libopen-pal.so.40 (0x00007efed5273000)
        librt.so.1 => /lib64/librt.so.1 (0x00007efed506b000)
        libutil.so.1 => /lib64/libutil.so.1 (0x00007efed4e68000)
        libz.so.1 => /lib64/libz.so.1 (0x00007efed4c52000)
        libifport.so.5 => /mnt/apps/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64/libifport.so.5 (0x00007efed4a23000)
        libifcore.so.5 => /mnt/apps/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64/libifcore.so.5 (0x00007efed46e3000)
        libimf.so => /mnt/apps/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64/libimf.so (0x00007efed421c000)
        libintlc.so.5 => /mnt/apps/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64/libintlc.so.5 (0x00007efed3fc6000)
        libsvml.so => /mnt/apps/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64/libsvml.so (0x00007efed33cf000)
        libifcoremt.so.5 => /mnt/apps/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64/libifcoremt.so.5 (0x00007efed3061000)
        libirng.so => /mnt/apps/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64/libirng.so (0x00007efed2e5a000)
        /lib64/ld-linux-x86-64.so.2 (0x00007efed9d1e000)

