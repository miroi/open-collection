======================
DFTD4 on hydra.jinr.ru
======================

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/.git clone git@github.com:dftd4/dftd4.git
Cloning into 'dftd4'...
.
.
.

interactive buildup with Intel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module add CMake/v3.29.2  intel/v2021.1

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.FC=ifort cmake -B build_intel/
-- The Fortran compiler identification is Intel 2021.1.0.20201112
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/ifort - skipped
-- Setting build type to 'RelWithDebInfo' as none was specified.
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- The C compiler identification is GNU 4.8.5
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
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
-- Found BLAS: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so;/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so;-lpthread;-lm;-ldl
-- mctc-lib: Find installed package
-- Could NOT find mctc-lib (missing: mctc-lib_DIR)
-- Retrieving mctc-lib revision v0.4.1 from https://github.com/grimme-lab/mctc-lib
-- Found OpenMP_C: -fopenmp (found version "3.1")
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "3.1")
-- mstore: Find installed package
-- Could NOT find mstore (missing: mstore_DIR)
-- Retrieving mstore revision v0.3.0 from https://github.com/grimme-lab/mstore
-- multicharge: Find installed package
-- Could NOT find multicharge (missing: multicharge_DIR)
-- Retrieving multicharge revision v0.4.0 from https://github.com/grimme-lab/multicharge
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so;/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Configuring done (351.7s)
CMake Warning at build_intel/_deps/multicharge-src/app/CMakeLists.txt:16 (add_executable):
  Cannot generate a safe runtime search path for target multicharge-exe
  because files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at build_intel/_deps/multicharge-src/test/unit/CMakeLists.txt:32 (add_executable):
  Cannot generate a safe runtime search path for target multicharge-tester
  because files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at app/CMakeLists.txt:17 (add_executable):
  Cannot generate a safe runtime search path for target dftd4-exe because
  files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at test/api/CMakeLists.txt:17 (add_executable):
  Cannot generate a safe runtime search path for target dftd4-api-tester
  because files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at test/unit/CMakeLists.txt:35 (add_executable):
  Cannot generate a safe runtime search path for target dftd4-tester because
  files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


-- Generating done (93.6s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.

compilation
~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.m -j2
[  1%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/error.f90.o
[  1%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/accuracy.f90.o
[  2%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/version.F90.o
[  2%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/system.f90.o
[  3%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/resize.f90.o
[  3%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/testing.f90.o
[  4%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/structure/info.f90.o
[  4%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/utils.f90.o
[  5%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env.f90.o
[  5%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/symbols.f90.o
[  5%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/filetype.f90.o
[  5%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/codata2018.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/structure.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/paulingen.f90.o
[  7%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/constants.f90.o
[  8%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/qcschema.F90.o
[  8%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/gaussian.f90.o
[ 10%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/gaussian.f90.o
[ 10%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/qcschema.f90.o
[ 12%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/math.f90.o
[ 12%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/convert.f90.o
[ 12%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/cutoff.f90.o
[ 12%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/atomicrad.f90.o
[ 14%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/aims.f90.o
[ 14%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/covrad.f90.o
[ 14%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/cjson.F90.o
[ 15%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/ctfile.f90.o
[ 15%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/genformat.f90.o
[ 17%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/pdb.f90.o
[ 17%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/qchem.f90.o
[ 18%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/vasp.f90.o
[ 18%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/turbomole.f90.o
[ 19%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/xyz.f90.o
[ 20%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/aims.f90.o
[ 21%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/cjson.f90.o
[ 21%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/ctfile.f90.o
[ 21%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/genformat.f90.o
[ 22%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/pdb.f90.o
[ 22%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/qchem.f90.o
[ 23%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/vasp.f90.o
[ 23%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/turbomole.f90.o
[ 24%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/xyz.f90.o
[ 25%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read.f90.o
[ 25%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/vdwrad.f90.o
[ 25%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write.f90.o
[ 26%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io.f90.o
[ 26%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data.f90.o
[ 27%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/type.f90.o
[ 28%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/erf.f90.o
[ 28%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/dexp.f90.o
[ 29%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/exp.f90.o
[ 30%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/erf/en.f90.o
[ 30%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/erf/dftd4.f90.o
[ 31%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord.f90.o
[ 32%] Linking Fortran static library libmctc-lib.a
[ 32%] Built target mctc-lib-lib
[ 33%] Building Fortran object _deps/mctc-lib-build/app/CMakeFiles/mctc-convert.dir/main.f90.o
[ 33%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/cutoff.f90.o
[ 34%] Linking Fortran executable mctc-convert
[ 35%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/blas.F90.o
[ 35%] Built target mctc-convert
[ 36%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/ewald.f90.o
[ 36%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/lapack.F90.o
[ 36%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/testsuite_structure.f90.o
[ 37%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/version.f90.o
[ 38%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_math.f90.o
[ 38%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/param/eeq2019.f90.o
[ 39%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read.f90.o
[ 40%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_aims.f90.o
[ 40%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/wignerseitz.f90.o
[ 40%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_cjson.f90.o
[ 41%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_ctfile.f90.o
[ 42%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/model.F90.o
[ 42%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_gaussian.f90.o
[ 43%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_genformat.f90.o
[ 45%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/output.f90.o
[ 45%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_pdb.f90.o
[ 45%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/param.f90.o
[ 45%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_qchem.f90.o
[ 46%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_qcschema.f90.o
[ 47%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge.f90.o
[ 47%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_turbomole.f90.o
[ 48%] Linking Fortran static library libmulticharge.a
[ 49%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_vasp.f90.o
[ 50%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_xyz.f90.o
[ 50%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_symbols.f90.o
[ 50%] Built target multicharge-lib
[ 50%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_ncoord.f90.o
[ 51%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/data/record.f90.o
[ 52%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore_version.f90.o
[ 53%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/amino20x4.f90.o
[ 53%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/but14diol.f90.o
[ 53%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/data/collection.f90.o
[ 54%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/f_block.f90.o
[ 56%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/heavy28.f90.o
[ 56%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write.f90.o
[ 56%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_aims.f90.o
[ 56%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/ice10.f90.o
[ 58%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_cjson.f90.o
[ 58%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/il16.f90.o
[ 58%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_ctfile.f90.o
[ 59%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/mb16_43.f90.o
[ 59%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_gaussian.f90.o
[ 60%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_genformat.f90.o
[ 61%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_pdb.f90.o
[ 61%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/upu23.f90.o
[ 63%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_qchem.f90.o
[ 63%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/x23.f90.o
[ 63%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_turbomole.f90.o
[ 64%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_vasp.f90.o
[ 65%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_xyz.f90.o
[ 66%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_cutoff.f90.o
[ 66%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_data.f90.o
[ 66%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/data/store.f90.o
[ 66%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore.f90.o
[ 66%] Linking Fortran static library libmstore.a
[ 67%] Built target mstore-lib
[ 67%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/main.f90.o
[ 67%] Linking Fortran executable mctc-lib-tester
[ 68%] Building Fortran object _deps/multicharge-build/app/CMakeFiles/multicharge-exe.dir/main.f90.o
[ 69%] Linking Fortran executable multicharge
[ 69%] Built target multicharge-exe
[ 70%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/test_model.f90.o
[ 70%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/test_pbc.f90.o
[ 70%] Built target mctc-lib-tester
[ 71%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/cutoff.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/cutoff.f90(121): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_lattice_points_cutoff
--------------------^
[ 72%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/test_wignerseitz.f90.o
[ 73%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/damping.f90.o
[ 74%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/damping/atm.f90.o
[ 74%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/main.f90.o
[ 75%] Linking Fortran executable multicharge-tester
[ 76%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/covrad.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/covrad.f90(72): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_covalent_rad_sym
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/covrad.f90(87): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_covalent_rad_num
--------------------^
[ 77%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/en.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/en.f90(68): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_electronegativity_sym
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/en.f90(83): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_electronegativity_num
--------------------^
[ 77%] Built target multicharge-tester
[ 77%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/hardness.f90.o
[ 78%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/r4r2.f90.o
[ 79%] Building Fortran object _deps/mstore-build/app/fortranize/CMakeFiles/mstore-fortranize.dir/main.f90.o
[ 79%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/wfpair.f90.o
[ 80%] Linking Fortran executable mstore-fortranize
[ 80%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/zeff.f90.o
[ 80%] Built target mstore-fortranize
[ 81%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/blas.F90.o
[ 82%] Building Fortran object _deps/mstore-build/app/info/CMakeFiles/mstore-info.dir/main.f90.o
[ 82%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/charge.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/charge.f90(34): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_charges
--------------------^
[ 83%] Linking Fortran executable mstore-info
[ 84%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/type.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/type.f90(167): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: d4_ref
--------------------^
[ 84%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/utils.f90.o
[ 84%] Built target mstore-info
[ 85%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/ncoord.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/ncoord.f90(37): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_coordination_number
--------------------^
[ 86%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/utils.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/utils.f90(29): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: wrap_to_central_cell
--------------------^
[ 87%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/version.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/version.f90(38): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dftd4_version
--------------------^
[ 87%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data.f90.o
[ 87%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/damping/rational.f90.o
[ 87%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/reference.f90.o
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
[ 88%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/d4s.f90.o
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
   !DEC$ ATTRIBUTES DLLEXPORT :: get_polarizibilities
--------------------^
[ 88%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/d4.f90.o
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
   !DEC$ ATTRIBUTES DLLEXPORT :: get_polarizibilities
--------------------^
[ 89%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/param.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/param.f90(100): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_functionals
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/param.f90(249): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_rational_damping_name
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/param.f90(270): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_rational_damping_id
--------------------^
[ 89%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model.f90.o
[ 90%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/disp.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/disp.f90(40): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dispersion
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/disp.f90(128): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_properties
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/disp.f90(172): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_pairwise_dispersion
--------------------^
[ 90%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/output.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(39): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_atomic_radii
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(72): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_atomic_references
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(121): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_system_properties
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(173): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_results
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(225): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_pairwise
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(277): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_damping_param
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(315): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: turbomole_gradlatt
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(405): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: turbomole_gradient
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(517): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: json_results
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(633): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: tagged_result
--------------------^
[ 91%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/numdiff.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/numdiff.f90(36): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dispersion_hessian
--------------------^
[ 92%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/api.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(95): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_version_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(109): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_error_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(124): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: delete_error_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(143): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: check_error_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(168): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_error_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(198): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_structure_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(247): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: delete_structure_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(266): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: update_structure_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(309): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_d4_model_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(349): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_d4s_model_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(389): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: custom_d4_model_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(432): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: custom_d4s_model_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(473): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: delete_model_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(493): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_rational_damping_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(527): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: load_rational_damping_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(564): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: delete_param_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(584): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dispersion_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(664): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_numerical_hessian_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(720): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_pairwise_dispersion_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(775): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_properties_api
--------------------^
[ 92%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4.f90.o
[ 92%] Linking Fortran static library libdftd4.a
[ 92%] Built target dftd4-lib
[ 92%] Building C object test/api/CMakeFiles/dftd4-api-tester.dir/example.c.o
In file included from /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:21:0:
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c: In function ‘test_uninitialized_structure’:
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:53:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(error);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:58:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(error);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c: In function ‘test_example’:
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:155:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(param);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:178:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(param);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:179:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(disp);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:211:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(param);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:212:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(disp);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:223:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(disp);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:234:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(disp);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:235:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(mol);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:236:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(error);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:266:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(param);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:267:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(disp);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:268:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(mol);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:269:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(error);
     ^
make[2]: *** [test/api/CMakeFiles/dftd4-api-tester.dir/example.c.o] Error 1
make[1]: *** [test/api/CMakeFiles/dftd4-api-tester.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 94%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/argument.f90.o
[ 94%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/help.f90.o
[ 94%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/cli.f90.o
[ 95%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/driver.f90.o
[ 95%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/main.f90.o
[ 95%] Linking Fortran executable dftd4
[ 95%] Built target dftd4-exe
make: *** [all] Error 2
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.
[  1%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/error.f90.o
[  1%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/accuracy.f90.o
[  2%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/version.F90.o
[  2%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/system.f90.o
[  3%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/resize.f90.o
[  3%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env/testing.f90.o
[  4%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/structure/info.f90.o
[  4%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/utils.f90.o
[  5%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/env.f90.o
[  5%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/symbols.f90.o
[  5%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/filetype.f90.o
[  5%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/codata2018.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/structure.f90.o
[  6%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/paulingen.f90.o
[  7%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/constants.f90.o
[  8%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/qcschema.F90.o
[  8%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/gaussian.f90.o
[ 10%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/gaussian.f90.o
[ 10%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/qcschema.f90.o
[ 12%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/math.f90.o
[ 12%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/convert.f90.o
[ 12%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/cutoff.f90.o
[ 12%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/atomicrad.f90.o
[ 14%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/aims.f90.o
[ 14%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/covrad.f90.o
[ 14%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/cjson.F90.o
[ 15%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/ctfile.f90.o
[ 15%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/genformat.f90.o
[ 17%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/pdb.f90.o
[ 17%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/qchem.f90.o
[ 18%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/vasp.f90.o
[ 18%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/turbomole.f90.o
[ 19%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read/xyz.f90.o
[ 20%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/aims.f90.o
[ 21%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/cjson.f90.o
[ 21%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/ctfile.f90.o
[ 21%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/genformat.f90.o
[ 22%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/pdb.f90.o
[ 22%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/qchem.f90.o
[ 23%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/vasp.f90.o
[ 23%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/turbomole.f90.o
[ 24%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write/xyz.f90.o
[ 25%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/read.f90.o
[ 25%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data/vdwrad.f90.o
[ 25%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io/write.f90.o
[ 26%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/io.f90.o
[ 26%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/data.f90.o
[ 27%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/type.f90.o
[ 28%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/erf.f90.o
[ 28%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/dexp.f90.o
[ 29%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/exp.f90.o
[ 30%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/erf/en.f90.o
[ 30%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord/erf/dftd4.f90.o
[ 31%] Building Fortran object _deps/mctc-lib-build/CMakeFiles/mctc-lib-lib.dir/src/mctc/ncoord.f90.o
[ 32%] Linking Fortran static library libmctc-lib.a
[ 32%] Built target mctc-lib-lib
[ 33%] Building Fortran object _deps/mctc-lib-build/app/CMakeFiles/mctc-convert.dir/main.f90.o
[ 33%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/cutoff.f90.o
[ 34%] Linking Fortran executable mctc-convert
[ 35%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/blas.F90.o
[ 35%] Built target mctc-convert
[ 36%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/ewald.f90.o
[ 36%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/lapack.F90.o
[ 36%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/testsuite_structure.f90.o
[ 37%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/version.f90.o
[ 38%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_math.f90.o
[ 38%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/param/eeq2019.f90.o
[ 39%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read.f90.o
[ 40%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_aims.f90.o
[ 40%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/wignerseitz.f90.o
[ 40%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_cjson.f90.o
[ 41%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_ctfile.f90.o
[ 42%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/model.F90.o
[ 42%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_gaussian.f90.o
[ 43%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_genformat.f90.o
[ 45%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/output.f90.o
[ 45%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_pdb.f90.o
[ 45%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge/param.f90.o
[ 45%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_qchem.f90.o
[ 46%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_qcschema.f90.o
[ 47%] Building Fortran object _deps/multicharge-build/CMakeFiles/multicharge-lib.dir/src/multicharge.f90.o
[ 47%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_turbomole.f90.o
[ 48%] Linking Fortran static library libmulticharge.a
[ 49%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_vasp.f90.o
[ 50%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_read_xyz.f90.o
[ 50%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_symbols.f90.o
[ 50%] Built target multicharge-lib
[ 50%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_ncoord.f90.o
[ 51%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/data/record.f90.o
[ 52%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore_version.f90.o
[ 53%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/amino20x4.f90.o
[ 53%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/but14diol.f90.o
[ 53%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/data/collection.f90.o
[ 54%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/f_block.f90.o
[ 56%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/heavy28.f90.o
[ 56%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write.f90.o
[ 56%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_aims.f90.o
[ 56%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/ice10.f90.o
[ 58%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_cjson.f90.o
[ 58%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/il16.f90.o
[ 58%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_ctfile.f90.o
[ 59%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/mb16_43.f90.o
[ 59%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_gaussian.f90.o
[ 60%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_genformat.f90.o
[ 61%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_pdb.f90.o
[ 61%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/upu23.f90.o
[ 63%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_qchem.f90.o
[ 63%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/x23.f90.o
[ 63%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_turbomole.f90.o
[ 64%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_vasp.f90.o
[ 65%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_write_xyz.f90.o
[ 66%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_cutoff.f90.o
[ 66%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/test_data.f90.o
[ 66%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore/data/store.f90.o
[ 66%] Building Fortran object _deps/mstore-build/CMakeFiles/mstore-lib.dir/src/mstore.f90.o
[ 66%] Linking Fortran static library libmstore.a
[ 67%] Built target mstore-lib
[ 67%] Building Fortran object _deps/mctc-lib-build/test/CMakeFiles/mctc-lib-tester.dir/main.f90.o
[ 67%] Linking Fortran executable mctc-lib-tester
[ 68%] Building Fortran object _deps/multicharge-build/app/CMakeFiles/multicharge-exe.dir/main.f90.o
[ 69%] Linking Fortran executable multicharge
[ 69%] Built target multicharge-exe
[ 70%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/test_model.f90.o
[ 70%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/test_pbc.f90.o
[ 70%] Built target mctc-lib-tester
[ 71%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/cutoff.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/cutoff.f90(121): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_lattice_points_cutoff
--------------------^
[ 72%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/test_wignerseitz.f90.o
[ 73%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/damping.f90.o
[ 74%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/damping/atm.f90.o
[ 74%] Building Fortran object _deps/multicharge-build/test/unit/CMakeFiles/multicharge-tester.dir/main.f90.o
[ 75%] Linking Fortran executable multicharge-tester
[ 76%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/covrad.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/covrad.f90(72): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_covalent_rad_sym
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/covrad.f90(87): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_covalent_rad_num
--------------------^
[ 77%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/en.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/en.f90(68): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_electronegativity_sym
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/data/en.f90(83): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_electronegativity_num
--------------------^
[ 77%] Built target multicharge-tester
[ 77%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/hardness.f90.o
[ 78%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/r4r2.f90.o
[ 79%] Building Fortran object _deps/mstore-build/app/fortranize/CMakeFiles/mstore-fortranize.dir/main.f90.o
[ 79%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/wfpair.f90.o
[ 80%] Linking Fortran executable mstore-fortranize
[ 80%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data/zeff.f90.o
[ 80%] Built target mstore-fortranize
[ 81%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/blas.F90.o
[ 82%] Building Fortran object _deps/mstore-build/app/info/CMakeFiles/mstore-info.dir/main.f90.o
[ 82%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/charge.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/charge.f90(34): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_charges
--------------------^
[ 83%] Linking Fortran executable mstore-info
[ 84%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/type.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/model/type.f90(167): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: d4_ref
--------------------^
[ 84%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/utils.f90.o
[ 84%] Built target mstore-info
[ 85%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/ncoord.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/ncoord.f90(37): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_coordination_number
--------------------^
[ 86%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/utils.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/utils.f90(29): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: wrap_to_central_cell
--------------------^
[ 87%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/version.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/version.f90(38): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dftd4_version
--------------------^
[ 87%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/data.f90.o
[ 87%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/damping/rational.f90.o
[ 87%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/reference.f90.o
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
[ 88%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/d4s.f90.o
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
   !DEC$ ATTRIBUTES DLLEXPORT :: get_polarizibilities
--------------------^
[ 88%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model/d4.f90.o
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
   !DEC$ ATTRIBUTES DLLEXPORT :: get_polarizibilities
--------------------^
[ 89%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/param.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/param.f90(100): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_functionals
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/param.f90(249): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_rational_damping_name
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/param.f90(270): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_rational_damping_id
--------------------^
[ 89%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/model.f90.o
[ 90%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/disp.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/disp.f90(40): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dispersion
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/disp.f90(128): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_properties
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/disp.f90(172): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_pairwise_dispersion
--------------------^
[ 90%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/output.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(39): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_atomic_radii
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(72): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_atomic_references
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(121): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_system_properties
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(173): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_results
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(225): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_pairwise
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(277): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: ascii_damping_param
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(315): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: turbomole_gradlatt
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(405): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: turbomole_gradient
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(517): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: json_results
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/output.f90(633): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: tagged_result
--------------------^
[ 91%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/numdiff.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/numdiff.f90(36): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dispersion_hessian
--------------------^
[ 92%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4/api.f90.o
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(95): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_version_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(109): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_error_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(124): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: delete_error_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(143): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: check_error_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(168): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_error_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(198): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_structure_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(247): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: delete_structure_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(266): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: update_structure_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(309): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_d4_model_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(349): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_d4s_model_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(389): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: custom_d4_model_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(432): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: custom_d4s_model_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(473): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: delete_model_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(493): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: new_rational_damping_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(527): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: load_rational_damping_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(564): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: delete_param_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(584): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_dispersion_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(664): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_numerical_hessian_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(720): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_pairwise_dispersion_api
--------------------^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/src/dftd4/api.f90(775): remark #7841: DLL IMPORT/EXPORT is not supported on this platform.   [DLLEXPORT]
   !DEC$ ATTRIBUTES DLLEXPORT :: get_properties_api
--------------------^
[ 92%] Building Fortran object CMakeFiles/dftd4-lib.dir/src/dftd4.f90.o
[ 92%] Linking Fortran static library libdftd4.a
[ 92%] Built target dftd4-lib
[ 92%] Building C object test/api/CMakeFiles/dftd4-api-tester.dir/example.c.o
In file included from /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:21:0:
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c: In function ‘test_uninitialized_structure’:
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:53:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(error);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:58:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(error);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c: In function ‘test_example’:
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:155:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(param);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:178:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(param);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:179:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(disp);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:211:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(param);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:212:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(disp);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:223:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(disp);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:234:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(disp);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:235:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(mol);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:236:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(error);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:266:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(param);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:267:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(disp);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:268:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(mol);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:269:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(error);
     ^
make[2]: *** [test/api/CMakeFiles/dftd4-api-tester.dir/example.c.o] Error 1
make[1]: *** [test/api/CMakeFiles/dftd4-api-tester.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 94%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/argument.f90.o
[ 94%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/help.f90.o
[ 94%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/cli.f90.o
[ 95%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/driver.f90.o
[ 95%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/main.f90.o
[ 95%] Linking Fortran executable dftd4
[ 95%] Built target dftd4-exe
make: *** [all] Error 2
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.

[ 95%] Building C object test/api/CMakeFiles/dftd4-api-tester.dir/example.c.o
cd /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/test/api && /usr/bin/cc -DIK=i4 -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-src/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-build/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/multicharge-build/include -O2 -g -DNDEBUG -MD -MT test/api/CMakeFiles/dftd4-api-tester.dir/example.c.o -MF CMakeFiles/dftd4-api-tester.dir/example.c.o.d -o CMakeFiles/dftd4-api-tester.dir/example.c.o -c /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c
In file included from /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:21:0:
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c: In function ‘test_uninitialized_structure’:
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \
                        ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c:53:5: note: in expansion of macro ‘dftd4_delete’
     dftd4_delete(error);
     ^
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include/dftd4.h:53:24: error: expected expression before ‘dftd4_error’
                        dftd4_error: dftd4_delete_error, \


milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/./usr/bin/cc --version
cc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44)
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


