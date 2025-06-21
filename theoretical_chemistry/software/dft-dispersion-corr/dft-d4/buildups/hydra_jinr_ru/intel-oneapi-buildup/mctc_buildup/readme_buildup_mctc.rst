============
MCTC-LIBRARY
============

clone
~~~~~
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/mctc/.git clone git@github.com:grimme-lab/mctc-lib.git
Cloning into 'mctc-lib'...

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/mctc/mctc-lib/.ls
app/     CMakeLists.txt  doc/     example/  include/  man/         meson_options.txt  src/          test/
_build/  config/         docs.md  fpm.toml  LICENSE   meson.build  README.md          subprojects/

configuration
~~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/mctc/mctc-lib/build_inteloneapi/.FC=ifort CC=icc cmake ..-- The Fortran compiler identification is Intel 2021.4.0.20210910
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/ifort - skipped
-- Setting build type to 'RelWithDebInfo' as none was specified.
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- Configuring done (58.7s)
-- Generating done (24.3s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/mctc/mctc-lib/build_inteloneapi

compilation
~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/mctc/mctc-lib/build_inteloneapi/.m -j4
[  4%] Building Fortran object CMakeFiles/mctc-lib-lib.dir/src/mctc/env/accuracy.f90.o
.
.
[100%] Linking Fortran executable mctc-lib-tester
[100%] Built target mctc-lib-tester

tests
~~~~~
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/mctc/mctc-lib/build_inteloneapi/.ctest -j4
Test project /lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/mctc/mctc-lib/build_inteloneapi
.
.
.
25/29 Test #25: mctc-lib/write-qchem .............   Passed    2.89 sec
26/29 Test #26: mctc-lib/write-qcschema ..........   Passed    3.10 sec
      Start 29: mctc-lib/write-xyz
27/29 Test #27: mctc-lib/write-turbomole .........   Passed    4.14 sec
28/29 Test #29: mctc-lib/write-xyz ...............   Passed    1.86 sec
29/29 Test #28: mctc-lib/write-vasp ..............   Passed    4.26 sec

100% tests passed, 0 tests failed out of 29

Total Test time (real) =  56.19 sec
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/mctc/mctc-lib/build_inteloneapi/.

