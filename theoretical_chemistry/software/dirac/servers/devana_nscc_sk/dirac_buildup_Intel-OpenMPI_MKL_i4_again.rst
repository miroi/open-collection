DIRAC buildups on Devana
=========================

/home/milias/work/software/dirac/dirac_public

modules
-------

OpenMPI-Intel
~~~~~~~~~~~~~
module load OpenMPI/4.1.1-intel-compilers-2021.4.0

milias@login02.devana.local:~/work/software/dirac/dirac_public/.which mpif90
/storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90
milias@login02.devana.local:~/work/software/dirac/dirac_public/.mpif90 --version
ifort (IFORT) 2021.4.0 20210910

milias@login02.devana.local:~/work/software/dirac/dirac_public/.which mpirun
/storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpirun
milias@login02.devana.local:~/work/software/dirac/dirac_public/.mpirun --version
mpirun (Open MPI) 4.1.1


MKL
~~~
milias@login02.devana.local:~/work/software/dirac/dirac_public/.module load mkl/latest
Loading mkl version 2023.0.0
Loading tbb version 2021.8.0
Loading compiler-rt version 2023.0.0

see: ls /storage-apps/intel-v.2023/oneapi/mkl/2023.0.0/lib/intel64/


CMake
~~~~~~
milias@login02.devana.local:~/work/software/dirac/dirac_public/.module load CMake/3.20.1-GCCcore-10.3.0


HDF5
~~~~
module load HDF5/1.10.7-iompi-2021a

All modules
~~~~~~~~~~~
module list


DIRAC with OpenMPI-Intel-i4
---------------------------
milias@login02.devana.local:~/work/software/dirac/dirac_public/../setup --mpi --fc=mpif90 --cc=mpicc --cxx=mpicxx  --mkl=parallel  build_openmpi_intel_mklpar_i4
cmake -DCMAKE_Fortran_COMPILER=mpif90 -DEXTRA_FCFLAGS="''" -DCMAKE_C_COMPILER=mpicc -DEXTRA_CFLAGS="''" -DCMAKE_CXX_COMPILER=mpicxx -DEXTRA_CXXFLAGS="''" -DPREPROCESSOR_DEFINITIONS="''" -DPYTHON_INTERPRETER="''" -DENABLE_BLAS=auto -DENABLE_LAPACK=auto -DMKL_FLAG=parallel -DMATH_LIB_SEARCH_ORDER="MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE" -DBLAS_LANG=Fortran -DLAPACK_LANG=Fortran -DENABLE_MPI=True -DENABLE_OPENMP=True -DENABLE_CODE_COVERAGE=False -DENABLE_STATIC_LINKING=False -DENABLE_PROFILING=False -DENABLE_RUNTIMECHECK=False -DENABLE_64BIT_INTEGERS=False -DEXPLICIT_LIBS="off" -DENABLE_EXATENSOR=ON -DENABLE_PCMSOLVER=ON -DPCMSOLVER_ROOT='' -DCMAKE_BUILD_TYPE=release -G"Unix Makefiles" -H/home/milias/work/software/dirac/dirac_public -Bbuild_openmpi_intel_mklpar_i4

-- The Fortran compiler identification is Intel 20.2.6.20220226
-- The C compiler identification is Intel 20.2.6.20220226
-- The CXX compiler identification is Intel 20.2.6.20220226
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90 - skipped
-- Checking whether /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90 supports Fortran 90
-- Checking whether /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90 supports Fortran 90 - yes
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpicc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpicxx - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PythonInterp: /usr/bin/python (found version "2.7.5")
-- User set explicit MKL flag which is passed to the compiler and linker: -mkl=parallel
-- This disables math detection and builtin math libraries
-- Setting -DHAVE_MKL_BLAS and -DHAVE_MKL_LAPACK
-- MATH_LIB_SEARCH_ORDER set to MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE
-- Found MPI_C: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpicc (found version "3.1")
-- Found MPI_CXX: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpicxx (found version "3.1")
-- Found MPI_Fortran: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90 (found version "3.1")
-- Found MPI: TRUE (found version "3.1")
-- Found OpenMP_C: -qopenmp (found version "5.0")
-- Found OpenMP_CXX: -qopenmp (found version "5.0")
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- Enable profiling: False
-- Enable run-time checking: False
-- Configure-time Linked math libs integer compatibility test ENABLED
-- Performing compile and run test of blas integer size (can deactivate with -D ENABLE_MATH_INT_TEST=OFF)
-- Performing Test blas_test_compiled ...
-- Performing Test blas_test_compiled - Success
-- Performing Test blas_test_run
-- Performing Test blas_test_run - Success
-- Test of blas integer size SUCCESS .. blas is integer*4
-- We have BLAS-integer*4
-- Found HDF5: /storage-apps/easybuild/software/HDF5/1.12.2-iimpi-2022a/lib/libhdf5.so;/usr/lib64/libpthread.so;/storage-apps/easybuild/software/Szip/2.1.1-GCCcore-11.3.0/lib/libsz.so;/storage-apps/easybuild/software/zlib/1.2.12-GCCcore-11.3.0/lib/libz.so;/usr/lib64/libdl.so;/usr/lib64/libm.so;/storage-apps/easybuild/software/intel-compilers/2022.1.0/compiler/2022.1.0/linux/compiler/lib/intel64/libiomp5.so;/usr/lib64/libpthread.so (found version "1.12.2") found components: C
-- HFD5 found, enabling HDF5 interface
-- HDF5 include directory location: /storage-apps/easybuild/software/HDF5/1.12.2-iimpi-2022a/include;/storage-apps/easybuild/software/zlib/1.2.12-GCCcore-11.3.0/include;/storage-apps/easybuild/software/Szip/2.1.1-GCCcore-11.3.0/include
-- MPI package type: OPENMPI
-- Compiling /home/milias/work/software/dirac/dirac_public/cmake/custom/test-MPI-compiler-compatibility.F90 ...
-- Performing Test MPI_COMPILER_MATCHES ...
-- Performing Test MPI_COMPILER_MATCHES - Success
-- mpi.mod matches the current MPI compiler, employing 'use mpi' and setting -DUSE_MPI_MOD_F90
-- Compiling /home/milias/work/software/dirac/dirac_public/cmake/custom/test-MPI-itype-compatibility.F90 ...
-- Performing Test MPI_ITYPE_MATCHES ...
-- Performing Test MPI_ITYPE_MATCHES - Success
-- Well, program got compiled with 32-bit integers, but the internal MPI integer compatibility test will be performed inside dirac.x.
-- Set CDash default timeout for single test set to 1500 seconds. Overwritten by test's TIMEOUT property label and, ultimatively, by pam timeout setting.
-- Test's 'basis_input_scripted' timeout set to 3600 seconds. Can be overwritten by pam's timeout setting.
-- -mkl=... flag for MKL libraries kept because Intel Fortran compiler is present
-- PCMSolver not found. The pre-packaged version will be built.
-- Polarizable Continuum Model via PCMSolver ENABLED
-- WARNING: No BLAS library for TALSH / EXATENSOR - certain functionalties will not work (cholesky)
-- The environment variables used to build ExaTensor are collected in the file ExaTensor_ENV (can be inspected/changed if necessary)
-- Enable ExaTENSOR library: ON
-- Gen1Int module: ON
-- PElib module: ON
-- The XCFun submodule ENABLED
-- ESR property module: ON
-- src/reladc/polprp_cousat.F: assigned -O2 optimization flag to fix the compilation with Intel
-- Stieltjes external module ENABLED
-- KRCC module: ON
-- Enable compilation of standalone relccsd.x: OFF
-- OpenRSP library: OFF
-- LAO properties without connection matrices: ON
-- Spinfree MCSCF module: ON
-- NOTE: tests for the (e)amfX2C 2e-scalar and spin-orbit picture-change correction module require h5py in your python env!
-- (e)amfX2C 2e-scalar and spin-orbit picture-change correction module: ON
-- srDFT module: ON
-- Specialized tutorial tests DISABLED
-- Unit control tests DISABLED
-- Versions from CMake variable (20.2.6.20220226) and Python script (2021.6) for C compiler are not equal!
-- Versions from CMake variable (20.2.6.20220226) and Python script (2021.6.0) for C++ compiler are not equal!
-- Versions from CMake variable (20.2.6.20220226) and Python script (2021.6) for Fortran compiler are not equal!
-- User name: milias
-- Host name: login02.devana.local
-- Operating system: Linux-3.10.0-1160.71.1.el7.x86_64
-- CMake version: 3.20.1
-- CMake generator: Unix Makefiles
-- CMake build type: release
-- Configuration time: 2023-07-24 13:01:23.172515
-- Fortran compiler ID: Intel
-- Fortran compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90
-- Fortran compiler version: Intel 2021.6
-- Fortran compiler flags:  -w -assume byterecl -g -traceback -DVAR_IFORT  -qopenmp
-- C compiler ID: Intel
-- C compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpicc
-- C compiler version: Intel 2021.6
-- C compiler flags:  -g -wd981 -wd279 -wd383 -wd1572 -wd177  -qopenmp
-- CXX compiler ID: Intel
-- CXX compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpicxx
-- CXX compiler version: Intel 2021.6.0
-- CXX compiler flags:  -Wno-unknown-pragmas  -qopenmp
-- Static linking: False
-- 64-bit integers: False
-- MPI parallelization: True
-- MPI launcher: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpiexec
-- Intel MKL flag: parallel
-- Compile definitions: HAVE_MKL_BLAS;HAVE_MKL_LAPACK;HAVE_MPI;HAVE_OPENMP;VAR_MPI;VAR_MPI2;USE_MPI_MOD_F90;SYS_LINUX;PRG_DIRAC;INSTALL_WRKMEM=64000000;HAS_PCMSOLVER;BUILD_GEN1INT;HAS_PELIB;HAS_STIELTJES;MOD_LAO_REARRANGED;MOD_MCSCF_spinfree;MOD_XAMFI;MOD_ESR;MOD_KRCC;MOD_SRDFT;MOD_EXACORR
-- Exacorr module enabled : ON
-- The Exacorr module will be included in the Dirac executable and to the standalone exacorr.x
-- Exacorr employs the ExaTensor library (https://github.com/ORNL-QCI/ExaTENSOR) for tensor operations
-- Please read carefully the Dirac documentation guide for setting up the Exacorr runtime environment
-- ExaTensor source code repository: https://github.com/RelMBdev/ExaTENSOR.git
-- Exatensor source code git hash: 35caded68340657186be190a2d68a98c9e2159bb
-- ExaTensor build environment: WRAP=NOWRAP BUILD_TYPE=OPT   TOOLKIT=INTEL EXA_OS=LINUX GPU_CUDA=NOCUDA MPILIB=OPENMPI PATH_OPENMPI=/storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0 BLASLIB=NONE
-- Found HDF5: /storage-apps/easybuild/software/HDF5/1.12.2-iimpi-2022a/lib/libhdf5.so;/usr/lib64/libpthread.so;/storage-apps/easybuild/software/Szip/2.1.1-GCCcore-11.3.0/lib/libsz.so;/storage-apps/easybuild/software/zlib/1.2.12-GCCcore-11.3.0/lib/libz.so;/usr/lib64/libdl.so;/usr/lib64/libm.so;/storage-apps/easybuild/software/intel-compilers/2022.1.0/compiler/2022.1.0/linux/compiler/lib/intel64/libiomp5.so;/usr/lib64/libpthread.so (found version "1.12.2") found components: C HL
-- For checking, linked libraries to dirac.x: objlib.dirac.x;pelib_interface;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i4/external/lib/libstieltjes.a;mpi;imf;svml;irng;stdc++;m;ipgo;decimal;stdc++;gcc;gcc_s;irc;svml;c;gcc;gcc_s;irc_s;dl;c;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i4/external/pcmsolver/install/lib/libpcm.a;/storage-apps/easybuild/software/zlib/1.2.12-GCCcore-11.3.0/lib/libz.so;mpi;imf;svml;irng;stdc++;m;ipgo;decimal;stdc++;gcc;gcc_s;irc;svml;c;gcc;gcc_s;irc_s;dl;c;/storage-apps/easybuild/software/zlib/1.2.12-GCCcore-11.3.0/lib/libz.so;xcfun_fortran_bindings;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i4/external/xcfun-build/src/libxcfun.a;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i4/external/lib/libpelib.a;gen1int_interface;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i4/external/lib/libgen1int.a;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i4/exatensor/src/exatensor/lib/libtalsh.a;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i4/exatensor/src/exatensor/lib/libexatensor.a;qcorr;HDF5::HDF5;laplace;-lstdc++
-- Could NOT find Sphinx (missing: SPHINX_EXECUTABLE)
-- Copied DIRAC basis set directories into the build directory
-- Copied data schema and python utilities into the build directory
-- Set CDash default timeout for single test set to 1500 seconds. Overwritten by test's TIMEOUT property label and, ultimatively, by pam timeout setting.
-- Test's 'basis_input_scripted' timeout set to 3600 seconds. Can be overwritten by pam's timeout setting.
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i4

   configure step is done
   now you need to compile the sources:
   $ cd build_openmpi_intel_mklpar_i4
   $ make



