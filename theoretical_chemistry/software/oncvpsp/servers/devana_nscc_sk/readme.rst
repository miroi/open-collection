=======
ONCVPSP
=======

https://github.com/oncvpsp/oncvpsp


milias@login01.devana.local:~/work/software/oncvpsp/.

module load gcc
module load FlexiBLAS

milias@login01.devana.local:~/work/software/oncvpsp/.module list

Currently Loaded Modules:
  1) gcc/12.2         3) zlib/1.2.12-GCCcore-12.2.0     5) GCC/12.2.0                   7) FlexiBLAS/3.2.1-GCC-12.2.0
  2) GCCcore/12.2.0   4) binutils/2.39-GCCcore-12.2.0   6) OpenBLAS/0.3.21-GCC-12.2.0


milias@login02.devana.local:~/work/software/oncvpsp/.elp
$LD_LIBRARY_PATH: /storage-apps/easybuild/software/FlexiBLAS/3.2.1-GCC-12.2.0/lib

milias@login02.devana.local:~/work/software/oncvpsp/.ep
$PATH: /storage-apps/easybuild/software/FlexiBLAS/3.2.1-GCC-12.2.0/bin

milias@login01.devana.local:~/work/software/oncvpsp/. make all >&make.log




