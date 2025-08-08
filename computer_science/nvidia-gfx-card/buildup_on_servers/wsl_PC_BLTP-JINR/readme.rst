================
NVidia on WSL-PC
================

install on WSL2-Ubuntu 22.04
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sudo apt-get update
sudo apt-get upgrade

sudo apt install nvidia-cuda-tool

torch-cuda
~~~~~~~~~~
python torch_cuda_check.py >  torch_cuda_check.py_logfile

nvidia-smi
~~~~~~~~~~
nvidia-smi > nvidia-smi.log

nvcc, nvcc example
~~~~~~~~~~~~~~~~~~~
nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0

nvcc cuda_hello_world.cu
a.out
Hello World from printf !
