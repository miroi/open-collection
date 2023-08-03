ASE
===

see https://asap3.readthedocs.io/en/latest/installation/Installation.html#simple-installation

Module
~~~~~~~
module load Python/3.9.5-GCCcore-10.3.0


python3 -m pip install --upgrade --user ase
.
.
.
  WARNING: The scripts f2py, f2py3 and f2py3.9 are installed in '/home/milias/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts fonttools, pyftmerge, pyftsubset and ttx are installed in '/home/milias/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts ase, ase-build, ase-db, ase-gui, ase-info and ase-run are installed in '/home/milias/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed ase-3.22.1 contourpy-1.1.0 cycler-0.11.0 fonttools-4.41.1 importlib-resources-6.0.0 kiwisolver-1.4.4 matplotlib-3.7.2 numpy-1.25.1 pillow-10.0.0 scipy-1.11.1
WARNING: You are using pip version 21.1.1; however, version 23.2.1 is available.
You should consider upgrading via the '/storage-apps/easybuild/software/Python/3.9.5-GCCcore-10.3.0/bin/python3 -m pip install --upgrade pip' command.

milias@login02.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/ace-molecule/.pip3 --versionpip 23.2.1 from /home/milias/.local/lib/python3.9/site-packages/pip (python 3.9)


ls /home/milias/.local/bin/
ase*        ase-db*   ase-info*  f2py*   f2py3.6*  fonttools*  pip3*     pip3.9*     pyftsubset*
ase-build*  ase-gui*  ase-run*   f2py3*  f2py3.9*  pip*        pip3.11*  pyftmerge*  ttx*


ase-info
~~~~~~~~
milias@login01.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/servers/devana_nscc_sk/.module load Python/3.9.5-GCCcore-10.3.0
milias@login01.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/servers/devana_nscc_sk/.ase-info    Please use "ase info" instead of "ase-info"
platform                 Linux-3.10.0-1160.71.1.el7.x86_64-x86_64-with-glibc2.17
python-3.9.5             /storage-apps/easybuild/software/Python/3.9.5-GCCcore-10.3.0/bin/python3
ase-3.22.1               /home/milias/.local/lib/python3.9/site-packages/ase
numpy-1.25.1             /home/milias/.local/lib/python3.9/site-packages/numpy
scipy-1.11.1             /home/milias/.local/lib/python3.9/site-packages/scipy
matplotlib-3.7.2         /home/milias/.local/lib/python3.9/site-packages/matplotlib
spglib                   not installed
ase_ext                  not installed
flask                    not installed
psycopg2                 not installed
pyamg                    not installed


asap
~~~~
https://asap3.readthedocs.io/en/latest/installation/Installation.html#simple-installation

pip install --upgrade --user ase asap3
Requirement already satisfied: ase in /home/milias/.local/lib/python3.9/site-packages (3.22.1)
Collecting asap3
  Downloading asap3-3.13.1.tar.gz (857 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 857.4/857.4 kB 16.8 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Requirement already satisfied: matplotlib>=3.1.0 in /home/milias/.local/lib/python3.9/site-packages (from ase) (3.7.2)
Requirement already satisfied: numpy>=1.15.0 in /home/milias/.local/lib/python3.9/site-packages (from ase) (1.25.1)
Requirement already satisfied: scipy>=1.1.0 in /home/milias/.local/lib/python3.9/site-packages (from ase) (1.11.1)
Requirement already satisfied: contourpy>=1.0.1 in /home/milias/.local/lib/python3.9/site-packages (from matplotlib>=3.1.0->ase) (1.1.0)
Requirement already satisfied: cycler>=0.10 in /home/milias/.local/lib/python3.9/site-packages (from matplotlib>=3.1.0->ase) (0.11.0)
Requirement already satisfied: fonttools>=4.22.0 in /home/milias/.local/lib/python3.9/site-packages (from matplotlib>=3.1.0->ase) (4.41.1)
Requirement already satisfied: kiwisolver>=1.0.1 in /home/milias/.local/lib/python3.9/site-packages (from matplotlib>=3.1.0->ase) (1.4.4)
Requirement already satisfied: packaging>=20.0 in /storage-apps/easybuild/software/Python/3.9.5-GCCcore-10.3.0/lib/python3.9/site-packages (from matplotlib>=3.1.0->ase) (20.9)
Requirement already satisfied: pillow>=6.2.0 in /home/milias/.local/lib/python3.9/site-packages (from matplotlib>=3.1.0->ase) (10.0.0)
Requirement already satisfied: pyparsing<3.1,>=2.3.1 in /storage-apps/easybuild/software/Python/3.9.5-GCCcore-10.3.0/lib/python3.9/site-packages (from matplotlib>=3.1.0->ase) (2.4.7)
Requirement already satisfied: python-dateutil>=2.7 in /storage-apps/easybuild/software/Python/3.9.5-GCCcore-10.3.0/lib/python3.9/site-packages (from matplotlib>=3.1.0->ase) (2.8.1)
Requirement already satisfied: importlib-resources>=3.2.0 in /home/milias/.local/lib/python3.9/site-packages (from matplotlib>=3.1.0->ase) (6.0.0)
Requirement already satisfied: zipp>=3.1.0 in /storage-apps/easybuild/software/Python/3.9.5-GCCcore-10.3.0/lib/python3.9/site-packages (from importlib-resources>=3.2.0->matplotlib>=3.1.0->ase) (3.4.1)
Requirement already satisfied: six>=1.5 in /storage-apps/easybuild/software/Python/3.9.5-GCCcore-10.3.0/lib/python3.9/site-packages (from python-dateutil>=2.7->matplotlib>=3.1.0->ase) (1.16.0)
Building wheels for collected packages: asap3
  Building wheel for asap3 (setup.py) ... done
  Created wheel for asap3: filename=asap3-3.13.1-cp39-cp39-linux_x86_64.whl size=4276379 sha256=89df9de05a510272971f9e3ecb337f299c08c7a7994e1be6f00c351028a9c7de
  Stored in directory: /home/milias/.cache/pip/wheels/12/4e/95/3ebb1c67ec2b3b9770f0deafd618612ce68951fae2773b75cf
Successfully built asap3
Installing collected packages: asap3
Successfully installed asap3-3.13.1

tk
~~
milias@login01.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/diatomics_on_metalsolid_ase_emt_bfgs/.python3 -m pip install --upgrade --user tk
Collecting tk
  Downloading tk-0.1.0-py3-none-any.whl (3.9 kB)
Installing collected packages: tk
Successfully installed tk-0.1.0

gulp
~~~~
pip install --upgrade --user ase gulp
Requirement already satisfied: ase in /home/milias/.local/lib/python3.9/site-packages (3.22.1)
Collecting gulp
  Downloading gulp-0.1.0.tar.gz (11 kB)
Installing collected packages: gulp
Successfully installed gulp-0.1.0

gpaw
~~~~
pip install --upgrade --user ase gpaw
ERROR: Failed building wheel for gpaw
ERROR: Could not build wheels for gpaw, which is required to install pyproject.toml-based projects



