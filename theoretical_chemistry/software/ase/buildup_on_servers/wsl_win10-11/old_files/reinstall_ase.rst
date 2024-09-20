=============
Reinstall ase
=============

https://gitlab.com/ase/ase/-/issues/1511#note_2093088892

milias@pc7321b:~/.pip install --force-reinstall ase==3.22.1
Defaulting to user installation because normal site-packages is not writeable
Collecting ase==3.22.1
  Downloading ase-3.22.1-py3-none-any.whl.metadata (3.1 kB)
Collecting matplotlib>=3.1.0 (from ase==3.22.1)
  Downloading matplotlib-3.9.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
Collecting numpy>=1.15.0 (from ase==3.22.1)
  Downloading numpy-2.1.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
Collecting scipy>=1.1.0 (from ase==3.22.1)
  Downloading scipy-1.14.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
Collecting contourpy>=1.0.1 (from matplotlib>=3.1.0->ase==3.22.1)
  Downloading contourpy-1.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.4 kB)
Collecting cycler>=0.10 (from matplotlib>=3.1.0->ase==3.22.1)
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib>=3.1.0->ase==3.22.1)
  Downloading fonttools-4.53.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (162 kB)
Collecting kiwisolver>=1.3.1 (from matplotlib>=3.1.0->ase==3.22.1)
  Downloading kiwisolver-1.4.7-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl.metadata (6.3 kB)
Collecting packaging>=20.0 (from matplotlib>=3.1.0->ase==3.22.1)
  Downloading packaging-24.1-py3-none-any.whl.metadata (3.2 kB)
Collecting pillow>=8 (from matplotlib>=3.1.0->ase==3.22.1)
  Downloading pillow-10.4.0-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (9.2 kB)
Collecting pyparsing>=2.3.1 (from matplotlib>=3.1.0->ase==3.22.1)
  Downloading pyparsing-3.1.4-py3-none-any.whl.metadata (5.1 kB)
Collecting python-dateutil>=2.7 (from matplotlib>=3.1.0->ase==3.22.1)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.7->matplotlib>=3.1.0->ase==3.22.1)
  Downloading six-1.16.0-py2.py3-none-any.whl.metadata (1.8 kB)
Downloading ase-3.22.1-py3-none-any.whl (2.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 4.1 MB/s eta 0:00:00
Downloading matplotlib-3.9.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (8.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 776.4 kB/s eta 0:00:00
Downloading numpy-2.1.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.3/16.3 MB 743.5 kB/s eta 0:00:00
Downloading scipy-1.14.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (41.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.2/41.2 MB 755.9 kB/s eta 0:00:00
Downloading contourpy-1.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (322 kB)
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.53.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 711.1 kB/s eta 0:00:00
Downloading kiwisolver-1.4.7-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 819.7 kB/s eta 0:00:00
Downloading packaging-24.1-py3-none-any.whl (53 kB)
Downloading pillow-10.4.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 1.1 MB/s eta 0:00:00
Downloading pyparsing-3.1.4-py3-none-any.whl (104 kB)
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, pyparsing, pillow, packaging, numpy, kiwisolver, fonttools, cycler, scipy, python-dateutil, contourpy, matplotlib, ase
  Attempting uninstall: pillow
    Found existing installation: pillow 10.3.0
    Uninstalling pillow-10.3.0:
      Successfully uninstalled pillow-10.3.0
  Attempting uninstall: packaging
    Found existing installation: packaging 24.0
    Uninstalling packaging-24.0:
      Successfully uninstalled packaging-24.0
  Attempting uninstall: numpy
    Found existing installation: numpy 1.26.4
    Uninstalling numpy-1.26.4:
      Successfully uninstalled numpy-1.26.4
  Attempting uninstall: kiwisolver
    Found existing installation: kiwisolver 1.4.5
    Uninstalling kiwisolver-1.4.5:
      Successfully uninstalled kiwisolver-1.4.5
  Attempting uninstall: fonttools
    Found existing installation: fonttools 4.52.4
    Uninstalling fonttools-4.52.4:
      Successfully uninstalled fonttools-4.52.4
  Attempting uninstall: cycler
    Found existing installation: cycler 0.12.1
    Uninstalling cycler-0.12.1:
      Successfully uninstalled cycler-0.12.1
  Attempting uninstall: scipy
    Found existing installation: scipy 1.13.1
    Uninstalling scipy-1.13.1:
      Successfully uninstalled scipy-1.13.1
  Attempting uninstall: python-dateutil
    Found existing installation: python-dateutil 2.9.0.post0
    Uninstalling python-dateutil-2.9.0.post0:
      Successfully uninstalled python-dateutil-2.9.0.post0
  Attempting uninstall: contourpy
    Found existing installation: contourpy 1.2.1
    Uninstalling contourpy-1.2.1:
      Successfully uninstalled contourpy-1.2.1
  Attempting uninstall: matplotlib
    Found existing installation: matplotlib 3.9.0
    Uninstalling matplotlib-3.9.0:
      Successfully uninstalled matplotlib-3.9.0
  Attempting uninstall: ase
    Found existing installation: ase 3.23.0
    Uninstalling ase-3.23.0:
      Successfully uninstalled ase-3.23.0
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
gpaw 24.6.0 requires ase>=3.23.0, but you have ase 3.22.1 which is incompatible.
gpaw 24.6.0 requires numpy<2, but you have numpy 2.1.1 which is incompatible.
ovito 3.10.6.post2 requires numpy<2,>=1.20, but you have numpy 2.1.1 which is incompatible.
Successfully installed ase-3.22.1 contourpy-1.3.0 cycler-0.12.1 fonttools-4.53.1 kiwisolver-1.4.7 matplotlib-3.9.2 numpy-2.1.1 packaging-24.1 pillow-10.4.0 pyparsing-3.1.4 python-dateutil-2.9.0.post0 scipy-1.14.1 six-1.16.0
milias@pc7321b:~/.


