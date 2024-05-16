ELPA buildup
============

download and unpack
~~~~~~~~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/elpa/.wget https://elpa.mpcdf.mpg.de/software/tarball-archive/Releases/2024.03.001/elpa-2024.03.001.tar.gz

milias@hydra.jinr.ru:~/work/software/elpa/.tar xvzf elpa-2024.03.001.tar.gz

milias@hydra.jinr.ru:~/work/software/elpa/elpa-2024.03.001/../configure --help

/lustre/home/user/m/milias/work/software/elpa/elpa-2024.03.001_gnu_openmpi

module load openmpi/v4.1.1_gcc1120 intel

milias@hydra.jinr.ru:~/work/software/elpa/elpa-2024.03.001/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1               3) gcc/v11.2.0              5) intel/v2021.1
  2) Python/v3.10.2           4) openmpi/v4.1.1_gcc1120

Intel for MKL libs !!!

configure and compile
~~~~~~~~~~~~~~~~~~~~~

milias@hydra.jinr.ru:~/work/software/elpa/elpa-2024.03.001/../configure --prefix=/lustre/home/user/m/milias/work/software/elpa/elpa-2024.03.001_gnu_openmpi  --enable-openmp

checking whether we can link a program with a blas lib... no
configure: error: could not link with blas: specify path


milias@hydra.jinr.ru:~/work/software/elpa/elpa-2024.03.001/.module load intel
milias@hydra.jinr.ru:~/work/software/elpa/elpa-2024.03.001/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1       2) BASE/1.0         3) Python/v3.10.2   4) intel/v2021.1


