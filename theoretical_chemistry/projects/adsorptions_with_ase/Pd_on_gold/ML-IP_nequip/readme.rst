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



Download and compile a foundation model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nequip-compile \
  nequip.net:mir-group/NequIP-OAM-L:0.1 \
  model.nequip.pth \
  --device cpu \
  --mode torchscript \
  --target ase

