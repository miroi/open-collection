==============================
GPU-QE on Govorun JINR cluster
==============================

wget https://github.com/QEF/q-e/archive/refs/tags/qe-6.8.zip

see https://gitlab.com/QEF/q-e/-/blob/develop/README_GPU.md

NVIDIA HPC SDK
--------------
see https://developer.nvidia.com/nvidia-hpc-sdk-downloads
wget https://developer.download.nvidia.com/hpc-sdk/21.7/nvhpc_2021_217_Linux_x86_64_cuda_11.4.tar.gz

milias@hydra.jinr.ru:~/work/software/NVIDIA_HPC_SDK/nvhpc_2021_217_Linux_x86_64_cuda_11.4/../install

Installation complete.
HPC SDK successfully installed into /zfs/hybrilit.jinr.ru/user/m/milias/work/software/NVIDIA_HPC_SDK

If you use the Environment Modules package, that is, the module load
command, the NVIDIA HPC SDK includes a script to set up the
appropriate module files.

% module load /zfs/hybrilit.jinr.ru/user/m/milias/work/software/NVIDIA_HPC_SDK/modulefiles/nvhpc/21.7
% module load nvhpc/21.7

Alternatively, the shell environment may be initialized to use the HPC SDK.

In csh, use these commands:

% setenv MANPATH "$MANPATH":/zfs/hybrilit.jinr.ru/user/m/milias/work/software/NVIDIA_HPC_SDK/Linux_x86_64/21.7/compilers/man
% set path = (/zfs/hybrilit.jinr.ru/user/m/milias/work/software/NVIDIA_HPC_SDK/Linux_x86_64/21.7/compilers/bin $path)

In bash, sh, or ksh, use these commands:

$ MANPATH=$MANPATH:/zfs/hybrilit.jinr.ru/user/m/milias/work/software/NVIDIA_HPC_SDK/Linux_x86_64/21.7/compilers/man; export MANPATH
$ PATH=/zfs/hybrilit.jinr.ru/user/m/milias/work/software/NVIDIA_HPC_SDK/Linux_x86_64/21.7/compilers/bin:$PATH; export PATH

Once the 64-bit compilers are available, you can make the OpenMPI
commands and man pages accessible using these commands.

% set path = (/zfs/hybrilit.jinr.ru/user/m/milias/work/software/NVIDIA_HPC_SDK/Linux_x86_64/21.7/comm_libs/mpi/bin $path)
% setenv MANPATH "$MANPATH":/zfs/hybrilit.jinr.ru/user/m/milias/work/software/NVIDIA_HPC_SDK/Linux_x86_64/21.7/comm_libs/mpi/man

And the equivalent in bash, sh, and ksh:

$ export PATH=/zfs/hybrilit.jinr.ru/user/m/milias/work/software/NVIDIA_HPC_SDK/Linux_x86_64/21.7/comm_libs/mpi/bin:$PATH
$ export MANPATH=$MANPATH:/zfs/hybrilit.jinr.ru/user/m/milias/work/software/NVIDIA_HPC_SDK/Linux_x86_64/21.7/comm_libs/mpi/man

Please check https://developer.nvidia.com for documentation,
use of NVIDIA HPC SDK software, and other questions.



