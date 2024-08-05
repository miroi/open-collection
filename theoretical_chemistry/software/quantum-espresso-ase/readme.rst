===========
QE with ASE
===========

WSL-Notebook
~~~~~~~~~~~~

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/runs/quantum-espresso-ase/.python3 rocksalt_optim.py
single point calc:
ase geometry optimization:
       Step     Time          Energy          fmax
LBFGS:    0 11:55:25    -1684.175469        0.000000
Obtained optimized lattice constant, a=
6.0

WSL-Desktop
~~~~~~~~~~~
milias@pc7321b:/mnt/c/Users/milias/My Documents/git-projects/open-collection/theoretical_chemistry/software/ase/runs/quantum-espresso-ase/.python3 rocksalt_optim2.py
single point calc:
ase lattice geometry optimization, with stress tensor:
/mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/ase/runs/quantum-espresso-ase/rocksalt_optim2.py:42: FutureWarning: Import StrainFilter from ase.filters
  sf = StrainFilter(rocksalt)
       Step     Time          Energy          fmax
LBFGS:    0 20:23:55    -1690.337655       31.464782
LBFGS:    1 20:23:56    -1690.221769       26.552469
LBFGS:    2 20:23:57    -1687.914916       12.932303
LBFGS:    3 20:23:58    -1679.174825       23.101026
LBFGS:    4 20:23:59    -1685.975258        3.588310
LBFGS:    5 20:24:00    -1685.384888        0.649137
LBFGS:    6 20:24:00    -1685.164700        0.477814
LBFGS:    7 20:24:01    -1684.840598        2.015651
LBFGS:    8 20:24:02    -1685.134616        0.178762
LBFGS:    9 20:24:03    -1685.165060        0.024743
LBFGS:   10 20:24:04    -1685.165060        0.031478
LBFGS:   11 20:24:05    -1685.165061        0.000000
ase geometry optimization, with LBFGS:
       Step     Time          Energy          fmax
LBFGS:    0 20:24:05    -1685.165061        0.000000
Obtained optimized lattice constant, a
4.305289947408856

TODO: Set ASE calculation for sole QE optimization 
