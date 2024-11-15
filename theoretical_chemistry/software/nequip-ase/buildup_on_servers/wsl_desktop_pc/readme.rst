=======
NequIP 
=======

Euclidian Equivariant neural network potentials. 

Nequip can fit neural network potentials to series of DFT calculations (using e.g. ASE trajectory files),
 and then be used to perform optimization and molecular dynamics in ASE or LAMMPS.

https://github.com/mir-group/nequip


paper
https://www.nature.com/articles/s41467-022-29939-5


installation
------------

torch
~~~~~
pip install torch==1.13.*   

scikit-learn
~~~~~~~~~~~~
pip install scikit-learn


nequip from github
~~~~~~~~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/.git clone https://github.com/mir-group/nequip.git
cd nequip
pip install . 

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/nequip-ase/buildup_on_servers/wsl_desktop_pc/.pip list | grep nequip
nequip                        0.6.1

testing
-------
milias@DESKTOP-7OTLCGO:~/work/software/nequip/.nohup pytest tests/unit/  &

see  tests_nohup.logfile 

