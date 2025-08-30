=================
QE buildup on GPU
=================

[ 15%] Building Fortran object FFTXlib/tests/CMakeFiles/qe_fftx_test_common.dir/recips.f90.o
../../lib/libqe_fftx.a(fft_scalar.FFTW3.f90.o): In function `fft_scalar_fftw3_initialize_threads_':
/lustre/home/user/m/milias/work/software/quantum-espresso/qe-develop/q-e/FFTXlib/src/fft_scalar.FFTW3.f90:54: undefined reference to `fftw
_init_threads'
/lustre/home/user/m/milias/work/software/quantum-espresso/qe-develop/q-e/FFTXlib/src/fft_scalar.FFTW3.f90:59: undefined reference to `fftw
_plan_with_nthreads'
pgacclnk: child process exit status 1: /usr/bin/ld
make[2]: *** [FFTXlib/tests/bin/qe_fftx_test.x] Error 2
make[1]: *** [FFTXlib/tests/CMakeFiles/qe_fftx_test.dir/all] Error 2

