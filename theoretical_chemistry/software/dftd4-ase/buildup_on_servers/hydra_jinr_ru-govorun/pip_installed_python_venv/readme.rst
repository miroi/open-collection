================
DFTD4 on Govorun
================

Python venv
------------

source /lustre/projects/m/milias/work/software/myvenv/bin/activate

((myvenv) ) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/dftd4-ase/buildup_on_servers/hydra_jinr_ru-govorun/pip_installed_python_venv/.which python
/lustre/projects/m/milias/work/software/myvenv/bin/python

((myvenv) ) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/dftd4-ase/buildup_on_servers/hydra_jinr_ru-govorun/pip_installed_python_venv/.which pip
/lustre/projects/m/milias/work/software/myvenv/bin/pip

pip install
-----------

(myvenv) ) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/dftd4-ase/buildup_on_servers/hydra_jinr_ru-govorun/pip_installed_python_venv/.module add openmpi/v4.1.8_gcc1230
((myvenv) ) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/dftd4-ase/buildup_on_servers/hydra_jinr_ru-govorun/pip_installed_python_venv/.pip install dftd4

((myvenv) ) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/dftd4-ase/buildup_on_servers/hydra_jinr_ru-govorun/pip_installed_python_venv/.pip install dftd4
.
Successfully installed cffi-2.0.0 dftd4-4.1.0 pycparser-3.0

((myvenv) ) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/dftd4-ase/buildup_on_servers/hydra_jinr_ru-govorun/pip_installed_python_venv/.pip install tomli
.
Successfully installed tomli-2.4.1


pip show
--------
((myvenv) ) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/dftd4-ase/buildup_on_servers/hydra_jinr_ru-govorun/pip_installed_python_venv/.pip show dftd4 ase
Name: dftd4
Version: 4.1.0
Summary: Python API of the DFT-D4 project
Home-page:
Author:
Author-email:
License: LGPL-3.0-or-later
Location: /lustre/projects/m/milias/work/software/myvenv/lib/python3.12/site-packages
Requires: cffi, numpy
Required-by:

Name: ase
Version: 3.28.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /lustre/projects/m/milias/work/software/myvenv/lib/python3.12/site-packages
Requires: matplotlib, numpy, scipy
Required-by:

pip list
--------
((myvenv) ) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/dftd4-ase/buildup_on_servers/hydra_jinr_ru-govorun/pip_installed_python_venv/.pip list
Package         Version
--------------- -----------
ase             3.28.0
cffi            2.0.0
contourpy       1.3.3
cycler          0.12.1
dftd4           4.1.0
fonttools       4.62.1
kiwisolver      1.5.0
matplotlib      3.10.8
numpy           2.4.4
packaging       26.0
pillow          12.2.0
pip             26.0.1
pycparser       3.0
pyparsing       3.3.2
python-dateutil 2.9.0.post0
scipy           1.17.1
six             1.17.0
tomli           2.4.1
