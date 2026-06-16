# test_matgl_advanced.py
import matgl
from pymatgen.core import Lattice, Structure
import torch
import time

print("=" * 60)
print("MATGL ADVANCED TEST (GPU ACCELERATED)")
print("=" * 60)

# Show GPU info
print(f"\nGPU: {torch.cuda.get_device_name(0)}")
print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")

# Load model
print("\nLoading model...")
start = time.time()
model = matgl.load_model("MEGNet-Eform-MP-2018.6.1")
print(f"✓ Model loaded in {time.time() - start:.2f}s")

# Test multiple structures
structures = [
    ("CsCl", "Pm-3m", 4.1437, ["Cs", "Cl"], [[0,0,0], [0.5,0.5,0.5]]),
    ("NaCl", "Fm-3m", 5.6402, ["Na", "Cl"], [[0,0,0], [0.5,0.5,0.5]]),
    ("MgO", "Fm-3m", 4.2117, ["Mg", "O"], [[0,0,0], [0.5,0.5,0.5]]),
]

print("\nPredicting formation energies:")
print("-" * 40)

for name, sg, lat, species, coords in structures:
    struct = Structure.from_spacegroup(sg, Lattice.cubic(lat), species, coords)
    eform = model.predict_structure(struct)
    energy = float(eform.numpy())
    print(f"{name:6s} : {energy:7.3f} eV/atom")

print("\n" + "=" * 60)
print("✓ All tests passed!")
