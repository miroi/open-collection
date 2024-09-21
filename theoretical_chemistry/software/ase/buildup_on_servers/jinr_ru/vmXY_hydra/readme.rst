ASE on vm01/vm01
================

milias@vm01.hydra.local:~/.pip install --upgrade ase
Defaulting to user installation because normal site-packages is not writeable

 WARNING: The script ase is installed in '/lustre/home/user/m/milias/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed ase-3.23.0

ilias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/vm01-vm02_hydra/.ase info 
platform                 Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.17
python-3.10.13           /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/bin/python3.10
ase-3.23.0               /lustre/home/user/m/milias/.local/lib/python3.10/site-packages/ase
numpy-1.26.4             /lustre/home/user/m/milias/.local/lib/python3.10/site-packages/numpy
scipy-1.12.0             /lustre/home/user/m/milias/.local/lib/python3.10/site-packages/scipy
matplotlib-3.8.3         /lustre/home/user/m/milias/.local/lib/python3.10/site-packages/matplotlib
spglib                   not installed
ase_ext                  not installed
flask                    not installed
psycopg2                 not installed
pyamg                    not installed

milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/vmXY_hydra/.pip list
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Package         Version
--------------- -----------
asap3           3.13.4
ase             3.23.0
.
.


ase-ext
-------
milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/vmXY_hydra/ase-tests/.python3 -m pip install ase-ext
Defaulting to user installation because normal site-packages is not writeable
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Collecting ase-ext
  Downloading ase-ext-20.9.0.tar.gz (21 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting cffi (from ase-ext)
  Downloading cffi-1.17.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.5 kB)
Collecting pycparser (from cffi->ase-ext)
  Downloading pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Downloading cffi-1.17.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (446 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 446.2/446.2 kB 864.7 kB/s eta 0:00:00
Downloading pycparser-2.22-py3-none-any.whl (117 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.6/117.6 kB 291.2 kB/s eta 0:00:00
Building wheels for collected packages: ase-ext
  Building wheel for ase-ext (pyproject.toml) ... done
  Created wheel for ase-ext: filename=ase_ext-20.9.0-cp310-cp310-linux_x86_64.whl size=34464 sha256=9c7a710f161dfbe2c9af38495634b6085e562b1cd1938b2d0b3fbd48602c22c3
  Stored in directory: /lustre/home/user/m/milias/.cache/pip/wheels/af/93/f6/4599e51d9db9e168e8c4065c7211d3b2d5595f270cf9a26959
Successfully built ase-ext
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Installing collected packages: pycparser, cffi, ase-ext
Successfully installed ase-ext-20.9.0 cffi-1.17.1 pycparser-2.22


milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/vmXY_hydra/ase-tests/.python3 -m pip install psycopg2-binary
Defaulting to user installation because normal site-packages is not writeable
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Collecting psycopg2-binary
  Downloading psycopg2_binary-2.9.9-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.4 kB)
Downloading psycopg2_binary-2.9.9-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 4.5 MB/s eta 0:00:00
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Installing collected packages: psycopg2-binary
Successfully installed psycopg2-binary-2.9.9

milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/vmXY_hydra/ase-tests/.python3 -m pip install flask
Defaulting to user installation because normal site-packages is not writeable
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Collecting flask
  Using cached flask-3.0.3-py3-none-any.whl.metadata (3.2 kB)
Collecting Werkzeug>=3.0.0 (from flask)
  Downloading werkzeug-3.0.4-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from flask)
  Downloading jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.1.2 (from flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from flask)
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting blinker>=1.6.2 (from flask)
  Downloading blinker-1.8.2-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->flask)
  Downloading MarkupSafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)
Downloading flask-3.0.3-py3-none-any.whl (101 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.7/101.7 kB 186.7 kB/s eta 0:00:00
Downloading blinker-1.8.2-py3-none-any.whl (9.5 kB)
Downloading click-8.1.7-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 195.2 kB/s eta 0:00:00
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.4-py3-none-any.whl (133 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.3/133.3 kB 460.7 kB/s eta 0:00:00
Downloading werkzeug-3.0.4-py3-none-any.whl (227 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 227.6/227.6 kB 498.3 kB/s eta 0:00:00
Downloading MarkupSafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, flask
Successfully installed Jinja2-3.1.4 MarkupSafe-2.1.5 Werkzeug-3.0.4 blinker-1.8.2 click-8.1.7 flask-3.0.3 itsdangerous-2.2.0


