===============
DIRAC on WSL PC
===============

MKL library
------------
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.sudo apt-get install intel-mkl-full libmkl-gf-ilp64 libmkl-gf-lp64 libmkl-gnu-thread libmkl-scalapack-ilp64 libmkl-scalapack-lp64
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
intel-mkl-full is already the newest version (2020.4.304-2ubuntu3).
libmkl-gf-ilp64 is already the newest version (2020.4.304-2ubuntu3).
libmkl-gf-ilp64 set to manually installed.
libmkl-gf-lp64 is already the newest version (2020.4.304-2ubuntu3).
libmkl-gf-lp64 set to manually installed.
libmkl-gnu-thread is already the newest version (2020.4.304-2ubuntu3).
libmkl-gnu-thread set to manually installed.
libmkl-scalapack-ilp64 is already the newest version (2020.4.304-2ubuntu3).
libmkl-scalapack-ilp64 set to manually installed.
libmkl-scalapack-lp64 is already the newest version (2020.4.304-2ubuntu3).
libmkl-scalapack-lp64 set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 17 not upgraded.

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.mpif90 --version
GNU Fortran (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.mpicc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.mpicxx --version
g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.mpirun --version
mpirun (Open MPI) 4.1.2

buildup
~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/../setup  --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx   build_gnu_mkl_ilp64


