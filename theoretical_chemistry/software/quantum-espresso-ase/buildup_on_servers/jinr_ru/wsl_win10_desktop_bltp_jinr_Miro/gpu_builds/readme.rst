====================
QE GPU build on WSL2
====================

Linux (x86_64) runfile
----------------------
milias@DESKTOP-7OTLCGO:~/work/software/nvhpc/.wget https://developer.download.nvidia.com/hpc-sdk/25.7/nvhpc_2025_257_Linux_x86_64_cuda_12.9.tar.gz
milias@DESKTOP-7OTLCGO:~/work/software/nvhpc/.tar xvzf nvhpc_2025_257_Linux_x86_64_cuda_12.9.tar.gz


Linux (x86_64) apt
------------------
also see

https://developer.nvidia.com/hpc-sdk-downloads

$ curl https://developer.download.nvidia.com/hpc-sdk/ubuntu/DEB-GPG-KEY-NVIDIA-HPC-SDK | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-hpcsdk-archive-keyring.gpg
$ echo 'deb [signed-by=/usr/share/keyrings/nvidia-hpcsdk-archive-keyring.gpg] https://developer.download.nvidia.com/hpc-sdk/ubuntu/amd64 /' | sudo tee /etc/apt/sources.list.d/nvhpc.list
$ sudo apt-get update -y
$ sudo apt-get install -y nvhpc-25-7

milias@DESKTOP-7OTLCGO:~/work/software/nvhpc/./opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin/nvfortran  -V

nvfortran 25.7-0 64-bit target on x86-64 Linux -tp alderlake
NVIDIA Compilers and Tools
Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.

milias@DESKTOP-7OTLCGO:~/work/software/nvhpc/./opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin/pgfortran -V

pgfortran (aka nvfortran) 25.7-0 64-bit target on x86-64 Linux -tp alderlake
PGI Compilers and Tools
Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.

milias@DESKTOP-7OTLCGO:~/work/software/nvhpc/./opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin/nvcc  -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Tue_May_27_02:21:03_PDT_2025
Cuda compilation tools, release 12.9, V12.9.86
Build cuda_12.9.r12.9/compiler.36037853_0

add vars
~~~~~~~~~
export PATH=/opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin:$PATH
export MANPATH=/opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/man:$MANPATH
export PATH=/opt/nvidia/hpc_sdk/Linux_x86_64/25.7/comm_libs/mpi/bin:$PATH

configure and compile
~~~~~~~~~~~~~~~~~~~~~

milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel/build_gpu/.export PATH=/opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin:$PATH
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel/build_gpu/.export MANPATH=/opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/man:$MANPATH

milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel/build_gpu/.cmake -DCMAKE_C_COMPILER=nvc -DCMAKE_Fortran_COMPILER=pgfortran -DQE_ENABLE_MPI=OFF -DQE_ENABLE_OPENMP=ON -DQE_ENABLE_CUDA=ON ..

milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel/build_gpu/.cmake -DCMAKE_C_COMPILER=nvc -DCMAKE_Fortran_COMPILER=pgfortran -DQE_ENABLE_MPI=OFF -DQE_ENABLE_OPENMP=ON -DQE_ENABLE_CUDA=ON ..
-- The Fortran compiler identification is NVHPC 25.7.0
-- The C compiler identification is NVHPC 25.7.0
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin/pgfortran - skipped
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin/nvc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Setting build type to 'Release' as none was specified
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /usr/bin/cpp
-- Performing Test Fortran_ISYSTEM_SUPPORTED
-- Performing Test Fortran_ISYSTEM_SUPPORTED - Success
-- Found OpenMP_Fortran: -mp
-- Found OpenMP: TRUE  found components: Fortran
-- Found OpenACC_C: -acc
-- Found OpenACC_Fortran: -acc
   nvfortran CUDA related compile and link options : -cuda
-- Performing Test NVFORTRAN_CUDA_VALID
-- Performing Test NVFORTRAN_CUDA_VALID - Success
-- Found Git: /usr/bin/git (found suitable version "2.34.1", minimum required is "2.13")
-- Source files are cloned from a git repository.
   sed supports -E
   Git branch: dftd4
   Git commit hash: 234d1ec8279940b25d9bc7437067330cd0755cf9
-- Trying to find LAPACK from Intel MKL
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /usr/lib/x86_64-linux-gnu/libmkl_intel_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_intel_thread.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;/usr/lib/x86_64-linux-gnu/libiomp5.so;-lm;-ldl
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /usr/lib/x86_64-linux-gnu/libmkl_intel_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_intel_thread.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;/usr/lib/x86_64-linux-gnu/libiomp5.so;-lm;-ldl;-lm;-ldl
-- Looking for Fortran zhpev
-- Looking for Fortran zhpev - found
Project C_FLAGS:  -fast -O3 -DNDEBUG
Project Fortran_FLAGS:  -Mcache_align -Mlarge_arrays -Mbackslash -fast
Project INCLUDE_DIRECTORIES: /home/milias/work/software/qe/q-e-devel/include
Project EXE_LINKER_FLAGS:
Project SHARED_LINKER_FLAGS:
-- Installing Wannier90 via submodule
-- Installing MBD via submodule
-- Found Git: /usr/bin/git (found version "2.34.1")
-- Setting version tag to 0.13.0-2-g89a3cc1 from Git
-- Installing DeviceXlib via submodule
-- Installing DFTD4 via submodule
-- mctc-lib: Find installed package
-- Could NOT find mctc-lib (missing: mctc-lib_DIR)
-- Retrieving mctc-lib revision v0.4.1 from https://github.com/grimme-lab/mctc-lib
-- Found OpenMP_C: -mp
-- Found OpenMP: TRUE
-- mstore: Find installed package
-- Could NOT find mstore (missing: mstore_DIR)
-- Retrieving mstore revision v0.3.0 from https://github.com/grimme-lab/mstore
-- multicharge: Find installed package
-- Could NOT find multicharge (missing: multicharge_DIR)
-- Retrieving multicharge revision v0.4.0 from https://github.com/grimme-lab/multicharge
-- Found VendorFFTW: /usr/lib/x86_64-linux-gnu/libmkl_intel_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_intel_thread.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;/usr/lib/x86_64-linux-gnu/libiomp5.so;-lm;-ldl;/usr/lib/x86_64-linux-gnu/libmkl_intel_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_intel_thread.so;/usr/lib/x86_64-linux-gnu/libmkl_core.so;/usr/lib/x86_64-linux-gnu/libiomp5.so;-lm;-ldl;-lm;-ldl
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Looking for cusolverDnZhegvdx
-- Looking for cusolverDnZhegvdx - found
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/qe/q-e-devel/build_gpu
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel/build_gpu/.m -j 8


