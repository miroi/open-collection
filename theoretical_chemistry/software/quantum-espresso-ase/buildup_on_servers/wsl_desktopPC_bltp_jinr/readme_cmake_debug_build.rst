===================
QE build with debug
===================

milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e/build_gnu_mkl_serial/.cmake -DQE_ENABLE_MPI=OFF -DCMAKE_Fortran_COMPILER=gfortran  -DQE_FFTW_VENDOR=Intel_FFTW3 -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
-- The Fortran compiler identification is GNU 11.4.0
-- The C compiler identification is GNU 11.4.0
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /usr/bin/gfortran - skipped
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /usr/bin/cpp
-- Performing Test Fortran_ISYSTEM_SUPPORTED
-- Performing Test Fortran_ISYSTEM_SUPPORTED - Success
-- Found Git: /usr/bin/git (found suitable version "2.34.1", minimum required is "2.13")
-- Source files are cloned from a git repository.
   sed supports -E
   Git branch: develop
   Git commit hash: 95bc91b9c3ff25f565697dd77c0850e0757537c6
-- Trying to find LAPACK from Intel MKL
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /usr/lib/x86_64-linux-gnu/libmkl_gf_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_sequential.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;-lm;-ldl
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /usr/lib/x86_64-linux-gnu/libmkl_gf_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_sequential.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;-lm;-ldl;-lm;-ldl
-- Looking for Fortran zhpev
-- Looking for Fortran zhpev - found
Project C_FLAGS:  -O2 -g -DNDEBUG
Project Fortran_FLAGS:  -fallow-argument-mismatch -O2 -g -DNDEBUG
Project INCLUDE_DIRECTORIES: /home/milias/work/software/qe/q-e/include
Project EXE_LINKER_FLAGS:
Project SHARED_LINKER_FLAGS:
-- Installing Wannier90 via submodule
-- Installing MBD via submodule
-- Found Git: /usr/bin/git (found version "2.34.1")
-- Setting version tag to 0.13.0-2-g89a3cc1 from Git
-- Installing DeviceXlib via submodule
-- Found VendorFFTW: /usr/lib/x86_64-linux-gnu/libmkl_gf_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_sequential.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;-lm;-ldl;/usr/lib/x86_64-linux-gnu/libmkl_gf_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_sequential.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;-lm;-ldl;-lm;-ldl
-- Found Intel_FFTW3 library
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/qe/q-e/build_gnu_mkl_serial
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e/build_gnu_mkl_serial/.



