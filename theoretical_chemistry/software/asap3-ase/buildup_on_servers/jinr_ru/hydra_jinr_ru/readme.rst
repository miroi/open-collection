======================
ASAP3 on hydra.jinr.ru
======================

modules
-------
milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.module add Python/v3.10.13

milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1        2) BASE/1.0          3) Python/v3.10.13

milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.pip show asap3 ase
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Name: asap3
Version: 3.13.6
Summary: ASAP - classical potentials for MD with ASE.
Home-page: https://wiki.fysik.dtu.dk/asap
Author:
Author-email:
License: LGPLv3
Location: /lustre/home/user/m/milias/.local/lib/python3.10/site-packages
Requires: ase
Required-by:
---
Name: ase
Version: 3.24.0
Summary: Atomic Simulation Environment
Home-page: https://wiki.fysik.dtu.dk/ase/
Author:
Author-email:
License: LGPLv2.1+
Location: /lustre/home/user/m/milias/.local/lib/python3.10/site-packages
Requires: matplotlib, numpy, scipy
Required-by: asap3

