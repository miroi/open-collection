===============
MACE on Govorun
===============

Modules and Python Virtual Environment
--------------------------------------
module add Python
python -V
Python 3.12.13

(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.python3 -m venv mace_volta_venv

(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.source mace_volta_venv/bin/activate
((mace_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.

one-command activate
~~~~~~~~~~~~~~~~~~~~
source /lustre/projects/m/milias/work/software/mace_volta_venv/bin/activate

pip install
-----------
((mace_volta_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip install torch --index-url https://download.pytorch.org/whl/cu126
Successfully installed MarkupSafe-3.0.3 cuda-bindings-12.9.7 cuda-pathfinder-1.6.0 cuda-toolkit-12.6.3 filelock-4.2.4 fsspec-2026.9.0 jinja2-3.1.6 mpmath-1.3.0 networkx-3.7 nvidia-cublas-cu12-12.6.4.1 nvidia-cuda-cupti-cu12-12.6.80 nvidia-cuda-nvrtc-cu12-12.6.85 nvidia-cuda-runtime-cu12-12.6.77 nvidia-cudnn-cu12-9.10.2.21 nvidia-cufft-cu12-11.3.0.4 nvidia-cufile-cu12-1.11.1.6 nvidia-curand-cu12-10.3.7.77 nvidia-cusolver-cu12-11.7.1.2 nvidia-cusparse-cu12-12.5.4.2 nvidia-cusparselt-cu12-0.7.1 nvidia-nccl-cu12-2.29.3 nvidia-nvjitlink-cu12-12.9.86 nvidia-nvshmem-cu12-3.4.5 nvidia-nvtx-cu12-12.6.77 setuptools-78.1.0 sympy-1.14.0 torch-2.14.1+cu126 triton-3.8.0 typing-extensions-4.16.0

((mace_volta_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip install mace-torch ase
Successfully installed GitPython-3.2.1 ase-3.29.0 configargparse-1.10.2 contourpy-1.4.0 cycler-0.12.1 e3nn-0.4.4 fonttools-4.68.0 gitdb-4.0.12 h5py-3.16.0 kiwisolver-1.5.1 lightning-utilities-0.15.3 lmdb-3.0.0 mace-torch-0.3.17 matplotlib-3.11.2 matscipy-1.3.1 numpy-2.5.5 opt-einsum-fx-0.1.4 opt_einsum-3.4.0 orjson-3.13.0 packaging-26.4 pandas-3.1.1 pillow-13.0.0 prettytable-3.19.0 pyYAML-6.0.4 pyparsing-3.3.3 python-dateutil-4.0.0 python-hostlist-2.3.0 scipy-1.18.1 smmap-5.0.3 torch-ema-0.3 torchmetrics-1.9.0 tqdm-4.70.1 tzdata-2026.6 wcwidth-0.9.5


((mace_volta_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip show ase mace-torch
Name: ase
Version: 3.29.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /lustre/projects/m/milias/work/software/mace_volta_venv/lib/python3.12/site-packages
Requires: matplotlib, numpy, scipy, typing_extensions
Required-by: mace-torch, matscipy
---
Name: mace-torch
Version: 0.3.17
Summary:
Home-page: https://github.com/ACEsuit/mace
Author:
Author-email:
License:
Location: /lustre/projects/m/milias/work/software/mace_volta_venv/lib/python3.12/site-packages
Requires: ase, configargparse, e3nn, GitPython, h5py, lmdb, matplotlib, matscipy, numpy, opt_einsum, orjson, pandas, prettytable, python-hostlist, pyYAML, torch, torch-ema, torchmetrics, tqdm
Required-by:

