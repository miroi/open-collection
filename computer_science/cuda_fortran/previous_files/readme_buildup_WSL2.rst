======================
 CUDA Fortran on WSL2
======================

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


add environvars
~~~~~~~~~~~~~~~~
export PATH=/opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin:$PATH
export MANPATH=/opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/man:$MANPATH
export PATH=/opt/nvidia/hpc_sdk/Linux_x86_64/25.7/comm_libs/mpi/bin:$PATH

CUDA-Fortran-Book
=================

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/computer_science/cuda_fortran/CUDA-Fortran-Book/.export FC=nvfortran

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/computer_science/cuda_fortran/CUDA-Fortran-Book/.make all > ../make.logfile 2>&1

1 Test Failed


