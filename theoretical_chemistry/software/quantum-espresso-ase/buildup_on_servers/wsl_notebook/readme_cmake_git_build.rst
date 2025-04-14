QE buildup on NB
================

miroi@MIRO:~/work/software/quantum_espresso/q-e/build_gnu_openmpi/.cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON
-DCMAKE_Fortran_COMPILER=mpif90 ..
-- The Fortran compiler identification is GNU 11.4.0
-- The C compiler identification is GNU 11.4.0
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /usr/bin/mpif90 - skipped
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Setting build type to 'Release' as none was specified
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /usr/bin/cpp
-- Performing Test Fortran_ISYSTEM_SUPPORTED
-- Performing Test Fortran_ISYSTEM_SUPPORTED - Success
-- Found MPI_Fortran: /usr/bin/mpif90 (found version "3.1")
-- Found MPI: TRUE (found version "3.1") found components: Fortran
-- Selected the Fortran 'mpi' module. QE_ENABLE_MPI_MODULE=ON
-- MPI settings used by CTest
     MPIEXEC_EXECUTABLE : /usr/bin/mpiexec
     MPIEXEC_NUMPROC_FLAG : -n
     MPIEXEC_PREFLAGS :
   Tests run as : /usr/bin/mpiexec -n <NUM_PROCS>  <EXECUTABLE>
-- Found Git: /usr/bin/git (found suitable version "2.34.1", minimum required is "2.13")
-- Source files are cloned from a git repository.
   sed supports -E
   Git branch: develop
   Git commit hash: c129e404a1b34e2d280280c5087d1dc05a879a3f
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
-- Installing Wannier90 via submodule
-- Installing MBD via submodule
-- Found Git: /usr/bin/git (found version "2.34.1")
-- Setting version tag to 0.13.0-2-g89a3cc1 from Git
-- Installing DeviceXlib via submodule
-- Found VendorFFTW: /usr/lib/x86_64-linux-gnu/libmkl_gf_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_sequential.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;-lm;-ldl;/usr/lib/x86_64-linux-gnu/libmkl_gf_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_sequential.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;-lm;-ldl;-lm;-ldl
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- Configuring done
-- Generating done
-- Build files have been written to: /home/miroi/work/software/quantum_espresso/q-e/build_gnu_openmpi
miroi@MIRO:~/work/software/quantum_espresso/q-e/build_gnu_openmpi/.

miroi@MIRO:~/work/software/quantum_espresso/q-e/build_gnu_openmpi/.m -j4

..
f951: Warning: Nonexistent include directory ‘/home/miroi/work/software/quantum_espresso/q-e/FFTXlib/VendorFFTW_INCLUDE_MKL_DFTI-NOTFOUND’ [-Wmissing-include-dirs]
/home/miroi/work/software/quantum_espresso/q-e/FFTXlib/src/fft_scalar.DFTI.f90:19:2:

   19 | !=----------------------------------------------------------------------=!
      |  1~~~~~~~~~~~~~
Fatal Error: mkl_dfti.f90: No such file or directory
compilation terminated.
make[2]: *** [FFTXlib/src/CMakeFiles/qe_fftx.dir/build.make:335: FFTXlib/src/CMakeFiles/qe_fftx.dir/fft_scalar.DFTI.f90.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:1315: FFTXlib/src/CMakeFiles/qe_fftx.dir/all] Error 2
make: *** [Makefile:146: all] Error 2



