==============
ASE on Govorun
==============

MUST HAVE Python/v3.10.13  !!!

clean .local directory
~~~~~~~~~~~~~~~~~~~~~~
/bin/rm -rf ~/.local/

install
~~~~~~~

module add  Python/v3.10.13

milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.pip install git+https://gitlab.com/ase/ase.git
Defaulting to user installation because normal site-packages is not writeable
Collecting git+https://gitlab.com/ase/ase.git
  Cloning https://gitlab.com/ase/ase.git to /tmp/pip-req-build-61oussjn
  Running command git clone --filter=blob:none --quiet https://gitlab.com/ase/ase.git /tmp/pip-req-build-61oussjn
  Resolved https://gitlab.com/ase/ase.git to commit 9c9eabdb4eda350d6e606f5462dbe479085694b5
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: numpy>=1.19.5 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from ase==3.27.0b1) (1.26.1)
Requirement already satisfied: scipy>=1.6.0 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from ase==3.27.0b1) (1.11.3)
Requirement already satisfied: matplotlib>=3.3.4 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from ase==3.27.0b1) (3.9.2)
Requirement already satisfied: contourpy>=1.0.1 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase==3.27.0b1) (1.3.1)
Requirement already satisfied: cycler>=0.10 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase==3.27.0b1) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase==3.27.0b1) (4.55.0)
Requirement already satisfied: kiwisolver>=1.3.1 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase==3.27.0b1) (1.4.7)
Requirement already satisfied: packaging>=20.0 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase==3.27.0b1) (24.2)
Requirement already satisfied: pillow>=8 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase==3.27.0b1) (11.0.0)
Requirement already satisfied: pyparsing>=2.3.1 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase==3.27.0b1) (3.2.0)
Requirement already satisfied: python-dateutil>=2.7 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase==3.27.0b1) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from python-dateutil>=2.7->matplotlib>=3.3.4->ase==3.27.0b1) (1.16.0)
Building wheels for collected packages: ase
  Building wheel for ase (pyproject.toml) ... done
  Created wheel for ase: filename=ase-3.27.0b1-py3-none-any.whl size=2947439 sha256=7bd3a5144382068926e203df60eface170a3c1b34dcbf42b6b26d70dd9da6096
  Stored in directory: /tmp/pip-ephem-wheel-cache-ojo1pe69/wheels/1d/54/ef/6da2fa4c90bb9e22acd3ddd813835ec891b0c2e4b535e4cf40
Successfully built ase
Installing collected packages: ase
Successfully installed ase-3.27.0b1


pytest 
~~~~~~
pip install pytest
Defaulting to user installation because normal site-packages is not writeable
Collecting pytest
  Downloading pytest-8.4.1-py3-none-any.whl.metadata (7.7 kB)
Requirement already satisfied: exceptiongroup>=1 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from pytest) (1.2.2)
Collecting iniconfig>=1 (from pytest)
  Downloading iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Requirement already satisfied: packaging>=20 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from pytest) (24.2)
Collecting pluggy<2,>=1.5 (from pytest)
  Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Requirement already satisfied: pygments>=2.7.2 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/site-packages (from pytest) (2.18.0)
Collecting tomli>=1 (from pytest)
  Downloading tomli-2.2.1-py3-none-any.whl.metadata (10 kB)
Downloading pytest-8.4.1-py3-none-any.whl (365 kB)
Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
Downloading iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Downloading tomli-2.2.1-py3-none-any.whl (14 kB)
Installing collected packages: tomli, pluggy, iniconfig, pytest
Successfully installed iniconfig-2.1.0 pluggy-1.6.0 pytest-8.4.1 tomli-2.2.1



