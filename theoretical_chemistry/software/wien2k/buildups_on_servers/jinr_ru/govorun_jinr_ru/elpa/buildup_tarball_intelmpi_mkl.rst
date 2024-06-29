ELPA buildup
============

download and unpack
~~~~~~~~~~~~~~~~~~~
wget https://elpa.mpcdf.mpg.de/software/tarball-archive/Releases/2024.03.001/elpa-2024.03.001.tar.gz

tar xvzf elpa-2024.03.001.tar.gz


./configure --help



module load intel/v2021.1

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.module list
Currently Loaded Modulefiles:
  1) BASE/1.0          2) Python/v3.10.13   3) GVR/v1.0-1        4) intel/v2021.1

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.mpiifort --version
ifort (IFORT) 2021.1 Beta 20201112
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.mpiicc --version
icc (ICC) 2021.1 Beta 20201112
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.mpiicpc --version
icpc (ICC) 2021.1 Beta 20201112
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.emkl
Intel MKL library ? MKLROOT=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest


configure and compile
~~~~~~~~~~~~~~~~~~~~~

milias@vm01.hydra.local:~/work/software/elpa/.cp -R elpa-2024.03.001_untouched  elpa-2024.03.001_intelmpi_mkl

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.CXX=mpicpc CC=mpicc FC=mpiifort ./configure --prefix=$PWD  --enable-openmp

configure: error: C++ compiler cannot create executables
See 'config.log' for more details

...leave out mpicpc !

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.g++ --version
g++ (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44)

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/. CC=mpicc FC=mpiifort ./configure --prefix=$PWD  --enable-openmp
configure: error: C++ compiler cannot create executables

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.module add gcc/v12.3.0 
milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.g++ --version
g++ (GCC) 12.3.0


as@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.module list
Currently Loaded Modulefiles:
  1) BASE/1.0          2) Python/v3.10.13   3) GVR/v1.0-1        4) intel/v2021.1     5) gcc/v12.3.0

configure: error: could not link with blas: specify path

Currently Loaded Modulefiles:
  1) BASE/1.0          2) Python/v3.10.13   3) GVR/v1.0-1        4) intel/v2021.1     5) gcc/v12.3.0
milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.LDFLAGS=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64 CC=mpicc  FC=mpiifort ./configure --prefix=$PWD  --enable-openmp


milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.LDFLAGS=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64 CXX=g++ CC=mpiicc   FC=mpiifort    ./configure --prefix=$PWD  --enable-openmp

configure: error: in '/lustre/home/user/m/milias/work/software/elpa/elpa-2024.03.001_intelmpi_mkl':
configure: error: C++ compiler cannot create executables
See 'config.log' for more details

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.SCALAPACK_LDFLAGS=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64 CXX=g++  CC=mpiicc   FC=mpiifort    ./configure --prefix=$PWD  --enable-openmp

milias@vm01.hydra.local:~/work/software/elpa/elpa-2024.03.001_intelmpi_mkl/.SCALAPACK_LDFLAGS="-L$MKLROOT/lib/intel64 -lmkl_scalapack_lp64 -lmkl_intel_lp64 -lmkl_sequential  -lmkl_core -lmkl_blacs_intelmpi_lp64 -lpthread -lm -Wl,-rpath,$MKLROOT/lib/intel64" SCALAPACK_FCFLAGS="-L$MKLROOT/lib/intel64 -lmkl_scalapack_lp64 -lmkl_intel_lp64 -lmkl_sequential -lmkl_core -lmkl_blacs_intelmpi_lp64 -lpthread -lm -I$MKL_HOME/include/intel64/lp64"  CXX=g++ CC=mpiicc   FC=mpiifort    ./configure --prefix=$PWD  --enable-openmp




