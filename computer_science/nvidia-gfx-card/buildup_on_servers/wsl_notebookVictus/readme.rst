============================
NVidia on WSL-notebookVictus
============================

sudo apt install nvidia-cuda-tool


miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/nequip-ase/buildup_on_servers/wsl_notebookVictus/.nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0


python3 torch_cuda_check.py
hello, torch.cuda.is_available ? True
