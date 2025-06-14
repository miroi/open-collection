======================
DFTD4 on hydra.jinr.ru
======================


git clone  git@github.com:dftd4/dftd4.git
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.mkdir build_gnu

module add gcc/v12.3.0 CMake/v3.29.2 LAPACK/v3.12.0_gcc1230

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1               3) gcc/v12.3.0              5) LAPACK/v3.12.0_gcc1230
  2) BASE/1.0                 4) CMake/v3.29.2

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.which gfortran
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gfortran
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.which gcc
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gcc

configuration
~~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.FC=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gfortran CC=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gcc   cmake -B build_gnu
-- The Fortran compiler identification is GNU 12.3.0
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gfortran - skipped
-- Setting build type to 'RelWithDebInfo' as none was specified.
-- Found OpenMP_Fortran: -fopenmp (found version "4.5")
-- Found OpenMP: TRUE (found version "4.5")
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - not found
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/LAPACK/v3.12.0_gcc1230/lib64/libblas.so
-- mctc-lib: Find installed package
-- Could NOT find mctc-lib (missing: mctc-lib_DIR)
-- Retrieving mctc-lib revision v0.4.1 from https://github.com/grimme-lab/mctc-lib
-- Found OpenMP_Fortran: -fopenmp (found version "4.5")
-- mstore: Find installed package
-- Could NOT find mstore (missing: mstore_DIR)
-- Retrieving mstore revision v0.3.0 from https://github.com/grimme-lab/mstore
-- multicharge: Find installed package
-- Could NOT find multicharge (missing: multicharge_DIR)
-- Retrieving multicharge revision v0.4.0 from https://github.com/grimme-lab/multicharge
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/LAPACK/v3.12.0_gcc1230/lib64/liblapack.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/LAPACK/v3.12.0_gcc1230/lib64/libblas.so
-- The C compiler identification is GNU 12.3.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Configuring done (305.6s)
-- Generating done (100.8s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu

compilation
~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/.make VERBOSE=1
.
.
.
[100%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/main.f90.o
cd /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/test/unit && /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gfortran -DIK=i4 -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/_deps/mctc-lib-src/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/_deps/mctc-lib-build/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/_deps/multicharge-build/include -I/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/_deps/mstore-build/include -O2 -g -fopenmp -c /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/test/unit/main.f90 -o CMakeFiles/dftd4-tester.dir/main.f90.o
[100%] Linking Fortran executable dftd4-tester
cd /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/test/unit && /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E cmake_link_script CMakeFiles/dftd4-tester.dir/link.txt --verbose=1
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gfortran -O2 -g "CMakeFiles/dftd4-tester.dir/main.f90.o" "CMakeFiles/dftd4-tester.dir/test_model.f90.o" "CMakeFiles/dftd4-tester.dir/test_dftd4.f90.o" "CMakeFiles/dftd4-tester.dir/test_pairwise.f90.o" "CMakeFiles/dftd4-tester.dir/test_param.f90.o" "CMakeFiles/dftd4-tester.dir/test_periodic.f90.o" -o dftd4-tester  ../../libdftd4.a ../../_deps/multicharge-build/libmulticharge.a /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/LAPACK/v3.12.0_gcc1230/lib64/liblapack.so /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/LAPACK/v3.12.0_gcc1230/lib64/libblas.so ../../_deps/mstore-build/libmstore.a ../../_deps/mctc-lib-build/libmctc-lib.a /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/lib64/libgomp.so -lpthread
make[2]: Leaving directory `/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu'
[100%] Built target dftd4-tester
make[1]: Leaving directory `/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu'
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/bin/cmake -E cmake_progress_start /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/CMakeFiles 0

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/.ls
app/            CMakeFiles/          config/              _deps/    libdftd4.a  src/
CMakeCache.txt  cmake_install.cmake  CTestTestfile.cmake  include/  Makefile    test/
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/.ls app/
CMakeFiles/  cmake_install.cmake  dftd4*  dftd4_argument.mod  dftd4_cli.mod  dftd4_driver.mod  dftd4_help.mod  Makefile
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/.ldd app/dftd4
        linux-vdso.so.1 =>  (0x00007ffe88fa3000)
        liblapack.so.3 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/LAPACK/v3.12.0_gcc1230/lib64/liblapack.so.3 (0x00002b6f2ce97000)
        libblas.so.3 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/LAPACK/v3.12.0_gcc1230/lib64/libblas.so.3 (0x00002b6f2d77b000)
        libgomp.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/lib64/libgomp.so.1 (0x00002b6f2da1e000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00002b6f2dc63000)
        libgfortran.so.5 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/lib64/libgfortran.so.5 (0x00002b6f2de7f000)
        libm.so.6 => /lib64/libm.so.6 (0x00002b6f2e345000)
        libgcc_s.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/lib64/libgcc_s.so.1 (0x00002b6f2e647000)
        libquadmath.so.0 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/lib64/libquadmath.so.0 (0x00002b6f2e865000)
        libc.so.6 => /lib64/libc.so.6 (0x00002b6f2eaaa000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00002b6f2ee78000)
        /lib64/ld-linux-x86-64.so.2 (0x00002b6f2cc73000)
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_gnu/.

