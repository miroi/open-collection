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
(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.source mace_cpu_venv/bin/activate


one-command activate
~~~~~~~~~~~~~~~~~~~~
source /lustre/projects/m/milias/work/software/mace_cpu_venv/bin/activate

pip install
-----------
((mace_cpu_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip install mace ase
.
.
Successfully installed ase-3.29.0 bcbio-gff-0.7.1 biopython-1.88 contourpy-1.4.0 cycler-0.12.1 fonttools-4.68.0 kiwisolver-1.5.1 mace-1.1.2 matplotlib-3.11.2 numpy-2.5.5 packaging-26.4 pillow-13.0.0 pyparsing-3.3.3 python-dateutil-4.0.0 scipy-1.18.1 six-1.17.0 typing_extensions-4.16.0 tzdata-2026.6

((mace_cpu_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip show mace ase
Name: MACE
Version: 1.1.2
Summary:
Home-page:
Author: Sergei F. Kliver
Author-email: mahajrod@gmail.com
License:
Location: /lustre/projects/m/milias/work/software/mace_cpu_venv/lib/python3.12/site-packages
Requires: bcbio-gff, biopython, matplotlib, numpy, scipy
Required-by:
---
Name: ase
Version: 3.29.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /lustre/projects/m/milias/work/software/mace_cpu_venv/lib/python3.12/site-packages
Requires: matplotlib, numpy, scipy, typing_extensions
Required-by:

