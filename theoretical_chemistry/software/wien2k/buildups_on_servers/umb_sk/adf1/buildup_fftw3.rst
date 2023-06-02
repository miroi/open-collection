=============
FFTW3 on adf1
=============

milias@adf1:~/Work/software/fftw3/.wget --no-check-certificate  https://www.fftw.org/fftw-3.3.10.tar.gz
tar xvzf https://www.fftw.org/fftw-3.3.10.tar.gz
milias@adf1:~/Work/software/fftw3/fftw-3.3.10/../configure --prefix=/home/milias/Work/software/fftw3
milias@adf1:~/Work/software/fftw3/fftw-3.3.10/.make -j4 all install


milias@adf1:~/Work/software/fftw3/fftw-3.3.10/.ls ../
bin/  fftw-3.3.10/  fftw-3.3.10.tar.gz  include/  lib/  share/

