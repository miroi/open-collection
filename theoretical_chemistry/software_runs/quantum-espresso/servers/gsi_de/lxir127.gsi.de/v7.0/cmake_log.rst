milias@lxir127.gsi.de:/data.local1/milias/software/quantum-epresso/qe-7.0/build_mpi/.cmake -DCMAKE_C_COMPILER=mpicc -DCMAKE_Fortran_COMPILER=mpif90  ..
-- The C compiler identification is Intel 17.0.4.20170411
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /u/milias/bin/openmpi/bin/mpicc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Setting build type to 'Release' as none was specified
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /usr/bin/cpp
-- Performing Test Fortran_ISYSTEM_SUPPORTED
-- Performing Test Fortran_ISYSTEM_SUPPORTED - Success
-- Found MPI_Fortran: /cvmfs/it.gsi.de/openmpi/gcc/3.1.0_gcc8.1/bin/mpif90 (found version "3.1") 
-- Found MPI: TRUE (found version "3.1") found components: Fortran 
-- MPI settings used by CTest
     MPIEXEC_EXECUTABLE : /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mpi/intel64/bin/mpiexec
     MPIEXEC_NUMPROC_FLAG : -n
     MPIEXEC_PREFLAGS : 
   Tests run as : /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mpi/intel64/bin/mpiexec -n <NUM_PROCS>  <EXECUTABLE>
-- Found Git: /usr/bin/git (found suitable version "2.20.1", minimum required is "2.13") 
-- Source files are not cloned from a git repository.
-- Trying to find LAPACK from Intel MKL
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_gf_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl  
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_gf_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;-lm;-ldl  
-- Found LAPACK: /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_gf_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_gf_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;-lm;-ldl
-- Looking for Fortran zhpev
-- Looking for Fortran zhpev - found
-- Installing FoX via submodule
-- Cloning https://github.com/pietrodelugas/fox.git into /data.local1/milias/software/quantum-epresso/qe-7.0/external/fox.
Initialized empty Git repository in /data.local1/milias/software/quantum-epresso/qe-7.0/external/fox/.git/
From https://github.com/pietrodelugas/fox
 * branch            98ce8e36c881ccf511c1c4991ff76c174eaaeab9 -> FETCH_HEAD
Switched to a new branch 'recorded_HEAD'
-- Determining operating system and architecture:
   -> your operating system is : Linux-4.19.0-20-amd64
   -> your architecture is     : x86_64
-- Searching for m4 scripting language
   -> /usr/bin/m4
-- Determining end-of-line character by the host name
   -> end-of-line character is LF
-- Determining method to call flush intrinsic
   -> flush intrinsic method is default
-- Checking for 'associated in restricted expression' bug
-- Determining method to call abort intrinsic
   -> abort : bare works
-- Cloning https://github.com/wannier-developers/wannier90.git into /data.local1/milias/software/quantum-epresso/qe-7.0/external/wannier90.
Initialized empty Git repository in /data.local1/milias/software/quantum-epresso/qe-7.0/external/wannier90/.git/
From https://github.com/wannier-developers/wannier90
 * branch            9676b93252046524852445c8e44fbe7ce347f63d -> FETCH_HEAD
Switched to a new branch 'recorded_HEAD'
-- Installing MBD via submodule
-- Cloning https://github.com/libmbd/libmbd.git into /data.local1/milias/software/quantum-epresso/qe-7.0/external/mbd.
Initialized empty Git repository in /data.local1/milias/software/quantum-epresso/qe-7.0/external/mbd/.git/
From https://github.com/libmbd/libmbd
 * branch            82005cbb65bdf5d32ca021848eec8f19da956a77 -> FETCH_HEAD
Switched to a new branch 'recorded_HEAD'
-- Cloning https://gitlab.com/max-centre/components/devicexlib.git into /data.local1/milias/software/quantum-epresso/qe-7.0/external/devxlib.
Initialized empty Git repository in /data.local1/milias/software/quantum-epresso/qe-7.0/external/devxlib/.git/
From https://gitlab.com/max-centre/components/devicexlib
 * branch            a6b89ef77b1ceda48e967921f1f5488d2df9226d -> FETCH_HEAD
Switched to a new branch 'recorded_HEAD'
-- Found VendorFFTW: /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_gf_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_gf_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;-lm;-ldl  
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- generating tests in ph category
-- generating tests in epw category
-- generating tests in tddfpt category
-- generating tests in hp category
-- Configuring done
You have changed variables that require your cache to be deleted.
Configure will be re-run and you may have to reset some variables.
The following variables have changed:
CMAKE_Fortran_COMPILER= mpif90
CMAKE_Fortran_COMPILER= mpif90
CMAKE_Fortran_COMPILER= mpif90

-- The Fortran compiler identification is Intel 17.0.4.20170411
-- The C compiler identification is Intel 17.0.4.20170411
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /u/milias/bin/openmpi/bin/mpif90 - skipped
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /u/milias/bin/openmpi/bin/mpicc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Setting build type to 'Release' as none was specified
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /usr/bin/cpp
-- Performing Test Fortran_ISYSTEM_SUPPORTED
-- Performing Test Fortran_ISYSTEM_SUPPORTED - Success
-- Found MPI_Fortran: /u/milias/bin/openmpi/bin/mpif90 (found version "3.1") 
-- Found MPI: TRUE (found version "3.1") found components: Fortran 
-- MPI settings used by CTest
     MPIEXEC_EXECUTABLE : /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mpi/intel64/bin/mpiexec
     MPIEXEC_NUMPROC_FLAG : -n
     MPIEXEC_PREFLAGS : 
   Tests run as : /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mpi/intel64/bin/mpiexec -n <NUM_PROCS>  <EXECUTABLE>
-- Found Git: /usr/bin/git (found suitable version "2.20.1", minimum required is "2.13") 
-- Source files are not cloned from a git repository.
-- Trying to find LAPACK from Intel MKL
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl  
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;-lm;-ldl  
-- Found LAPACK: /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;-lm;-ldl
-- Looking for Fortran zhpev
-- Looking for Fortran zhpev - found
-- Installing FoX via submodule
-- Previous clone found at /data.local1/milias/software/quantum-epresso/qe-7.0/external/fox.
-- Determining operating system and architecture:
   -> your operating system is : Linux-4.19.0-20-amd64
   -> your architecture is     : x86_64
-- Searching for m4 scripting language
   -> /usr/bin/m4
-- Determining end-of-line character by the host name
   -> end-of-line character is LF
-- Determining method to call flush intrinsic
   -> flush intrinsic method is default
-- Checking for 'associated in restricted expression' bug
   -> yes
-- Determining method to call abort intrinsic
   -> abort : bare works
-- Previous clone found at /data.local1/milias/software/quantum-epresso/qe-7.0/external/wannier90.
-- Installing MBD via submodule
-- Previous clone found at /data.local1/milias/software/quantum-epresso/qe-7.0/external/mbd.
-- Previous clone found at /data.local1/milias/software/quantum-epresso/qe-7.0/external/devxlib.
-- Found VendorFFTW: /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;-lm;-ldl  
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- generating tests in ph category
-- generating tests in epw category
-- generating tests in tddfpt category
-- generating tests in hp category
-- Configuring done
-- Generating done
-- Build files have been written to: /data.local1/milias/software/quantum-epresso/qe-7.0/build_mpi


