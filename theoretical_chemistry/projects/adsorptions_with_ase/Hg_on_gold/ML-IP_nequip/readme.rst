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


wget https://developer.download.nvidia.com/compute/cuda/12.4.0/local_installers/cuda_12.4.0_550.54.14_linux.run
sudo sh cuda_12.4.0_550.54.14_linux.run
nvcc --version

export CUDA_HOME=/usr/local/cuda-12.4
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH


Download and compile a foundation model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nequip-compile \
  nequip.net:mir-group/NequIP-OAM-L:0.1 \
  model.nequip.pt2 \
  --device cuda \
  --mode aotinductor \
  --target ase

