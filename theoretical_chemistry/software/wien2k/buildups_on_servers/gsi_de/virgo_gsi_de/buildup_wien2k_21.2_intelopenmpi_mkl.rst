===================
Wien2k_23.2 buildup
===================



Packages
--------

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack find --loaded
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
autoconf@2.69                automake@1.16.5  gawk@5.1.1  gmp@6.2.1                                  libiconv@1.16    libtool@2.4.7  mpc@1.2.1   ncurses@6.1      perl@5.16.3     texinfo@6.5  zstd@1.5.2
autoconf-archive@2022.02.11  diffutils@3.8    gcc@10.2.0  intel-parallel-studio@professional.2020.1  libsigsegv@2.13  m4@1.4.19      mpfr@4.1.0  patchelf@0.16.1  readline@8.1.2  zlib@1.2.13

-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdfftw@3.0                         cmake@3.24.3      glib@2.74.1           libffi@3.4.2       libxml2@2.10.1  numactl@2.0.14   pmix@3.2.2            sqlite@3.39.4           zstd@1.5.2
amdscalapack@3.2                    curl@7.85.0       gmp@6.2.1             libgcrypt@1.10.1   lz4@1.9.4       openblas@0.3.21  py-pip@22.2.2         tar@1.34
autoconf@2.69                       diffutils@3.8     hwloc@2.8.0           libgpg-error@1.46  m4@1.4.19       openssh@9.1p1    py-setuptools@59.4.0  texinfo@6.5
autoconf-archive@2022.02.11         elpa@2021.11.001  json-c@0.16           libiconv@1.16      meson@0.63.3    openssl@1.1.1s   py-wheel@0.37.1       ucx@1.9.0
automake@1.16.5                     expat@2.4.8       krb5@1.19.3           libmd@1.0.4        mpfr@4.1.0      pcre2@10.39      python@3.10.8         util-linux-uuid@2.38.1
bison@3.8.2                         gawk@5.1.1        libbsd@0.11.5         libpciaccess@0.16  munge@0.5.13    perl@5.16.3      rdma-core@22.4        util-macros@1.19.3
bzip2@1.0.8                         gdbm@1.23         libedit@3.1-20210216  libsigsegv@2.13    ncurses@6.1     pigz@2.7         readline@8.1.2        xz@5.2.7
ca-certificates-mozilla@2022-10-11  gettext@0.21.1    libevent@2.1.12       libtool@2.4.7      ninja@1.11.1    pkgconf@1.8.0    slurm@21-08-8-2       zlib@1.2.13

-- linux-debian10-x86_64 / intel@19.1.1.217 ---------------------
openmpi@4.1.5  pkgconf@1.8.0
==> 88 loaded packages


milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack unload openmpi@4.1.5%gcc
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.mpif90 --version
ifort (IFORT) 19.1.1.217 20200306
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.mpicc --version
icc (ICC) 19.1.1.217 20200306
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.emkl
Intel MKL library ? MKLROOT=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack find --loaded | grep elpa
elpa@2021.11.001
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack find --loaded | grep fftw
amdfftw@3.0

FFTW3 library
~~~~~~~~~~~~~
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/projects/open-collection/theoretical_chemistry/software/wien2k/buildups_on_servers/gsi_de/virgo_gsi_de/.ls /usr/lib/x86_64-linux-gnu/libfftw*
/usr/lib/x86_64-linux-gnu/libfftw3_omp.so.3@     /usr/lib/x86_64-linux-gnu/libfftw3.so.3@     /usr/lib/x86_64-linux-gnu/libfftw3_threads.so.3@
/usr/lib/x86_64-linux-gnu/libfftw3_omp.so.3.5.8  /usr/lib/x86_64-linux-gnu/libfftw3.so.3.5.8  /usr/lib/x86_64-linux-gnu/libfftw3_threads.so.3.5.8



 R   R_LIBS (LAPACK+BLAS):    $(MKLROOT)/lib/intel64/libmkl_blas95_lp64.a $(MKLROOT)/lib/intel64/libmkl_lapack95_lp64.a -L$(MKLROOT)/lib/intel64 -lmkl_scalapack_lp64 -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_lp64 -liomp5 -lpthread -lm -ldl


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
  R   R_LIBS (LAPACK+BLAS):    $(MKLROOT)/lib/intel64/libmkl_blas95_lp64.a $(MKLROOT)/lib/intel64/libmkl_lapack95_lp64.a -L$(MKLROOT)/lib/intel64 -lmkl_scalapack_lp64 -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_lp64 -liomp5 -lpthread -lm -ldl
  F   FFTW options:            -DFFTW3 -DFFTW_OMP -I/usr/lib/x86_64-linux-gnu/include
      FFTW-LIBS:               -L/usr/lib/x86_64-linux-gnu/ -lfftw3 -lfftw3_omp
      FFTW-PLIBS:              NOT FOUND!
  X   LIBX options:
      LIBXC-LIBS:

