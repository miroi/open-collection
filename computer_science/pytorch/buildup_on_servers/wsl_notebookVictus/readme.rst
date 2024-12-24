=======
PyTorch
=======

https://en.wikipedia.org/wiki/PyTorch

pip install torch==1.11.*
pip show torch

miroi@MIRO:~/work/projects/open-collection/computer_science/pytorch/buildup_on_servers/wsl_notebookVictus/.python3 test.py
/home/miroi/.local/lib/python3.10/site-packages/torch/cuda/__init__.py:145: UserWarning:
NVIDIA GeForce RTX 3050 Laptop GPU with CUDA capability sm_86 is not compatible with the current PyTorch installation.
The current PyTorch install supports CUDA capabilities sm_37 sm_50 sm_60 sm_70.
If you want to use the NVIDIA GeForce RTX 3050 Laptop GPU GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/

  warnings.warn(incompatible_device_warn.format(device_name, capability, " ".join(arch_list), device_name))

see also https://github.com/mir-group/nequip/discussions/311#discussioncomment-11277247
https://github.com/pytorch/pytorch/issues/31285#issuecomment-2480545010


miroi@MIRO:~/work/projects/open-collection/computer_science/pytorch/buildup_on_servers/wsl_notebookVictus/.pip install torch --force-reinstall
.
.
.
Successfully installed MarkupSafe-3.0.2 filelock-3.16.1 fsspec-2024.10.0 jinja2-3.1.4 mpmath-1.3.0 networkx-3.4.2 nvidia-cublas-cu12-12.4.5.8 nvidia-cuda-cupti-cu12-12.4.127 nvidia-cuda-nvrtc-cu12-12.4.127 nvidia-cuda-runtime-cu12-12.4.127 nvidia-cudnn-cu12-9.1.0.70 nvidia-cufft-cu12-11.2.1.3 nvidia-curand-cu12-10.3.5.147 nvidia-cusolver-cu12-11.6.1.9 nvidia-cusparse-cu12-12.3.1.170 nvidia-nccl-cu12-2.21.5 nvidia-nvjitlink-cu12-12.4.127 nvidia-nvtx-cu12-12.4.127 sympy-1.13.1 torch-2.5.1 triton-3.1.0 typing-extensions-4.12.2

quick test
~~~~~~~~~~
miroi@MIRO:~/work/projects/open-collection/computer_science/pytorch/buildup_on_servers/wsl_notebookVictus/.python3 torch_cuda_test.py
torch.cuda.get_device_name() ? NVIDIA GeForce RTX 3050 Laptop GPU
torch.cuda.is_available ? True
 torch.version.cuda ? 12.4
torch.tensor([1.0, 2.0]) ?  tensor([1., 2.])
torch.tensor([1.0, 2.0]).cuda() ? tensor([1., 2.], device='cuda:0')
 y=x*x, y.shape ?  torch.Size([1024, 1024])
 y=x*x, y.device ?  cuda:0



