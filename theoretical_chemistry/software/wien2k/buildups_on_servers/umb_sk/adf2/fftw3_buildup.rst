=============
FFTW3 buildup
=============

milias@adf2:~/work/software/fftw3/fftw-3.3.10/.module load mpi/openmpi3-x86_64
milias@adf2:~/work/software/fftw3/fftw-3.3.10/../configure  --enable-mpi  --prefix=$PWD

see  milias@adf2:~/work/software/fftw3/fftw-3.3.10/.less config.log 

milias@adf2:~/work/software/fftw3/fftw-3.3.10/.make -j8 all install


milias@adf2:~/work/software/fftw3/fftw-3.3.10/.ls bin/ lib/ include/
bin/:
fftw-wisdom*  fftw-wisdom-to-conf*

include/:
fftw3-mpi.f03  fftw3-mpi.h  fftw3.f  fftw3.f03  fftw3.h  fftw3l-mpi.f03  fftw3l.f03  fftw3q.f03

lib/:
cmake/  libfftw3.a  libfftw3.la*  libfftw3_mpi.a  libfftw3_mpi.la*  pkgconfig/


