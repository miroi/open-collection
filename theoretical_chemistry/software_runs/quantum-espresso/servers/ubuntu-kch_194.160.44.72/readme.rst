Quantum Espresso on @194.160.44.72 (ubuntu-kch)
===============================================

Find version
------------
milias@194.160.44.72:~/work/projects/open-collection/theoretical_chemistry/software_runs/quantum-espresso/servers/ubuntu-kch_194.160.44.72/.apt-cache madison quantum-espresso

quantum-espresso | 6.4.1-1build2 | http://archive.ubuntu.com/ubuntu focal/universe amd64 Packages


installed package QE 6.4.1

pw.x

Find all package files
----------------------

sudo apt-file update
sudo apt-file list quantum-espresso  > quantum-espresso.ubuntu_files
sudo apt-file list quantum-espresso-data  >>  quantum-espresso.ubuntu_files

see
quantum-espresso: /usr/bin/*.x
quantum-espresso-data: /usr/share/doc/quantum-espresso
quantum-espresso-data: /usr/share/espresso/

