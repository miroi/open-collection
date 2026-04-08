ASE on Govorun
==============

module add Python

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.python -m venv  myvenv

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.source myvenv/bin/activate

((myvenv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.which python
/lustre/projects/m/milias/work/software/myvenv/bin/python
((myvenv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.which pip
/lustre/projects/m/milias/work/software/myvenv/bin/pip
((myvenv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.

((myvenv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip install ase
.
.
Installing collected packages: six, pyparsing, pillow, packaging, numpy, kiwisolver, fonttools, cycler, scipy, python-dateutil, contourpy, matplotlib, ase
Successfully installed ase-3.28.0 contourpy-1.3.3 cycler-0.12.1 fonttools-4.62.1 kiwisolver-1.5.0 matplotlib-3.10.8 numpy-2.4.4 packaging-26.0 pillow-12.2.0 pyparsing-3.3.2 python-dateutil-2.9.0.post0 scipy-1.17.1 six-1.17.0

((myvenv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip show ase
Name: ase
Version: 3.28.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /lustre/projects/m/milias/work/software/myvenv/lib/python3.12/site-packages
Requires: matplotlib, numpy, scipy



