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

