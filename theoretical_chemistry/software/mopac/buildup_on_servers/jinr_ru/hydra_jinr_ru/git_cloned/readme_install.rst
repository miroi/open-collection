===================
MOPAC CMake install
===================

milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build2/.cmake -DCMAKE_Fortran_COMPILER=ifort -DCMAKE_C_COMPILER=icc  --install-prefix /lustre/home/user/m/milias/work/software/mopac/git_cloned/install ..
-- Build type is Release
-- The Fortran compiler identification is Intel 2021.4.0.20210910
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/ifort - skipped
-- The C compiler identification is Intel 2021.4.0.20210910
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/icc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Shared library and dynamic executables
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
-- Found BLAS: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libiomp5.so;-lpthread;-lm;-ldl
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libiomp5.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Found OpenMP_C: -qopenmp (found version "5.0")
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- Found Python3: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/bin/python3.10 (found version "3.10.13") found components: Interpreter NumPy Development.Module
-- OMP packaging: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/../../compiler/lib/intel64_lin/libiomp5.so -> /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libiomp5.so
-- Configuring done (96.3s)
-- Generating done (31.6s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/mopac/git_cloned/mopac/build2
milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build2/.

milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build2/.m -j4
.
.
[100%] Built target mopac
[100%] Built target mopac-param
[100%] Linking Fortran executable mopac-api-test
[100%] Built target mopac-api-test

install
~~~~~~~
milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build2/.make all install
[ 92%] Built target mopac-core
[ 92%] Built target mopac
[ 93%] Built target mopac-param
[ 99%] Built target mopac-makpol
[100%] Built target mopac-api-test
Install the project...
-- Install configuration: "Release"
-- Installing: /lustre/home/user/m/milias/work/software/mopac/git_cloned/install/include/mopac.h
-- Installing: /lustre/home/user/m/milias/work/software/mopac/git_cloned/install/bin/mopac
-- Set non-toolchain portion of runtime path of "/lustre/home/user/m/milias/work/software/mopac/git_cloned/install/bin/mopac" to "$ORIGIN/../lib"
-- Installing: /lustre/home/user/m/milias/work/software/mopac/git_cloned/install/bin/mopac-param
-- Set non-toolchain portion of runtime path of "/lustre/home/user/m/milias/work/software/mopac/git_cloned/install/bin/mopac-param" to "$ORIGIN/../lib"
-- Installing: /lustre/home/user/m/milias/work/software/mopac/git_cloned/install/bin/mopac-makpol
-- Set non-toolchain portion of runtime path of "/lustre/home/user/m/milias/work/software/mopac/git_cloned/install/bin/mopac-makpol" to "$ORIGIN/../lib"
-- Installing: /lustre/home/user/m/milias/work/software/mopac/git_cloned/install/lib64/libmopac.so.2
-- Set non-toolchain portion of runtime path of "/lustre/home/user/m/milias/work/software/mopac/git_cloned/install/lib64/libmopac.so.2" to "$ORIGIN/../lib"
-- Installing: /lustre/home/user/m/milias/work/software/mopac/git_cloned/install/lib64/libmopac.so
milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build2/.

milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build2/.export LD_LIBRARY_PATH=/lustre/home/user/m/milias/work/software/mopac/git_cloned/install/lib64:$LD_LIBRARY_PATH

milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build2/.ldd /lustre/home/user/m/milias/work/software/mopac/git_cloned/install/bin/mopac
        linux-vdso.so.1 =>  (0x00007ffd80bed000)
        libmopac.so.2 => /lustre/home/user/m/milias/work/software/mopac/git_cloned/install/lib64/libmopac.so.2 (0x00007f44e83dd000)
        libmkl_intel_lp64.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so.1 (0x00007f44e783e000)
        libmkl_intel_thread.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so.1 (0x00007f44e40ef000)
        libmkl_core.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so.1 (0x00007f44dfc81000)
        libiomp5.so => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libiomp5.so (0x00007f44df861000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f44df645000)
        libm.so.6 => /lib64/libm.so.6 (0x00007f44df343000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f44df13f000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f44ded71000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f44ecf5b000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f44deb5b000)
        libifport.so.5 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libifport.so.5 (0x00007f44de92d000)
        libifcoremt.so.5 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libifcoremt.so.5 (0x00007f44ecfd0000)
        libimf.so => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libimf.so (0x00007f44de29f000)
        libsvml.so => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libsvml.so (0x00007f44dc169000)
        libintlc.so.5 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libintlc.so.5 (0x00007f44dbef1000)
        librt.so.1 => /lib64/librt.so.1 (0x00007f44dbce9000)
milias@hydra.jinr.ru:~/work/software/mopac/git_cloned/mopac/build2/.

