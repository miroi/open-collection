PyTorch
=======

pip install torch==1.11.*
pip show torch

https://en.wikipedia.org/wiki/PyTorch


miroi@MIRO:~/work/projects/open-collection/computer_science/pytorch/buildup_on_servers/wsl_notebookVictus/.python3 test.py
/home/miroi/.local/lib/python3.10/site-packages/torch/cuda/__init__.py:145: UserWarning:
NVIDIA GeForce RTX 3050 Laptop GPU with CUDA capability sm_86 is not compatible with the current PyTorch installation.
The current PyTorch install supports CUDA capabilities sm_37 sm_50 sm_60 sm_70.
If you want to use the NVIDIA GeForce RTX 3050 Laptop GPU GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/

  warnings.warn(incompatible_device_warn.format(device_name, capability, " ".join(arch_list), device_name))

see also https://github.com/mir-group/nequip/discussions/311#discussioncomment-11277247
