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


milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel_api/.FC=ifort CC=icc cmake  -Dmctc-lib_DIR=$MCTCDIR   -DWITH_API=OFF  -DCMAKE_INSTALL_PREFIX=/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4   ..
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- mctc-lib: Find installed package
-- Could NOT find mctc-lib (missing: mctc-lib_DIR)
-- Retrieving mctc-lib revision v0.4.2 from https://github.com/grimme-lab/mctc-lib
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- mstore: Find installed package
-- Could NOT find mstore (missing: mstore_DIR)
-- Retrieving mstore revision v0.3.0 from https://github.com/grimme-lab/mstore
-- multicharge: Find installed package
-- Could NOT find multicharge (missing: multicharge_DIR)
-- Retrieving multicharge revision v0.4.0 from https://github.com/grimme-lab/multicharge
-- Configuring done (51.3s)
CMake Warning at build_intel_api/_deps/multicharge-src/app/CMakeLists.txt:16 (add_executable):
  Cannot generate a safe runtime search path for target multicharge-exe
  because files in some directories may conflict with libraries in implicit
  directories:

    runtime library [libiomp5.so] in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin may be hidden by files in:
      /lustre/home/user/m/milias/work/software/ams/linux.openmpi/ams2021.107/bin/lib

  Some of these libraries may not be found correctly.


CMake Warning at build_intel_api/_deps/multicharge-src/test/unit/CMakeLists.txt:32 (add_executable):
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


-- Generating done (48.4s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel_api
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel_api/.
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel_api/.make -j2 all install    
.
.
.
[ 33%] Built target mctc-lib-lib
[ 34%] Built target mctc-convert
[ 47%] Built target multicharge-lib
[ 70%] Built target mstore-lib
[ 70%] Built target mctc-lib-tester
[ 71%] Built target multicharge-exe
[ 74%] Built target multicharge-tester
[ 75%] Linking Fortran static library libdftd4.a
[ 76%] Built target mstore-fortranize
[ 81%] Built target mstore-info
[ 93%] Built target dftd4-lib
[ 94%] Linking Fortran executable dftd4
[ 95%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_dftd4.f90.o
[ 97%] Built target dftd4-exe
[ 98%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_model.f90.o
[ 98%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_pairwise.f90.o
[ 99%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_param.f90.o
[ 99%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_periodic.f90.o
[ 99%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/main.f90.o
[100%] Linking Fortran executable dftd4-tester
[100%] Built target dftd4-tester
Install the project...
-- Install configuration: "RelWithDebInfo"
-- Installing: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4/lib64/cmake/dftd4
-- Installing: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4/lib64/cmake/dftd4/Findmctc-lib.cmake
-- Installing: /lustre/home/user/m/milias/w
.
.
-- Installing: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4/include/dftd4/Intel-2021.4.0.20210910/dftd4_data_zeff.mod
-- Installing: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4/share/licenses/dftd4/COPYING
-- Installing: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4/share/licenses/dftd4/COPYING.LESSER
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel_api/.

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel_api/.ctest -j4
Test project /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel_api
      Start  1: mctc-lib/cutoff
      Start  2: mctc-lib/data
      Start  3: mctc-lib/math
      Start  4: mctc-lib/ncoord
 1/36 Test  #1: mctc-lib/cutoff ..................   Passed    0.23 sec
 2/36 Test  #2: mctc-lib/data ....................   Passed    0.50 sec
 3/36 Test  #3: mctc-lib/math ....................   Passed    0.87 sec
      Start  5: mctc-lib/read
      Start  6: mctc-lib/read-aims
      Start  7: mctc-lib/read-cjson
 4/36 Test  #4: mctc-lib/ncoord ..................   Passed    1.14 sec
      Start  8: mctc-lib/read-ctfile
 5/36 Test  #5: mctc-lib/read ....................   Passed    2.96 sec
      Start  9: mctc-lib/read-gaussian
 6/36 Test  #6: mctc-lib/read-aims ...............   Passed    3.66 sec
      Start 10: mctc-lib/read-genformat
 7/36 Test  #9: mctc-lib/read-gaussian ...........   Passed    1.63 sec
      Start 11: mctc-lib/read-pdb
 8/36 Test  #7: mctc-lib/read-cjson ..............   Passed    6.57 sec
      Start 12: mctc-lib/read-qchem
 9/36 Test #11: mctc-lib/read-pdb ................   Passed    2.21 sec
      Start 13: mctc-lib/read-qcschema
10/36 Test  #8: mctc-lib/read-ctfile .............   Passed    7.69 sec
      Start 14: mctc-lib/read-turbomole
11/36 Test #10: mctc-lib/read-genformat ..........   Passed    4.39 sec
      Start 15: mctc-lib/read-vasp
12/36 Test #12: mctc-lib/read-qchem ..............   Passed    4.15 sec
      Start 16: mctc-lib/read-xyz
13/36 Test #15: mctc-lib/read-vasp ...............   Passed    3.76 sec
      Start 17: mctc-lib/symbols
14/36 Test #17: mctc-lib/symbols .................   Passed    0.31 sec
      Start 18: mctc-lib/write
15/36 Test #16: mctc-lib/read-xyz ................   Passed    3.77 sec
      Start 19: mctc-lib/write-aims
16/36 Test #13: mctc-lib/read-qcschema ...........   Passed    8.56 sec
17/36 Test #14: mctc-lib/read-turbomole ..........   Passed    8.13 sec
18/36 Test #19: mctc-lib/write-aims ..............   Passed    1.46 sec
      Start 20: mctc-lib/write-cjson
      Start 21: mctc-lib/write-ctfile
      Start 22: mctc-lib/write-gaussian
19/36 Test #18: mctc-lib/write ...................   Passed    3.72 sec
      Start 23: mctc-lib/write-genformat
20/36 Test #22: mctc-lib/write-gaussian ..........   Passed    0.40 sec
      Start 24: mctc-lib/write-pdb
21/36 Test #20: mctc-lib/write-cjson .............   Passed    0.83 sec
22/36 Test #21: mctc-lib/write-ctfile ............   Passed    1.12 sec
      Start 25: mctc-lib/write-qchem
      Start 26: mctc-lib/write-turbomole
23/36 Test #23: mctc-lib/write-genformat .........   Passed    1.26 sec
24/36 Test #24: mctc-lib/write-pdb ...............   Passed    1.15 sec
      Start 27: mctc-lib/write-vasp
      Start 28: mctc-lib/write-xyz
25/36 Test #25: mctc-lib/write-qchem .............   Passed    0.91 sec
      Start 29: model
26/36 Test #28: mctc-lib/write-xyz ...............   Passed    0.61 sec
      Start 30: pbc
27/36 Test #26: mctc-lib/write-turbomole .........   Passed    1.60 sec
28/36 Test #29: model ............................   Passed    0.68 sec
      Start 31: wignerseitz
      Start 32: model
29/36 Test #27: mctc-lib/write-vasp ..............   Passed    1.60 sec
30/36 Test #30: pbc ..............................   Passed    1.03 sec
      Start 33: dftd4
      Start 34: pairwise
31/36 Test #31: wignerseitz ......................   Passed    0.61 sec
32/36 Test #32: model ............................   Passed    0.87 sec
      Start 35: param
      Start 36: periodic
33/36 Test #34: pairwise .........................   Passed    0.55 sec
34/36 Test #35: param ............................   Passed    0.57 sec
35/36 Test #33: dftd4 ............................   Passed    1.13 sec
36/36 Test #36: periodic .........................   Passed    1.41 sec

100% tests passed, 0 tests failed out of 36

Total Test time (real) =  24.84 sec
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel_api/.

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel_api/./lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4/bin/dftd4 --help
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

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/build_intel_api/.

