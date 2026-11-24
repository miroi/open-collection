===============
MACE on Govorun
===============


Modules and Python Virtual Environment
--------------------------------------

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.module add Python

(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.python3 -m venv mace_venv


(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.source mace_venv/bin/activate
((mace_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.

((mace_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.module add cuda
((mace_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.module list

Currently Loaded Modules:
  1) Python/v3.12.13   2) cuda/v13.0

one-command activate
~~~~~~~~~~~~~~~~~~~~
source /lustre/projects/m/milias/work/software/mace_venv/bin/activate

pip install
-----------
((mace_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip install ase mace-torch

pip show ase mace-torch
Name: ase
Version: 3.29.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /lustre/projects/m/milias/work/software/mace_venv/lib/python3.12/site-packages
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
Location: /lustre/projects/m/milias/work/software/mace_venv/lib/python3.12/site-packages
Requires: ase, configargparse, e3nn, GitPython, h5py, lmdb, matplotlib, matscipy, numpy, opt_einsum, orjson, pandas, prettytable, python-hostlist, pyYAML, torch, torch-ema, torchmetrics, tqdm
Required-by:


