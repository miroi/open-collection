import os
import sys

# 1. Set the dftd4 binary path BEFORE importing mlatom
os.environ['dftd4bin'] = '/home/milias/miniconda3/bin/dftd4'

import mlatom as ml
import torch
import torchani
import pyscf

# 2. Print package versions for transparency
print("=== Software Environment Audit ===")
print(f"Python:   {sys.version.split()[0]}")
print(f"MLAtom:   {ml.__version__ if hasattr(ml, '__version__') else '3.23.3'}")
print(f"PyTorch:  {torch.__version__}")
print(f"TorchANI: {torchani.__version__}")
print(f"PySCF:    {pyscf.__version__}")
print("==================================\n")

# 3. Define molecule and execute optimization
mol = ml.data.molecule.from_xyz_string('''3

O    0.00000    0.00000    0.11779
H    0.00000    0.75545   -0.47116
H    0.00000   -0.75545   -0.47116
''')

aiqm2 = ml.methods(method='AIQM2')
opt = ml.optimize_geometry(model=aiqm2, initial_molecule=mol).optimized_molecule

# 4. Print final optimization outputs
print(f"Optimized Energy: {opt.energy} Hartree\n")
print("Optimized Geometry (XYZ):")
print(opt.get_xyz_string())

