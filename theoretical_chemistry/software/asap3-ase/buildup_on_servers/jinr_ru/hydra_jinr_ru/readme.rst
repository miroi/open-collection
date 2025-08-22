======================
ASAP3 on hydra.jinr.ru
======================

modules
-------
milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.module add Python/v3.10.13

milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1        2) BASE/1.0          3) Python/v3.10.13


install interactively
~~~~~~~~~~~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.pip install asap3
Defaulting to user installation because normal site-packages is not writeable
Collecting asap3
  Downloading asap3-3.13.7.tar.gz (855 kB)
.
.
.



test the presence
~~~~~~~~~~~~~~~~~

milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.pip show asap3
Name: asap3
Version: 3.13.7
Summary: ASAP - classical potentials for MD with ASE.
Home-page: https://wiki.fysik.dtu.dk/asap
Author:
Author-email:
License: LGPLv3
Location: /lustre/home/user/m/milias/.local/lib/python3.10/site-packages
Requires: ase
Required-by:


milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.pip show ase
Name: ase
Version: 3.27.0b1
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /lustre/home/user/m/milias/.local/lib/python3.10/site-packages
Requires: matplotlib, numpy, scipy
Required-by: asap3


