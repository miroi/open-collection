==============
ASE on Govorun
==============

master version
~~~~~~~~~~~~~~
pip install --upgrade git+https://gitlab.com/ase/ase.git@master

  ERROR: Command errored out with exit status 1:
   command: /usr/bin/python3 /lustre/home/user/m/milias/.local/lib/python3.6/site-packages/pip install --ignore-installed --no-user --prefix /tmp/pip-build-env-wo0eztel/overlay --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- 'setuptools >= 77.0.3'
       cwd: None
  Complete output (2 lines):
  ERROR: Could not find a version that satisfies the requirement setuptools>=77.0.3

distribution version
~~~~~~~~~~~~~~~~~~~~
pip install --upgrade ase
Defaulting to user installation because normal site-packages is not writeable
Collecting ase
  Using cached ase-3.22.1-py3-none-any.whl (2.2 MB)
Collecting numpy>=1.15.0
  Downloading numpy-1.19.5-cp36-cp36m-manylinux2010_x86_64.whl (14.8 MB)
     |████████████████████████████████| 14.8 MB 1.7 MB/s
Collecting scipy>=1.1.0
  Using cached scipy-1.5.4-cp36-cp36m-manylinux1_x86_64.whl (25.9 MB)
Collecting matplotlib>=3.1.0
  Using cached matplotlib-3.3.4-cp36-cp36m-manylinux1_x86_64.whl (11.5 MB)
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3
  Using cached pyparsing-3.1.4-py3-none-any.whl (104 kB)
Collecting pillow>=6.2.0
  Downloading Pillow-8.4.0-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
     |████████████████████████████████| 3.1 MB 42.2 MB/s
Collecting kiwisolver>=1.0.1
  Using cached kiwisolver-1.3.1-cp36-cp36m-manylinux1_x86_64.whl (1.1 MB)
Collecting python-dateutil>=2.1
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Collecting cycler>=0.10
  Using cached cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting six>=1.5
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, python-dateutil, pyparsing, pillow, numpy, kiwisolver, cycler, scipy, matplotlib, ase

Successfully installed ase-3.22.1 cycler-0.11.0 kiwisolver-1.3.1 matplotlib-3.3.4 numpy-1.19.5 pillow-8.4.0 pyparsing-3.1.4 python-dateutil-2.9.0.post0 scipy-1.5.4 six-1.17.0
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4/bin/.
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4/bin/.pip show ase
Name: ase
Version: 3.22.1
Summary: Atomic Simulation Environment
Home-page: https://wiki.fysik.dtu.dk/ase
Author:
Author-email:
License: LGPLv2.1+
Location: /lustre/home/user/m/milias/.local/lib/python3.6/site-packages
Requires: matplotlib, numpy, scipy
Required-by:

pytest 
~~~~~~
pip install pytest
Defaulting to user installation because normal site-packages is not writeable
Collecting pytest
  Downloading pytest-7.0.1-py3-none-any.whl (296 kB)
     |████████████████████████████████| 296 kB 1.7 MB/s
Collecting iniconfig
  Downloading iniconfig-1.1.1-py2.py3-none-any.whl (5.0 kB)
Collecting importlib-metadata>=0.12
  Downloading importlib_metadata-4.8.3-py3-none-any.whl (17 kB)
Collecting attrs>=19.2.0
  Downloading attrs-22.2.0-py3-none-any.whl (60 kB)
     |████████████████████████████████| 60 kB 191 kB/s
Collecting tomli>=1.0.0
  Downloading tomli-1.2.3-py3-none-any.whl (12 kB)
Collecting pluggy<2.0,>=0.12
  Downloading pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Collecting packaging
  Downloading packaging-21.3-py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 146 kB/s
Collecting py>=1.8.2
  Downloading py-1.11.0-py2.py3-none-any.whl (98 kB)
     |████████████████████████████████| 98 kB 228 kB/s
Collecting zipp>=0.5
  Downloading zipp-3.6.0-py3-none-any.whl (5.3 kB)
Collecting typing-extensions>=3.6.4
  Downloading typing_extensions-4.1.1-py3-none-any.whl (26 kB)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /lustre/home/user/m/milias/.local/lib/python3.6/site-packages (from packaging->pytest) (3.1.4)
Installing collected packages: zipp, typing-extensions, importlib-metadata, tomli, py, pluggy, packaging, iniconfig, attrs, pytest
Successfully installed attrs-22.2.0 importlib-metadata-4.8.3 iniconfig-1.1.1 packaging-21.3 pluggy-1.0.0 py-1.11.0 pytest-7.0.1 tomli-1.2.3 typing-extensions-4.1.1 zipp-3.6.0

milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/.pip install tk
Defaulting to user installation because normal site-packages is not writeable
Collecting tk
  Downloading tk-0.1.0-py3-none-any.whl (3.9 kB)
Installing collected packages: tk
Successfully installed tk-0.1.0



