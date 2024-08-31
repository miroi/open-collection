ASE on Mogon(HIM)
=================

mirilias@login23.mogon:~/work/projects/open-collection/theoretical_chemistry/software/.module add  lang/Python/3.10.8-GCCcore-12.2.0

mirilias@login23.mogon:~/work/projects/open-collection/theoretical_chemistry/software/.module list

Currently Loaded Modules:
  1) compiler/GCCcore/12.2.0              3) system/OpenSSL/1.1
  2) devel/SQLite/3.39.4-GCCcore-12.2.0   4) lang/Python/3.10.8-GCCcore-12.2.0

mirilias@login23.mogon:~/work/projects/open-collection/theoretical_chemistry/software/.pip install ase

Installing collected packages: ase
ERROR: Could not install packages due to an OSError: [Errno 122] Disk quota exceeded: '/home/mirilias/.local/lib/python3.10/site-packages/ase/__man__.py'

WARNING: There was an error checking the latest version of pip.
mirilias@login23.mogon:~/work/projects/open-collection/theoretical_chemistry/software/.

Fixed wrt to the disk space:
~~~~~~~~~~~~~~~~~~~~~~~~~~~
mirilias@login23.mogon:~/work/software/.pip install ase
Defaulting to user installation because normal site-packages is not writeable
Collecting ase
  Using cached ase-3.23.0-py3-none-any.whl (2.9 MB)
Requirement already satisfied: matplotlib>=3.3.4 in /gpfs/fs1/home/mirilias/.local/lib/python3.10/site-packages (from ase) (3.9.2)
Requirement already satisfied: numpy>=1.18.5 in /gpfs/fs1/home/mirilias/.local/lib/python3.10/site-packages (from ase) (2.1.0)
Requirement already satisfied: scipy>=1.6.0 in /gpfs/fs1/home/mirilias/.local/lib/python3.10/site-packages (from ase) (1.14.1)
Requirement already satisfied: python-dateutil>=2.7 in /cluster/easybuild/broadwell/software/Python/3.10.8-GCCcore-12.2.0/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (2.8.2)
Requirement already satisfied: kiwisolver>=1.3.1 in /gpfs/fs1/home/mirilias/.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (1.4.5)
Requirement already satisfied: fonttools>=4.22.0 in /gpfs/fs1/home/mirilias/.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (4.53.1)
Requirement already satisfied: packaging>=20.0 in /cluster/easybuild/broadwell/software/Python/3.10.8-GCCcore-12.2.0/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (21.3)
Requirement already satisfied: cycler>=0.10 in /gpfs/fs1/home/mirilias/.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (0.12.1)
Requirement already satisfied: contourpy>=1.0.1 in /gpfs/fs1/home/mirilias/.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (1.3.0)
Requirement already satisfied: pyparsing>=2.3.1 in /cluster/easybuild/broadwell/software/Python/3.10.8-GCCcore-12.2.0/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (3.0.9)
Requirement already satisfied: pillow>=8 in /gpfs/fs1/home/mirilias/.local/lib/python3.10/site-packages (from matplotlib>=3.3.4->ase) (10.4.0)
Requirement already satisfied: six>=1.5 in /cluster/easybuild/broadwell/software/Python/3.10.8-GCCcore-12.2.0/lib/python3.10/site-packages (from python-dateutil>=2.7->matplotlib>=3.3.4->ase) (1.16.0)
Installing collected packages: ase

  WARNING: The scripts pip, pip3 and pip3.10 are installed in '/home/mirilias/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.


mirilias@login23.mogon:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/mogon_him/.which ase
~/.local/bin/ase
mirilias@login23.mogon:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/mogon_him/.ase info

platform                 Linux-4.18.0-348.12.2.el8_5.x86_64-x86_64-with-glibc2.28
python-3.10.8            /cluster/easybuild/broadwell/software/Python/3.10.8-GCCcore-12.2.0/bin/python
ase-3.23.0               /home/mirilias/.local/lib/python3.10/site-packages/ase
numpy-2.1.0              /home/mirilias/.local/lib/python3.10/site-packages/numpy
scipy-1.14.1             /home/mirilias/.local/lib/python3.10/site-packages/scipy
matplotlib-3.9.2         /home/mirilias/.local/lib/python3.10/site-packages/matplotlib
spglib                   not installed
ase_ext                  not installed
flask                    not installed
psycopg2                 not installed
pyamg                    not installed


mirilias@login21.mogon:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/mogon_uni-mainz_de/.module add  lang/Python/3.10.8-GCCcore-12.2.0
mirilias@login21.mogon:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/mogon_uni-mainz_de/.ase --version       ase-3.23.0





