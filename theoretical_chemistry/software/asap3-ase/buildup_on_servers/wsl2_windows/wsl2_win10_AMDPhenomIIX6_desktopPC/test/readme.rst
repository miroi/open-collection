===========
ASAP3 tests
===========

https://asap3.readthedocs.io/en/latest/installation/Installation.html#testing-the-installation

sudo apt install python3-pytest

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/wsl2_windows/wsl2_win10_AMDPhenomIIX6_desktopPC/test/.pip show asap3
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


error: https://gitlab.com/asap/asap/-/issues/79


simple MD test
--------------
(venv) miroi@MiroPhenomII-X6:~/work/git-projects/collection/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/wsl2_windows/wsl2_win10_AMDPhenomIIX6_desktopPC/test/.python SimpleMD.py > SimpleMD.py_logfile
/home/miroi/work/git-projects/collection/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/wsl2_windows/wsl2_win10_AMDPhenomIIX6_desktopPC/test/SimpleMD.py:25: FutureWarning: Please use atoms.calc = calc
  atoms.set_calculator(EMT())
Using Asap-optimized Verlet algorithm




