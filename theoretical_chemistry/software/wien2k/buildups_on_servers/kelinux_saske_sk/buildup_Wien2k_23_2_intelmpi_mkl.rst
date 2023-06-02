======================
Wien2k_23.2 on kelinux
======================

see also https://www.youtube.com/watch?v=K9q2rCBf33Y

Modules
--------
module use /lustre/home/utils/easybuild_old/modules/all/
module load ELPA/2021.11.001-foss-2022a
module load FFTW/3.3.9-intel-2021a

module load imkl/2021.2.0-iimpi-2021a
module load ELPA/2021.11.001-foss-2022a

module unload OpenMPI/4.1.4-GCC-11.3.0
module unload openmpi3/3.1.0

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.module unload FFTW.MPI/3.3.10-gompi-2022a ScaLAPACK/2.2.0-gompi-2022a-fb 
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.module load FFTW/3.3.9-intel-2021a

module list
Currently Loaded Modules:
  1) prun/1.3                          10) libevent/2.1.12-GCCcore-11.3.0   19) binutils/2.36.1-GCCcore-10.3.0
  2) gnu7/7.3.0                        11) libfabric/1.15.1-GCCcore-11.3.0  20) intel-compilers/2021.2.0
  3) ohpc                              12) PMIx/4.1.2-GCCcore-11.3.0        21) GCCcore/10.3.0
  4) GCC/11.3.0                        13) UCC/1.0.0-GCCcore-11.3.0         22) numactl/2.0.14-GCCcore-10.3.0
  5) XZ/5.2.5-GCCcore-11.3.0           14) OpenBLAS/0.3.20-GCC-11.3.0       23) impi/2021.2.0-intel-compilers-2021.2.0
  6) libxml2/2.9.13-GCCcore-11.3.0     15) FlexiBLAS/3.2.0-GCC-11.3.0       24) iimpi/2021a
  7) libpciaccess/0.16-GCCcore-11.3.0  16) gompi/2022a                      25) intel/2021a
  8) hwloc/2.7.1-GCCcore-11.3.0        17) foss/2022a                       26) imkl/2021.2.0-iimpi-2021a
  9) OpenSSL/1.1                       18) ELPA/2021.11.001-foss-2022a      27) FFTW/3.3.9-intel-2021a


Check compilers and libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.which mpirun
/lustre/home/utils/easybuild_old/software/impi/2021.2.0-intel-compilers-2021.2.0/mpi/2021.2.0/bin/mpirun

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.which mpirun
/lustre/home/utils/easybuild_old/software/impi/2021.2.0-intel-compilers-2021.2.0/mpi/2021.2.0/bin/mpirun
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.which mpiifort 
/lustre/home/utils/easybuild_old/software/impi/2021.2.0-intel-compilers-2021.2.0/mpi/2021.2.0/bin/mpiifort
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.mpiifort --version
ifort (IFORT) 2021.2.0 20210228
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.ifort --version
ifort (IFORT) 2021.2.0 20210228
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2021.2 Build 20210302 (id: f4f7c92cd)
Copyright 2003-2021, Intel Corporation.

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.mpiifort --version
ifort (IFORT) 2021.2.0 20210228
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.mpiicc --version
icc (ICC) 2021.2.0 20210228
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.


ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.export MKL_TARGET_ARCH=linuxifs

Wien2k buildup
--------------

gunzip *
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.expand_lapw
.
.
python found at /usr/bin/python.

WIEN is now expanded. The shell-script commands were copied and links created.
To configure your Fortran-executables run:

./siteconfig_lapw

Configuration and compilation
-----------------------------

S: LS, linuxifs
C: mpiifort, mpicc
MKL_TARGET_ARCH was set to intel64
O:
P:

Compiler options:
-----------------

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
  F   FFTW options:
      FFTW-LIBS:
  X   LIBX options:
      LIBXC-LIBS:

  PO  Parallel options

  S   Save and Quit
  Q   Quit and abandon changes


 R   R_LIBS (LAPACK+BLAS):    $(MKLROOT)/lib/intel64/libmkl_blas95_lp64.a $(MKLROOT)/lib/intel64/libmkl_lapack95_lp64.a -L$(MKLROOT)/lib/intel64 -lmkl_scalapack_lp64 -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_lp64 -liomp5 -lpthread -lm -ldl

FFTW
~~~~

  Your current FFTW options are:
   
   FFTW_OPT:             -DFFTW3 -I/lustre/home/utils/easybuild_old/software/FFTW/3.3.9-intel-2021a/lib/include
   FFTW_LIBS:            -L/lustre/home/utils/easybuild_old/software/FFTW/3.3.9-intel-2021a/lib/lib64 -lfftw3
   
   which are derived from following settings:
   
   R  FFTWROOT:          /lustre/home/utils/easybuild_old/software/FFTW/3.3.9-intel-2021a/lib/
   V  FFTW_VERSION:      FFTW3
   L  FFTW_LIB:          lib64
   N  FFTW_LIBNAME:      fftw3

ELPA
~~~~
ls /lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a
bin/  easybuild/  include/  lib/  lib64@  share/

   Your current ELPA options are:
   
   ELPA_OPT:             -DELPA -I/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/include/elpa_openmp-2021.11.001/elpa 
                  -I/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/include/elpa_openmp-2021.11.001/modules
   ELPA_LIBS:            -lelpa_openmp -L/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/lib64 -Wl,-rpath=/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/lib64
   
   which are derived from following settings:
   
   R  ELPAROOT:          /lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/
   V  ELPA_VERSION:      2021.11.001
   L  ELPA_LIB:          lib64
   N  ELPA_LIBNAME:      elpa_openmp


