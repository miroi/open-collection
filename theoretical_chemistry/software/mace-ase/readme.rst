=============
MACE with ASE
=============


installation
------------
https://github.com/ACEsuit/mace?tab=readme-ov-file#installation-from-pypi

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/.source ~/work/software/myenv/bin/activate
(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/.pip install --upgrade pip
.
.
      Successfully uninstalled pip-24.0
Successfully installed pip-25.3

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/.pip install mace-torch
Collecting mace-torch
.
.
Successfully built python-hostlist
Installing collected packages: python-hostlist, wcwidth, smmap, opt_einsum, lightning-utilities, configargparse, prettytable, gitdb, GitPython, torchmetrics, torch-ema, opt-einsum-fx, matscipy, e3nn, mace-torch
Successfully installed GitPython-3.1.45 configargparse-1.7.1 e3nn-0.4.4 gitdb-4.0.12 lightning-utilities-0.15.2 mace-torch-0.3.14 matscipy-1.1.1 opt-einsum-fx-0.1.4 opt_einsum-3.4.0 prettytable-3.16.0 python-hostlist-2.3.0 smmap-5.0.2 torch-ema-0.3 torchmetrics-1.8.2 wcwidth-0.2.14

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mace-ase/.pip show mace-torch
Name: mace-torch
Version: 0.3.14
Summary:
Home-page: https://github.com/ACEsuit/mace
Author:
Author-email:
License:
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Requires: ase, configargparse, e3nn, GitPython, h5py, lmdb, matplotlib, matscipy, numpy, opt_einsum, orjson, pandas, prettytable, python-hostlist, pyYAML, torch, torch-ema, torchmetrics, tqdm
Required-by:


documentation
~~~~~~~~~~~~~

https://mace-docs.readthedocs.io/en/latest




