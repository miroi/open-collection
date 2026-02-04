====================================
ASE on Windows10-WSL Notevook Victus
====================================

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/servers/windows10_wsl$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.4 LTS
Release:        22.04
Codename:       jammy

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/servers/windows10_wsl$ pip install --upgrade git+https://gitlab.com/ase/ase.git@master
Defaulting to user installation because normal site-packages is not writeable
Collecting git+https://gitlab.com/ase/ase.git@master
  Cloning https://gitlab.com/ase/ase.git (to revision master) to /tmp/pip-req-build-xijkmo49
  Running command git clone --filter=blob:none --quiet https://gitlab.com/ase/ase.git /tmp/pip-req-build-xijkmo49
  Resolved https://gitlab.com/ase/ase.git to commit a4b1986e2596e53216e56c36368ba15659fa4e50
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: UNKNOWN
  Building wheel for UNKNOWN (pyproject.toml) ... done
  Created wheel for UNKNOWN: filename=UNKNOWN-0.0.0-py3-none-any.whl size=18091 sha256=9e2fd56b732554fcbbef040a2dbe612dda77b35e4f5beee6f532c0313da6b954
  Stored in directory: /tmp/pip-ephem-wheel-cache-ek6uelk9/wheels/01/fc/60/e6134958a4ba6921161034c849be512a068712df0013719724
Successfully built UNKNOWN
Installing collected packages: UNKNOWN
Successfully installed UNKNOWN-0.0.0

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/servers/windows10_wsl$ ase --version
ase-3.22.1
milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/servers/windows10_wsl$ ase info
platform                 Linux-5.15.146.1-microsoft-standard-WSL2-x86_64-with-glibc2.35
python-3.10.12           /usr/bin/python3
ase-3.22.1               /home/milias/.local/lib/python3.10/site-packages/ase
numpy-1.26.4             /home/milias/.local/lib/python3.10/site-packages/numpy
scipy-1.13.0             /home/milias/.local/lib/python3.10/site-packages/scipy
matplotlib-3.9.0         /home/milias/.local/lib/python3.10/site-packages/matplotlib
spglib-2.4.0             /home/milias/.local/lib/python3.10/site-packages/spglib
ase_ext-20.9.0           /home/milias/.local/lib/python3.10/site-packages/ase_ext
flask-3.0.3              /home/milias/.local/lib/python3.10/site-packages/flask
psycopg2                 not installed
pyamg-5.1.0              /home/milias/.local/lib/python3.10/site-packages/pyamg



