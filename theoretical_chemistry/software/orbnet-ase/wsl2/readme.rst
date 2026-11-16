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

# 5. Verify version and orbmol_v2 availability
python -c "import orb_models; print('orb_models:', orb_models.__version__)"
python -c "from orb_models.forcefield import pretrained; print('orbmol_v2 present:', hasattr(pretrained, 'orbmol_v2'))"
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"

test
----



