#!/bin/bash
# Setup MACE with Python 3.11

echo "Setting up MACE environment with Python 3.11..."

# Create environment
conda create -n mace_working python=3.11 -y

# Activate
source $(conda info --base)/etc/profile.d/conda.sh
conda activate mace_working

# Install packages
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install ase e3nn mace-torch numpy scipy matplotlib tqdm

# Verify
python -c "import mace_torch; print('✓ MACE version:', mace_torch.__version__)"
python -c "from ase.calculators.mace import MACECalculator; print('✓ MACE calculator available')"
python -c "import torch; print('✓ PyTorch CUDA:', torch.cuda.is_available())"

echo "✓ MACE environment 'mace_working' is ready!"
echo "Activate with: conda activate mace_working"
