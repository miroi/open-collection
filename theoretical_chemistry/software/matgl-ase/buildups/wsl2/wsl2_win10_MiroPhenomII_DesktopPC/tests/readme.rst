Simple test
===========

https://github.com/materialyzeai/matgl#code

error: https://github.com/materialyzeai/matgl/issues/699

also  https://discuss.pytorch.org/t/userwarning-cuda-initialization-the-nvidia-driver-on-your-system-is-too-old-found-version-10010/141547/18?u=miroslav_ilias


(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win10_MiroPhenomII_DesktopPC/tests/.python formation_energy_CsCl.py

miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win10_MiroPhenomII_DesktopPC/tests/.python formation_energy_CsCl.py
Do you really want to delete everything in /home/miroi/.cache/matgl (y|n)? y
/home/miroi/software/venv/lib/python3.12/site-packages/torch/__config__.py:9: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11040). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at /pytorch/c10/cuda/CUDAFunctions.cpp:109.)
  return torch._C._show_config()
Floating point exception (core dumped)


(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win10_MiroPhenomII_DesktopPC/tests/.pip show torch
Name: torch
Version: 2.8.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3-Clause
Location: /home/miroi/software/venv/lib/python3.12/site-packages
Requires: filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvtx-cu12, setuptools, sympy, triton, typing-extensions
Required-by: chgnet, lightning, matgl, pytorch-lightning, torchdata, torchmetrics

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win10_MiroPhenomII_DesktopPC/tests/.nvidia-smi
Mon Dec 22 22:25:54 2025
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.57.01    Driver Version: 471.41       CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:01:00.0 N/A |                  N/A |
|ERR!    0C    P8    N/A /  N/A |    486MiB /  2048MiB |     N/A      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/matgl/buildups/wsl2/wsl2_win10_MiroPhenomII_DesktopPC/tests/.python
Python 3.12.3 (main, Nov  6 2025, 13:44:16) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch; torch.cuda.is_available()
/home/miroi/software/venv/lib/python3.12/site-packages/torch/cuda/__init__.py:182: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11040). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at /pytorch/c10/cuda/CUDAFunctions.cpp:109.)
  return torch._C._cuda_getDeviceCount() > 0
False
>>>
