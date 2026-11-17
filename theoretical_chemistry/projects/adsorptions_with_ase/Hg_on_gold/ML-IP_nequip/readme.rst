===========================
Hg@Au(111) with Nequip MLIP
===========================

installation into own conda environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MUST BE OWN PYTHON ENVIRONMENT TO AVOID CONFLICTS !!!

conda create -n nequip_env python=3.11 -y
conda activate nequip_env

# CPU-only PyTorch (skip the --index-url line if you want the default build)
pip install torch --index-url https://download.pytorch.org/whl/cpu

pip install nequip ase

gpu
~~~
pip install torch --index-url https://download.pytorch.org/whl/cu124 --force-reinstall 




Download and compile a foundation model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

