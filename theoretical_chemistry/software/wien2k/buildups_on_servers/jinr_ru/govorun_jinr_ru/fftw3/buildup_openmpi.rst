FFTW3 for Wien2k
================


http://fftw.org/download.html

download and unpack
~~~~~~~~~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/fftw3/.wget http://fftw.org/fftw-3.3.10.tar.gz

milias@hydra.jinr.ru:~/work/software/fftw3/.nohup tar xvzf fftw-3.3.10.tar.gz  &
[1] 63599

configuration and installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/fftw3/fftw-3.3.10/.less INSTALL

milias@hydra.jinr.ru:~/work/software/fftw3/fftw-3.3.10/.module load openmpi
milias@hydra.jinr.ru:~/work/software/fftw3/fftw-3.3.10/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1               3) Python/v3.10.2           5) openmpi/v4.1.1_gcc1120
  2) BASE/1.0                 4) gcc/v11.2.0

milias@hydra.jinr.ru:~/work/software/fftw3/fftw-3.3.10/../configure --help
milias@hydra.jinr.ru:~/work/software/fftw3/fftw-3.3.10/../configure --enable-mpi --enable-openmp --prefix=/lustre/home/user/m/milias/work/software/fftw3

make install

milias@hydra.jinr.ru:~/work/software/fftw3/.ls
bin/  fftw-3.3.10/  fftw-3.3.10.tar.gz  include/  lib/  nohup.out  share/


