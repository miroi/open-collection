======================
DFTD4 on hydra.jinr.ru
======================

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/.git clone git@github.com:dftd4/dftd4.git
Cloning into 'dftd4'...
.
.
.

interactive buildup with Intel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module add CMake/v3.29.2  intel/v2021.1

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.FC=ifort cmake -B build_intel/
-- The Fortran compiler identification is Intel 2021.1.0.20201112
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/ifort - skipped
-- Setting build type to 'RelWithDebInfo' as none was specified.
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- The C compiler identification is GNU 4.8.5
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
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
-- Found BLAS: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so;/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so;-lpthread;-lm;-ldl
-- mctc-lib: Find installed package
-- Could NOT find mctc-lib (missing: mctc-lib_DIR)
-- Retrieving mctc-lib revision v0.4.1 from https://github.com/grimme-lab/mctc-lib
-- Found OpenMP_C: -fopenmp (found version "3.1")
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "3.1")
-- mstore: Find installed package
-- Could NOT find mstore (missing: mstore_DIR)
-- Retrieving mstore revision v0.3.0 from https://github.com/grimme-lab/mstore
-- multicharge: Find installed package
-- Could NOT find multicharge (missing: multicharge_DIR)
-- Retrieving multicharge revision v0.4.0 from https://github.com/grimme-lab/multicharge
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so;/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Configuring done (351.7s)
CMake Warning at build_intel/_deps/multicharge-src/app/CMakeLists.txt:16 (add_executable):
  Cannot generate a safe runtime search path for target multicharge-exe
  because files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at build_intel/_deps/multicharge-src/test/unit/CMakeLists.txt:32 (add_executable):
  Cannot generate a safe runtime search path for target multicharge-tester
  because files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at app/CMakeLists.txt:17 (add_executable):
  Cannot generate a safe runtime search path for target dftd4-exe because
  files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at test/api/CMakeLists.txt:17 (add_executable):
  Cannot generate a safe runtime search path for target dftd4-api-tester
  because files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at test/unit/CMakeLists.txt:35 (add_executable):
  Cannot generate a safe runtime search path for target dftd4-tester because
  files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


-- Generating done (93.6s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.

compilation
~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.m -j2


