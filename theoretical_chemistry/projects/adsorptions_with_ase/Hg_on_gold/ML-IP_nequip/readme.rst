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


(nequip_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/Hg_on_gold/ML-IP_nequip/.export LIBRARY_PATH=/usr/lib/wsl/lib:$LIBRARY_PATH
(nequip_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/Hg_on_gold/ML-IP_nequip/.nequip-compile \
  ~/.nequip/model_cache/039e5620e6c89fd53bdd3b6bd33574e5b29704bb4df5bc339869baca3d5eead6.nequip.zip \
  model.nequip.pt2 \
  --device cuda \
  --mode aotinductor \
  --target ase

[2026-11-17 12:24:30,121][nequip.scripts.compile][INFO] - [rank: 0] Exported model saved to model.nequip.pt2
(nequip_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/adsorptions_with_ase/Hg_on_gold/ML-IP_nequip/.ls -lh model.nequip.pt2
-rw-r--r-- 1 miroi miroi 43M Nov 17 12:24 model.nequip.pt2
