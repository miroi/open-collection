Quantum Espresso on milias@194.160.44.72
----------------------------------------

milias@194.160.44.72:~/work/software/theoretical_chemistry/quantum-epresso/.git clone git@gitlab.com:QEF/q-e.git

milias@194.160.44.72:~/work/software/theoretical_chemistry/quantum-epresso/q-e/.mkdir build
milias@194.160.44.72:~/work/software/theoretical_chemistry/quantum-epresso/q-e/.cd build/
milias@194.160.44.72:~/work/software/theoretical_chemistry/quantum-epresso/q-e/build/.cmake ..
-- The Fortran compiler identification is GNU 9.3.0
-- The C compiler identification is GNU 9.3.0
-- Check for working Fortran compiler: /usr/bin/f95
-- Check for working Fortran compiler: /usr/bin/f95  -- works
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Checking whether /usr/bin/f95 supports Fortran 90
-- Checking whether /usr/bin/f95 supports Fortran 90 -- yes
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Setting build type to 'Release' as none was specified
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Found MPI_Fortran: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_usempif08.so (found version "3.1")
-- Found MPI: TRUE (found version "3.1") found components: Fortran
-- Trying to find LAPACK from Intel MKL
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- Could NOT find BLAS (missing: BLAS_LIBRARIES)
-- LAPACK requires BLAS
-- A library with LAPACK API not found. Please specify library location.
-- Trying to find alternative LAPACK libraries
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - not found
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /usr/lib/x86_64-linux-gnu/libopenblas.so
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- A library with LAPACK API found.
-- Found LAPACK: /usr/lib/x86_64-linux-gnu/libopenblas.so;/usr/lib/x86_64-linux-gnu/libopenblas.so
-- Installing FoX via submodule
-- Found Git: /usr/bin/git (found version "2.25.1")
Submodule 'external/fox' (https://github.com/pietrodelugas/fox.git) registered for path 'external/fox'
Cloning into '/home/milias/work/software/theoretical_chemistry/quantum-epresso/q-e/external/fox'...
Submodule path 'external/fox': checked out '819745f5849de5c9de516be133ab206691738257'
-- determining operating system and architecture:
   -> your operating system is : Linux-5.4.0-62-generic
   -> your architecture is     : x86_64
-- Searching for m4 scripting language
   -> /usr/bin/m4
-- Determining end-of-line character by the host name
   -> end-of-line character is LF
-- Determining method to call flush intrinsic
   -> flush intrinsic method is default
-- Checking for 'associated in restricted expression' bug
-- Determining method to call abort intrinsic
 abort : bare works
Submodule 'external/wannier90' (https://github.com/wannier-developers/wannier90.git) registered for path 'external/wannier90'
Cloning into '/home/milias/work/software/theoretical_chemistry/quantum-epresso/q-e/external/wannier90'...
Submodule path 'external/wannier90': checked out '9676b93252046524852445c8e44fbe7ce347f63d'
-- Installing MBD via submodule
Submodule 'external/mbd' (https://github.com/libmbd/libmbd.git) registered for path 'external/mbd'
Cloning into '/home/milias/work/software/theoretical_chemistry/quantum-epresso/q-e/external/mbd'...
Submodule path 'external/mbd': checked out '82005cbb65bdf5d32ca021848eec8f19da956a77'
Submodule 'external/devxlib' (https://gitlab.com/max-centre/components/devicexlib.git) registered for path 'external/devxlib'
Cloning into '/home/milias/work/software/theoretical_chemistry/quantum-epresso/q-e/external/devxlib'...
Submodule path 'external/devxlib': checked out '00c140557725bdd9b155566924c01cfe3d61081a'
-- Could NOT find VendorFFTW (missing: VendorFFTW_LIBRARIES VendorFFTW_INCLUDE_DIRS VendorFFTW_ID)
-- No vendor FFTW found
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1")
-- Found FFTW3: /usr/lib/x86_64-linux-gnu/libfftw3.so
-- generating tests in pw category
-- generating tests in cp category
-- generating tests in ph category
-- generating tests in epw category
-- generating tests in tddfpt category
-- generating tests in hp category
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/theoretical_chemistry/quantum-epresso/q-e/build
milias@194.160.44.72:~/work/software/theoretical_chemistry/quantum-epresso/q-e/build/.
.
.
.
milias@194.160.44.72:~/work/software/theoretical_chemistry/quantum-epresso/q-e/build/.m -j2
.
.
.
[100%] Linking Fortran static library ../lib/libqe_epw.a
[100%] Built target qe_epw
Scanning dependencies of target qe_epw_exe
[100%] Building Fortran object EPW/CMakeFiles/qe_epw_exe.dir/src/epw.f90.o
[100%] Linking Fortran executable ../bin/epw.x
[100%] Built target qe_epw_exe


milias@194.160.44.72:~/work/software/theoretical_chemistry/quantum-epresso/q-e/build/.ctest -j4
Test project /home/milias/work/software/theoretical_chemistry/quantum-epresso/q-e/build
        Start 239: test-suite_pseudo_cp
        Start   1: test_qe_fftx
        Start   2: test_qe_utilx_mp_count_nodes
        Start   3: test_qe_utilx_mp_bcast_i1
  1/444 Test   #3: test_qe_utilx_mp_bcast_i1 .........................................   Passed    0.33 sec
        Start   4: test_qe_utilx_mp_bcast_iv
  2/444 Test   #2: test_qe_utilx_mp_count_nodes ......................................   Passed    0.34 sec
        Start   5: test_qe_utilx_mp_bcast_im
  3/444 Test   #4: test_qe_utilx_mp_bcast_iv .........................................   Passed    0.27 sec
        Start   6: test_qe_utilx_mp_bcast_it
  4/444 Test   #5: test_qe_utilx_mp_bcast_im .........................................   Passed    0.27 sec
        Start   7: test_qe_utilx_mp_bcast_iv_buffer
  5/444 Test   #1: test_qe_fftx ......................................................   Passed    0.68 sec
        Start   8: test_qe_utilx_mp_bcast_lv_buffer
  6/444 Test   #6: test_qe_utilx_mp_bcast_it .........................................   Passed    0.32 sec
        Start   9: test_qe_utilx_mp_bcast_rv_buffer
  7/444 Test   #7: test_qe_utilx_mp_bcast_iv_buffer ..................................   Passed    0.32 sec
        Start  10: test_qe_utilx_mp_max_iv_buffer
  8/444 Test   #8: test_qe_utilx_mp_bcast_lv_buffer ..................................   Passed    0.32 sec
        Start  11: test_qe_utilx_mp_max_rv_buffer
  9/444 Test #239: test-suite_pseudo_cp ..............................................   Passed    1.04 sec
        Start  17: test-suite_pseudo_pw
 10/444 Test   #9: test_qe_utilx_mp_bcast_rv_buffer ..................................   Passed    0.35
.
.
.
59% tests passed, 183 tests failed out of 444

