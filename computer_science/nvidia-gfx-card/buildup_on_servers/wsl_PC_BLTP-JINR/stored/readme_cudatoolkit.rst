CUDA Toolkit 13.0 Downloads
============================

see  https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0

wget https://developer.download.nvidia.com/compute/cuda/13.0.0/local_installers/cuda_13.0.0_580.65.06_linux.run
sudo sh cuda_13.0.0_580.65.06_linux.run

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/computer_science/nvidia-gfx-card/buildup_on_servers/wsl_PC_BLTP-JINR/.sudo sh cuda_13.0.0_580.65.06_linux.run
[sudo] password for milias:
===========
= Summary =
===========

Driver:   Not Selected
Toolkit:  Installed in /usr/local/cuda-13.0/

Please make sure that
 -   PATH includes /usr/local/cuda-13.0/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-13.0/lib64, or, add /usr/local/cuda-13.0/lib64 to /etc/ld.so.conf and run ldconfig as root

To uninstall the CUDA Toolkit, run cuda-uninstaller in /usr/local/cuda-13.0/bin
***WARNING: Incomplete installation! This installation did not install the CUDA Driver. A driver of version at least 580.00 is required for CUDA 13.0 functionality to work.
To install the driver using this installer, run the following command, replacing <CudaInstaller> with the name of this run file:
    sudo <CudaInstaller>.run --silent --driver

Logfile is /var/log/cuda-installer.log

checks
~~~~~~~
/usr/local/cuda-13.0/bin/nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Wed_Jul_16_07:30:01_PM_PDT_2025
Cuda compilation tools, release 13.0, V13.0.48
Build cuda_13.0.r13.0/compiler.36260728_0

uninstall
~~~~~~~~~
sudo  /usr/local/cuda-13.0/bin/cuda-uninstaller

WE DO NOT NEED CUDA TOOLKIT, WE NEED NVIDIA HPC SDK !!!
