====================================
ASE on Windows11-WSL Notevook Victus
====================================

lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.4 LTS
Release:        22.04
Codename:       jammy

ase and dependecies installed as sudo packages !

ase info
~~~~~~~~
platform                 Linux-5.15.146.1-microsoft-standard-WSL2-x86_64-with-glibc2.35
python-3.10.12           /usr/bin/python3
ase-3.22.1               /usr/lib/python3/dist-packages/ase
numpy-1.21.5             /usr/lib/python3/dist-packages/numpy
scipy-1.8.0              /usr/lib/python3/dist-packages/scipy
matplotlib-3.5.1         /usr/lib/python3/dist-packages/matplotlib
spglib-1.16.2            /usr/lib/python3/dist-packages/spglib
ase_ext                  not installed
flask-2.0.1              /usr/lib/python3/dist-packages/flask
psycopg2-2.9.2 (dt dec pq3 ext lo64) /usr/lib/python3/dist-packages/psycopg2
pyamg                    not installed

milias@Miro:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/wsl_win10-11/.pip show asap3
Name: asap3
Version: 3.13.4
Summary: ASAP - classical potentials for MD with ASE.
Home-page: https://wiki.fysik.dtu.dk/asap
Author:
Author-email:
License: LGPLv3
Location: /home/milias/.local/lib/python3.10/site-packages
Requires: ase
Required-by:
milias@Miro:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/wsl_win10-11/.pip show ase
Name: ase
Version: 3.22.1
Summary: Atomic Simulation Environment
Home-page: https://wiki.fysik.dtu.dk/ase
Author:
Author-email:
License: LGPLv2.1+
Location: /usr/lib/python3/dist-packages
Requires:
Required-by: asap3


