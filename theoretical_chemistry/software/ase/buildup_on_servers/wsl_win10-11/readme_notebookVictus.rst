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
platform                 Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35
python-3.10.12           /usr/bin/python3
ase-3.23.0               /home/miroi/.local/lib/python3.10/site-packages/ase
numpy-1.26.4             /home/miroi/.local/lib/python3.10/site-packages/numpy
scipy-1.14.1             /home/miroi/.local/lib/python3.10/site-packages/scipy
matplotlib-3.9.2         /home/miroi/.local/lib/python3.10/site-packages/matplotlib
spglib                   not installed
ase_ext                  not installed
flask                    not installed
psycopg2-2.9.9 (dt dec pq3 ext lo64) /home/miroi/.local/lib/python3.10/site-packages/psycopg2
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

pip show ase
Name: ase
Version: 3.23.0
Summary: Atomic Simulation Environment
Home-page:
Author:
Author-email:
License: LGPLv2.1+
Location: /home/miroi/.local/lib/python3.10/site-packages
Requires: matplotlib, numpy, scipy
Required-by: asap3, gpaw

