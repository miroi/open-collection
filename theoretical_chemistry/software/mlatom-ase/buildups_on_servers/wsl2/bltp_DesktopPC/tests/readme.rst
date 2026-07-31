===================
MLAtom simple tests
===================

https://share.google/aimode/TGN9Pmn0sMa4yvZ25

pip install torchani==2.2.3 torch
pip install "setuptools<82"

needs dftd4 (from conda), specific version of torch...

(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mlatom-ase/buildups_on_servers/wsl2/bltp_DesktopPC/tests/.pip show mlatom
Name: mlatom
Version: 3.23.3
Summary: A Package for AI-enhanced computational chemistry
Home-page: http://mlatom.com
Author: Pavlo O. Dral
Author-email: admin@mlatom.com
License: MIT (modified)
Location: /home/milias/work/software/venv/lib/python3.12/site-packages
Requires: h5py, matplotlib, numpy, pyh5md, scipy, statsmodels, torch, torchani, tqdm
Required-by:
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mlatom-ase/buildups_on_servers/wsl2/bltp_DesktopPC/tests/.pip show torchani
Name: torchani
Version: 2.2.3
Summary: PyTorch implementation of ANI
Home-page: https://github.com/aiqm/torchani
Author: Xiang Gao
Author-email: qasdfgtyuiop@gmail.com
License: MIT
Location: /home/milias/work/software/venv/lib/python3.12/site-packages
Requires: importlib-metadata, lark-parser, requests, torch
Required-by: mlatom

run
---
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mlatom-ase/buildups_on_servers/wsl2/bltp_DesktopPC/tests/.export dftd4bin=/home/milias/miniconda3/bin/dftd4
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mlatom-ase/buildups_on_servers/wsl2/bltp_DesktopPC/tests/.python water-optim.py
-76.38409860835867
(venv) milias@DESKTOP-7OTLCGO:~

The script has successfully run, and the AIQM2 optimized energy for your water molecule is -76.38409860835867 Hartree.

