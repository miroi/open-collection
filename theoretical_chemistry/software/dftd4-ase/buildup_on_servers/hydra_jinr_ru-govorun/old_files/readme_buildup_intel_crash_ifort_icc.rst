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

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/FC=ifort CC=icc  cmake -B build_intel/
-- The Fortran compiler identification is Intel 2021.1.0.20201112
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/ifort - skipped
-- Setting build type to 'RelWithDebInfo' as none was specified.
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- The C compiler identification is Intel 2021.1.0.20201112
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/icc - skipped
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
-- Found LAPACK: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so;/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Configuring done (367.6s)
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


-- Generating done (95.2s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/.m VERBOSE=1 -j2
.
.
.
Scanning dependencies of target dftd4-exe
make[2]: Leaving directory `/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel'
make  -f test/api/CMakeFiles/dftd4-api-tester.dir/build.make test/api/CMakeFiles/dftd4-api-tester.dir/build
make[2]: Entering directory `/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel'
[ 92%] Building C object test/api/CMakeFiles/dftd4-api-tester.dir/example.c.o
cd /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/test/api && /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/icc -DIK=i4 -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-src/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-build/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/multicharge-build/include -O2 -g -DNDEBUG -MD -MT test/api/CMakeFiles/dftd4-api-tester.dir/example.c.o -MF CMakeFiles/dftd4-api-tester.dir/example.c.o.d -o CMakeFiles/dftd4-api-tester.dir/example.c.o -c /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c
/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(53): error: type name is not allowed
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(53): error: expected a ")"
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(53): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(58): error: type name is not allowed
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(58): error: expected a ")"
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(58): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(155): error: type name is not allowed
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(155): error: expected a ")"
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(155): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(178): error: type name is not allowed
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(178): error: expected a ")"
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(178): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(179): error: type name is not allowed
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(179): error: expected a ")"
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(179): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(211): error: type name is not allowed
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(211): error: expected a ")"
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(211): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(212): error: type name is not allowed
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(212): error: expected a ")"
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(212): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(223): error: type name is not allowed
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(223): error: expected a ")"
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(223): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(234): error: type name is not allowed
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(234): error: expected a ")"
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(234): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(235): error: type name is not allowed
      dftd4_delete(mol);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(235): error: expected a ")"
      dftd4_delete(mol);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(235): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(mol);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(236): error: type name is not allowed
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(236): error: expected a ")"
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(236): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(266): error: type name is not allowed
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(266): error: expected a ")"
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(266): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(param);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(267): error: type name is not allowed
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(267): error: expected a ")"
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(267): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(disp);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(268): error: type name is not allowed
      dftd4_delete(mol);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(268): error: expected a ")"
      dftd4_delete(mol);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(268): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(mol);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(269): error: type name is not allowed
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(269): error: expected a ")"
      dftd4_delete(error);
      ^

/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c(269): error: expression preceding parentheses of apparent call must have (pointer-to-) function type
      dftd4_delete(error);
      ^

compilation aborted for /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/api/example.c (code 2)
make[2]: *** [test/api/CMakeFiles/dftd4-api-tester.dir/example.c.o] Error 2
make[2]: Leaving directory `/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel'
make[1]: *** [test/api/CMakeFiles/dftd4-api-tester.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
make[2]: Leaving directory `/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel'
make  -f app/CMakeFiles/dftd4-exe.dir/build.make app/CMakeFiles/dftd4-exe.dir/build
make[2]: Entering directory `/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel'
[ 94%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/argument.f90.o
[ 94%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/help.f90.o
cd /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/app && /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/ifort -DIK=i4 -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-src/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-build/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/multicharge-build/include -O2 -g -qopenmp -c /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/app/help.f90 -o CMakeFiles/dftd4-exe.dir/help.f90.o
cd /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/app && /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/ifort -DIK=i4 -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-src/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-build/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/multicharge-build/include -O2 -g -qopenmp -c /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/app/argument.f90 -o CMakeFiles/dftd4-exe.dir/argument.f90.o
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E cmake_copy_f90_mod app/dftd4_help.mod app/CMakeFiles/dftd4-exe.dir/dftd4_help.mod.stamp Intel
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E cmake_copy_f90_mod app/dftd4_argument.mod app/CMakeFiles/dftd4-exe.dir/dftd4_argument.mod.stamp Intel
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E touch app/CMakeFiles/dftd4-exe.dir/help.f90.o.provides.build
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E touch app/CMakeFiles/dftd4-exe.dir/argument.f90.o.provides.build
[ 94%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/cli.f90.o
cd /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/app && /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/ifort -DIK=i4 -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-src/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-build/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/multicharge-build/include -O2 -g -qopenmp -c /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/app/cli.f90 -o CMakeFiles/dftd4-exe.dir/cli.f90.o
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E cmake_copy_f90_mod app/dftd4_cli.mod app/CMakeFiles/dftd4-exe.dir/dftd4_cli.mod.stamp Intel
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E touch app/CMakeFiles/dftd4-exe.dir/cli.f90.o.provides.build
[ 95%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/driver.f90.o
cd /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/app && /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/ifort -DIK=i4 -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-src/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-build/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/multicharge-build/include -O2 -g -qopenmp -c /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/app/driver.f90 -o CMakeFiles/dftd4-exe.dir/driver.f90.o
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E cmake_copy_f90_mod app/dftd4_driver.mod app/CMakeFiles/dftd4-exe.dir/dftd4_driver.mod.stamp Intel
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E touch app/CMakeFiles/dftd4-exe.dir/driver.f90.o.provides.build
[ 95%] Building Fortran object app/CMakeFiles/dftd4-exe.dir/main.f90.o
cd /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/app && /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/ifort -DIK=i4 -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-src/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/mctc-lib-build/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/_deps/multicharge-build/include -O2 -g -qopenmp -c /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/app/main.f90 -o CMakeFiles/dftd4-exe.dir/main.f90.o
[ 95%] Linking Fortran executable dftd4
cd /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel/app && /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E cmake_link_script CMakeFiles/dftd4-exe.dir/link.txt --verbose=1
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/ifort -O2 -g "CMakeFiles/dftd4-exe.dir/main.f90.o" "CMakeFiles/dftd4-exe.dir/argument.f90.o" "CMakeFiles/dftd4-exe.dir/cli.f90.o" "CMakeFiles/dftd4-exe.dir/driver.f90.o" "CMakeFiles/dftd4-exe.dir/help.f90.o" -o dftd4  -Wl,-rpath,/lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib: ../libdftd4.a ../_deps/multicharge-build/libmulticharge.a ../_deps/mctc-lib-build/libmctc-lib.a /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_thread.so /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib/libiomp5.so -lpthread -lm -ldl /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin/libiomp5.so
make[2]: Leaving directory `/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel'
[ 95%] Built target dftd4-exe
make[1]: Leaving directory `/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel'
make: *** [all] Error 2


