=====================
ASE on theor.jinr.ru
=====================

milias@theor.jinr.ru:~/work/projects/.pip3 install ase
Collecting ase
  Downloading ase-3.22.1-py3-none-any.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 1.4 MB/s
Requirement already satisfied: numpy>=1.15.0 in /usr/lib/python3/dist-packages (from ase) (1.19.5)
Collecting matplotlib>=3.1.0
  Downloading matplotlib-3.9.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (8.3 MB)
     |████████████████████████████████| 8.3 MB 2.8 MB/s
Requirement already satisfied: scipy>=1.1.0 in /usr/lib/python3/dist-packages (from ase) (1.6.0)
Collecting pyparsing>=2.3.1
  Downloading pyparsing-3.1.2-py3-none-any.whl (103 kB)
     |████████████████████████████████| 103 kB 50.1 MB/s
Collecting numpy>=1.15.0
  Downloading numpy-1.26.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.2 MB)
     |████████████████████████████████| 18.2 MB 1.6 MB/s
Collecting contourpy>=1.0.1
  Downloading contourpy-1.2.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (304 kB)
     |████████████████████████████████| 304 kB 1.7 MB/s
Collecting packaging>=20.0
  Downloading packaging-24.0-py3-none-any.whl (53 kB)
     |████████████████████████████████| 53 kB 190 kB/s
Collecting importlib-resources>=3.2.0
  Downloading importlib_resources-6.4.0-py3-none-any.whl (38 kB)
Collecting fonttools>=4.22.0
  Downloading fonttools-4.51.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
     |████████████████████████████████| 4.6 MB 1.6 MB/s
Requirement already satisfied: pillow>=8 in /usr/lib/python3/dist-packages (from matplotlib>=3.1.0->ase) (8.1.2)
Collecting kiwisolver>=1.3.1
  Downloading kiwisolver-1.4.5-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
     |████████████████████████████████| 1.6 MB 1.4 MB/s
Collecting python-dateutil>=2.7
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
     |████████████████████████████████| 229 kB 2.0 MB/s
Collecting cycler>=0.10
  Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Collecting zipp>=3.1.0
  Downloading zipp-3.18.2-py3-none-any.whl (8.3 kB)
Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.7->matplotlib>=3.1.0->ase) (1.16.0)
Installing collected packages: zipp, numpy, python-dateutil, pyparsing, packaging, kiwisolver, importlib-resources, fonttools, cycler, contourpy, matplotlib, ase
  WARNING: The script f2py is installed in '/home/ltph/milias/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts fonttools, pyftmerge, pyftsubset and ttx are installed in '/home/ltph/milias/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts ase, ase-build, ase-db, ase-gui, ase-info and ase-run are installed in '/home/ltph/milias/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed ase-3.22.1 contourpy-1.2.1 cycler-0.12.1 fonttools-4.51.0 importlib-resources-6.4.0 kiwisolver-1.4.5 matplotlib-3.9.0 numpy-1.26.4 packaging-24.0 pyparsing-3.1.2 python-dateutil-2.9.0.post0 zipp-3.18.2


milias@theor.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/ase/servers/jinr_ru/theor_jinr_ru/.pip3 install pytest
Collecting pytest
  Downloading pytest-8.2.1-py3-none-any.whl (339 kB)
     |████████████████████████████████| 339 kB 1.3 MB/s
Collecting tomli>=1
  Downloading tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting pluggy<2.0,>=1.5
  Downloading pluggy-1.5.0-py3-none-any.whl (20 kB)
Collecting iniconfig
  Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
Requirement already satisfied: packaging in /home/ltph/milias/.local/lib/python3.9/site-packages (from pytest) (24.0)
Collecting exceptiongroup>=1.0.0rc8
  Downloading exceptiongroup-1.2.1-py3-none-any.whl (16 kB)
Installing collected packages: tomli, pluggy, iniconfig, exceptiongroup, pytest
Successfully installed exceptiongroup-1.2.1 iniconfig-2.0.0 pluggy-1.5.0 pytest-8.2.1 tomli-2.0.1

milias@theor.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/ase/servers/jinr_ru/theor_jinr_ru/.pip3 install tk
Collecting tk
  Downloading tk-0.1.0-py3-none-any.whl (3.9 kB)
Installing collected packages: tk
Successfully installed tk-0.1.0

