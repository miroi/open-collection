Quantum Espresso on virgo.gsi.de
================================


milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/.git clone git@gitlab.com:QEF/q-e.git

module purge
module load cmake
module load openmpi/intel/4.0.3_intel19.0

milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/q-e/build_gnu8_openmpi3/.module list

Currently Loaded Modules:
  1) compiler/intel/19.0   2) openmpi/intel/4.0.3_intel19.0   3) cmake/3.15.4

milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/q-e/build_gnu8_openmpi3/.cmake ..
-- The Fortran compiler identification is Intel 19.0.4.20190416
-- The C compiler identification is GNU 4.8.5
-- Check for working Fortran compiler: /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/bin/intel64/ifort
-- Check for working Fortran compiler: /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/bin/intel64/ifort  -- works
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Checking whether /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/bin/intel64/ifort supports Fortran 90
-- Checking whether /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/bin/intel64/ifort supports Fortran 90 -- yes
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Setting build type to 'Release' as none was specified
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Found MPI_Fortran: /cvmfs/it.gsi.de/openmpi/intel/4.0.3_intel19.0/lib/libmpi_usempif08.so (found version "3.1")
-- Found MPI: TRUE (found version "3.1") found components:  Fortran
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
-- Found BLAS: /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_core.so;-lpthread;-lm;-ldl
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- A library with LAPACK API found.
-- Found LAPACK: /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_core.so;-lpthread;-lm;-ldl;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_core.so;-lpthread;-lm;-ldl
-- Installing FoX via submodule
-- Found Git: /usr/bin/git (found version "1.8.3.1")
Submodule 'external/fox' (https://github.com/pietrodelugas/fox.git) registered for path 'external/fox'
Cloning into 'external/fox'...
Submodule path 'external/fox': checked out '819745f5849de5c9de516be133ab206691738257'
-- determining operating system and architecture:
   -> your operating system is : Linux-3.10.0-1127.18.2.el7.x86_64
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
 abort : bare works
Submodule 'external/wannier90' (https://github.com/wannier-developers/wannier90.git) registered for path 'external/wannier90'
Cloning into 'external/wannier90'...
Submodule path 'external/wannier90': checked out '9676b93252046524852445c8e44fbe7ce347f63d'
-- Installing MBD via submodule
Submodule 'external/mbd' (https://github.com/libmbd/libmbd.git) registered for path 'external/mbd'
Cloning into 'external/mbd'...
Submodule path 'external/mbd': checked out '82005cbb65bdf5d32ca021848eec8f19da956a77'
Submodule 'external/devxlib' (https://gitlab.com/max-centre/components/devicexlib.git) registered for path 'external/devxlib'
Cloning into 'external/devxlib'...
Submodule path 'external/devxlib': checked out '00c140557725bdd9b155566924c01cfe3d61081a'
-- Found VendorFFTW: /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_core.so;-lpthread;-lm;-ldl;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_core.so;-lpthread;-lm;-ldl
-- generating tests in pw category
-- generating tests in cp category
-- generating tests in ph category
-- generating tests in epw category
-- generating tests in tddfpt category
-- generating tests in hp category
-- Configuring done
-- Generating done
-- Build files have been written to: /lustre/ukt/milias/work/software/quantum-espresso/q-e/build_gnu8_openmpi3
milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/q-e/build_gnu8_openmpi3/.
milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/q-e/build_gnu8_openmpi3/.np
Number of processors:128
milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/q-e/build_gnu8_openmpi3/.m -j16


