===========
NVHPC build
===========

from https://developer.nvidia.com/hpc-sdk-downloads

NVIDIA HPC SDK Current Downloads

Linux 86_64 (tar file)

wget https://developer.download.nvidia.com/hpc-sdk/25.7/nvhpc_2025_257_Linux_x86_64_cuda_12.9.tar.gz
tar xpzf nvhpc_2025_257_Linux_x86_64_cuda_12.9.tar.gz
nvhpc_2025_257_Linux_x86_64_cuda_12.9/install


interactive installation
------------------------

milias@vm02.hydra.local:~/work/software/nvhpc/nvhpc_2025_253_Linux_x86_64_cuda_12.8/../install

Welcome to the NVIDIA HPC SDK Linux installer!

You are installing NVIDIA HPC SDK 2025 version 25.3 for Linux_x86_64.
Please note that all Trademarks and Marks are the properties
of their respective owners.

Press enter to continue...


A single system installation is appropriate for a single system or a
homogeneous cluster.  A network installation should be selected for a
heterogeneous cluster.  For either a single system or network installation,
the HPC SDK configuration (localrc) is created at install time and saved
in the installation directory.

An auto installation is appropriate for any scenario.  The HPC SDK
configuration (localrc) is created at first use and stored in each user's
home directory.

1  Single system install
2  Network install
3  Auto install

Please choose install option: 
3

Please specify the directory path under which the software will be installed.
The default directory is /opt/nvidia/hpc_sdk, but you may install anywhere
you wish, assuming you have permission to do so.

Installation directory? [/opt/nvidia/hpc_sdk] 
/lustre/home/user/m/milias/work/software/nvhpc

Installing NVIDIA HPC SDK version 25.3 into /lustre/home/user/m/milias/work/software/nvhpc


