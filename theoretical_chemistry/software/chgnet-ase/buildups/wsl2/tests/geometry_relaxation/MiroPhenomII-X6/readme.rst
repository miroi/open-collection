===========
CHGNet test
===========

MiroPhenomII-X6 old Desktop PC
------------------------------
(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/chgnet-ase/buildups/wsl2/tests/geometry_relaxation/.python struct_optim.py
CHGNet v0.3.0 initialized with 412,525 parameters
/home/miroi/software/venv/lib/python3.12/site-packages/torch/cuda/__init__.py:182: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11040). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at /pytorch/c10/cuda/CUDAFunctions.cpp:119.)
  return torch._C._cuda_getDeviceCount() > 0
CHGNet will run on cpu
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
Floating point exception (core dumped)


see https://github.com/CederGroupHub/chgnet/issues/248

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/chgnet-ase/buildups/wsl2/tests/geometry_relaxation/MiroPhenomII-X6/.python struct_optim_cpu.py
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
Floating point exception (core dumped)

verbose run
~~~~~~~~~~~
(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/chgnet-ase/buildups/wsl2/tests/geometry_relaxation/MiroPhenomII-X6/.python -vvv struct_optim_cpu.py  >  struct_optim_cpu.py_logfile 2>&1
Floating point exception (core dumped)


(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/chgnet-ase/buildups/wsl2/tests/geometry_relaxation/MiroPhenomII-X6/.pip show chgnet torch
Name: chgnet
Version: 0.4.2
Summary: Pretrained Universal Neural Network Potential for Charge-informed Atomistic Modeling
Home-page:
Author:
Author-email: Bowen Deng <bowendeng@berkeley.edu>
License: Modified BSD
Location: /home/miroi/software/venv/lib/python3.12/site-packages
Requires: ase, cython, numpy, nvidia-ml-py3, pymatgen, torch, typing-extensions
Required-by:
---
Name: torch
Version: 2.8.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3-Clause
Location: /home/miroi/software/venv/lib/python3.12/site-packages
Requires: filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvtx-cu12, setuptools, sympy, triton, typing-extensions
Required-by: chgnet, lightning, matgl, pytorch-lightning, torchdata, torchmetrics, torchvision

new debug run
-------------

https://github.com/CederGroupHub/chgnet/issues/248#issuecomment-3712318947

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/chgnet-ase/buildups/wsl2/tests/geometry_relaxation/MiroPhenomII-X6/.python   struct_optim_cpu_debug.py
CHGNet v0.3.0 initialized with 412,525 parameters
/home/miroi/software/venv/lib/python3.12/site-packages/torch/cuda/__init__.py:182: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11040). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at /pytorch/c10/cuda/CUDAFunctions.cpp:109.)
  return torch._C._cuda_getDeviceCount() > 0
CHGNet will run on cpu
CHGNet v0.3.0 initialized with 412,525 parameters
CHGNet will run on cpu
Floating point exception (core dumped)


