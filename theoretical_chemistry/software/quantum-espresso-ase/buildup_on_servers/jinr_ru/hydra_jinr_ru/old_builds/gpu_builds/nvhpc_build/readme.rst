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

Making symbolic link in /lustre/home/user/m/milias/work/software/nvhpc/Linux_x86_64

generating environment modules for NV HPC SDK 25.3 ... done.
Installation complete.
HPC SDK successfully installed into /lustre/home/user/m/milias/work/software/nvhpc

If you use the Environment Modules package, that is, the module load
command, the NVIDIA HPC SDK includes a script to set up the
appropriate module files.

% module load /lustre/home/user/m/milias/work/software/nvhpc/modulefiles/nvhpc/25.3
% module load nvhpc/25.3

Alternatively, the shell environment may be initialized to use the HPC SDK.

In csh, use these commands:

% set path = (/lustre/home/user/m/milias/work/software/nvhpc/Linux_x86_64/25.3/compilers/bin $path)
% setenv MANPATH /lustre/home/user/m/milias/work/software/nvhpc/Linux_x86_64/25.3/compilers/man:"$MANPATH"

To use MPI, also set:

% set path = (/lustre/home/user/m/milias/work/software/nvhpc/Linux_x86_64/25.3/comm_libs/mpi/bin $path)

In bash, sh, or ksh, use these commands:

$ export PATH=/lustre/home/user/m/milias/work/software/nvhpc/Linux_x86_64/25.3/compilers/bin:$PATH
$ export MANPATH=/lustre/home/user/m/milias/work/software/nvhpc/Linux_x86_64/25.3/compilers/man:$MANPATH

To use MPI, also set:

$ export PATH=/lustre/home/user/m/milias/work/software/nvhpc/Linux_x86_64/25.3/comm_libs/mpi/bin:$PATH

Please check https://developer.nvidia.com for documentation,
use of NVIDIA HPC SDK software, and other questions.

