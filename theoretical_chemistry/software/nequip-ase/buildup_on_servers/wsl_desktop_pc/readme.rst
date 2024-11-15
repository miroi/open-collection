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

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/nequip-ase/runs/minimal/.nequip-train -h
/home/milias/.local/lib/python3.10/site-packages/nequip/__init__.py:20: UserWarning: !! PyTorch version 1.13.1 found. Upstream issues in PyTorch versions 1.13.* and 2.* have been seen to cause unusual performance degredations on some CUDA systems that become worse over time; see https://github.com/mir-group/nequip/discussions/311. The best tested PyTorch version to use with CUDA devices is 1.11; while using other versions if you observe this problem, an unexpected lack of this problem, or other strange behavior, please post in the linked GitHub issue.
  warnings.warn(
usage: nequip-train [-h] [--equivariance-test [EQUIVARIANCE_TEST]] [--model-debug-mode] [--grad-anomaly-mode] [--gpu-oom-offload] [--log LOG]
                    [--warn-unused]
                    config

pip uninstall torch

pip install torch==1.11.*
pip show torch

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

