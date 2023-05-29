=========================
Wien2k on @lxir127.gsi.de
=========================

Loading of packages
-------------------
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.spack load intel-mkl@2020.4.304
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.spack load intel-parallel-studio@professional.2020.1
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.spack load amdfftw@3.0 arch=broadwell

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.spack find --loaded
==> 41 loaded packages
-- linux-debian10-broadwell / gcc@8.3.0 -------------------------
amdfftw@3.0   gettext@0.21    libffi@3.3         libpciaccess@0.16  openmpi@3.1.6   rdma-core@20     util-linux-uuid@2.36.2
bzip2@1.0.8   glib@2.70.0     libgcrypt@1.9.3    libxml2@2.9.12     openssl@1.1.1l  readline@8.1     xz@5.2.5
cmake@3.21.4  hwloc@1.11.13   libgpg-error@1.42  lz4@1.9.3          pcre@8.44       slurm@18-08-9-1  zlib@1.2.11
curl@7.79.0   json-c@0.15     libiconv@1.16      munge@0.5.13       perl@5.28.1     sqlite@3.36.0
expat@2.4.1   libbsd@0.11.3   libmd@1.0.3        ncurses@6.1        pmix@2.2.2      tar@1.34
gdbm@1.21     libevent@2.1.8  libnl@3.3.0        numactl@2.0.14     python@3.8.12   texinfo@6.5

-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
intel-mkl@2020.4.304  intel-parallel-studio@professional.2020.1

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.spack unload openmpi@3.1.6
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.which mpif90
/u/milias/bin/openmpi/bin/mpif90

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.spack find --loaded
==> 40 loaded packages
-- linux-debian10-broadwell / gcc@8.3.0 -------------------------
amdfftw@3.0   gettext@0.21    libffi@3.3         libpciaccess@0.16  openssl@1.1.1l  readline@8.1            xz@5.2.5
bzip2@1.0.8   glib@2.70.0     libgcrypt@1.9.3    libxml2@2.9.12     pcre@8.44       slurm@18-08-9-1         zlib@1.2.11
cmake@3.21.4  hwloc@1.11.13   libgpg-error@1.42  lz4@1.9.3          perl@5.28.1     sqlite@3.36.0
curl@7.79.0   json-c@0.15     libiconv@1.16      munge@0.5.13       pmix@2.2.2      tar@1.34
expat@2.4.1   libbsd@0.11.3   libmd@1.0.3        ncurses@6.1        python@3.8.12   texinfo@6.5
gdbm@1.21     libevent@2.1.8  libnl@3.3.0        numactl@2.0.14     rdma-core@20    util-linux-uuid@2.36.2

-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
intel-mkl@2020.4.304  intel-parallel-studio@professional.2020.1



Intel-OpeMPI 
~~~~~~~~~~~~~
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.export PATH=/u/milias/bin/openmpi/bin:$PATH
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.export LD_LIBRARY_PATH=/u/milias/bin/openmpi/lib:$LD_LIBRARY_PATH

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.which mpif90
/u/milias/bin/openmpi/bin/mpif90
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.which mpirun
/u/milias/bin/openmpi/bin/mpirun

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.mpif90 --version
ifort (IFORT) 19.1.1.217 20200306
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.mpirun --version
mpirun (Open MPI) 3.1.0

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.emkl
Intel MKL library ? MKLROOT=/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/mkl


Upacking
---------
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.tar xvf WIEN2k_21.1.tar 
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/gunzip *
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.expand_lapw 
.
.
case.win   linked to   template.win
python found at /usr/bin/python.

WIEN is now expanded. The shell-script commands were copied and links created.
To configure your Fortran-executables run:

./siteconfig_lapw


Wien2k configuration
--------------------
LI
mpif90
mpicc
MKL_TARGET_ARCH was set to intel64

Recommended options for system linuxifc are:
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
  R   R_LIBS (LAPACK+BLAS):    $MKLROOT/lib/intel64/libmkl_blas95_lp64.a $MKLROOT/lib/intel64/libmkl_lapack95_lp64.a -L$MKLROOT/lib/intel64 -lmkl_scalapack_lp64 -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_lp64 -liomp5 -lpthread -lm -ldl
  F   FFTW options:            -DFFTW3 -DFFTW_OMP -I/usr/lib/x86_64-linux-gnu/include
      FFTW-LIBS:               -L/usr/lib/x86_64-linux-gnu/ -lfftw3 -lfftw3_omp
  X   LIBX options:
      LIBXC-LIBS:

compilation ...



