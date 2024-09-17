===================
ASE on Window10-WSL 
===================

ase gui problem : https://gitlab.com/ase/ase/-/issues/1511

conda installation
~~~~~~~~~~~~~~~~~~
https://stackoverflow.com/a/75314060/3101910

curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
export PATH=$PATH:/miniconda3/bin

ase installation
~~~~~~~~~~~~~~~~~

conda install --channel conda-forge ase==3.22.1

compare pip and conda installed ase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

milias@pc7321b:~/work/projects/.~/.local/bin/ase info
platform                 Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35
python-3.10.12           /usr/bin/python3
ase-3.23.0               /home/milias/.local/lib/python3.10/site-packages/ase
numpy-2.1.1              /home/milias/.local/lib/python3.10/site-packages/numpy
scipy-1.14.1             /home/milias/.local/lib/python3.10/site-packages/scipy
matplotlib-3.9.2         /home/milias/.local/lib/python3.10/site-packages/matplotlib
spglib                   not installed
ase_ext                  not installed
flask                    not installed
psycopg2                 not installed
pyamg-5.2.1              /home/milias/.local/lib/python3.10/site-packages/pyamg

asap3 via pip
~~~~~~~~~~~~~

for asap3, see https://gitlab.com/asap/asap/-/issues/63

milias@pc7321b:~/work/projects/.ase info
platform                 Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35
python-3.12.2            /home/milias/miniconda3/bin/python3.12
ase-3.22.1               /home/milias/miniconda3/lib/python3.12/site-packages/ase
numpy-1.26.4             /home/milias/miniconda3/lib/python3.12/site-packages/numpy
scipy-1.13.1             /home/milias/miniconda3/lib/python3.12/site-packages/scipy
matplotlib-3.9.2         /home/milias/miniconda3/lib/python3.12/site-packages/matplotlib
spglib                   not installed
ase_ext                  not installed
flask-3.0.3              /home/milias/miniconda3/lib/python3.12/site-packages/flask
psycopg2                 not installed
pyamg                    not installed


