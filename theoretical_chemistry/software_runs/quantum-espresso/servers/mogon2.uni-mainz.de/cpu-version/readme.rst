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

mirilias@login21.mogon:~/work/software/quantum_espresso/qe-devel/build_openmpi_intel/.ldd bin/pw.x 
        linux-vdso.so.1 (0x00007fffc61e0000)
        libmkl_intel_lp64.so.1 => /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_intel_lp64.so.1 (0x00007fba137af000)
        libmkl_sequential.so.1 => /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_sequential.so.1 (0x00007fba11d98000)
        libmkl_core.so.1 => /cluster/easybuild/broadwell/software/imkl/2021.4.0/mkl/2021.4.0/lib/intel64/libmkl_core.so.1 (0x00007fba0d92a000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fba0d70a000)
        libm.so.6 => /lib64/libm.so.6 (0x00007fba0d388000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007fba0d184000)
        libirng.so => /cluster/easybuild/broadwell/software/imkl/2021.4.0/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libirng.so (0x00007fba0ce1a000)
        libcilkrts.so.5 => /cluster/easybuild/broadwell/software/intel-compilers/2021.4.0/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libcilkrts.so.5 (0x00007fba0cbdd000)
        libstdc++.so.6 => /cluster/easybuild/broadwell/software/GCCcore/11.2.0/lib64/libstdc++.so.6 (0x00007fba0c9b8000)
        libmpi_usempif08.so.40 => /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/lib/libmpi_usempif08.so.40 (0x00007fba0c780000)
        libmpi_usempi_ignore_tkr.so.40 => /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/lib/libmpi_usempi_ignore_tkr.so.40 (0x00007fba0c575000)
        libmpi_mpifh.so.40 => /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/lib/libmpi_mpifh.so.40 (0x00007fba0c30b000)
        libmpi.so.40 => /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/lib/libmpi.so.40 (0x00007fba0bfc7000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fba0bc02000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fba1434e000)
        libgcc_s.so.1 => /cluster/easybuild/broadwell/software/GCCcore/11.2.0/lib64/libgcc_s.so.1 (0x00007fba14544000)
        libintlc.so.5 => /cluster/easybuild/broadwell/software/imkl/2021.4.0/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libintlc.so.5 (0x00007fba0b98a000)
        libopen-rte.so.40 => /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/lib/libopen-rte.so.40 (0x00007fba0b6c3000)
        libopen-orted-mpir.so => /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/lib/libopen-orted-mpir.so (0x00007fba0b4c1000)
        libopen-pal.so.40 => /cluster/easybuild/broadwell/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/lib/libopen-pal.so.40 (0x00007fba0b1fa000)
        librt.so.1 => /lib64/librt.so.1 (0x00007fba0aff2000)
        libutil.so.1 => /lib64/libutil.so.1 (0x00007fba0adee000)
        libiomp5.so => /cluster/easybuild/broadwell/software/imkl/2021.4.0/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libiomp5.so (0x00007fba0a9ce000)
        libz.so.1 => /lib64/libz.so.1 (0x00007fba0a7b7000)
        libhwloc.so.15 => /cluster/easybuild/broadwell/software/hwloc/2.5.0-GCCcore-11.2.0/lib/libhwloc.so.15 (0x00007fba144e8000)
        libxml2.so.2 => /lib64/libxml2.so.2 (0x00007fba0a44f000)
        libevent_core-2.1.so.7 => /cluster/easybuild/broadwell/software/libevent/2.1.12-GCCcore-11.2.0/lib/libevent_core-2.1.so.7 (0x00007fba144af000)
        libevent_pthreads-2.1.so.7 => /cluster/easybuild/broadwell/software/libevent/2.1.12-GCCcore-11.2.0/lib/libevent_pthreads-2.1.so.7 (0x00007fba144ab000)
        libifport.so.5 => /cluster/easybuild/broadwell/software/intel-compilers/2021.4.0/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libifport.so.5 (0x00007fba0a221000)
        libifcoremt.so.5 => /cluster/easybuild/broadwell/software/intel-compilers/2021.4.0/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libifcoremt.so.5 (0x00007fba0a08c000)
        libimf.so => /cluster/easybuild/broadwell/software/imkl/2021.4.0/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libimf.so (0x00007fba099fe000)
        libsvml.so => /cluster/easybuild/broadwell/software/imkl/2021.4.0/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libsvml.so (0x00007fba0796b000)
        liblzma.so.5 => /lib64/liblzma.so.5 (0x00007fba07744000)

