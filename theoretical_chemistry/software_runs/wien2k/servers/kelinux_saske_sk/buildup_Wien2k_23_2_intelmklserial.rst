======================
Wien2k_23.2 on kelinux
======================

Modules
--------
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.module load imkl/2021.2.0-iimpi-2021a
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.module list

Currently Loaded Modules:
  1) prun/1.3         6) zlib/1.2.11-GCCcore-10.3.0      11) impi/2021.2.0-intel-compilers-2021.2.0
  2) gnu7/7.3.0       7) binutils/2.36.1-GCCcore-10.3.0  12) iimpi/2021a
  3) openmpi3/3.1.0   8) intel-compilers/2021.2.0        13) imkl/2021.2.0-iimpi-2021a
  4) ohpc             9) numactl/2.0.14-GCCcore-10.3.0
  5) GCCcore/10.3.0  10) UCX/1.10.0-GCCcore-10.3.0
 

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.emkl
Intel MKL library ? MKLROOT=/lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.ifort --version
ifort (IFORT) 2021.2.0 20210228
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.module load imkl/2021.2.0-iimpi-2021a
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.module list

Currently Loaded Modules:
  1) prun/1.3         6) zlib/1.2.11-GCCcore-10.3.0      11) impi/2021.2.0-intel-compilers-2021.2.0
  2) gnu7/7.3.0       7) binutils/2.36.1-GCCcore-10.3.0  12) iimpi/2021a
  3) openmpi3/3.1.0   8) intel-compilers/2021.2.0        13) imkl/2021.2.0-iimpi-2021a
  4) ohpc             9) numactl/2.0.14-GCCcore-10.3.0
  5) GCCcore/10.3.0  10) UCX/1.10.0-GCCcore-10.3.0

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.emkl
Intel MKL library ? MKLROOT=/lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.ifort --version
ifort (IFORT) 2021.2.0 20210228
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_intelmklserial/.


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






