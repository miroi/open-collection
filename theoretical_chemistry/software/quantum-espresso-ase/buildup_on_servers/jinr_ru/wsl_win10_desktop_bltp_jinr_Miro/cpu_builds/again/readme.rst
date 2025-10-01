========================
QE local buildup on WSL2
========================

cloning
-------
milias@DESKTOP-7OTLCGO:~/work/software/qe/.git clone git@gitlab.com:QEF/q-e.git  q-e-devel-official

milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel-official/.git submodule update --init --recursive

buildup
-------

installed Ubuntu packages
~~~~~~~~~~~~~~~~~~~~~~~~~
openmpi-bin gfortran  libopenmpi-dev libfftw3-bin libfftw3-mpi-dev

mpif90 --version
GNU Fortran (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0

mpirun --version
mpirun (Open MPI) 4.1.2

mkl library:
~~~~~~~~~~~~
ls /usr/lib/x86_64-linux-gnu/libmkl_*
dpkg -L libmkl-* 

cmake configuration
~~~~~~~~~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel-official/build_openmpi/.cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON  -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_Fortran_COMPILER=mpif90 ..
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
   Git commit hash: 41de32dbdb0942acb75a8fa2409ce4953be06473
-- Trying to find LAPACK from Intel MKL
Project C_FLAGS:  -O3 -DNDEBUG
Project Fortran_FLAGS:  -fallow-argument-mismatch -O3 -DNDEBUG -O3
Project INCLUDE_DIRECTORIES: /home/milias/work/software/qe/q-e-devel-official/include
Project EXE_LINKER_FLAGS:
Project SHARED_LINKER_FLAGS:
-- Installing Wannier90 via submodule
-- Installing MBD via submodule
-- Found Git: /usr/bin/git (found version "2.34.1")
-- Setting version tag to 89a3cc1 from Git
-- Installing DeviceXlib via submodule
-- QE internal implementation of FFTW (FFTXLib)
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/qe/q-e-devel-official/build_openmpi

compilation
~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel-official/build_openmpi/.m -j 8.
.
.
.
[100%] Building Fortran object EPW/CMakeFiles/qe_epw.dir/src/tdbe_driver.f90.o
[100%] Building Fortran object EPW/CMakeFiles/qe_epw.dir/src/supercond_driver.f90.o
[100%] Linking Fortran static library ../lib/libqe_epw.a
[100%] Built target qe_epw
Scanning dependencies of target qe_epw_exe
[100%] Building Fortran object EPW/CMakeFiles/qe_epw_exe.dir/src/epw.f90.o
[100%] Linking Fortran executable ../bin/epw.x
[100%] Built target qe_epw_exe
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel-official/build_openmpi/.ldd bin/pw.x
        linux-vdso.so.1 (0x00007ffd539cb000)
        libmkl_gf_lp64.so => /lib/x86_64-linux-gnu/libmkl_gf_lp64.so (0x0000734d4be00000)
        libmkl_sequential.so => /lib/x86_64-linux-gnu/libmkl_sequential.so (0x0000734d4a000000)
        libmkl_core.so => /lib/x86_64-linux-gnu/libmkl_core.so (0x0000734d45800000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x0000734d45400000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x0000734d4bd19000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x0000734d4bc1c000)
        libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x0000734d4eaff000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x0000734d4cbe0000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x0000734d45000000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x0000734d4eafa000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x0000734d4cbdb000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x0000734d4cb93000)
        /lib64/ld-linux-x86-64.so.2 (0x0000734d4eb75000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x0000734d49ec9000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x0000734d4574d000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x0000734d45343000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x0000734d4cb37000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x0000734d49e94000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x0000734d4cb30000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x0000734d49e78000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x0000734d49e4e000)

ctest run
~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel-official/build_openmpi/.ctest -j8
.
.
.



