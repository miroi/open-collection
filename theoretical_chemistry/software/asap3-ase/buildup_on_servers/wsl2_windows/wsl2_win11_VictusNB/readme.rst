======================
ASAP3 on Windows11-WSL
======================

https://asap3.readthedocs.io/en/latest/

install and test
----------------

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/asap3/servers/windows10_wsl$ sudo apt-get install libopenmpi-dev

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/wsl_win11_VictusNB/.pip install --upgrade asap3
.
.
Successfully installed asap3-3.13.10

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/runs/.pip show asap3
Name: asap3
Version: 3.13.10
Summary: ASAP - classical potentials for MD with ASE.
Home-page: https://wiki.fysik.dtu.dk/asap
Author:
Author-email:
License-Expression: LGPL-3.0
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Requires: ase, numpy
Required-by:

testing
~~~~~~~
(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/runs/.pip install --upgrade pytest
.
.
Successfully installed pytest-9.0.2

pytest --pyargs asap3 -m core
==================================== 86 passed, 3 skipped, 184 deselected in 22.24s

mpirun -np 4 pytest --pyargs asap3 -m core
==================================== 24 passed, 65 skipped, 180 deselected in 5.45s ====================================







