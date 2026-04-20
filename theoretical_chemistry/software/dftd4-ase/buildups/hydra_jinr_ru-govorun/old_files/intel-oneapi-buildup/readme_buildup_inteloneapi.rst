======================
DFTD4 on hydra.jinr.ru
======================

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/.git clone git@github.com:dftd4/dftd4.git
Cloning into 'dftd4'...
.
.
.
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.gsu
Submodule 'assets/aur/dftd4' (https://aur.archlinux.org/dftd4.git) registered for path 'assets/aur/dftd4'
Submodule 'assets/aur/dftd4-git' (https://aur.archlinux.org/dftd4-git.git) registered for path 'assets/aur/dftd4-git'
Cloning into '/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/assets/aur/dftd4'...
Cloning into '/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/assets/aur/dftd4-git'...
Submodule path 'assets/aur/dftd4': checked out 'a8947fb60f1b6d192046cb91c7c0524fd4470885'
Submodule path 'assets/aur/dftd4-git': checked out '7e92bd04dea45dcba5d127938d55e85f73c6e753'


interactive buildup with Intel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module add CMake/v3.29.2  intel/oneapi

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.ifort --version
ifort (IFORT) 2021.4.0 20210910

MCTCDIR=/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/mctc/mctc-lib/build_inteloneapi
BUILD==build_inteloneapi

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.FC=ifort CC=icc cmake -B $BUILD  -Dmctc-lib_DIR=$MCTCDIR

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.FC=ifort CC=icc cmake -B $BUILD  -Dmctc-lib_DIR=$MCTCDIR -DMCTCLIB_FIND_METHOD=cmake

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.FC=ifort CC=icc cmake -B $BUILD  -Dmctc-libDIR=$MCTCDIR -DMCTCLIB_FIND_METHOD=cmake
-- The Fortran compiler identification is Intel 2021.4.0.20210910
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/inte64/ifort - skipped
-- Setting build type to 'RelWithDebInfo' as none was specified.
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- The C compiler identification is Intel 2021.4.0.20210910
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/ic - skipped
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
-- Found BLAS: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x8-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so;/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021107/bin/lib/libiomp5.so;-lpthread;-lm;-ldl
-- mctc-lib: Find installed package
-- Could NOT find mctc-lib (missing: mctc-lib_DIR)
CMake Error at config/cmake/dftd4-utils.cmake:114 (message):
  Could not find dependency mctc-lib
Call Stack (most recent call first):
  config/cmake/Findmctc-lib.cmake:33 (dftd4_find_package)
  CMakeLists.txt:48 (find_package)


-- Configuring incomplete, errors occurred!

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.ls $MCTCDIR
app/            CMakeFiles/          config/              include/       Makefile  test/
CMakeCache.txt  cmake_install.cmake  CTestTestfile.cmake  libmctc-lib.a  src/      Testing/




compilation
~~~~~~~~~~~
