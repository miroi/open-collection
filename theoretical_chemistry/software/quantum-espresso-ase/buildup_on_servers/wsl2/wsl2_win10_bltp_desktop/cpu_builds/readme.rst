========================
Quantum Espresso buildup
========================

WSL2, MS Windows 10, BLTP Desktop PC

download & unpack
-----------------
register in https://www.quantum-espresso.org/download-page/

https://www.quantum-espresso.org/rdm-download/8/v7-5/56fcba4032c67b74eb9c138e59c579ce/qe-7.5-ReleasePack.tar.gz

milias@DESKTOP-7OTLCGO:~/work/software/qe/.tar xvzf qe-7.5-ReleasePack.tar.gz

configure & compile
-------------------
milias@DESKTOP-7OTLCGO:~/work/software/qe/qe-7.5/../configure  --enable-parallel MPIF90=mpif90.openmpi
milias@DESKTOP-7OTLCGO:~/work/software/qe/qe-7.5/.make -j8 all

milias@DESKTOP-7OTLCGO:~/work/software/qe/qe-7.5/.ls -lt bin/pw.x
lrwxrwxrwx 1 milias milias 14 Aug 21 14:55 bin/pw.x -> ../PW/src/pw.x*
milias@DESKTOP-7OTLCGO:~/work/software/qe/qe-7.5/.ls -lt bin/dos.x
lrwxrwxrwx 1 milias milias 15 Aug 21 14:55 bin/dos.x -> ../PP/src/dos.x*


testing the QE installation
---------------------------
milias@DESKTOP-7OTLCGO:~/work/software/qe/qe-7.5/test-suite/.export PATH=~/work/software/qe/qe-7.5/bin:$PATH
milias@DESKTOP-7OTLCGO:~/work/software/qe/qe-7.5/test-suite/.which pw.x
/home/milias/work/software/qe/qe-7.5/bin/pw.x
milias@DESKTOP-7OTLCGO:~/work/software/qe/qe-7.5/test-suite/.make NRPOCS=10 VERBOSE=1 run-tests

env QE_USE_MPI= env QE_USE_BGRP= /home/milias/work/software/qe/qe-7.5/test-suite/..//test-suite/testcode/bin/testcode.py --verbose --category=pw_all
Using executable: /home/milias/work/software/qe/qe-7.5/test-suite/..//test-suite/run-pw.sh.
Test id: 210826.
Benchmark: git.

pw_atom - atom.in: Passed.

pw_atom - atom-lsda.in: Passed.
.
.





