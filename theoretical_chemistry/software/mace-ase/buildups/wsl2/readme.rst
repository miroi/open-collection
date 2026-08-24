=========================
MACE installation on WSL2
=========================

Victus notebook
---------------
con
miniconda activated :conda 26.5.3
conda activate mace_env

which ase
/home/miroi/miniconda3/envs/mace_env/bin/ase
ase --version
ase-3.29.0

(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/buildups/wsl2/.pip list | grep mace
mace-torch             0.3.16
(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/buildups/wsl2/.pip show mace-torch
Name: mace-torch
Version: 0.3.16
Summary:
Home-page: https://github.com/ACEsuit/mace
Author:
Author-email:
License:
Location: /home/miroi/miniconda3/envs/mace_env/lib/python3.13/site-packages
Requires: ase, configargparse, e3nn, GitPython, h5py, lmdb, matplotlib, matscipy, numpy, opt_einsum, orjson, pandas, prettytable, python-hostlist, pyYAML, torch, torch-ema, torchmetrics, tqdm
Required-by:


conda config --add channels conda-forge
Warning: 'conda-forge' already in 'channels' list, moving to the top
conda config --set channel_priority strict
conda install setuptools

tests
-----

(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/buildups/wsl2/.python model_analyzer.py  > model_analyzer.py_logfile

(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/buildups/wsl2/.python model_element_detector.py  > model_element_detector.py_logfile

(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/buildups/wsl2/.python check_mace_ml_installation.py > python check_mace_ml_installation.py_logfileSAVED

Deepseek AI
-----------
https://chat.deepseek.com/share/xdmwtw118hiqj9y0to
