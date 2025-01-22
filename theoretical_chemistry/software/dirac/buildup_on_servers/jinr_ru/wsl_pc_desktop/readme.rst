===============
DIRAC on WSL PC
===============

MKL library
------------
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.sudo apt-get install intel-mkl-full libmkl-gf-ilp64 libmkl-gf-lp64 libmkl-gnu-thread libmkl-scalapack-ilp64 libmkl-scalapack-lp64
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
intel-mkl-full is already the newest version (2020.4.304-2ubuntu3).
libmkl-gf-ilp64 is already the newest version (2020.4.304-2ubuntu3).
libmkl-gf-ilp64 set to manually installed.
libmkl-gf-lp64 is already the newest version (2020.4.304-2ubuntu3).
libmkl-gf-lp64 set to manually installed.
libmkl-gnu-thread is already the newest version (2020.4.304-2ubuntu3).
libmkl-gnu-thread set to manually installed.
libmkl-scalapack-ilp64 is already the newest version (2020.4.304-2ubuntu3).
libmkl-scalapack-ilp64 set to manually installed.
libmkl-scalapack-lp64 is already the newest version (2020.4.304-2ubuntu3).
libmkl-scalapack-lp64 set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 17 not upgraded.

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.mpif90 --version
GNU Fortran (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.mpicc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.mpicxx --version
g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.mpirun --version
mpirun (Open MPI) 4.1.2

buildup
~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.sudo  apt-get install hdf5-tools  libhdf5-openmpi-dev

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/../setup  --int64 --mpi  --fc=mpif90 --cc=mpicc --cxx=mpicxx  --cmake-options="-D ENABLE_PELIB=OFF"  build_gnu_mkl_ilp64
cmake -DCMAKE_Fortran_COMPILER=mpif90 -DEXTRA_FCFLAGS="''" -DCMAKE_C_COMPILER=mpicc -DEXTRA_CFLAGS="''" -DCMAKE_CXX_COMPILER=mpicxx -DEXTRA_CXXFLAGS="''" -DPREPROCESSOR_DEFINITIONS="''" -DPYTHON_INTERPRETER="''" -DENABLE_BLAS=auto -DENABLE_LAPACK=auto -DMKL_FLAG=off -DMATH_LIB_SEARCH_ORDER="MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE" -DBLAS_LANG=Fortran -DLAPACK_LANG=Fortran -DENABLE_MPI=True -DENABLE_OPENMP=True -DENABLE_CODE_COVERAGE=False -DENABLE_STATIC_LINKING=False -DENABLE_PROFILING=False -DENABLE_RUNTIMECHECK=False -DENABLE_64BIT_INTEGERS=True -DEXPLICIT_LIBS="off" -DENABLE_EXATENSOR=ON -DENABLE_PCMSOLVER=OFF -DPCMSOLVER_ROOT='' -DENABLE_STIELTJES=OFF -DCMAKE_BUILD_TYPE=release -G"Unix Makefiles" -D ENABLE_PELIB=OFF -H/home/milias/work/software/dirac/trunk_cloned -Bbuild_gnu_mkl_ilp64

-- The Fortran compiler identification is GNU 11.4.0
-- The C compiler identification is GNU 11.4.0
-- The CXX compiler identification is GNU 11.4.0
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /usr/bin/mpif90 - skipped
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/mpicc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/mpicxx - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found Python: /usr/bin/python3.10 (found version "3.10.12") found components: Interpreter
-- Searching for BLAS using search order MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE
-- Setting -DHAVE_MKL_BLAS
-- Found BLAS: MKL (-Wl,--start-group;/usr/lib/x86_64-linux-gnu/libmkl_gf_ilp64.so;/usr/lib/x86_64-linux-gnu/libmkl_gnu_thread.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;/usr/lib/x86_64-linux-gnu/libpthread.a;/usr/lib/x86_64-linux-gnu/libm.so;-fopenmp;-Wl,--end-group)
-- Searching for LAPACK using search order MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE
-- Setting -DHAVE_MKL_LAPACK
-- Found LAPACK: MKL (-Wl,--start-group;/usr/lib/x86_64-linux-gnu/libmkl_lapack95_ilp64.a;/usr/lib/x86_64-linux-gnu/libmkl_gf_ilp64.so;-fopenmp;-Wl,--end-group)
-- MATH_LIB_SEARCH_ORDER set to MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE
-- Found MPI_C: /usr/bin/mpicc (found version "3.1")
-- Found MPI_CXX: /usr/bin/mpicxx (found version "3.1")
-- Found MPI_Fortran: /usr/bin/mpif90 (found version "3.1")
-- Found MPI: TRUE (found version "3.1")
-- Found OpenMP_C: -fopenmp (found version "4.5")
-- Found OpenMP_CXX: -fopenmp (found version "4.5")
-- Found OpenMP_Fortran: -fopenmp (found version "4.5")
-- Found OpenMP: TRUE (found version "4.5")
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
-- Found HDF5: /usr/lib/x86_64-linux-gnu/hdf5/openmpi/libhdf5.so;/usr/lib/x86_64-linux-gnu/libcrypto.so;/usr/lib/x86_64-linux-gnu/libcurl.so;/usr/lib/x86_64-linux-gnu/libsz.so;/usr/lib/x86_64-linux-gnu/libz.so;/usr/lib/x86_64-linux-gnu/libdl.a;/usr/lib/x86_64-linux-gnu/libm.so (found version "1.10.7") found components: C
-- HFD5 found, enabling HDF5 interface
-- HDF5 include directory location: /usr/include/hdf5/openmpi
-- MPI package type: MPICH
-- Compiling /home/milias/work/software/dirac/trunk_cloned/cmake/custom/test-MPI-compiler-compatibility.F90 ...
-- Performing Test MPI_COMPILER_MATCHES ...
-- Performing Test MPI_COMPILER_MATCHES - Failed
-- ...for the corresponding error message check the file /home/milias/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64/CMakeFiles/CMakeError.log
-- mpi.mod is compiled with different compiler or compiler flags, using '#include "mpif.h"' instead
-- Compiling /home/milias/work/software/dirac/trunk_cloned/cmake/custom/test-MPI-itype-compatibility.F90 ...
-- Performing Test MPI_ITYPE_MATCHES ...
-- Performing Test MPI_ITYPE_MATCHES - Success
-- Well, program got compiled with 64-bit integers, but the internal MPI integer compatibility test will be performed inside dirac.x.
-- Set CDash default timeout for single test set to 1500 seconds. Overwritten by test's TIMEOUT property label and, ultimatively, by pam timeout setting.
-- Test's 'basis_input_scripted' timeout set to 3600 seconds. Can be overwritten by pam's timeout setting.
-- -mkl=... flag removed due to lacking Intel Fortran compiler. THEREFORE CHECK IF YOU HAVE SET MATH LIBRARIES !
-- Polarizable Continuum Model via PCMSolver DISABLED
-- ExaTensor library cannot work with 64 bit integers, switched off
-- Enable ExaTENSOR library: OFF
-- Gen1Int module: ON
-- PElib module: OFF
-- The XCFun submodule ENABLED
-- ESR property module: ON
-- Stieltjes external module DISABLED
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
-- User name: milias
-- Host name: DESKTOP-7OTLCGO
-- Operating system: Linux-5.15.167.4-microsoft-standard-WSL2
-- CMake version: 3.22.1
-- CMake generator: Unix Makefiles
-- CMake build type: release
-- Configuration time: 2025-01-22 13:30:28.490181+00:00
-- Fortran compiler ID: GNU
-- Fortran compiler: /usr/bin/mpif90
-- Fortran compiler version: GNU 11.4.0
-- Fortran compiler flags:  -g -fcray-pointer -fbacktrace -fno-range-check -DVAR_GFORTRAN -DVAR_MFDS -fallow-argument-mismatch  -fopenmp -fdefault-integer-8 -fno-lto
-- C compiler ID: GNU
-- C compiler: /usr/bin/mpicc
-- C compiler version: GNU 11.4.0
-- C compiler flags:  -g  -fopenmp -fno-lto
-- CXX compiler ID: GNU
-- CXX compiler: /usr/bin/mpicxx
-- CXX compiler version: GNU 11.4.0
-- CXX compiler flags:  -g -Wall -Wno-unknown-pragmas -Wno-sign-compare -Woverloaded-virtual -Wwrite-strings -Wno-unused  -fopenmp -fno-lto
-- Static linking: False
-- 64-bit integers: True
-- MPI parallelization: True
-- MPI launcher: /usr/bin/mpiexec
-- Math libraries: -Wl,--start-group;/usr/lib/x86_64-linux-gnu/libmkl_lapack95_ilp64.a;/usr/lib/x86_64-linux-gnu/libmkl_gf_ilp64.so;-fopenmp;-Wl,--end-group;-Wl,--start-group;/usr/lib/x86_64-linux-gnu/libmkl_gf_ilp64.so;/usr/lib/x86_64-linux-gnu/libmkl_gnu_thread.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;/usr/lib/x86_64-linux-gnu/libpthread.a;/usr/lib/x86_64-linux-gnu/libm.so;-fopenmp;-Wl,--end-group
-- Compile definitions: HAVE_MKL_BLAS;HAVE_MKL_LAPACK;HAVE_MPI;HAVE_OPENMP;VAR_MPI;VAR_MPI2;SYS_LINUX;PRG_DIRAC;INT_STAR8;INSTALL_WRKMEM=64000000;BUILD_GEN1INT;MOD_LAO_REARRANGED;MOD_MCSCF_spinfree;MOD_XAMFI;MOD_ESR;MOD_KRCC;MOD_SRDFT
-- Exacorr module enabled : OFF
-- Found HDF5: /usr/lib/x86_64-linux-gnu/hdf5/openmpi/libhdf5.so;/usr/lib/x86_64-linux-gnu/libcrypto.so;/usr/lib/x86_64-linux-gnu/libcurl.so;/usr/lib/x86_64-linux-gnu/libsz.so;/usr/lib/x86_64-linux-gnu/libz.so;/usr/lib/x86_64-linux-gnu/libdl.a;/usr/lib/x86_64-linux-gnu/libm.so (found version "1.10.7") found components: C HL
-- For checking, linked libraries to dirac.x: objlib.dirac.x;xcfun_fortran_bindings;/home/milias/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64/external/xcfun-build/src/libxcfun.a;gen1int_interface;/home/milias/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64/external/lib/libgen1int.a;-Wl,--start-group;/usr/lib/x86_64-linux-gnu/libmkl_lapack95_ilp64.a;/usr/lib/x86_64-linux-gnu/libmkl_gf_ilp64.so;-fopenmp;-Wl,--end-group;-Wl,--start-group;/usr/lib/x86_64-linux-gnu/libmkl_gf_ilp64.so;/usr/lib/x86_64-linux-gnu/libmkl_gnu_thread.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;/usr/lib/x86_64-linux-gnu/libpthread.a;/usr/lib/x86_64-linux-gnu/libm.so;-fopenmp;-Wl,--end-group;qcorr;HDF5::HDF5;laplace
-- Found Sphinx: /home/milias/.local/bin/sphinx-build
-- Copied DIRAC basis set directories into the build directory
-- Copied data schema and python utilities into the build directory
-- Set CDash default timeout for single test set to 1500 seconds. Overwritten by test's TIMEOUT property label and, ultimatively, by pam timeout setting.
-- Test's 'basis_input_scripted' timeout set to 3600 seconds. Can be overwritten by pam's timeout setting.
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64

   configure step is done
   now you need to compile the sources:
   $ cd build_gnu_mkl_ilp64
   $ make
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/.

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64/.ldd dirac.x
        linux-vdso.so.1 (0x00007ffede9ac000)
        libmkl_gf_ilp64.so => /lib/x86_64-linux-gnu/libmkl_gf_ilp64.so (0x00007f6dbbc00000)
        libmkl_gnu_thread.so => /lib/x86_64-linux-gnu/libmkl_gnu_thread.so (0x00007f6db9e00000)
        libmkl_core.so => /lib/x86_64-linux-gnu/libmkl_core.so (0x00007f6db5600000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007f6db5325000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f6dbc999000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x00007f6dbc89c000)
        libhdf5_openmpi.so.103 => /lib/x86_64-linux-gnu/libhdf5_openmpi.so.103 (0x00007f6db4f70000)
        libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007f6dbbb9a000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x00007f6db9cc9000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x00007f6db9c7f000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f6dbbb7a000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f6db4d47000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f6dbc895000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f6dbc890000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f6db4cff000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f6dde559000)
        libcrypto.so.3 => /lib/x86_64-linux-gnu/libcrypto.so.3 (0x00007f6db48bb000)
        libcurl.so.4 => /lib/x86_64-linux-gnu/libcurl.so.4 (0x00007f6db4814000)
        libsz.so.2 => /lib/x86_64-linux-gnu/libsz.so.2 (0x00007f6dbc889000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f6db9c63000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007f6db4761000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007f6db46a4000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x00007f6db4648000)
        libnghttp2.so.14 => /lib/x86_64-linux-gnu/libnghttp2.so.14 (0x00007f6db461e000)
        libidn2.so.0 => /lib/x86_64-linux-gnu/libidn2.so.0 (0x00007f6db9c42000)
        librtmp.so.1 => /lib/x86_64-linux-gnu/librtmp.so.1 (0x00007f6db45ff000)
        libssh.so.4 => /lib/x86_64-linux-gnu/libssh.so.4 (0x00007f6db4592000)
        libpsl.so.5 => /lib/x86_64-linux-gnu/libpsl.so.5 (0x00007f6dbbb66000)
        libssl.so.3 => /lib/x86_64-linux-gnu/libssl.so.3 (0x00007f6db44ee000)
        libgssapi_krb5.so.2 => /lib/x86_64-linux-gnu/libgssapi_krb5.so.2 (0x00007f6db449a000)
        libldap-2.5.so.0 => /lib/x86_64-linux-gnu/libldap-2.5.so.0 (0x00007f6db443b000)
        liblber-2.5.so.0 => /lib/x86_64-linux-gnu/liblber-2.5.so.0 (0x00007f6db442a000)
        libzstd.so.1 => /lib/x86_64-linux-gnu/libzstd.so.1 (0x00007f6db435b000)
        libbrotlidec.so.1 => /lib/x86_64-linux-gnu/libbrotlidec.so.1 (0x00007f6db434d000)
        libaec.so.0 => /lib/x86_64-linux-gnu/libaec.so.0 (0x00007f6db4344000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x00007f6db430f000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x00007f6db430a000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007f6db42e0000)
        libunistring.so.2 => /lib/x86_64-linux-gnu/libunistring.so.2 (0x00007f6db4136000)
        libgnutls.so.30 => /lib/x86_64-linux-gnu/libgnutls.so.30 (0x00007f6db3f4b000)
        libhogweed.so.6 => /lib/x86_64-linux-gnu/libhogweed.so.6 (0x00007f6db3f03000)
        libnettle.so.8 => /lib/x86_64-linux-gnu/libnettle.so.8 (0x00007f6db3ebd000)
        libgmp.so.10 => /lib/x86_64-linux-gnu/libgmp.so.10 (0x00007f6db3e3b000)
        libkrb5.so.3 => /lib/x86_64-linux-gnu/libkrb5.so.3 (0x00007f6db3d70000)
        libk5crypto.so.3 => /lib/x86_64-linux-gnu/libk5crypto.so.3 (0x00007f6db3d41000)
        libcom_err.so.2 => /lib/x86_64-linux-gnu/libcom_err.so.2 (0x00007f6db3d3b000)
        libkrb5support.so.0 => /lib/x86_64-linux-gnu/libkrb5support.so.0 (0x00007f6db3d2d000)
        libsasl2.so.2 => /lib/x86_64-linux-gnu/libsasl2.so.2 (0x00007f6db3d12000)
        libbrotlicommon.so.1 => /lib/x86_64-linux-gnu/libbrotlicommon.so.1 (0x00007f6db3cef000)
        libp11-kit.so.0 => /lib/x86_64-linux-gnu/libp11-kit.so.0 (0x00007f6db3bb2000)
        libtasn1.so.6 => /lib/x86_64-linux-gnu/libtasn1.so.6 (0x00007f6db3b9a000)
        libkeyutils.so.1 => /lib/x86_64-linux-gnu/libkeyutils.so.1 (0x00007f6db3b93000)
        libresolv.so.2 => /lib/x86_64-linux-gnu/libresolv.so.2 (0x00007f6db3b7f000)
        libffi.so.8 => /lib/x86_64-linux-gnu/libffi.so.8 (0x00007f6db3b72000)

Tests
~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64/.export DIRAC_MPI_COMMAND="mpirun -np 2"
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64/.ctest -L short -j2
Test project /home/milias/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64
      Start  87: fscc_finite-field
      Start  88: reladc_dip
 1/81 Test  #88: reladc_dip .......................   Passed    1.02 sec
      Start  89: x2c-SCF_to_4c-SCF
 2/81 Test  #89: x2c-SCF_to_4c-SCF ................   Passed    2.76 sec
      Start  90: xyz_symmetry_recognition
 3/81 Test  #90: xyz_symmetry_recognition .........   Passed    7.64 sec
      Start  91: nmqm_operator
 4/81 Test  #87: fscc_finite-field ................   Passed   12.33 sec
      Start  92: visual_div_rot
.
.
.
getting errors, due to memory allocations..
