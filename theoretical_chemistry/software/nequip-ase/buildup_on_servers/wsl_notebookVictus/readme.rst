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
cuda
~~~~
nvcc -V

torch
~~~~~
pip install torch==1.11.*
pip show torch

NOTE: needs up-to-date version of torch for notebook's gfx card CUDA !!!

scikit-learn
~~~~~~~~~~~~
pip install scikit-learn
pip show scikit-learn

nequip from github
~~~~~~~~~~~~~~~~~~
miroi@MIRO:~/work/software/.git clone https://github.com/mir-group/nequip.git 

cd nequip
miroi@MIRO:~/work/software/nequip/.pip install .

pip list | grep nequip
nequip                        0.6.1

testing
-------
miroi@MIRO:~/work/software/nequip/.nohup pytest tests/unit/  &
tail -f nohup.out

individual tests 
miroi@MIRO:~/work/software/nequip/.pytest tests/unit/model/test_nequip_model.py


see tests_nohup.logfile 


