=========================
DFTD4 interactive buildup
=========================

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1      2) BASE/1.0        3) CMake/v3.29.2   4) intel/oneapi


milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.export MCTCDIR=/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/mctc/mctc_installed
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.export LD_LIBRARY_PATH=$MCTCDIR:$LD_LIBRARY_PATH

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.ls $MCTCDIR
bin/  include/  lib64/  share/
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.ls $MCTCDIR/lib64
cmake/  libmctc-lib.a  pkgconfig/

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.FC=ifort CC=icc cmake  -Dmctc-lib_DIR=$MCTCDIR -DWITH_API=OFF ..
-- The Fortran compiler identification is Intel 2021.4.0.20210910
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/ifort - skipped
-- Setting build type to 'RelWithDebInfo' as none was specified.
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- The C compiler identification is Intel 2021.4.0.20210910
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/icc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - not found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so;/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so;-lpthread;-lm;-ldl
-- mctc-lib: Find installed package
-- Could NOT find mctc-lib (missing: mctc-lib_DIR)
-- Retrieving mctc-lib revision v0.4.2 from https://github.com/grimme-lab/mctc-lib
-- Found OpenMP_C: -qopenmp (found version "5.0")
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- mstore: Find installed package
-- Could NOT find mstore (missing: mstore_DIR)
-- Retrieving mstore revision v0.3.0 from https://github.com/grimme-lab/mstore
-- multicharge: Find installed package
-- Could NOT find multicharge (missing: multicharge_DIR)
-- Retrieving multicharge revision v0.4.0 from https://github.com/grimme-lab/multicharge
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so;/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Configuring done (234.0s)
CMake Warning at build_intel/_deps/multicharge-src/app/CMakeLists.txt:16 (add_executable):
  Cannot generate a safe runtime search path for target multicharge-exe
  because files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at build_intel/_deps/multicharge-src/test/unit/CMakeLists.txt:32 (add_executable):
  Cannot generate a safe runtime search path for target multicharge-tester
  because files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at app/CMakeLists.txt:17 (add_executable):
  Cannot generate a safe runtime search path for target dftd4-exe because
  files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at test/unit/CMakeLists.txt:35 (add_executable):
  Cannot generate a safe runtime search path for target dftd4-tester because
  files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


-- Generating done (55.9s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel


milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.m -j4
[  0%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/accuracy.f90.o
[  0%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/system.f90.o
[  1%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/error.f90.o
[  2%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/version.F90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/utils.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/testing.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/resize.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/structure/info.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/codata2018.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/symbols.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/filetype.f90.o
[  9%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/structure.f90.o
[  9%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/paulingen.f90.o
[  9%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/constants.f90.o
[ 11%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/qcschema.F90.o
[ 11%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/gaussian.f90.o
[ 11%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/gaussian.f90.o
[ 11%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/qcschema.f90.o
[ 13%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/math.f90.o
[ 13%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/convert.f90.o
[ 15%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/covrad.f90.o
[ 15%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/cutoff.f90.o
[ 16%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/atomicrad.f90.o
[ 16%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/aims.f90.o
[ 16%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/cjson.F90.o
[ 18%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/ctfile.f90.o
[ 18%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/genformat.f90.o
[ 20%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/qchem.f90.o
[ 20%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/pdb.f90.o
[ 21%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/turbomole.f90.o
[ 22%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/vasp.f90.o
[ 23%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/xyz.f90.o
[ 23%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/aims.f90.o
[ 23%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/cjson.f90.o
[ 24%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/genformat.f90.o
[ 25%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/ctfile.f90.o
[ 25%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/pdb.f90.o
[ 25%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/qchem.f90.o
[ 26%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/vasp.f90.o
[ 26%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/turbomole.f90.o
[ 27%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/xyz.f90.o
[ 28%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read.f90.o
[ 28%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write.f90.o
[ 28%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/vdwrad.f90.o
[ 28%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io.f90.o
[ 28%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data.f90.o
[ 29%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/type.f90.o
[ 29%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/erf.f90.o
[ 30%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/dexp.f90.o
[ 30%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/exp.f90.o
[ 32%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/erf/en.f90.o
[ 32%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/erf/dftd4.f90.o
[ 33%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord.f90.o
[ 33%] Linking Fortran static library libmctc-lib.a
[ 33%] Built target mctc-lib-lib
[ 34%] Building Fortran object _deps/mctc-lib-build/app/CMakeFiles/mctc-convert.dir/main.f90.o
[ 34%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/data/record.f90.o
[ 34%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/cutoff.f90.o
[ 34%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/testsuite_structure.f90.o
[ 34%] Linking Fortran executable mctc-convert
[ 36%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_math.f90.o
[ 36%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore_version.f90.o
[ 36%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/blas.F90.o
[ 36%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read.f90.o
[ 36%] Built target mctc-convert
[ 37%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_aims.f90.o
[ 38%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/amino20x4.f90.o
[ 39%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/ewald.f90.o
[ 40%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/but14diol.f90.o
[ 40%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_cjson.f90.o
[ 40%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/lapack.F90.o
[ 40%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_ctfile.f90.o
[ 42%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/version.f90.o
[ 42%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/data/collection.f90.o
[ 43%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/f_block.f90.o
[ 44%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/heavy28.f90.o
[ 44%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/param/eeq2019.f90.o
[ 45%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_gaussian.f90.o
[ 46%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_genformat.f90.o
[ 46%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/ice10.f90.o
[ 47%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/il16.f90.o
[ 47%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/wignerseitz.f90.o
[ 48%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/mb16_43.f90.o
[ 48%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_pdb.f90.o
[ 50%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_qchem.f90.o
[ 50%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/upu23.f90.o
[ 51%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/x23.f90.o
[ 51%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/model.F90.o
[ 51%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_qcschema.f90.o
[ 52%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_turbomole.f90.o
[ 52%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_vasp.f90.o
[ 54%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_xyz.f90.o
[ 54%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/data/store.f90.o
[ 55%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_symbols.f90.o
[ 56%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/output.f90.o
[ 57%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore.f90.o
[ 58%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_ncoord.f90.o
[ 58%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/param.f90.o
[ 58%] Linking Fortran static library libmstore.a
[ 59%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge.f90.o
[ 60%] Linking Fortran static library libmulticharge.a
[ 60%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write.f90.o
[ 60%] Built target mstore-lib
[ 61%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_aims.f90.o
[ 61%] Building Fortran object _deps/mstore-build/app/fortranize/CMakeFiles/mstore-fortranize.dir/main.f90.o
[ 61%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_cjson.f90.o
[ 61%] Built target multicharge-lib
[ 64%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_ctfile.f90.o
[ 64%] Linking Fortran executable mstore-fortranize
[ 64%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_gaussian.f90.o
[ 65%] Building Fortran object _deps/mstore-build/app/info/CMakeFiles/mstore-info.dir/main.f90.o
[ 65%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_genformat.f90.o
[ 65%] Linking Fortran executable mstore-info
[ 65%] Built target mstore-fortranize
[ 66%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_pdb.f90.o
[ 67%] Building Fortran object _deps/multicharge-build/app/CMakeFiles/multicharge-exe.dir/main.f90.o
[ 67%] Built target mstore-info
[ 68%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_qchem.f90.o
[ 68%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/test_model.f90.o
[ 68%] Linking Fortran executable multicharge
[ 69%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_turbomole.f90.o
[ 70%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/cutoff.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/cutoff.f90(121): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_lattice_points_cutoff
--------------------^
[ 71%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_vasp.f90.o
[ 71%] Built target multicharge-exe
[ 72%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/damping.f90.o
[ 73%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/damping/atm.f90.o
[ 73%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/test_pbc.f90.o
[ 73%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_xyz.f90.o
[ 74%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/covrad.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/covrad.f90(72): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_covalent_rad_sym
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/covrad.f90(87): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_covalent_rad_num
--------------------^
[ 75%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_cutoff.f90.o
[ 75%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/en.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/en.f90(68): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_electronegativity_sym
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/en.f90(83): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_electronegativity_num
--------------------^
[ 76%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/test_wignerseitz.f90.o
[ 77%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_data.f90.o
[ 78%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/hardness.f90.o
[ 79%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/r4r2.f90.o
[ 79%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/wfpair.f90.o
[ 80%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/zeff.f90.o
[ 81%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/main.f90.o
[ 81%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/blas.F90.o
[ 82%] Linking Fortran executable multicharge-tester
[ 82%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/charge.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/charge.f90(34): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_charges
--------------------^
[ 83%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/type.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/type.f90(167): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: d4_ref
--------------------^
[ 83%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/utils.f90.o
[ 84%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/utils.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/utils.f90(29): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: wrap_to_central_cell
--------------------^
[ 85%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/ncoord.f90.o
[ 85%] Built target multicharge-tester
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/ncoord.f90(37): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_coordination_number
--------------------^
[ 87%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/main.f90.o
[ 87%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/version.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/version.f90(38): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dftd4_version
--------------------^
[ 88%] Linking Fortran executable mctc-lib-tester
[ 88%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data.f90.o
[ 88%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/damping/rational.f90.o
[ 88%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/reference.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/damping/rational.f90(61): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dispersion2
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/damping/rational.f90(326): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dispersion3
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/damping/rational.f90(376): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_pairwise_dispersion2
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/damping/rational.f90(455): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_pairwise_dispersion3
--------------------^
[ 89%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/d4.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/d4.f90(75): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_d4_model_with_checks
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/d4.f90(227): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_d4_model_no_checks
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/d4.f90(368): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: weight_references
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/d4.f90(491): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_atomic_c6
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/d4.f90(588): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_polarizabilities
--------------------^
[ 90%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/d4s.f90.o
[ 90%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/param.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/d4s.f90(72): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_d4_model_with_checks
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/d4s.f90(224): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_d4_model_no_checks
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/d4s.f90(365): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: weight_references
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/d4s.f90(503): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_atomic_c6
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/d4s.f90(600): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_polarizabilities
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/param.f90(100): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_functionals
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/param.f90(249): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_rational_damping_name
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/param.f90(276): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_rational_damping_id
--------------------^
[ 90%] Built target mctc-lib-tester
[ 90%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model.f90.o
[ 91%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/output.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(39): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_atomic_radii
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(72): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_atomic_references
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(121): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_system_properties
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(177): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_results
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(229): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_pairwise
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(281): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_damping_param
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(319): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: turbomole_gradlatt
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(409): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: turbomole_gradient
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(521): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: json_results
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(637): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: tagged_result
--------------------^
[ 91%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/disp.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/disp.f90(40): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dispersion
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/disp.f90(128): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_properties
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/disp.f90(172): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_pairwise_dispersion
--------------------^
[ 92%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/numdiff.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/numdiff.f90(36): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dispersion_hessian
--------------------^
[ 92%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4.f90.o
[ 93%] Linking Fortran static library libdftd4.a
[ 93%] Built target dftd4-lib
[ 95%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/help.f90.o
[ 96%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/argument.f90.o
[ 96%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_dftd4.f90.o
[ 96%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_model.f90.o
[ 96%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_pairwise.f90.o
[ 96%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/cli.f90.o
[ 97%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_param.f90.o
[ 98%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/driver.f90.o
[ 98%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_periodic.f90.o
[ 98%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/main.f90.o
[ 99%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/main.f90.o
[ 99%] Linking Fortran executable dftd4
[100%] Linking Fortran executable dftd4-tester
[100%] Built target dftd4-exe
[100%] Built target dftd4-tester

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.ctest -j4
Test project /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel
      Start  1: mctc-lib/cutoff
      Start  2: mctc-lib/data
      Start  3: mctc-lib/math
      Start  4: mctc-lib/ncoord
 1/36 Test  #1: mctc-lib/cutoff ..................   Passed    0.32 sec
 2/36 Test  #2: mctc-lib/data ....................   Passed    0.54 sec
 3/36 Test  #3: mctc-lib/math ....................   Passed    0.79 sec
      Start  5: mctc-lib/read
      Start  6: mctc-lib/read-aims
      Start  7: mctc-lib/read-cjson
 4/36 Test  #4: mctc-lib/ncoord ..................   Passed    0.92 sec
      Start  8: mctc-lib/read-ctfile
 5/36 Test  #5: mctc-lib/read ....................   Passed    2.88 sec
      Start  9: mctc-lib/read-gaussian
 6/36 Test  #6: mctc-lib/read-aims ...............   Passed    3.38 sec
      Start 10: mctc-lib/read-genformat
 7/36 Test  #9: mctc-lib/read-gaussian ...........   Passed    1.45 sec
      Start 11: mctc-lib/read-pdb
 8/36 Test  #7: mctc-lib/read-cjson ..............   Passed    6.35 sec
      Start 12: mctc-lib/read-qchem
 9/36 Test #11: mctc-lib/read-pdb ................   Passed    2.01 sec
      Start 13: mctc-lib/read-qcschema
10/36 Test  #8: mctc-lib/read-ctfile .............   Passed    7.26 sec
      Start 14: mctc-lib/read-turbomole
11/36 Test #10: mctc-lib/read-genformat ..........   Passed    4.18 sec
      Start 15: mctc-lib/read-vasp
12/36 Test #12: mctc-lib/read-qchem ..............   Passed    3.54 sec
      Start 16: mctc-lib/read-xyz
13/36 Test #15: mctc-lib/read-vasp ...............   Passed    3.29 sec
      Start 17: mctc-lib/symbols
14/36 Test #17: mctc-lib/symbols .................   Passed    0.27 sec
      Start 18: mctc-lib/write
15/36 Test #16: mctc-lib/read-xyz ................   Passed    3.35 sec
      Start 19: mctc-lib/write-aims
16/36 Test #13: mctc-lib/read-qcschema ...........   Passed    7.50 sec
17/36 Test #14: mctc-lib/read-turbomole ..........   Passed    7.13 sec
18/36 Test #19: mctc-lib/write-aims ..............   Passed    1.06 sec
      Start 20: mctc-lib/write-cjson
      Start 21: mctc-lib/write-ctfile
      Start 22: mctc-lib/write-gaussian
19/36 Test #18: mctc-lib/write ...................   Passed    3.13 sec
      Start 23: mctc-lib/write-genformat
20/36 Test #22: mctc-lib/write-gaussian ..........   Passed    0.62 sec
      Start 24: mctc-lib/write-pdb
21/36 Test #20: mctc-lib/write-cjson .............   Passed    0.91 sec
22/36 Test #21: mctc-lib/write-ctfile ............   Passed    1.17 sec
      Start 25: mctc-lib/write-qchem
      Start 26: mctc-lib/write-turbomole
23/36 Test #23: mctc-lib/write-genformat .........   Passed    1.17 sec
24/36 Test #24: mctc-lib/write-pdb ...............   Passed    0.83 sec
      Start 27: mctc-lib/write-vasp
      Start 28: mctc-lib/write-xyz
25/36 Test #25: mctc-lib/write-qchem .............   Passed    0.79 sec
      Start 29: model
26/36 Test #28: mctc-lib/write-xyz ...............   Passed    0.51 sec
      Start 30: pbc
27/36 Test #26: mctc-lib/write-turbomole .........   Passed    1.31 sec
      Start 31: wignerseitz
28/36 Test #27: mctc-lib/write-vasp ..............   Passed    1.28 sec
29/36 Test #31: wignerseitz ......................   Passed    0.56 sec
      Start 32: model
      Start 33: dftd4
30/36 Test #29: model ............................   Passed    1.45 sec
      Start 34: pairwise
31/36 Test #30: pbc ..............................   Passed    1.33 sec
      Start 35: param
32/36 Test #32: model ............................   Passed    0.58 sec
      Start 36: periodic
33/36 Test #33: dftd4 ............................   Passed    0.82 sec
34/36 Test #34: pairwise .........................   Passed    0.98 sec
35/36 Test #35: param ............................   Passed    0.91 sec
36/36 Test #36: periodic .........................   Passed    1.09 sec

100% tests passed, 0 tests failed out of 36

Total Test time (real) =  22.51 sec
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.app/dftd4 -h
Usage: dftd4 [run|param] [options] ...

Generally Applicable Atomic-Charge Dependent London Dispersion Correction.
Takes an geometry input to calculate the D4(S) dispersion correction.
Periodic calculations are performed automatically for periodic input formats.
Reads .CHRG file (if present) from the same directory as the input.
Specify the functional to select the correct parameters.

Commands

  run       Evaluate dispersion correction on the provided input structure.
            Periodic calculations are performed automatically for periodic inputs
            If no command is specified run is selected by default.

  param     Inspect damping parameters.

Options

-c,--charge <real>       Set charge to molecule, overwrites .CHRG file
-i,--input <format>      Hint for the format of the input file
-f,--func <method>       Use damping parameters for given functional
   --param <list>        Specify parameters for rational damping,
                         expected order is s6, s8, a1, a2 (requires four arguments)
   --mbdscale <s9>       Use scaled ATM three-body dispersion
   --zeta <list>         Adjust charge scaling parameters, takes two reals,
                         expected order is ga, gc (default: 3.0, 2.0)
   --wfactor <real>      Adjust weighting factor for interpolation (only D4)
                         (default: 6.0)
-m,--model <model>       Use specific D4 model (options: D4 (default), D4S)
-g,--grad [file]         Evaluate molecular gradient and virial,
                         write results to file (default: dftd4.txt),
                         attempts to add to Turbomole gradient and gradlatt files
   --hessian             Evaluate molecular hessian
   --property            Show dispersion related atomic and system properties
   --pair-resolved       Calculate pairwise representation of dispersion energy
   --noedisp             Disable writing of dispersion energy to .EDISP file
   --json [file]         Dump results to JSON output (default: dftd4.json)
-v,--verbose             Show more, can be used multiple times
-s,--silent              Show less, use twice to supress all output
   --version             Print program version and exit
   --citation            Print citation information and exit
   --license             Print license header and exit
-h,--help                Show this help message

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.

