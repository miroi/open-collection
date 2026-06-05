DIRAC interactive buildup
=========================

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk/.module add CMake/v4.2.3
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk/.module add Python/v3.12.13  intel/v2025.3.1
(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk/../setup --mpi --exatensor=OFF --pcmsolver=OFF  --pelib=OFF  --fc=mpiifx   --extra-fc-flags="-O3 -xHost -ilp64" --cc=mpiicx --extra-cc-flags="-O"  --cxx=mpiicpx --int64  build_intelmpi2025_mkl_i8_interact
-- The Fortran compiler identification is IntelLLVM 2025.3.2
-- The C compiler identification is IntelLLVM 2025.3.2
-- The CXX compiler identification is IntelLLVM 2025.3.2
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mpi/latest/bin/mpiifx - skipped
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mpi/latest/bin/mpiicx - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mpi/latest/bin/mpiicpx - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found Python: /cvmfs/hlit.jinr.ru/alma9/miniconda/envs/Py3.12.13/bin/python3.12 (found version "3.12.13") found components: Interpreter
-- BLAS will be searched for based on MKLROOT=/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest
-- Searching for BLAS using search order MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE
-- Setting -DHAVE_MKL_BLAS
-- Found BLAS: MKL (-Wl,--start-group;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_intel_ilp64.so;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_core.so;/usr/lib64/libpthread.a;/usr/lib64/libm.so;-qopenmp;-Wl,--end-group)
-- LAPACK will be searched for based on MKLROOT=/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest
-- Searching for LAPACK using search order MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE
-- Setting -DHAVE_MKL_LAPACK
-- Found LAPACK: MKL (-Wl,--start-group;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_lapack95_ilp64.a;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_intel_ilp64.so;-qopenmp;-Wl,--end-group)
-- MATH_LIB_SEARCH_ORDER set to MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE
-- Found MPI_C: /cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mpi/latest/bin/mpiicx (found version "4.1")
-- Found MPI_CXX: /cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mpi/latest/bin/mpiicpx (found version "4.1")
-- Found MPI_Fortran: /cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mpi/latest/bin/mpiifx (found version "4.1")
-- Found MPI: TRUE (found version "4.1")
-- Found OpenMP_C: -fiopenmp (found version "5.1")
-- Found OpenMP_CXX: -fiopenmp (found version "5.1")
-- Found OpenMP_Fortran: -fiopenmp (found version "5.2")
-- Found OpenMP: TRUE (found version "5.1")
-- Enable profiling: False
-- Enable run-time checking: False
-- Configure-time Linked math libs integer compatibility test ENABLED
-- Performing compile and run test of blas integer size (can deactivate with -D ENABLE_MATH_INT_TEST=OFF)
-- Performing Test blas_test_compiled ...
-- Performing Test blas_test_compiled - Success
-- Performing Test blas_test_run
-- Performing Test blas_test_run - Failed
-- Test of blas integer size SUCCESS .. blas is integer*8
-- We have BLAS-integer*8
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found HDF5: hdf5-shared (found version "2.1.0") found components: C
-- HFD5 found, enabling HDF5 interface
-- HDF5 include directory location: /cvmfs/hlit.jinr.ru/alma9/miniconda/envs/Py3.12.13/include
-- MPI package type: INTEL
-- Compiling /lustre/projects/m/milias/work/software/dirac/trunk/cmake/custom/test-MPI-compiler-compatibility.F90 ...
-- Performing Test MPI_COMPILER_MATCHES ...
-- Performing Test MPI_COMPILER_MATCHES - Success
-- mpi.mod matches the current MPI compiler, employing 'use mpi' and setting -DUSE_MPI_MOD_F90
-- Compiling /lustre/projects/m/milias/work/software/dirac/trunk/cmake/custom/test-MPI-itype-compatibility.F90 ...
-- Performing Test MPI_ITYPE_MATCHES ...
-- Performing Test MPI_ITYPE_MATCHES - Success
-- Well, program got compiled with 64-bit integers, but the internal MPI integer compatibility test will be performed inside dirac.x.
-- Set CDash default timeout for single test set to 1500 seconds. Overwritten by test's TIMEOUT property label and, ultimatively, by pam timeout setting.
-- Test's 'basis_input_scripted' timeout set to 3600 seconds. Can be overwritten by pam's timeout setting.
-- Polarizable Continuum Model via PCMSolver DISABLED
-- Enable ExaTENSOR library: OFF
-- NOTE: tests for the (e)amfX2C 2e-scalar and spin-orbit picture-change correction module require h5py in your python env!
-- (e)amfX2C 2e-scalar and spin-orbit picture-change correction module: ON
-- The XCFun submodule ENABLED
-- ESR property module: ON
-- src/reladc/polprp_cousat.F: assigned -O2 optimization flag to fix the compilation with Intel
-- Stieltjes external module DISABLED
-- KRCC module: ON
-- Enable compilation of standalone relccsd.x: OFF
-- OpenRSP library: OFF
-- LAO properties without connection matrices: ON
-- Spinfree MCSCF module: ON
-- srDFT module: ON
-- Specialized tutorial tests DISABLED
-- Unit control tests DISABLED
-- Found HDF5: hdf5-shared (found version "2.1.0") found components: C HL
-- User name: milias
-- Host name: space03.hydra.local
-- Operating system: Linux-5.14.0-570.62.1.el9_6.x86_64
-- CMake version: 4.2.3
-- CMake generator: Unix Makefiles
-- CMake build type: release
-- Configuration time: 2026-06-05 21:30:49.370599+00:00
-- Fortran compiler ID: IntelLLVM
-- Fortran compiler: /cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mpi/latest/bin/mpiifx
-- Fortran compiler version: IntelLLVM 2025.3.2
-- Fortran compiler flags:  -O3 -xHost -ilp64 -w -assume byterecl -g -traceback -DVAR_IFX  -fiopenmp -i8
-- C compiler ID: IntelLLVM
-- C compiler: /cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mpi/latest/bin/mpiicx
-- C compiler version: IntelLLVM 2025.3.2
-- C compiler flags:  -O -g  -fiopenmp
-- CXX compiler ID: IntelLLVM
-- CXX compiler: /cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mpi/latest/bin/mpiicpx
-- CXX compiler version: IntelLLVM 2025.3.2
-- CXX compiler flags:  -Wno-unknown-pragmas  -fiopenmp
-- Static linking: False
-- 64-bit integers: True
-- MPI parallelization: True
-- MPI launcher: /cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mpi/latest/bin/mpiexec
-- Math libraries: -Wl,--start-group;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_lapack95_ilp64.a;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_intel_ilp64.so;-qopenmp;-Wl,--end-group;-Wl,--start-group;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_intel_ilp64.so;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_core.so;/usr/lib64/libpthread.a;/usr/lib64/libm.so;-qopenmp;-Wl,--end-group
-- Compile definitions: HAVE_MKL_BLAS;HAVE_MKL_LAPACK;HAVE_MPI;HAVE_OPENMP;VAR_MPI;VAR_MPI2;USE_MPI_MOD_F90;SYS_LINUX;PRG_DIRAC;INT_STAR8;INSTALL_WRKMEM=64000000;BUILD_GEN1INT;MOD_LAO_REARRANGED;MOD_MCSCF_spinfree;MOD_XAMFI;MOD_ESR;MOD_KRCC;MOD_SRDFT
-- Exacorr module enabled : OFF
-- For checking, linked libraries to dirac.x: diracobj;xcfun_fortran_bindings;/lustre/projects/m/milias/work/software/dirac/trunk/build_intelmpi2025_mkl_i8_interact/external/xcfun-build/src/libxcfun.a;gen1int_interface;-Wl,--start-group;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_lapack95_ilp64.a;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_intel_ilp64.so;-qopenmp;-Wl,--end-group;-Wl,--start-group;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_intel_ilp64.so;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hlit.jinr.ru/alma9/intel/v2025.3.1/mkl/latest/lib/intel64/libmkl_core.so;/usr/lib64/libpthread.a;/usr/lib64/libm.so;-qopenmp;-Wl,--end-group;laplace;laplace-minimax;qcorr;HDF5::HDF5
-- Found Sphinx: /cvmfs/hlit.jinr.ru/alma9/miniconda/envs/Py3.12.13/bin/sphinx-build
-- Copied DIRAC basis set directories into the build directory
-- Copied data schema and python utilities into the build directory
-- Set CDash default timeout for single test set to 1500 seconds. Overwritten by test's TIMEOUT property label and, ultimatively, by pam timeout setting.
-- Test's 'basis_input_scripted' timeout set to 3600 seconds. Can be overwritten by pam's timeout setting.
-- Configuring done (42.4s)
-- Generating done (11.1s)
-- Build files have been written to: /lustre/projects/m/milias/work/software/dirac/trunk/build_intelmpi2025_mkl_i8_interact

CMake Warning:
  Manually-specified variables were not used by the project:

    ENABLE_TBLIS
    TENSOR_EXECUTOR


   configure step is done
   now you need to compile the sources:
   $ cd build_intelmpi2025_mkl_i8_interact
   $ make

(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk/build_intelmpi2025_mkl_i8_interact/.m -j4
[  1%] Building Fortran object src/interest/CMakeFiles/interest.dir/module_interest_interface.F90.o
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(39): error #7013: This module file was not generated by any release of this compiler.   [MPI]
  use mpi
------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(228): error #6683: A kind type parameter must be a compile-time constant.   [MPI_ADDRESS_KIND]
    integer(kind=mpi_address_kind) :: disp(9)                      !mpi_address_kind is always = 8
-----------------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(233): error #6404: This name does not have a type, and must have an explicit type.   [MPI_COMM_WORLD]
    call MPI_comm_rank( MPI_comm_world, myrank,  ier )
------------------------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(241): error #6404: This name does not have a type, and must have an explicit type.   [MPI_REAL8]
       call mpi_bcast(constant%alpha, 1, mpi_real8,0,mpi_comm_world,ier)
-----------------------------------------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(247): error #6404: This name does not have a type, and must have an explicit type.   [MPI_INTEGER]
       call mpi_bcast(nr_atoms,1,mpi_integer,0,mpi_comm_world,ier)
---------------------------------^
compilation aborted for /lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90 (code 1)
make[2]: *** [src/interest/CMakeFiles/interest.dir/build.make:77: src/interest/CMakeFiles/interest.dir/module_interest_interface.F90.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:3978: src/interest/CMakeFiles/interest.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[  1%] Built target git_info
[  1%] Building Fortran object src/pdpack/CMakeFiles/pdpack.dir/arhpack.F.o
[  1%] Building Fortran object src/interface_mpi/CMakeFiles/interface_mpi.dir/integer_model.F90.o
[  1%] Building Fortran object src/pdpack/CMakeFiles/pdpack.dir/dge.F.o
[  1%] Building Fortran object src/interface_mpi/CMakeFiles/interface_mpi.dir/interface_to_mpi.F90.o
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/integer_model.F90(23): error #7013: This module file was not generated by any release of this compiler.   [MPI]
  use mpi
------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/integer_model.F90(43): error #6404: This name does not have a type, and must have an explicit type.   [MPI_INTEGER]
  integer_kind_in_mpi = sizeof(MPI_INTEGER)
-------------------------------^
compilation aborted for /lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/integer_model.F90 (code 1)
make[2]: *** [src/interface_mpi/CMakeFiles/interface_mpi.dir/build.make:101: src/interface_mpi/CMakeFiles/interface_mpi.dir/integer_model.F90.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/interface_to_mpi.F90(36): error #7013: This module file was not generated by any release of this compiler.   [MPI]
  use mpi
------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/interface_to_mpi.F90(237): error #6592: This symbol must be a defined parameter, an enumerator, or an argument of an inquiry function that evaluates to a compile-time constant.   [MPI_COMM_WORLD][  1%] Building Fortran object src/interest/CMakeFiles/interest.dir/module_interest_interface.F90.o
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(39): error #7013: This module file was not generated by any release of this compiler.   [MPI]
  use mpi
------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(228): error #6683: A kind type parameter must be a compile-time constant.   [MPI_ADDRESS_KIND]
    integer(kind=mpi_address_kind) :: disp(9)                      !mpi_address_kind is always = 8
-----------------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(233): error #6404: This name does not have a type, and must have an explicit type.   [MPI_COMM_WORLD]
    call MPI_comm_rank( MPI_comm_world, myrank,  ier )
------------------------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(241): error #6404: This name does not have a type, and must have an explicit type.   [MPI_REAL8]
       call mpi_bcast(constant%alpha, 1, mpi_real8,0,mpi_comm_world,ier)
-----------------------------------------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(247): error #6404: This name does not have a type, and must have an explicit type.   [MPI_INTEGER]
       call mpi_bcast(nr_atoms,1,mpi_integer,0,mpi_comm_world,ier)
---------------------------------^
compilation aborted for /lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90 (code 1)
make[2]: *** [src/interest/CMakeFiles/interest.dir/build.make:77: src/interest/CMakeFiles/interest.dir/module_interest_interface.F90.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:3978: src/interest/CMakeFiles/interest.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[  1%] Built target git_info
[  1%] Building Fortran object src/pdpack/CMakeFiles/pdpack.dir/arhpack.F.o
[  1%] Building Fortran object src/interface_mpi/CMakeFiles/interface_mpi.dir/integer_model.F90.o
[  1%] Building Fortran object src/pdpack/CMakeFiles/pdpack.dir/dge.F.o
[  1%] Building Fortran object src/interface_mpi/CMakeFiles/interface_mpi.dir/interface_to_mpi.F90.o
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/integer_model.F90(23): error #7013: This module file was not generated by any release of this compiler.   [MPI]
  use mpi
------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/integer_model.F90(43): error #6404: This name does not have a type, and must have an explicit type.   [MPI_INTEGER]
  integer_kind_in_mpi = sizeof(MPI_INTEGER)
-------------------------------^
compilation aborted for /lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/integer_model.F90 (code 1)
make[2]: *** [src/interface_mpi/CMakeFiles/interface_mpi.dir/build.make:101: src/interface_mpi/CMakeFiles/interface_mpi.dir/integer_model.F90.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/interface_to_mpi.F90(36): error #7013: This module file was not generated by any release of this compiler.   [MPI]
  use mpi
------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/interface_to_mpi.F90(237): error #6592: This symbol must be a defined parameter, an enumerator, or an argument of an inquiry function that evaluates to a compile-time constant.   [MPI_COMM_WORLD][  1%] Building Fortran object src/interest/CMakeFiles/interest.dir/module_interest_interface.F90.o
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(39): error #7013: This module file was not generated by any release of this compiler.   [MPI]
  use mpi
------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(228): error #6683: A kind type parameter must be a compile-time constant.   [MPI_ADDRESS_KIND]
    integer(kind=mpi_address_kind) :: disp(9)                      !mpi_address_kind is always = 8
-----------------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(233): error #6404: This name does not have a type, and must have an explicit type.   [MPI_COMM_WORLD]
    call MPI_comm_rank( MPI_comm_world, myrank,  ier )
------------------------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(241): error #6404: This name does not have a type, and must have an explicit type.   [MPI_REAL8]
       call mpi_bcast(constant%alpha, 1, mpi_real8,0,mpi_comm_world,ier)
-----------------------------------------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90(247): error #6404: This name does not have a type, and must have an explicit type.   [MPI_INTEGER]
       call mpi_bcast(nr_atoms,1,mpi_integer,0,mpi_comm_world,ier)
---------------------------------^
compilation aborted for /lustre/projects/m/milias/work/software/dirac/trunk/src/interest/module_interest_interface.F90 (code 1)
make[2]: *** [src/interest/CMakeFiles/interest.dir/build.make:77: src/interest/CMakeFiles/interest.dir/module_interest_interface.F90.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:3978: src/interest/CMakeFiles/interest.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[  1%] Built target git_info
[  1%] Building Fortran object src/pdpack/CMakeFiles/pdpack.dir/arhpack.F.o
[  1%] Building Fortran object src/interface_mpi/CMakeFiles/interface_mpi.dir/integer_model.F90.o
[  1%] Building Fortran object src/pdpack/CMakeFiles/pdpack.dir/dge.F.o
[  1%] Building Fortran object src/interface_mpi/CMakeFiles/interface_mpi.dir/interface_to_mpi.F90.o
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/integer_model.F90(23): error #7013: This module file was not generated by any release of this compiler.   [MPI]
  use mpi
------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/integer_model.F90(43): error #6404: This name does not have a type, and must have an explicit type.   [MPI_INTEGER]
  integer_kind_in_mpi = sizeof(MPI_INTEGER)
-------------------------------^
compilation aborted for /lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/integer_model.F90 (code 1)
make[2]: *** [src/interface_mpi/CMakeFiles/interface_mpi.dir/build.make:101: src/interface_mpi/CMakeFiles/interface_mpi.dir/integer_model.F90.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/interface_to_mpi.F90(36): error #7013: This module file was not generated by any release of this compiler.   [MPI]
  use mpi
------^
/lustre/projects/m/milias/work/software/dirac/trunk/src/interface_mpi/interface_to_mpi.F90(237): error #6592: This symbol must be a defined parameter, an enumerator, or an argument of an inquiry function that evaluates to a compile-time constant.   [MPI_COMM_WORLD]
.
.
.

