# quick_check.py
import matgl
import numpy as np
import torch
from importlib.metadata import version

print(f"matgl: {matgl.__version__}")
print(f"pymatgen: {version('pymatgen')}")
print(f"numpy: {np.__version__}")
print(f"torch: {torch.__version__}")

# Optional: Show CUDA availability
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA device: {torch.cuda.get_device_name(0)}")

# Test if model loads
model = matgl.load_model("MEGNet-Eform-MP-2018.6.1")
print("✓ Model loaded successfully")
