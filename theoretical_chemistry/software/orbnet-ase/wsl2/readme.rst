=====================
OrbNet-ASE under WSL2
=====================

https://github.com/orbital-materials/orb-models


install in own conda environment
--------------------------------

conda create -n orb_env python=3.12 -y

conda activate orb_env
python -m pip install --upgrade pip
python -m pip install "orb-models>=0.7,<0.8"

#  Verify version and orbmol_v2 availability
python -c "import orb_models; print('orb_models:', orb_models.__version__)"
python -c "from orb_models.forcefield import pretrained; print('orbmol_v2 present:', hasattr(pretrained, 'orbmol_v2'))"
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"

orb_models: v0.7.0
/home/miroi/miniconda3/envs/orb_env/lib/python3.12/site-packages/torch/jit/_script.py:1491: FutureWarning: `torch.jit.script` is deprecated. Please switch to `torch.compile` or `torch.export`.
  warnings.warn(
Warp 1.19.0 initialized:
   CUDA Toolkit 13.4, Driver 13.3
   Devices:
     "cpu"      : "x86_64"
     "cuda:0"   : "NVIDIA GeForce RTX 3050 Laptop GPU" (4 GiB, sm_86, mempool enabled)
   Kernel cache:
     /home/miroi/.cache/warp/1.19.0
orbmol_v2 present: True
CUDA available: True

test
----



