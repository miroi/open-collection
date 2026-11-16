#!/usr/bin/env python
"""
nh3_orbmol_opt.py
NH3 geometry optimization with orb-models (orbmol_v2) and comparison
with experimental geometry parameters.

Requirements:
  - Python >= 3.12 (orb-models >= 0.6.0 requirement)
  - orb-models >= 0.7.0 (provides orbmol_v2)
  - ASE
"""

import sys
import numpy as np
import torch
from ase import Atoms
from ase.optimize import FIRE
from ase.build import molecule

# ---------- 1. Version check ----------
print("=" * 60)
print("Environment check")
print("=" * 60)
print(f"Python: {sys.version}")

import orb_models
print(f"orb_models: {orb_models.__version__}")
if not hasattr(orb_models, "__version__") or orb_models.__version__ < "0.7":
    print("⚠ Warning: orbmol_v2 requires orb-models >= 0.7.0")

from orb_models.forcefield import pretrained
from orb_models.forcefield.calculator import ORBCalculator

# Confirm orbmol_v2 available
if not hasattr(pretrained, "orbmol_v2"):
    print("✗ pretrained.orbmol_v2 not found. Please upgrade orb-models "
          "in a Python >= 3.12 environment.")
    sys.exit(1)

# ---------- 2. Load model ----------
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"\nLoading orbmol_v2 on device='{device}' ...")
orbff, atoms_adapter = pretrained.orbmol_v2(device=device)

# ---------- 3. Build NH3 ----------
atoms = molecule("NH3")
atoms.info["charge"] = 0
atoms.info["spin"] = 1
print(f"\nInitial NH3: {len(atoms)} atoms")

# Initial geometry before optimization (for reference)
def get_params(atoms):
    """Extract N-H bond length and H-N-H angle."""
    n_idx = [a.index for a in atoms if a.symbol == "N"][0]
    h_indices = [a.index for a in atoms if a.symbol == "H"]

    n_pos = atoms.positions[n_idx]
    h_positions = [atoms.positions[i] for i in h_indices]

    # N-H bond lengths (three)
    nh_dists = [np.linalg.norm(hp - n_pos) for hp in h_positions]

    # H-N-H angles (three pairs)
    angles = []
    for i in range(3):
        for j in range(i + 1, 3):
            v1 = h_positions[i] - n_pos
            v2 = h_positions[j] - n_pos
            cos_ang = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
            cos_ang = np.clip(cos_ang, -1.0, 1.0)
            angles.append(np.degrees(np.arccos(cos_ang)))

    return np.array(nh_dists), np.array(angles)

nh0, ang0 = get_params(atoms)
print(f"Initial N-H lengths (Å):  {nh0.mean():.4f} ± {nh0.std():.4f}")
print(f"Initial H-N-H angle (°):  {ang0.mean():.2f} ± {ang0.std():.2f}")

# ---------- 4. Attach calculator and optimize ----------
calc = ORBCalculator(orbff, atoms_adapter=atoms_adapter, device=device)
atoms.calc = calc

print("\nRunning FIRE optimization (fmax=0.01 eV/Å) ...")
opt = FIRE(atoms, logfile="-")
opt.run(fmax=0.01, steps=500)

# ---------- 5. Extract optimized parameters ----------
nh1, ang1 = get_params(atoms)
energy = atoms.get_potential_energy()

print("\n" + "=" * 60)
print("Optimized geometry")
print("=" * 60)
print(f"Final energy: {energy:.6f} eV")
print(f"N-H lengths (Å):  {nh1.mean():.4f} ± {nh1.std():.4f}")
print(f"H-N-H angle (°):  {ang1.mean():.2f} ± {ang1.std():.2f}")

# ---------- 6. Compare with experiment ----------
exp_nh = 1.019    # Å
exp_angle = 109.1 # degrees

print("\n" + "=" * 60)
print("Comparison with experiment (gas-phase NH3)")
print("=" * 60)
print(f"{'Parameter':<18} {'MLIP':>10} {'Experiment':>12} {'Δ':>10}")
print("-" * 52)
print(f"{'N-H length (Å)':<18} {nh1.mean():>10.4f} {exp_nh:>12.4f} "
      f"{nh1.mean()-exp_nh:>+10.4f}")
print(f"{'H-N-H angle (°)':<18} {ang1.mean():>10.2f} {exp_angle:>12.1f} "
      f"{ang1.mean()-exp_angle:>+10.2f}")

# Assess deviation
nh_err = abs(nh1.mean() - exp_nh)
ang_err = abs(ang1.mean() - exp_angle)
print("\nAssessment:")
if nh_err < 0.02:
    print(f"  ✓ N-H length within 0.02 Å of experiment")
else:
    print(f"  ⚠ N-H length deviation {nh_err:.3f} Å exceeds 0.02 Å")
if ang_err < 3.0:
    print(f"  ✓ H-N-H angle within 3° of experiment")
else:
    print(f"  ⚠ H-N-H angle deviation {ang_err:.1f}° exceeds 3°")

print("\nDone.")
