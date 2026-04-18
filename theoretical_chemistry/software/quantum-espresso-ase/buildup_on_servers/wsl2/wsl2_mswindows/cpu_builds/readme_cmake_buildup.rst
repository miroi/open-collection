=======================
QE buildup on WSL-Win10
=======================


milias@DESKTOP-7OTLCGO:~/.sudo apt-get install libfftw3-bin libfftw3-mpi-dev

milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e/build_gnu_openmpi/.cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON  -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_Fortran_COMPILER=mpif90  ..

error,  see  https://gitlab.com/QEF/q-e/-/issues/777


better buildup
~~~~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e/build_gnu_openmpi/.cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON  -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_Fortran_COMPILER=mpif90  -DQE_FFTW_VENDOR=Internal    ..
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /usr/bin/cpp
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
-- Installing Wannier90 via submodule
-- Installing MBD via submodule
-- Found Git: /usr/bin/git (found version "2.34.1")
-- Setting version tag to 0.13.0-2-g89a3cc1 from Git
-- Installing DeviceXlib via submodule
-- QE internal implementation of FFTW (FFTXLib)
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/qe/q-e/build_gnu_openmpi
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e/build_gnu_openmpi/make -j 4
.
.
.

milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e/build_gnu_openmpi/.ctest -j8
.
.
.
97% tests passed, 12 tests failed out of 361

also works
~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e/build_gnu_openmpi/.cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON -DCMAKE_Fortran_COMPILER=mpif90  -DQE_FFTW_VENDOR=Intel_FFTW3 ..

97% tests passed, 12 tests failed out of 361





