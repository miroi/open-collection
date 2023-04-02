Wien2k_23.2 on kelinux
======================


Modules
--------

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2/.module load imkl/2021.2.0-iimpi-2021a
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2/.module list

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2/.emkl
Intel MKL library ? MKLROOT=/lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0

module use /lustre/home/utils/easybuild_old/modules/all/


Wien2k buildup
--------------

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2/.gunzip *

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2/.expand_lapw

python found at /usr/bin/python.

WIEN is now expanded. The shell-script commands were copied and links created.
To configure your Fortran-executables run:

./siteconfig_lapw

LS   Linux+SLURM-batchsystem (Intel ifort (12.0 or later)+mkl+intelmpi)

mpiifort ....




