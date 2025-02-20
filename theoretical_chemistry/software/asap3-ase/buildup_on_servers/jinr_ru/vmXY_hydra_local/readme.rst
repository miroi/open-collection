=========================
ASAP3 on vmXY.hydra.local
=========================

milias@vm02.hydra.local:~/.pip install asap3
Defaulting to user installation because normal site-packages is not writeable
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Requirement already satisfied: asap3 in ./.local/lib/python3.10/site-packages (3.13.4)
Requirement already satisfied: ase>=3.22.1 in ./.local/lib/python3.10/site-packages (from asap3) (3.23.0)
Requirement already satisfied: numpy>=1.18.5 in ./.local/lib/python3.10/site-packages (from ase>=3.22.1->asap3) (1.26.4)
Requirement already satisfied: scipy>=1.6.0 in ./.local/lib/python3.10/site-packages (from ase>=3.22.1->asap3) (1.12.0)
Requirement already satisfied: matplotlib>=3.3.4 in ./.local/lib/python3.10/site-packages (from ase>=3.22.1->asap3) (3.8.3)
Requirement already satisfied: contourpy>=1.0.1 in ./.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase>=3.22.1->asap3) (1.2.0)
Requirement already satisfied: cycler>=0.10 in ./.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase>=3.22.1->asap3) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in ./.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase>=3.22.1->asap3) (4.50.0)
Requirement already satisfied: kiwisolver>=1.3.1 in ./.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase>=3.22.1->asap3) (1.4.5)
Requirement already satisfied: packaging>=20.0 in ./.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase>=3.22.1->asap3) (24.0)
Requirement already satisfied: pillow>=8 in ./.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase>=3.22.1->asap3) (10.3.0)
Requirement already satisfied: pyparsing>=2.3.1 in ./.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase>=3.22.1->asap3) (3.1.2)
Requirement already satisfied: python-dateutil>=2.7 in ./.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase>=3.22.1->asap3) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in ./.local/lib/python3.10/site-packages (from python-dateutil>=2.7->matplotlib>=3.3.4->ase>=3.22.1->asap3) (1.16.0)
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)

milias@vm02.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.pip install --upgrade --user  asap3
.
.
 Stored in directory: /lustre/home/user/m/milias/.cache/pip/wheels/f2/f7/48/10a78efcea5b08cb4fe6c97dd2d21b1e09e2fe5fee963c26fe
Successfully built asap3
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Installing collected packages: asap3
Successfully installed asap3-3.13.6


milias@vm02.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.pip show asap3 ase
milias@vm02.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.pip show asap3 ase
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



