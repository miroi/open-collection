=====================
ASAP3 on lx-pool.gsi.de
=====================

milias@lxi100.gsi.de:~/Work/qch/projects/open-collection/.python3 -m pip install --upgrade --user asap3
..fails..

https://gitlab.com/asap/asap/-/issues/57

milias@lxi090.gsi.de:~/.python3 -m pip install --upgrade --user numpy
Cache entry deserialization failed, entry ignored
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/45/b7/de7b8e67f2232c26af57c205aaad29fe17754f793404f59c8a730c7a191a/numpy-1.21.6.zip (10.3MB)
    100% |████████████████████████████████| 10.3MB 134kB/s
  Installing build dependencies ... done
Building wheels for collected packages: numpy
  Running setup.py bdist_wheel for numpy ... done
  Stored in directory: /u/milias/.cache/pip/wheels/73/70/b5/557358663d5c8e7dcc61c63e487c005c0b3d1240d328500183
Successfully built numpy
Installing collected packages: numpy
Successfully installed numpy-1.21.6
milias@lxi090.gsi.de:~/.


milias@lxi090.gsi.de:~/.python3 -m pip install --upgrade --user asap3
Requirement already up-to-date: asap3 in ./.local/lib/python3.7/site-packages (3.13.2)
Requirement already satisfied, skipping upgrade: ase>=3.22.1 in ./.local/lib/python3.7/site-packages (from asap3) (3.22.1)
Requirement already satisfied, skipping upgrade: matplotlib>=3.1.0 in ./.local/lib/python3.7/site-packages (from ase>=3.22.1->asap3) (3.5.3)
Requirement already satisfied, skipping upgrade: scipy>=1.1.0 in /usr/lib/python3/dist-packages (from ase>=3.22.1->asap3) (1.1.0)
Requirement already satisfied, skipping upgrade: numpy>=1.15.0 in ./.local/lib/python3.7/site-packages (from ase>=3.22.1->asap3) (1.21.6)
Requirement already satisfied, skipping upgrade: fonttools>=4.22.0 in ./.local/lib/python3.7/site-packages (from matplotlib>=3.1.0->ase>=3.22.1->asap3) (4.38.0)
Requirement already satisfied, skipping upgrade: kiwisolver>=1.0.1 in /usr/lib/python3/dist-packages (from matplotlib>=3.1.0->ase>=3.22.1->asap3) (1.0.1)
Requirement already satisfied, skipping upgrade: python-dateutil>=2.7 in /usr/lib/python3/dist-packages (from matplotlib>=3.1.0->ase>=3.22.1->asap3) (2.7.3)
Requirement already satisfied, skipping upgrade: pyparsing>=2.2.1 in ./.local/lib/python3.7/site-packages (from matplotlib>=3.1.0->ase>=3.22.1->asap3) (3.1.1)
Requirement already satisfied, skipping upgrade: packaging>=20.0 in ./.local/lib/python3.7/site-packages (from matplotlib>=3.1.0->ase>=3.22.1->asap3) (23.2)
Requirement already satisfied, skipping upgrade: pillow>=6.2.0 in ./.local/lib/python3.7/site-packages (from matplotlib>=3.1.0->ase>=3.22.1->asap3) (9.5.0)
Requirement already satisfied, skipping upgrade: cycler>=0.10 in /usr/lib/python3/dist-packages (from matplotlib>=3.1.0->ase>=3.22.1->asap3) (0.10.0)




