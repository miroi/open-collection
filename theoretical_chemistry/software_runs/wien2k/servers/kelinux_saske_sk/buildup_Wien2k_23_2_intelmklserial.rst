======================
Wien2k_23.2 on kelinux
======================

Modules
--------
module use /lustre/home/utils/easybuild_old/modules/all/
module load ELPA/2021.11.001-foss-2022a
module load FFTW/3.3.9-intel-2021a

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.module load imkl/2021.2.0-iimpi-2021a
module load ELPA/2021.11.001-foss-2022a

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.module list

Currently Loaded Modules:
  1) prun/1.3                                12) XZ/5.2.5-GCCcore-11.3.0           23) PMIx/4.1.2-GCCcore-11.3.0
  2) gnu7/7.3.0                              13) libxml2/2.9.13-GCCcore-11.3.0     24) UCC/1.0.0-GCCcore-11.3.0
  3) openmpi3/3.1.0                          14) libpciaccess/0.16-GCCcore-11.3.0  25) OpenMPI/4.1.4-GCC-11.3.0
  4) ohpc                                    15) hwloc/2.7.1-GCCcore-11.3.0        26) OpenBLAS/0.3.20-GCC-11.3.0
  5) intel-compilers/2021.2.0                16) OpenSSL/1.1                       27) FlexiBLAS/3.2.0-GCC-11.3.0
  6) impi/2021.2.0-intel-compilers-2021.2.0  17) libevent/2.1.12-GCCcore-11.3.0    28) FFTW/3.3.10-GCC-11.3.0
  7) iimpi/2021a                             18) GCCcore/11.3.0                    29) gompi/2022a
  8) imkl/2021.2.0-iimpi-2021a               19) zlib/1.2.12-GCCcore-11.3.0        30) FFTW.MPI/3.3.10-gompi-2022a
  9) fftw/3.3.8                              20) numactl/2.0.14-GCCcore-11.3.0     31) ScaLAPACK/2.2.0-gompi-2022a-fb
 10) binutils/2.38-GCCcore-11.3.0            21) UCX/1.12.1-GCCcore-11.3.0         32) foss/2022a
 11) GCC/11.3.0                              22) libfabric/1.15.1-GCCcore-11.3.0   33) ELPA/2021.11.001-foss-2022a


ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.emkl
Intel MKL library ? MKLROOT=/lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.ifort --version
ifort (IFORT) 2021.2.0 20210228
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.


module unload OpenMPI/4.1.4-GCC-11.3.0
module unload openmpi3/3.1.0

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.module list

Currently Loaded Modules:
  1) prun/1.3                                12) libxml2/2.9.13-GCCcore-11.3.0     23) UCC/1.0.0-GCCcore-11.3.0
  2) gnu7/7.3.0                              13) libpciaccess/0.16-GCCcore-11.3.0  24) OpenBLAS/0.3.20-GCC-11.3.0
  3) ohpc                                    14) hwloc/2.7.1-GCCcore-11.3.0        25) FlexiBLAS/3.2.0-GCC-11.3.0
  4) intel-compilers/2021.2.0                15) OpenSSL/1.1                       26) FFTW/3.3.10-GCC-11.3.0
  5) impi/2021.2.0-intel-compilers-2021.2.0  16) libevent/2.1.12-GCCcore-11.3.0    27) gompi/2022a
  6) iimpi/2021a                             17) GCCcore/11.3.0                    28) FFTW.MPI/3.3.10-gompi-2022a
  7) imkl/2021.2.0-iimpi-2021a               18) zlib/1.2.12-GCCcore-11.3.0        29) ScaLAPACK/2.2.0-gompi-2022a-fb
  8) fftw/3.3.8                              19) numactl/2.0.14-GCCcore-11.3.0     30) foss/2022a
  9) binutils/2.38-GCCcore-11.3.0            20) UCX/1.12.1-GCCcore-11.3.0         31) ELPA/2021.11.001-foss-2022a
 10) GCC/11.3.0                              21) libfabric/1.15.1-GCCcore-11.3.0
 11) XZ/5.2.5-GCCcore-11.3.0                 22) PMIx/4.1.2-GCCcore-11.3.0

 
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

LI
mpiifort
mpiicc
MKL_TARGET_ARCH was set to intel64

