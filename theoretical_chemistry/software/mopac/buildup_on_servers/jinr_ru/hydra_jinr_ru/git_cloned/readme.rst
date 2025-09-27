================
MOPAC git cloned
================

clone
~~~~~
milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/.git clone git@github.com:openmopac/mopac.git


CMake buildup
~~~~~~~~~~~~~
https://github.com/openmopac/mopac?tab=readme-ov-file#cmake

module add intel/oneapi   CMake/v3.29.2  Python/v3.10.13

milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build/.module list

mkdir build
cd build

milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build/.cmake -DCMAKE_Fortran_COMPILER=ifort -DCMAKE_C_COMPILER=icc ..
-- Build type is Release
-- The Fortran compiler identification is Intel 2021.4.0.20210910
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/ifort - skipped
-- The C compiler identification is Intel 2021.4.0.20210910
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/icc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Shared library and dynamic executables
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - not found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so;/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so;-lpthread;-lm;-ldl
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so;/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Found OpenMP_C: -qopenmp (found version "5.0")
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- Found Python3: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/bin/python3.10 (found version "3.10.13") found components: Interpreter NumPy Development.Module
-- OMP packaging: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/../../compiler/lib/intel64_lin/libiomp5.so -> /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libiomp5.so
-- Configuring done (78.9s)
-- Generating done (23.1s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/mopac/git_cloned/mopac/build

milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build/.make -j4
[ 98%] Linking Fortran shared library libmopac.so
[ 98%] Built target mopac-core
[ 98%] Building Fortran object CMakeFiles/mopac.dir/src/mopac.F90.o
[ 98%] Building Fortran object CMakeFiles/mopac-param.dir/src/param.F90.o
[ 98%] Building Fortran object CMakeFiles/mopac-api-test.dir/include/mopac_wrapper.F90.o
[ 99%] Linking Fortran executable mopac
[ 99%] Linking Fortran executable mopac-param
[ 99%] Building Fortran object CMakeFiles/mopac-api-test.dir/include/mopac_wrapper_internal.F90.o
[100%] Building Fortran object CMakeFiles/mopac-api-test.dir/tests/mopac_api_test.F90.o
[100%] Built target mopac
[100%] Built target mopac-param
[100%] Linking Fortran executable mopac-api-test
[100%] Built target mopac-api-test
milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build/.

milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build/.ldd mopac
        linux-vdso.so.1 =>  (0x00007fffc65df000)
        libmopac.so.2 => /lustre/home/user/m/milias/work/software/mopac/git_cloned/mopac/build/libmopac.so.2 (0x00007fb3212d5000)
        libmkl_intel_lp64.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so.1 (0x00007fb320736000)
        libmkl_intel_thread.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so.1 (0x00007fb31cfe7000)
        libmkl_core.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so.1 (0x00007fb318b79000)
        libiomp5.so => /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so (0x00007fb3187d7000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fb3185bb000)
        libm.so.6 => /lib64/libm.so.6 (0x00007fb3182b9000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007fb3180b5000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fb317ce7000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fb325e53000)
        libgcc_s.so.1 => /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libgcc_s.so.1 (0x00007fb317acf000)
        libifport.so.5 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libifport.so.5 (0x00007fb3178a1000)
        libifcoremt.so.5 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libifcoremt.so.5 (0x00007fb325ec8000)
        libimf.so => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libimf.so (0x00007fb317213000)
        libsvml.so => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libsvml.so (0x00007fb3150dd000)
        libintlc.so.5 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libintlc.so.5 (0x00007fb314e65000)
milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build/.


