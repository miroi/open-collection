DIRAC buildups on Devana
=========================

/home/milias/work/software/dirac/dirac_public

modules
-------

OpenMPI-Intel
~~~~~~~~~~~~~
module load OpenMPI/4.1.1-intel-compilers-2021.4.0

which mpif90
/storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90
mpif90 --version
ifort (IFORT) 2021.4.0 20210910

which mpirun
/storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpirun
milias@login02.devana.local:~/work/software/dirac/dirac_public/.mpirun --version
mpirun (Open MPI) 4.1.1


MKL
~~~
module load mkl/latest
Loading mkl version 2023.0.0
Loading tbb version 2021.8.0
Loading compiler-rt version 2023.0.0

ls /storage-apps/intel-v.2023/oneapi/mkl/2023.0.0/lib/intel64/


CMake
~~~~~~
milias@login02.devana.local:~/work/software/dirac/dirac_public/.module load CMake/3.20.1-GCCcore-10.3.0


HDF5
~~~~
module load HDF5/1.10.7-iompi-2021a

All modules
~~~~~~~~~~~
module list

Currently Loaded Modules:
  1) OpenSSL/1.1                 10) XZ/5.2.5-GCCcore-10.3.0           19) libevent/2.1.12-GCCcore-10.3.0
  2) tbb/2021.8.0                11) libarchive/3.5.1-GCCcore-10.3.0   20) UCX/1.10.0-GCCcore-10.3.0
  3) compiler-rt/2023.0.0        12) CMake/3.20.1-GCCcore-10.3.0       21) libfabric/1.12.1-GCCcore-10.3.0
  4) mkl/latest                  13) binutils/2.36.1-GCCcore-10.3.0    22) PMIx/3.2.3-GCCcore-10.3.0
  5) GCCcore/10.3.0              14) intel-compilers/2021.2.0          23) OpenMPI/4.1.1-intel-compilers-2021.2.0
  6) ncurses/6.2-GCCcore-10.3.0  15) numactl/2.0.14-GCCcore-10.3.0     24) iompi/2021a
  7) zlib/1.2.11-GCCcore-10.3.0  16) libxml2/2.9.10-GCCcore-10.3.0     25) Szip/2.1.1-GCCcore-10.3.0
  8) bzip2/1.0.8-GCCcore-10.3.0  17) libpciaccess/0.16-GCCcore-10.3.0  26) HDF5/1.10.7-iompi-2021a
  9) cURL/7.76.0-GCCcore-10.3.0  18) hwloc/2.4.1-GCCcore-10.3.0



DIRAC with OpenMPI-Intel-i8
---------------------------

milias@login02.devana.local:~/work/software/dirac/dirac_public/../setup --mpi --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx  --mkl=parallel  build_openmpi_intel_mklpar_i8

-- The Fortran compiler identification is Intel 20.2.2.20210228
-- The C compiler identification is Intel 20.2.2.20210228
-- The CXX compiler identification is Intel 20.2.2.20210228
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpif90 - skipped
-- Checking whether /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpif90 supports Fortran 90
-- Checking whether /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpif90 supports Fortran 90 - yes
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpicc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpicxx - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PythonInterp: /usr/bin/python (found version "2.7.5") 
-- User set explicit MKL flag which is passed to the compiler and linker: -mkl=parallel
-- This disables math detection and builtin math libraries
-- Setting -DHAVE_MKL_BLAS and -DHAVE_MKL_LAPACK
-- MATH_LIB_SEARCH_ORDER set to MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE
-- Found MPI_C: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpicc (found version "3.1") 
-- Found MPI_CXX: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpicxx (found version "3.1") 
-- Found MPI_Fortran: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpif90 (found version "3.1") 
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
-- Performing Test blas_test_run - Failed
-- Test of blas integer size SUCCESS .. blas is integer*8 
-- We have BLAS-integer*8
-- Found HDF5: /storage-apps/easybuild/software/HDF5/1.10.7-iompi-2021a/lib/libhdf5.so;/usr/lib64/libpthread.so;/storage-apps/easybuild/software/Szip/2.1.1-GCCcore-10.3.0/lib/libsz.so;/storage-apps/easybuild/software/zlib/1.2.11-GCCcore-10.3.0/lib/libz.so;/usr/lib64/libdl.so;/usr/lib64/libm.so;/storage-apps/easybuild/software/intel-compilers/2021.2.0/compiler/2021.2.0/linux/compiler/lib/intel64/libiomp5.so;/usr/lib64/libpthread.so (found version "1.10.7") found components: C 
-- HFD5 found, enabling HDF5 interface 
-- HDF5 include directory location: /storage-apps/easybuild/software/HDF5/1.10.7-iompi-2021a/include;/storage-apps/easybuild/software/zlib/1.2.11-GCCcore-10.3.0/include;/storage-apps/easybuild/software/Szip/2.1.1-GCCcore-10.3.0/include 
-- MPI package type: OPENMPI
-- Compiling /home/milias/work/software/dirac/dirac_public/cmake/custom/test-MPI-compiler-compatibility.F90 ...
-- Performing Test MPI_COMPILER_MATCHES ...
-- Performing Test MPI_COMPILER_MATCHES - Failed
-- ...for the corresponding error message check the file /home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i8/CMakeFiles/CMakeError.log
-- mpi.mod is compiled with different compiler or compiler flags, using '#include "mpif.h"' instead
-- Compiling /home/milias/work/software/dirac/dirac_public/cmake/custom/test-MPI-itype-compatibility.F90 ...
-- Performing Test MPI_ITYPE_MATCHES ...
-- Performing Test MPI_ITYPE_MATCHES - Success
-- Well, program got compiled with 64-bit integers, but the internal MPI integer compatibility test will be performed inside dirac.x.
-- Set CDash default timeout for single test set to 1500 seconds. Overwritten by test's TIMEOUT property label and, ultimatively, by pam timeout setting.
-- Test's 'basis_input_scripted' timeout set to 3600 seconds. Can be overwritten by pam's timeout setting.
-- -mkl=... flag for MKL libraries kept because Intel Fortran compiler is present
-- PCMSolver not found. The pre-packaged version will be built.
-- Polarizable Continuum Model via PCMSolver ENABLED
-- ExaTensor library can not work with 64 bit integers, switched off
-- Enable ExaTENSOR library: OFF
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
-- Versions from CMake variable (20.2.2.20210228) and Python script (2021.2) for C compiler are not equal!
-- Versions from CMake variable (20.2.2.20210228) and Python script (2021.2.0) for C++ compiler are not equal!
-- Versions from CMake variable (20.2.2.20210228) and Python script (2021.2) for Fortran compiler are not equal!
-- User name: milias
-- Host name: login01.devana.local
-- Operating system: Linux-3.10.0-1160.71.1.el7.x86_64
-- CMake version: 3.20.1
-- CMake generator: Unix Makefiles
-- CMake build type: release
-- Configuration time: 2023-08-14 08:49:54.146769
-- Fortran compiler ID: Intel
-- Fortran compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpif90
-- Fortran compiler version: Intel 2021.2
-- Fortran compiler flags:  -w -assume byterecl -g -traceback -DVAR_IFORT  -qopenmp -i8
-- C compiler ID: Intel
-- C compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpicc
-- C compiler version: Intel 2021.2
-- C compiler flags:  -g -wd981 -wd279 -wd383 -wd1572 -wd177  -qopenmp
-- CXX compiler ID: Intel
-- CXX compiler: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpicxx
-- CXX compiler version: Intel 2021.2.0
-- CXX compiler flags:  -Wno-unknown-pragmas  -qopenmp
-- Static linking: False
-- 64-bit integers: True
-- MPI parallelization: True
-- MPI launcher: /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/bin/mpiexec
-- Intel MKL flag: parallel
-- Compile definitions: HAVE_MKL_BLAS;HAVE_MKL_LAPACK;HAVE_MPI;HAVE_OPENMP;VAR_MPI;VAR_MPI2;SYS_LINUX;PRG_DIRAC;INT_STAR8;INSTALL_WRKMEM=64000000;HAS_PCMSOLVER;BUILD_GEN1INT;HAS_PELIB;HAS_STIELTJES;MOD_LAO_REARRANGED;MOD_MCSCF_spinfree;MOD_XAMFI;MOD_ESR;MOD_KRCC;MOD_SRDFT
-- Exacorr module enabled : OFF
-- Found HDF5: /storage-apps/easybuild/software/HDF5/1.10.7-iompi-2021a/lib/libhdf5.so;/usr/lib64/libpthread.so;/storage-apps/easybuild/software/Szip/2.1.1-GCCcore-10.3.0/lib/libsz.so;/storage-apps/easybuild/software/zlib/1.2.11-GCCcore-10.3.0/lib/libz.so;/usr/lib64/libdl.so;/usr/lib64/libm.so;/storage-apps/easybuild/software/intel-compilers/2021.2.0/compiler/2021.2.0/linux/compiler/lib/intel64/libiomp5.so;/usr/lib64/libpthread.so (found version "1.10.7") found components: C HL 
-- For checking, linked libraries to dirac.x: objlib.dirac.x;pelib_interface;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i8/external/lib/libstieltjes.a;mpi;imf;svml;irng;stdc++;m;ipgo;decimal;stdc++;gcc;gcc_s;irc;svml;c;gcc;gcc_s;irc_s;dl;c;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i8/external/pcmsolver/install/lib/libpcm.a;/storage-apps/easybuild/software/zlib/1.2.11-GCCcore-10.3.0/lib/libz.so;mpi;imf;svml;irng;stdc++;m;ipgo;decimal;stdc++;gcc;gcc_s;irc;svml;c;gcc;gcc_s;irc_s;dl;c;/storage-apps/easybuild/software/zlib/1.2.11-GCCcore-10.3.0/lib/libz.so;xcfun_fortran_bindings;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i8/external/xcfun-build/src/libxcfun.a;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i8/external/lib/libpelib.a;gen1int_interface;/home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i8/external/lib/libgen1int.a;qcorr;HDF5::HDF5;laplace 
-- Could NOT find Sphinx (missing: SPHINX_EXECUTABLE) 
-- Copied DIRAC basis set directories into the build directory
-- Copied data schema and python utilities into the build directory
-- Set CDash default timeout for single test set to 1500 seconds. Overwritten by test's TIMEOUT property label and, ultimatively, by pam timeout setting.
-- Test's 'basis_input_scripted' timeout set to 3600 seconds. Can be overwritten by pam's timeout setting.
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i8

m -j16
.
.
milias@login01.devana.local:~/work/software/dirac/dirac_public/build_openmpi_intel_mklpar_i8/.ldd dirac.x 
        linux-vdso.so.1 =>  (0x00007ffdb057a000)
        libmkl_intel_ilp64.so.2 => /storage-apps/intel-v.2023/oneapi/mkl/2023.0.0/lib/intel64/libmkl_intel_ilp64.so.2 (0x00002baa032ce000)
        libmkl_intel_thread.so.2 => /storage-apps/intel-v.2023/oneapi/mkl/2023.0.0/lib/intel64/libmkl_intel_thread.so.2 (0x00002baa04189000)
        libmkl_core.so.2 => /storage-apps/intel-v.2023/oneapi/mkl/2023.0.0/lib/intel64/libmkl_core.so.2 (0x00002baa07922000)
        libiomp5.so => /storage-apps/easybuild/software/intel-compilers/2021.2.0/compiler/2021.2.0/linux/compiler/lib/intel64_lin/libiomp5.so (0x00002baa0bd04000)
        libmpi.so.40 => /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/lib/libmpi.so.40 (0x00002baa030d0000)
        libimf.so => /storage-apps/easybuild/software/intel-compilers/2021.2.0/compiler/2021.2.0/linux/compiler/lib/intel64_lin/libimf.so (0x00002baa0c11b000)
        libsvml.so => /storage-apps/easybuild/software/intel-compilers/2021.2.0/compiler/2021.2.0/linux/compiler/lib/intel64_lin/libsvml.so (0x00002baa0c7a3000)
        libirng.so => /storage-apps/easybuild/software/intel-compilers/2021.2.0/compiler/2021.2.0/linux/compiler/lib/intel64_lin/libirng.so (0x00002baa0e2a0000)
        libstdc++.so.6 => /storage-apps/easybuild/software/GCCcore/10.3.0/lib64/libstdc++.so.6 (0x00002baa0e60a000)
        libm.so.6 => /lib64/libm.so.6 (0x00002baa0e7f1000)
        libgcc_s.so.1 => /storage-apps/easybuild/software/GCCcore/10.3.0/lib64/libgcc_s.so.1 (0x00002baa032ab000)
        libirc.so => /storage-apps/easybuild/software/intel-compilers/2021.2.0/compiler/2021.2.0/linux/compiler/lib/intel64_lin/libirc.so (0x00002baa0eaf3000)
        libc.so.6 => /lib64/libc.so.6 (0x00002baa0ed6b000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00002baa0f139000)
        libz.so.1 => /storage-apps/easybuild/software/zlib/1.2.11-GCCcore-10.3.0/lib/libz.so.1 (0x00002baa0f33d000)
        libhdf5.so.103 => /storage-apps/easybuild/software/HDF5/1.10.7-iompi-2021a/lib/libhdf5.so.103 (0x00002baa0f356000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00002baa0f856000)
        libsz.so.2 => /storage-apps/easybuild/software/Szip/2.1.1-GCCcore-10.3.0/lib/libsz.so.2 (0x00002baa0fa72000)
        libmpi_usempif08.so.40 => /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/lib/libmpi_usempif08.so.40 (0x00002baa0fa89000)
        libmpi_usempi_ignore_tkr.so.40 => /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/lib/libmpi_usempi_ignore_tkr.so.40 (0x00002baa0fac4000)
        libmpi_mpifh.so.40 => /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/lib/libmpi_mpifh.so.40 (0x00002baa0fad1000)
        librt.so.1 => /lib64/librt.so.1 (0x00002baa0fb3d000)
        /lib64/ld-linux-x86-64.so.2 (0x00002baa030aa000)
        libopen-rte.so.40 => /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/lib/libopen-rte.so.40 (0x00002baa0fd45000)
        libopen-orted-mpir.so => /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/lib/libopen-orted-mpir.so (0x00002baa032c4000)
        libopen-pal.so.40 => /storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.2.0/lib/libopen-pal.so.40 (0x00002baa0fe0e000)
        libutil.so.1 => /lib64/libutil.so.1 (0x00002baa0fed9000)
        libhwloc.so.15 => /storage-apps/easybuild/software/hwloc/2.4.1-GCCcore-10.3.0/lib/libhwloc.so.15 (0x00002baa100dc000)
        libpciaccess.so.0 => /storage-apps/easybuild/software/libpciaccess/0.16-GCCcore-10.3.0/lib/libpciaccess.so.0 (0x00002baa10137000)
        libxml2.so.2 => /storage-apps/easybuild/software/libxml2/2.9.10-GCCcore-10.3.0/lib/libxml2.so.2 (0x00002baa10142000)
        liblzma.so.5 => /storage-apps/easybuild/software/XZ/5.2.5-GCCcore-10.3.0/lib/liblzma.so.5 (0x00002baa102b2000)
        libevent_core-2.1.so.7 => /storage-apps/easybuild/software/libevent/2.1.12-GCCcore-10.3.0/lib/libevent_core-2.1.so.7 (0x00002baa102da000)
        libevent_pthreads-2.1.so.7 => /storage-apps/easybuild/software/libevent/2.1.12-GCCcore-10.3.0/lib/libevent_pthreads-2.1.so.7 (0x00002baa10311000)
        libintlc.so.5 => /storage-apps/easybuild/software/intel-compilers/2021.2.0/compiler/2021.2.0/linux/compiler/lib/intel64_lin/libintlc.so.5 (0x00002baa10315000)
        libifport.so.5 => /storage-apps/easybuild/software/intel-compilers/2021.2.0/compiler/2021.2.0/linux/compiler/lib/intel64_lin/libifport.so.5 (0x00002baa1058d000)
        libifcoremt.so.5 => /storage-apps/easybuild/software/intel-compilers/2021.2.0/compiler/2021.2.0/linux/compiler/lib/intel64_lin/libifcoremt.so.5 (0x00002baa107bb000)


