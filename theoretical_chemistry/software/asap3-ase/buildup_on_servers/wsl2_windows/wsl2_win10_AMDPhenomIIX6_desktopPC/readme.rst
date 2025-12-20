======================================
ASAP3-ASE on Windows10 AMD PhenomII X6
======================================

Python venv
~~~~~~~~~~~
@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/wsl2_windows/wsl2_win10_AMDPhenomIIX6_desktopPC/.source ~/software/venv/bin/activate

installation
~~~~~~~~~~~~
https://asap3.readthedocs.io/en/latest/installation/Installation.html#simple-installation

sudo apt-get install  libscalapack-openmpi-dev openmpi-common libmkl-blacs-openmpi-ilp64 libmkl-blacs-openmpi-lp64  build-essential linux-generic libmpich-dev libopenmpi-dev

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/wsl2_windows/wsl2_win10_AMDPhenomIIX6_desktopPC/.pip install --upgrade  asap3
.
.
.
Successfully built asap3
Installing collected packages: asap3
Successfully installed asap3-3.13.10
(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/wsl2_windows/wsl2_win10_AMDPhenomIIX6_desktopPC/.

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/wsl2_windows/wsl2_win10_AMDPhenomIIX6_desktopPC/.pip show asap3 ase
Name: asap3
Version: 3.13.10
Summary: ASAP - classical potentials for MD with ASE.
Home-page:
Author:
Author-email:
License:
Location: /home/miroi/software/venv/lib/python3.12/site-packages
Requires: ase, numpy
Required-by:

Name: ase
Version: 3.26.0
Summary: Atomic Simulation Environment
Home-page:
Author:
Author-email:
License:
Location: /home/miroi/software/venv/lib/python3.12/site-packages
Requires: matplotlib, numpy, scipy
Required-by: asap3, chgnet

