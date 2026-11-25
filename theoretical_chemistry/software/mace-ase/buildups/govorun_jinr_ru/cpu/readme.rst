===============
MACE on Govorun
===============

Modules and Python Virtual Environment
--------------------------------------
module add Python
python -V
Python 3.12.13

(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.python3 -m venv mace_cpu_venv

(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.source mace_cpu_venv/bin/activate


one-command activate
~~~~~~~~~~~~~~~~~~~~
source /lustre/projects/m/milias/work/software/mace_cpu_venv/bin/activate

pip install
-----------
((mace_cpu_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.
.
Successfully installed MarkupSafe-3.0.3 filelock-4.2.4 fsspec-2026.9.0 jinja2-3.1.6 mpmath-1.3.0 networkx-3.7 setuptools-78.1.0 sympy-1.14.0 torch-2.15.0+cpu

((mace_cpu_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.python -m pip install mace-torch ase
.
.
Successfully installed GitPython-3.2.1 configargparse-1.10.2 e3nn-0.4.4 gitdb-4.0.12 h5py-3.16.0 lightning-utilities-0.15.3 lmdb-3.0.0 mace-torch-0.3.17 matscipy-1.3.1 opt-einsum-fx-0.1.4 opt_einsum-3.4.0 orjson-3.13.0 pandas-3.1.1 prettytable-3.19.0 pyYAML-6.0.4 python-hostlist-2.3.0 smmap-5.0.3 torch-ema-0.3 torchmetrics-1.9.0 tqdm-4.70.1 wcwidth-0.9.5


((mace_cpu_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip show ase mace-torch torch
Name: ase
Version: 3.29.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /lustre/projects/m/milias/work/software/mace_cpu_venv/lib/python3.12/site-packages
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
Location: /lustre/projects/m/milias/work/software/mace_cpu_venv/lib/python3.12/site-packages
Requires: ase, configargparse, e3nn, GitPython, h5py, lmdb, matplotlib, matscipy, numpy, opt_einsum, orjson, pandas, prettytable, python-hostlist, pyYAML, torch, torch-ema, torchmetrics, tqdm
Required-by:
---
Name: torch
Version: 2.15.0+cpu
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org
Author:
Author-email: PyTorch Team <packages@pytorch.org>
License-Expression: Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND ISC AND MIT AND Zlib
Location: /lustre/projects/m/milias/work/software/mace_cpu_venv/lib/python3.12/site-packages
Requires: filelock, fsspec, jinja2, networkx, setuptools, sympy, typing-extensions
Required-by: e3nn, mace-torch, opt-einsum-fx, torch-ema, torchmetrics

check mace_run_train
--------------------
((mace_cpu_venv) ) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/mace-ase/buildups/govorun_jinr_ru/cpu/.which mace_run_train
/lustre/projects/m/milias/work/software/mace_cpu_venv/bin/mace_run_train
