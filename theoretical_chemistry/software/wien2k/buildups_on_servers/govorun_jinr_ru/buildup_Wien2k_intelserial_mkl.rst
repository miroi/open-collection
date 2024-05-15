Wien2k buildup
==============

module load  openmpi fftw ELPA

module list

FFTW3
~~~~~

/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/latest-release

ScaLAPACK
~~~~~~~~~

ELPA
~~~~
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/ELPA/v2020.05.001_intel2018_python365

/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/ELPA/v2020.05.001_intel2018_python365/lib/

 Please specify the name of your installed ELPA library (e.g. elpa or elpa_openmp):
elpa


Compilation of lapw0:
~~~~~~~~~~~~~~~~~~~~

xcpot1.o xcpot1Q.o xcpot3.o ykav.o ylm.o coulint.o c_alpha_m.o gaunt.o notri.o t3j0.o t3j.o ph.o finl_elect_str.o kahan_summ_gxyz.o stress_gga.o -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/include  -DFFTW3 -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/include  -qopenmp -L/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/ -lpthread -lm -ldl -liomp5 -L/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5//cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/latest-release -llib  -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core
ld: cannot find -llib
make[1]: *** [lapw0] Error 1


mpiifort -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/include  -DFFTW3 -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.7-5/include  -qopenmp -DParallel -c fft_modules.F
fft_modules.F(62): error #5102: Cannot open include file 'fftw3-mpi.f03'
        include 'fftw3-mpi.f03'


