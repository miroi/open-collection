DFTB+ on WSL2
=============


https://github.com/dftbplus/dftbplus


clone devel version
--------------------
miroi@MIRO:~/work/software/dftbplus/.git clone git@github.com:dftbplus/dftbplus.git  dftbplus_cloned

get submodules
~~~~~~~~~~~~~~
miroi@MIRO:~/work/software/dftbplus/dftbplus_cloned/.gsu

installation
------------
https://github.com/dftbplus/dftbplus/blob/main/INSTALL.rst

externals
~~~~~~~~~
miroi@MIRO:~/work/software/dftbplus/dftbplus_cloned/../utils/get_opt_externals

see also miroi@MIRO:~/work/software/dftbplus/dftbplus_cloned/../utils/get_opt_externals -h

configuration
-------------
miroi@MIRO:~/work/software/dftbplus/dftbplus_cloned/.FC=gfortran CC=gcc  cmake  -DLAPACK_LIBRARY="-Wl,--start-group -lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -Wl,--end-group"  -DWITH_MBD=ON -DWITH_TBLITE=ON -DWITH_SDFTD3=ON   -DCMAKE_INSTALL_PREFIX=/home/miroi/work/software/dftbplus/dftb+_installed -B _build .
-- Reading global build config file: /home/miroi/work/software/dftbplus/dftbplus_cloned/config.cmake
-- The Fortran compiler identification is GNU 13.3.0
-- The C compiler identification is GNU 13.3.0
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /usr/bin/gfortran - skipped
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Build type: RelWithDebInfo (default single-config)
-- Reading build environment specific toolchain file: /home/miroi/work/software/dftbplus/dftbplus_cloned/sys/gnu.cmake
-- Flags for Fortran-compiler (build type: RelWithDebInfo):    -g -O2 -funroll-all-loops
-- Flags for C-compiler (build type: RelWithDebInfo):
-- Found OpenMP_C: -fopenmp (found version "4.5")
-- Found OpenMP_Fortran: -fopenmp (found version "4.5")
-- Found OpenMP: TRUE (found version "4.5")
-- Found Git: /usr/bin/git (found version "2.43.0")
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - not found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /usr/lib/x86_64-linux-gnu/libmkl_gf_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_gnu_thread.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;/usr/lib/gcc/x86_64-linux-gnu/13/libgomp.so;-lm;-ldl
-- Found CustomBlas: /usr/lib/x86_64-linux-gnu/libmkl_gf_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_gnu_thread.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;/usr/lib/gcc/x86_64-linux-gnu/13/libgomp.so;-lm;-ldl
-- Found CustomLapack: -Wl,--start-group -lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -Wl,--end-group
-- Mbd: Using source in external/mbd/origin
-- Setting version tag to 0.12.8 from Git
-- mctc-lib: Using source in external/mctc-lib/origin
-- mstore: Using source in external/mstore/origin
-- toml-f: Using source in external/toml-f/origin
CMake Deprecation Warning at external/toml-f/origin/CMakeLists.txt:14 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- test-drive: Find installed package
-- Could NOT find test-drive (missing: test-drive_DIR)
-- Retrieving test-drive from https://github.com/fortran-lang/test-drive
CMake Deprecation Warning at _build/_deps/test-drive-src/CMakeLists.txt:14 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- Performing Test WITH_QP
-- Performing Test WITH_QP - Success
-- Performing Test WITH_XDP
-- Performing Test WITH_XDP - Success
-- s-dftd3: Using source in external/s-dftd3/origin
-- multicharge: Using source in external/multicharge/origin
-- dftd4: Using source in external/dftd4/origin
-- tblite: Using source in external/tblite/origin
-- DFTB+ API version: 0.4.0
-- Configuring done (13.3s)
CMake Warning (dev) in external/toml-f/origin/test/version/CMakeLists.txt:
  Policy CMP0110 is not set: add_test() supports arbitrary characters in test
  names.  Run "cmake --help-policy CMP0110" for policy details.  Use the
  cmake_policy command to set the policy and suppress this warning.

  The following name given to add_test() is invalid if CMP0110 is not set or
  set to OLD:

    toml-f/"version"´

This warning is for project developers.  Use -Wno-dev to suppress it.

-- Generating done (0.3s)
-- Build files have been written to: /home/miroi/work/software/dftbplus/dftbplus_cloned/_build

compilation
-----------
miroi@MIRO:~/work/software/dftbplus/dftbplus_cloned/. cmake --build _build -- -j


testing
-------
miroi@MIRO:~/work/software/dftbplus/dftbplus_cloned/_build/.ctest -j2
.
.
439/441 Test #440: app/modes/C24O6H8_extfile ........................................   Passed    0.08 sec
        Start 441: app/modes/C24O6H8_select
440/441 Test #441: app/modes/C24O6H8_select .........................................   Passed    0.10 sec
441/441 Test #430: app/dftb+/scc/SiC64+V_dynforce ...................................   Passed    2.30 sec

100% tests passed, 0 tests failed out of 441

Total Test time (real) = 264.80 sec

installation
------------
cmake --install _build
.
.
-- Installing: /home/miroi/work/software/dftbplus/dftb+_installed/lib/cmake/dftbplus/Modules/CustomLibraryFinder.cmake
-- Installing: /home/miroi/work/software/dftbplus/dftb+_installed/lib/cmake/dftbplus/Modules/FindCustomMagma.cmake
-- Installing: /home/miroi/work/software/dftbplus/dftb+_installed/lib/pkgconfig/dftbplus.pc
miroi@MIRO:~/work/software/dftbplus/dftbplus_cloned/.

miroi@MIRO:~/work/software/dftbplus/dftb+_installed/.ls
bin/  include/  lib/  share/

miroi@MIRO:~/work/software/dftbplus/dftb+_installed/.ls bin/
calc_timeprop_maxpoldir*  dftb+*  integvalue*    modes*              mstore-info*  polyvalue*   s-dftd3*   splvalue*  waveplot*
calc_timeprop_spectrum*   dftd4*  mctc-convert*  mstore-fortranize*  multicharge*  printunits*  skderivs*  tblite*



