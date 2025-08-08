======================
Install NVIDIA HPC SDK
=======================

https://developer.nvidia.com/hpc-sdk-downloads

Linux x86_64 Ubuntu(apt)
~~~~~~~~~~~~~~~~~~~~~~~~~

curl https://developer.download.nvidia.com/hpc-sdk/ubuntu/DEB-GPG-KEY-NVIDIA-HPC-SDK | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-hpcsdk-archive-keyring.gpg


echo 'deb [signed-by=/usr/share/keyrings/nvidia-hpcsdk-archive-keyring.gpg] https://developer.download.nvidia.com/hpc-sdk/ubuntu/amd64 /' | sudo tee /etc/apt/sources.list.d/nvhpc.list

sudo apt-get update -y 

sudo apt-get install -y nvhpc-25-7 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  avogadro-utils cclib libavogadro-data libavogadro2-1 libevdev2 libglew2.2 libgudev-1.0-0 libinput-bin libinput10 libmd4c0 libmtdev1 libqt5concurrent5 libqt5gui5 libqt5svg5 libqt5widgets5
  libsymspg1 libwacom-bin libwacom-common libwacom9 libxcb-xinput0 molequeue python3-cclib python3-numpy qt5-gtk-platformtheme
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  nvhpc-25-7
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 5576 MB of archives.
After this operation, 18.7 GB of additional disk space will be used.
Get:1 https://developer.download.nvidia.com/hpc-sdk/ubuntu/amd64  nvhpc-25-7 25.7-0 [5576 MB]
Fetched 5576 MB in 9min 40s (9613 kB/s)
Selecting previously unselected package nvhpc-25-7.
(Reading database ... 101950 files and directories currently installed.)
Preparing to unpack .../nvhpc-25-7_25.7-0_amd64.deb ...
Unpacking nvhpc-25-7 (25.7-0) ...
Setting up nvhpc-25-7 (25.7-0) ...

check the installation
~~~~~~~~~~~~~~~~~~~~~~~
/opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin/nvcc --version
25.7/compilers/bin/nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Tue_May_27_02:21:03_PDT_2025
Cuda compilation tools, release 12.9, V12.9.86
Build cuda_12.9.r12.9/compiler.36037853_0

/opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin/nvfortran  --version

nvfortran 25.7-0 64-bit target on x86-64 Linux -tp alderlake
NVIDIA Compilers and Tools
Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.


CUDA-Fortran
~~~~~~~~~~~~
ls /opt/nvidia/hpc_sdk/Linux_x86_
64/25.7/examples/
AutoPar/  CUDA-Fortran/  CUDA-Libraries/  F2003/  MPI/  NVLAmath/  OpenACC/  OpenMP/  README  stdpar/

small example
~~~~~~~~~~~~~~
./opt/nvidia/hpc_sdk/Linux_x86_64/25.7/compilers/bin/nvfortran  deviceQuery.cuf
a.out

One CUDA device found

Device Number: 0
  Device Name: NVIDIA GeForce GTX 1650
  Compute Capability: 7.5
  Number of Multiprocessors: 14
  Single- to Double-Precision Perf Ratio: 32
  Max Threads per Multiprocessor: 1024
  Supports Cooperative Kernels: Yes

  Global Memory (GB):     4.000

  Execution Configuration Limits
    Max Grid Dims: 2147483647 x 65535 x 65535
    Max Block Dims: 1024 x 1024 x 64
    Max Threads per Block: 1024

  Managed Memory
    Can Allocate Managed Memory: Yes
    Device/CPU Concurrent Access to Managed Memory: No
