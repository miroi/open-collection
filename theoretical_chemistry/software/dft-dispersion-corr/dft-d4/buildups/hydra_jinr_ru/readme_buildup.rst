=======================================
DFTD4 on vm02.hydra.local/hydra.jinr.ru
=======================================


milias@vm02.hydra.local:~/work/software/dft_dispersion_corrections/dft-d4/.git clone  git@github.com:dftd4/dftd4.git

milias@vm02.hydra.local:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.git pull
Already up-to-date.


milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.mkdir build_gnu

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/.module add gcc/v12.3.0
module add CMake/v3.29.2


interactive with Intel
~~~~~~~~~~~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.FC=ifort cmake ..
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


