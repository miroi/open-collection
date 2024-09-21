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
.
.
Successfully installed ase-ext-20.9.0 cffi-1.17.1 pycparser-2.22


milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/vmXY_hydra/ase-tests/.python3 -m pip install psycopg2-binary
.
.
Successfully installed psycopg2-binary-2.9.9

milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/vmXY_hydra/ase-tests/.python3 -m pip install flask
Defaulting to user installation because normal site-packages is not writeable
.
.

Successfully installed Jinja2-3.1.4 MarkupSafe-2.1.5 Werkzeug-3.0.4 blinker-1.8.2 click-8.1.7 flask-3.0.3 itsdangerous-2.2.0

ase-datafiles
-------------
milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/vmXY_hydra/ase-tests/.pip3 install --user --upgrade git+https://gitlab.com/ase/ase-datafiles.git
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Collecting git+https://gitlab.com/ase/ase-datafiles.git
  Cloning https://gitlab.com/ase/ase-datafiles.git to /tmp/pip-req-build-9_b7cxoh
  Running command git clone --quiet https://gitlab.com/ase/ase-datafiles.git /tmp/pip-req-build-9_b7cxoh
  Resolved https://gitlab.com/ase/ase-datafiles.git to commit 9938478fc4d7c4d4333ee00fab5b9adbef4b3c38
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: ase-datafiles
  Building wheel for ase-datafiles (pyproject.toml) ... done
  Created wheel for ase-datafiles: filename=ase_datafiles-0.1-py3-none-any.whl size=15859526 sha256=50991540cbaf8a7d84ba5978981e0f92ed99a72ee4a3e45560e798ccc0cea1df
  Stored in directory: /tmp/pip-ephem-wheel-cache-9zirfjnv/wheels/a8/7b/36/4bae9bea0601ddbc7995de66280f746ff6b7781c9adfff8d8a
Successfully built ase-datafiles
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Installing collected packages: ase-datafiles
Successfully installed ase-datafiles-0.1
milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/vmXY_hydra/ase-tests/.

