==========================
LibXC on Aphroditu cluster
==========================

https://libxc.gitlab.io/

download & unpack
-----------------
ru26mi1@front01:~/work/software/libcx/.wget https://gitlab.com/libxc/libxc/-/archive/7.1.2/libxc-7.1.2.tar.bz2

ru26mi1@front01:~/work/software/libcx/.tar -xvf libxc-7.1.2.tar.bz2

add pip modules to python
~~~~~~~~~~~~~~~~~~~~~~~~~
module list python

Currently Loaded Modules Matching: python
  1) Python/3.13.5-GCCcore-14.3.0

which python; python -V
/eb/software/Python/3.13.5-GCCcore-14.3.0/bin/python
Python 3.13.5

pip install pytest --user
pip install numpy  --user

buildup
-------
sbatch aphroditi_libxc_buildup_intel.01

check
-----
ru26mi1@front01:~/work/software/libcx/install_build_intel/.ls
bin/  include/  lib64/
ru26mi1@front01:~/work/software/libcx/install_build_intel/.ls bin/
xc-info*

