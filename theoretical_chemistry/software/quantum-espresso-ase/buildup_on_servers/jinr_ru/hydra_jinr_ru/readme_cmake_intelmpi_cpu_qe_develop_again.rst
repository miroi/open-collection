====================================
QE-develop build with CMake/IntelMPI 
====================================


milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-develop/q-e/build_intelmpi_mkl/.module list
Currently Loaded Modulefiles:
  1) BASE/1.0                                4) intel/v2018.1.163-9                     7) ELPA/v2020.05.001_intel2018_python365
  2) CMake/v3.29.2                           5) openmpi/v1.8.8-1
  3) fftw/v3.3.7-5                           6) Python/v3.6.5


build
~~~~~
milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-develop/q-e/build_intelmpi_mkl/. nohup cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON   -DCMAKE_C_COMPILER=icc -DCMAKE_CXX_COMPILER=icpc -DCMAKE_Fortran_COMPILER=mpiifort ..  &

-- The Fortran compiler identification is Intel 18.0.1.20171018
-- The C compiler identification is Intel 18.0.1.20171018
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mpi/intel64/bin/mpiifort - skipped
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/bin/intel64/icc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Setting build type to 'Release' as none was specified
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /usr/bin/cpp
-- Performing Test Fortran_ISYSTEM_SUPPORTED
-- Performing Test Fortran_ISYSTEM_SUPPORTED - Success
-- Found MPI_Fortran: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mpi/intel64/bin/mpiifort (found version "3.1")
-- Found MPI: TRUE (found version "3.1") found components: Fortran
-- Selected the Fortran 'mpi' module. QE_ENABLE_MPI_MODULE=ON
-- MPI settings used by CTest
     MPIEXEC_EXECUTABLE : /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/openmpi/v1.8.8-1/bin/mpiexec
     MPIEXEC_NUMPROC_FLAG : -n
     MPIEXEC_PREFLAGS : 
   Tests run as : /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/openmpi/v1.8.8-1/bin/mpiexec -n <NUM_PROCS>  <EXECUTABLE>
-- Found Git: /usr/bin/git (found suitable version "2.23.0", minimum required is "2.13")
-- Source files are cloned from a git repository.
   sed supports -E
   Git branch: develop
   Git commit hash: c129e404a1b34e2d280280c5087d1dc05a879a3f
-- Trying to find LAPACK from Intel MKL
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_core.so;-lpthread;-lm;-ldl
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_core.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Looking for Fortran zhpev
-- Looking for Fortran zhpev - found
-- Installing Wannier90 via submodule
-- Installing MBD via submodule
-- Found Git: /usr/bin/git (found version "2.23.0")
-- Setting version tag to 0.13.0-2-g89a3cc1 from Git
-- Installing DeviceXlib via submodule
-- Found VendorFFTW: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_core.so;-lpthread;-lm;-ldl;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2018.1.163-9/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin/libmkl_core.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- Configuring done (104.1s)
-- Generating done (340.2s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/quantum-espresso/qe-develop/q-e/build_intelmpi_mkl
milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-develop/q-e/build_intelmpi_mkl/.nohup make -j 2 &
[1] 25118

milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-develop/q-e/build_intelmpi_mkl/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1                              4) openmpi/v1.8.8-1                        7) CMake/v3.29.2
  2) BASE/1.0                                5) Python/v3.6.5
  3) intel/v2018.1.163-9                     6) ELPA/v2020.05.001_intel2018_python365
milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-develop/q-e/build_intelmpi_mkl/.np
Number of processors:6
milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-develop/q-e/build_intelmpi_mkl/.ctest -j2
Test project /lustre/home/user/m/milias/work/software/quantum-espresso/qe-develop/q-e/build_intelmpi_mkl
        Start 314: system--cp-pseudo

