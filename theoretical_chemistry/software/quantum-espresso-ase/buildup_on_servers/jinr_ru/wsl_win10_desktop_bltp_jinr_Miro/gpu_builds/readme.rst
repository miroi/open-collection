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

milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel/build_gpu/.ldd bin/pw.x
        linux-vdso.so.1 (0x00007fff2a4d1000)
        libmkl_intel_lp64.so => /lib/x86_64-linux-gnu/libmkl_intel_lp64.so (0x00007474d8600000)
        libmkl_intel_thread.so => /lib/x86_64-linux-gnu/libmkl_intel_thread.so (0x00007474d4c00000)
        libmkl_core.so => /lib/x86_64-linux-gnu/libmkl_core.so (0x00007474d0400000)
        libomp.so.5 => /lib/x86_64-linux-gnu/libomp.so.5 (0x00007474d4ae0000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007474d8519000)
        libnvhpcwrapcufft.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libnvhpcwrapcufft.so (0x00007474d0000000)
        libcufft.so.11 => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/math_libs/12.9/lib64/libcufft.so.11 (0x00007474be200000)
        libcudaforwraprand.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libcudaforwraprand.so (0x00007474bde00000)
        libcurand.so.10 => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/math_libs/12.9/lib64/libcurand.so.10 (0x00007474b3600000)
        libcusolver.so.11 => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/math_libs/12.9/lib64/libcusolver.so.11 (0x00007474a1400000)
        libnvJitLink.so.12 => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/cuda/12.9/lib64/libnvJitLink.so.12 (0x000074749b600000)
        libcublas.so.12 => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/math_libs/12.9/lib64/libcublas.so.12 (0x0000747494e00000)
        libcublasLt.so.12 => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/math_libs/12.9/lib64/libcublasLt.so.12 (0x0000747462a00000)
        libcudaforwrapblas.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libcudaforwrapblas.so (0x0000747462600000)
        libcudaforwrapblas117.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libcudaforwrapblas117.so (0x0000747462200000)
        libcudart.so.12 => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/cuda/12.9/lib64/libcudart.so.12 (0x0000747461e00000)
        libcudafor_128.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libcudafor_128.so (0x000074745f000000)
        libcudafor.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libcudafor.so (0x000074745ec00000)
        libacchost.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libacchost.so (0x000074745e800000)
        libaccdevaux.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libaccdevaux.so (0x000074745e400000)
        libaccdevice.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libaccdevice.so (0x000074745e000000)
        libcudadevice.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libcudadevice.so (0x000074745dc00000)
        libcudafor2.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libcudafor2.so (0x000074745d800000)
        libnvf.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libnvf.so (0x000074745d000000)
        libnvomp.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libnvomp.so (0x000074745be00000)
        libnvhpcatm.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libnvhpcatm.so (0x000074745ba00000)
        libnvcpumath.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libnvcpumath.so (0x000074745b400000)
        libnvc.so => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/lib/libnvc.so (0x000074745b000000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x000074745ac00000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007474d938b000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007474d9386000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007474d9381000)
        /lib64/ld-linux-x86-64.so.2 (0x00007474d93c3000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007474d937c000)
        libcusparse.so.12 => /opt/nvidia/hpc_sdk/Linux_x86_64/25.7/math_libs/12.9/lib64/libcusparse.so.12 (0x000074743da00000)
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel/build_gpu/.ctest -j4
.
.
.
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel/build_gpu/test-suite/.grep 'GPU acceleration is ACTIVE'  */test.out*
cp_h2o/test.out.010121.inp=h2o-mt-blyp-1.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
cp_h2o/test.out.010121.inp=h2o-mt-blyp-2.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
cp_h2o/test.out.010121.inp=h2o-mt-blyp-3.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
cp_h2o/test.out.010121.inp=h2o-mt-blyp-4.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
cp_h2o/test.out.010121.inp=h2o-mt-blyp-5.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
cp_o2/test.out.010121.inp=o2-us-para-pbe-1.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
cp_o2/test.out.010121.inp=o2-us-para-pbe-2.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
cp_o2/test.out.010121.inp=o2-us-para-pbe-3.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
cp_sio2/test.out.010121.inp=sio2-us-lda-1.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
pw_berry/test.out.010121.inp=berry.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
pw_electric/test.out.010121.inp=electric.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
pw_metaGGA/test.out.010121.inp=metaGGA.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
pw_metal/test.out.010121.inp=metal-tetrahedra.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
pw_noncolin/test.out.010121.inp=noncolin.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
pw_scf/test.out.010121.inp=scf-disk_io.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank
pw_scf/test.out.010121.inp=scf.in:     GPU acceleration is ACTIVE.  1 visible GPUs per MPI rank

