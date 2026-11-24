#!/usr/bin/env python
"""
nh3_orbmol_opt.py
NH3 geometry optimization with orb-models 0.7.x (orbmol_v2) and
comparison with experimental geometry parameters.

Requires:
  - Python 3.12
  - orb-models >= 0.7, < 0.8
"""

import sys
import numpy as np
import torch
from ase.optimize import FIRE
from ase.build import molecule

# ---------- 1. Version check ----------
print("=" * 60)
print("Environment check")
print("=" * 60)
print(f"Python: {sys.version}")

import orb_models
print(f"orb_models: {orb_models.__version__}")

# Accept any 0.7.x; refuse older versions that lack orbmol_v2
try:
    major, minor = (int(x) for x in orb_models.__version__.lstrip("v").split(".")[:2])
except Exception:
    major, minor = 0, 0
if (major, minor) < (0, 7):
    print("✗ orbmol_v2 requires orb-models >= 0.7.0. "
          "Recreate orb_env with Python 3.12 and reinstall.")
    sys.exit(1)

# ---------- 2. Imports specific to 0.7.x ----------
from orb_models.forcefield import pretrained
# 0.7.x location:
from orb_models.forcefield.inference.calculator import ORBCalculator

if not hasattr(pretrained, "orbmol_v2"):
    print("✗ pretrained.orbmol_v2 not found even though version >= 0.7. "
          "Check installation integrity.")
    sys.exit(1)

# ---------- 3. Load model ----------
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"\nLoading orbmol_v2 on device='{device}' ...")
orbff, atoms_adapter = pretrained.orbmol_v2(device=device)

# ---------- 4. Build NH3 ----------
atoms = molecule("NH3")
atoms.info["charge"] = 0   # neutral
atoms.info["spin"] = 1     # singlet (2S+1)
print(f"\nInitial NH3: {len(atoms)} atoms")

def get_params(atoms):
    """Return (N-H lengths [Å], H-N-H angles [°]) as numpy arrays."""
    n_idx = [a.index for a in atoms if a.symbol == "N"][0]
    h_indices = [a.index for a in atoms if a.symbol == "H"]
    n_pos = atoms.positions[n_idx]
    h_positions = [atoms.positions[i] for i in h_indices]

    nh = np.array([np.linalg.norm(hp - n_pos) for hp in h_positions])

    angles = []
    for i in range(3):
        for j in range(i + 1, 3):
            v1 = h_positions[i] - n_pos
            v2 = h_positions[j] - n_pos
            cos_ang = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
            angles.append(np.degrees(np.arccos(np.clip(cos_ang, -1.0, 1.0))))
    return nh, np.array(angles)

nh0, ang0 = get_params(atoms)
print(f"Initial N-H lengths (Å):  {nh0.mean():.4f} ± {nh0.std():.4f}")
print(f"Initial H-N-H angle (°):  {ang0.mean():.2f} ± {ang0.std():.2f}")

# ---------- 5. Optimize ----------
calc = ORBCalculator(orbff, atoms_adapter=atoms_adapter, device=device)
atoms.calc = calc

print("\nRunning FIRE optimization (fmax=0.01 eV/Å) ...")
opt = FIRE(atoms, logfile="-")
opt.run(fmax=0.01, steps=500)

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

nh_err = abs(nh1.mean() - exp_nh)
ang_err = abs(ang1.mean() - exp_angle)
print("\nAssessment:")
print(f"  {'✓' if nh_err < 0.02 else '⚠'} N-H length deviation {nh_err:.4f} Å "
      f"({'within' if nh_err < 0.02 else 'exceeds'} 0.02 Å)")
print(f"  {'✓' if ang_err < 3.0 else '⚠'} H-N-H angle deviation {ang_err:.2f}° "
      f"({'within' if ang_err < 3.0 else 'exceeds'} 3°)")

print("\nDone.")
