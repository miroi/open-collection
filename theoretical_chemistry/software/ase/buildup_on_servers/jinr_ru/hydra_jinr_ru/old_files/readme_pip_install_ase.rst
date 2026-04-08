==============
ASE on Govorun
==============

clean .local directory
~~~~~~~~~~~~~~~~~~~~~~
/bin/rm -rf ~/.local/

install
~~~~~~~
module add  Python/v3.10.13

pip install ase
Defaulting to user installation because normal site-packages is not writeable
Collecting ase
  Downloading ase-3.26.0-py3-none-any.whl.metadata (4.1 kB)
Requirement already satisfied: numpy>=1.19.5 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from ase) (1.26.1)
Requirement already satisfied: scipy>=1.6.0 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from ase) (1.11.3)
Requirement already satisfied: matplotlib>=3.3.4 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from ase) (3.9.2)
Requirement already satisfied: contourpy>=1.0.1 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (1.3.1)
Requirement already satisfied: cycler>=0.10 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (4.55.0)
Requirement already satisfied: kiwisolver>=1.3.1 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (1.4.7)
Requirement already satisfied: packaging>=20.0 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (24.2)
Requirement already satisfied: pillow>=8 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (11.0.0)
Requirement already satisfied: pyparsing>=2.3.1 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (3.2.0)
Requirement already satisfied: python-dateutil>=2.7 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from python-dateutil>=2.7->matplotlib>=3.3.4->ase) (1.16.0)
Downloading ase-3.26.0-py3-none-any.whl (2.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.9/2.9 MB 864.0 kB/s  0:00:03
Installing collected packages: ase
Successfully installed ase-3.26.0

pip show ase
Name: ase
Version: 3.26.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: /lustre/home/user/m/milias/.local/lib/python3.10/site-packages
Requires: matplotlib, numpy, scipy
Required-by:

pytest 
~~~~~~
pip install pytest
Defaulting to user installation because normal site-packages is not writeable
Collecting pytest
  Downloading pytest-8.4.2-py3-none-any.whl.metadata (7.7 kB)
Requirement already satisfied: exceptiongroup>=1 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from pytest) (1.2.2)
Collecting iniconfig>=1 (from pytest)
  Using cached iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Requirement already satisfied: packaging>=20 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from pytest) (24.2)
Collecting pluggy<2,>=1.5 (from pytest)
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Requirement already satisfied: pygments>=2.7.2 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from pytest) (2.18.0)
Collecting tomli>=1 (from pytest)
  Using cached tomli-2.2.1-py3-none-any.whl.metadata (10 kB)
Downloading pytest-8.4.2-py3-none-any.whl (365 kB)
Using cached pluggy-1.6.0-py3-none-any.whl (20 kB)
Using cached iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Using cached tomli-2.2.1-py3-none-any.whl (14 kB)
Installing collected packages: tomli, pluggy, iniconfig, pytest
Successfully installed iniconfig-2.1.0 pluggy-1.6.0 pytest-8.4.2 tomli-2.2.1

pip show pytest
Name: pytest
Version: 8.4.2
Summary: pytest: simple powerful testing with Python
Home-page: https://docs.pytest.org/en/latest/
Author: Holger Krekel, Bruno Oliveira, Ronny Pfannschmidt, Floris Bruynooghe, Brianna Laugher, Florian Bruhin, Others (See AUTHORS)
Author-email:
License: MIT
Location: /lustre/home/user/m/milias/.local/lib/python3.10/site-packages
Requires: exceptiongroup, iniconfig, packaging, pluggy, pygments, tomli
Required-by:





