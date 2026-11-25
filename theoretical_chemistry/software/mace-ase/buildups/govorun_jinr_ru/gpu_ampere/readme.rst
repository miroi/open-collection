===============
MACE on Govorun
===============

Modules and Python Virtual Environment
--------------------------------------
module add Python
python -V
Python 3.12.13

(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.python3 -m venv mace_ampere_venv

(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.source mace_ampere_venv/bin/activate
((mace_ampere_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.

one-command activate
~~~~~~~~~~~~~~~~~~~~
source /lustre/projects/m/milias/work/software/mace_ampere_venv/bin/activate

pip install
-----------
((mace_ampere_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip install torch
.
.
Successfully installed MarkupSafe-3.0.4 cuda-bindings-13.5.0 cuda-pathfinder-1.9.1 cuda-toolkit-13.2.2 filelock-4.3.1 fsspec-2026.9.0 jinja2-3.1.6 mpmath-1.3.0 networkx-3.7 nvidia-cublas-13.4.1.3 nvidia-cuda-cccl-13.3.5.0.6 nvidia-cuda-cupti-13.2.86 nvidia-cuda-nvrtc-13.2.86 nvidia-cuda-runtime-13.2.86 nvidia-cudnn-cu13-9.26.0.51 nvidia-cufft-12.2.0.57 nvidia-cufile-1.17.1.22 nvidia-cusolver-12.2.0.11 nvidia-cusparse-12.7.10.12 nvidia-cusparselt-cu13-0.8.1 nvidia-nccl-cu13-2.30.7 nvidia-nvjitlink-13.5.37 nvidia-nvshmem-cu13-3.7.2 nvidia-nvtx-13.2.86 setuptools-84.2.1 sympy-1.14.0 torch-2.15.0 triton-3.9.0 typing-extensions-4.16.0

((mace_volta_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip install mace-torch ase
.
.
Installing collected packages: python-hostlist, wcwidth, tzdata, tqdm, smmap, pyYAML, pyparsing, pillow, packaging, orjson, opt_einsum, numpy, lmdb, kiwisolver, fonttools, cycler, configargparse, scipy, python-dateutil, prettytable, lightning-utilities, h5py, gitdb, contourpy, pandas, matplotlib, GitPython, ase, torchmetrics, torch-ema, opt-einsum-fx, matscipy, e3nn, mace-torch
Successfully installed GitPython-3.2.1 ase-3.29.0 configargparse-1.10.2 contourpy-1.4.0 cycler-0.12.1 e3nn-0.4.4 fonttools-4.68.0 gitdb-4.0.12 h5py-3.16.0 kiwisolver-1.5.1 lightning-utilities-0.15.3 lmdb-3.0.0 mace-torch-0.3.17 matplotlib-3.11.2 matscipy-1.3.1 numpy-2.5.5 opt-einsum-fx-0.1.4 opt_einsum-3.4.0 orjson-3.13.0 packaging-26.4 pandas-3.1.1 pillow-13.0.0 prettytable-3.19.0 pyYAML-6.0.4 pyparsing-3.3.3 python-dateutil-4.0.0 python-hostlist-2.3.0 scipy-1.18.1 smmap-5.0.3 torch-ema-0.3 torchmetrics-1.9.0 tqdm-4.70.1 tzdata-2026.6 wcwidth-0.9.5

((mace_ampere_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip show torch mace-torch ase
Name: torch
Version: 2.15.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org
Author:
Author-email: PyTorch Team <packages@pytorch.org>
License-Expression: Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND ISC AND MIT AND Zlib
Location: /lustre/projects/m/milias/work/software/mace_ampere_venv/lib/python3.12/site-packages
Requires: cuda-bindings, cuda-toolkit, filelock, fsspec, jinja2, networkx, nvidia-cudnn-cu13, nvidia-cusparselt-cu13, nvidia-nccl-cu13, nvidia-nvshmem-cu13, setuptools, sympy, triton, typing-extensions
Required-by: e3nn, mace-torch, opt-einsum-fx, torch-ema, torchmetrics
---
Name: mace-torch
Version: 0.3.17
Summary:
Home-page: https://github.com/ACEsuit/mace
Author:
Author-email:
License:
Location: /lustre/projects/m/milias/work/software/mace_ampere_venv/lib/python3.12/site-packages
Requires: ase, configargparse, e3nn, GitPython, h5py, lmdb, matplotlib, matscipy, numpy, opt_einsum, orjson, pandas, prettytable, python-hostlist, pyYAML, torch, torch-ema, torchmetrics, tqdm
Required-by:
---
Name: ase
Version: 3.29.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /lustre/projects/m/milias/work/software/mace_ampere_venv/lib/python3.12/site-packages
Requires: matplotlib, numpy, scipy, typing_extensions
Required-by: mace-torch, matscipy

