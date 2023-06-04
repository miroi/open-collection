=============
FFTW3 buildup
=============

milias@adf2:~/work/software/fftw3/fftw-3.3.10/.module load mpi/openmpi3-x86_64
milias@adf2:~/work/software/fftw3/fftw-3.3.10/../configure --prefix=/home/milias/work/software/fftw3  --enable-openmp 

see  milias@adf2:~/work/software/fftw3/fftw-3.3.10/.less config.log 

milias@adf2:~/work/software/fftw3/fftw-3.3.10/.make -j4 all install

milias@adf2:~/work/software/fftw3/fftw-3.3.10/.ls ../bin/ ../lib/ ../include/

milias@adf2:~/work/software/fftw3/fftw-3.3.10/.ls ../bin/ ../lib/ ../include/                                         
../bin/:
fftw-wisdom*  fftw-wisdom-to-conf*

../include/:
fftw3.f  fftw3.f03  fftw3.h  fftw3l.f03  fftw3q.f03

../lib/:
cmake/  libfftw3.a  libfftw3.la*  libfftw3_omp.a  libfftw3_omp.la*  pkgconfig/

