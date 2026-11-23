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


pip install
-----------
((mace_venv) ) (Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/.pip install ase mace-torch




