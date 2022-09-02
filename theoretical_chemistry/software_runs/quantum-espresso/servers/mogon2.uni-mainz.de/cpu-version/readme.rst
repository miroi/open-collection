===============
QE-devel on CPU
===============

modules
~~~~~~~
module load mpi/OpenMPI/4.1.1-intel-compilers-2021.4.0
module load numlib/imkl-FFTW/2021.4.0-iimpi-2021b

mirilias@login21.mogon:~/work/software/quantum_espresso/qe-devel/.module list

Currently Loaded Modules:
  1) compiler/GCCcore/11.2.0
  2) compiler/intel-compilers/2021.4.0
  3) system/hwloc/2.5.0-GCCcore-11.2.0
  4) lib/libfabric/1.13.2-GCCcore-11.2.0
  5) system/OpenSSL/1.1
  6) lib/libevent/2.1.12-GCCcore-11.2.0
  7) lib/PMIx/4.1.0-GCCcore-11.2.0
  8) mpi/OpenMPI/4.1.1-intel-compilers-2021.4.0
  9) mpi/impi/2021.4.0-intel-compilers-2021.4.0
 10) toolchain/iimpi/2021b
 11) numlib/imkl/2021.4.0
 12) numlib/imkl-FFTW/2021.4.0-iimpi-2021b

buildup
~~~~~~~

mirilias@login22.mogon:~/work/software/quantum_espresso/qe-devel/build_openmpi_intel/.cmake -DCMAKE_Fortran_COMPILER=mpif90 -DCMAKE_C_COMPILER=mpicc ..
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /cluster/easybuild/broadwell/software/GCCcore/11.2.0/bin/cpp
-- MPI settings used by CTest
     MPIEXEC_EXECUTABLE : /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpiexec
     MPIEXEC_NUMPROC_FLAG : -n
     MPIEXEC_PREFLAGS :
   Tests run as : /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpiexec -n <NUM_PROCS>  <EXECUTABLE>
-- Source files are cloned from a git repository.
   sed supports -E
   Git branch: develop
   Git commit hash: d50f574154e75c88044778d91e67d6e00f487b1e
-- Trying to find LAPACK from Intel MKL
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Found LAPACK: /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Looking for Fortran zhpev
-- Looking for Fortran zhpev - found
-- Installing FoX via submodule
Submodule 'external/fox' (https://github.com/pietrodelugas/fox.git) registered for path 'external/fox'
Cloning into '/gpfs/fs1/home/mirilias/work/software/quantum_espresso/qe-devel/external/fox'...
Submodule path 'external/fox': checked out '3453648e6837658b747b895bb7bef4b1ed2eac40'
-- Determining operating system and architecture:
   -> your operating system is : Linux-4.18.0-348.12.2.el8_5.x86_64
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
-- Installing Wannier90 via submodule
Submodule 'external/wannier90' (https://github.com/wannier-developers/wannier90.git) registered for path 'external/wannier90'
Cloning into '/gpfs/fs1/home/mirilias/work/software/quantum_espresso/qe-devel/external/wannier90'...
From https://github.com/wannier-developers/wannier90
 * branch            1d6b187374a2d50b509e5e79e2cab01a79ff7ce1 -> FETCH_HEAD
Submodule path 'external/wannier90': checked out '1d6b187374a2d50b509e5e79e2cab01a79ff7ce1'
-- Installing MBD via submodule
Submodule 'external/mbd' (https://github.com/libmbd/libmbd.git) registered for path 'external/mbd'
Cloning into '/gpfs/fs1/home/mirilias/work/software/quantum_espresso/qe-devel/external/mbd'...
From https://github.com/libmbd/libmbd
 * branch            82005cbb65bdf5d32ca021848eec8f19da956a77 -> FETCH_HEAD
Submodule path 'external/mbd': checked out '82005cbb65bdf5d32ca021848eec8f19da956a77'
-- Installing DeviceXlib via submodule
Submodule 'external/devxlib' (https://gitlab.com/max-centre/components/devicexlib.git) registered for path 'external/devxlib'
Cloning into '/gpfs/fs1/home/mirilias/work/software/quantum_espresso/qe-devel/external/devxlib'...
From https://gitlab.com/max-centre/components/devicexlib
 * branch            a6b89ef77b1ceda48e967921f1f5488d2df9226d -> FETCH_HEAD
Submodule path 'external/devxlib': checked out 'a6b89ef77b1ceda48e967921f1f5488d2df9226d'
-- Found VendorFFTW: /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
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
CMAKE_C_COMPILER= mpicc
CMAKE_Fortran_COMPILER= mpif90
CMAKE_Fortran_COMPILER= mpif90
CMAKE_C_COMPILER= mpicc

-- The Fortran compiler identification is Intel 2021.4.0.20210910
-- The C compiler identification is Intel 2021.4.0.20210910
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90 - skipped
-- Checking whether /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90 supports Fortran 90
-- Checking whether /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90 supports Fortran 90 - yes
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpicc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Setting build type to 'Release' as none was specified
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /cluster/easybuild/broadwell/software/GCCcore/11.2.0/bin/cpp
-- Performing Test Fortran_ISYSTEM_SUPPORTED
-- Performing Test Fortran_ISYSTEM_SUPPORTED - Success
-- Found MPI_Fortran: /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90 (found version "3.1")
-- Found MPI: TRUE (found version "3.1") found components: Fortran
-- MPI settings used by CTest
     MPIEXEC_EXECUTABLE : /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpiexec
     MPIEXEC_NUMPROC_FLAG : -n
     MPIEXEC_PREFLAGS :
   Tests run as : /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpiexec -n <NUM_PROCS>  <EXECUTABLE>
-- Found Git: /usr/bin/git (found suitable version "2.27.0", minimum required is "2.13")
-- Source files are cloned from a git repository.
   sed supports -E
   Git branch: develop
   Git commit hash: d50f574154e75c88044778d91e67d6e00f487b1e
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
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Found LAPACK: /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Looking for Fortran zhpev
-- Looking for Fortran zhpev - found
-- Installing FoX via submodule
-- Determining operating system and architecture:
   -> your operating system is : Linux-4.18.0-348.12.2.el8_5.x86_64
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
-- Installing Wannier90 via submodule
-- Installing MBD via submodule
-- Installing DeviceXlib via submodule
-- Found VendorFFTW: /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so;/cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
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
-- Build files have been written to: /home/mirilias/work/software/quantum_espresso/qe-devel/build_openmpi_intel
mirilias@login22.mogon:~/work/software/quantum_espresso/qe-devel/build_openmpi_intel/m -j8



