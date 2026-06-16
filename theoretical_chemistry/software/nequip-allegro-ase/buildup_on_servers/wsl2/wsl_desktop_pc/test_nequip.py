import torch
import numpy as np
from ase.build import bulk
from nequip.integrations.ase import NequIPCalculator

# --- Set up the calculator ---
model_path = "allegro_oam_l.nequip.pt2"
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {device}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")

# Load the compiled model
calculator = NequIPCalculator.from_compiled_model(
    compile_path=model_path,
    device=device,
    chemical_species_to_atom_type_map=True,
)

# --- Set up the structure ---
# Create a cubic diamond silicon structure
atoms = bulk("Si", crystalstructure="diamond", a=5.43, cubic=True)
print(f"Number of atoms: {len(atoms)}")

# Attach calculator and run
atoms.calc = calculator

# Get energy and forces
energy = atoms.get_potential_energy()
forces = atoms.get_forces()

# Print results
print(f"Potential Energy: {energy:.6f} eV")
print(f"Max force component: {np.max(np.abs(forces)):.6f} eV/Å")
print(f"Force array shape: {forces.shape}")

# Optional: Show a few force components
print("\nFirst few force components (eV/Å):")
for i in range(min(3, len(atoms))):
    print(f"Atom {i}: {forces[i]}")
