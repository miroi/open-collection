ELPA buildup
============

download and unpack
~~~~~~~~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/elpa/.wget https://elpa.mpcdf.mpg.de/software/tarball-archive/Releases/2024.03.001/elpa-2024.03.001.tar.gz

milias@hydra.jinr.ru:~/work/software/elpa/.tar xvzf elpa-2024.03.001.tar.gz

milias@hydra.jinr.ru:~/work/software/elpa/elpa-2024.03.001/../configure --help

/lustre/home/user/m/milias/work/software/elpa/elpa-2024.03.001_gnu_openmpi

module load openmpi/v4.1.1_gcc1120   LAPACK

milias@hydra.jinr.ru:~/work/software/elpa/elpa-2024.03.001/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1               3) Python/v3.10.2           5) openmpi/v4.1.1_gcc1120
  2) BASE/1.0                 4) gcc/v11.2.0              6) LAPACK/v3.9.0


configure and compile
~~~~~~~~~~~~~~~~~~~~~

milias@hydra.jinr.ru:~/work/software/elpa/elpa-2024.03.001/../configure --prefix=/lustre/home/user/m/milias/work/software/elpa/elpa-2024.03.001_gnu_openmpi  --enable-openmp



