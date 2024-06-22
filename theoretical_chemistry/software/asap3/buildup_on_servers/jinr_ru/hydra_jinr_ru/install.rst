Asap3 installation
===================

numpy
-----
milias@hydra.jinr.ru:~/.pip install --upgrade --user  numpy
.
Successfully installed numpy-1.26.4

pip
----
milias@hydra.jinr.ru:~/.python3.10 -m pip install --upgrade pip
.
Successfully installed pip-24.0

milias@hydra.jinr.ru:~/.pip --version
pip 24.0 from /lustre/home/user/m/milias/.local/lib/python3.10/site-packages/pip (python 3.10)


python
------
milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3/servers/hydra_jinr_ru/.python -V
Python 3.10.2


asap3
-----
milias@hydra.jinr.ru:~/.pip install --upgrade --user  asap3
.

https://gitlab.com/asap/asap/-/issues/57

milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3/servers/hydra_jinr_ru/.pip install --upgrade --user  asap3
Collecting asap3
  Downloading asap3-3.13.4.tar.gz (849 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 849.9/849.9 kB 1.6 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Collecting ase>=3.22.1 (from asap3)
  Downloading ase-3.22.1-py3-none-any.whl.metadata (3.1 kB)
Collecting matplotlib>=3.1.0 (from ase>=3.22.1->asap3)
  Downloading matplotlib-3.8.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
Requirement already satisfied: numpy>=1.15.0 in /lustre/home/user/m/milias/.local/lib/python3.10/site-packages (from ase>=3.22.1->asap3) (1.26.4)
Collecting scipy>=1.1.0 (from ase>=3.22.1->asap3)
  Downloading scipy-1.12.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.4/60.4 kB 140.7 kB/s eta 0:00:00
Collecting contourpy>=1.0.1 (from matplotlib>=3.1.0->ase>=3.22.1->asap3)
  Downloading contourpy-1.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
Collecting cycler>=0.10 (from matplotlib>=3.1.0->ase>=3.22.1->asap3)
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib>=3.1.0->ase>=3.22.1->asap3)
  Downloading fonttools-4.50.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (159 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 159.4/159.4 kB 394.4 kB/s eta 0:00:00
Collecting kiwisolver>=1.3.1 (from matplotlib>=3.1.0->ase>=3.22.1->asap3)
  Downloading kiwisolver-1.4.5-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl.metadata (6.4 kB)
Collecting packaging>=20.0 (from matplotlib>=3.1.0->ase>=3.22.1->asap3)
  Downloading packaging-24.0-py3-none-any.whl.metadata (3.2 kB)
Collecting pillow>=8 (from matplotlib>=3.1.0->ase>=3.22.1->asap3)
  Downloading pillow-10.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.2 kB)
Collecting pyparsing>=2.3.1 (from matplotlib>=3.1.0->ase>=3.22.1->asap3)
  Downloading pyparsing-3.1.2-py3-none-any.whl.metadata (5.1 kB)
Collecting python-dateutil>=2.7 (from matplotlib>=3.1.0->ase>=3.22.1->asap3)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Requirement already satisfied: six>=1.5 in /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.2/lib/python3.10/site-packages (from python-dateutil>=2.7->matplotlib>=3.1.0->ase>=3.22.1->asap3) (1.16.0)
Downloading ase-3.22.1-py3-none-any.whl (2.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 5.2 MB/s eta 0:00:00
Downloading matplotlib-3.8.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 15.7 MB/s eta 0:00:00
Downloading scipy-1.12.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (38.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 38.4/38.4 MB 13.3 MB/s eta 0:00:00
Downloading contourpy-1.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (310 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 310.7/310.7 kB 926.8 kB/s eta 0:00:00
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.50.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 10.6 MB/s eta 0:00:00
Downloading kiwisolver-1.4.5-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 4.0 MB/s eta 0:00:00
Downloading packaging-24.0-py3-none-any.whl (53 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.5/53.5 kB 126.6 kB/s eta 0:00:00
Downloading pillow-10.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 8.7 MB/s eta 0:00:00
Downloading pyparsing-3.1.2-py3-none-any.whl (103 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.2/103.2 kB 268.0 kB/s eta 0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 670.4 kB/s eta 0:00:00
Building wheels for collected packages: asap3
  Building wheel for asap3 (pyproject.toml) ... done
  Created wheel for asap3: filename=asap3-3.13.4-cp310-cp310-linux_x86_64.whl size=3886888 sha256=a81602955625beaf9847b9e346f762ca4585723364c3dbe791cc99fbd0c21f10
  Stored in directory: /lustre/home/user/m/milias/.cache/pip/wheels/b3/ed/d6/84236570928d1e712d01e2b9d6e88afac78c21dc126a547bec
Successfully built asap3
Installing collected packages: scipy, python-dateutil, pyparsing, pillow, packaging, kiwisolver, fonttools, cycler, contourpy, matplotlib, ase, asap3

Successfully installed asap3-3.13.4 ase-3.22.1 contourpy-1.2.0 cycler-0.12.1 fonttools-4.50.0 kiwisolver-1.4.5 matplotlib-3.8.3 packaging-24.0 pillow-10.3.0 pyparsing-3.1.2 python-dateutil-2.9.0.post0 scipy-1.12.0
milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3/servers/hydra_jinr_ru/.




