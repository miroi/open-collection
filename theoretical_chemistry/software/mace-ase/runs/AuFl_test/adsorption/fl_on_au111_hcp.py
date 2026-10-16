#!/usr/bin/env python3
"""
Adsorption of Fl on Au(111) hcp site using a MACE model.

Includes extensive diagnostics:
  - Prints MACE's internal per-element reference energies.
  - Prints forces on Fl before/after optimization.
  - Runs a rigid (unrelaxed) E vs. height scan to test whether the
    model produces any Au-Fl interaction.
  - Reports both MACE and QE isolated-Fl reference energies.

Saves trajectories of both optimizations.
"""

import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.io import write
from mace.calculators import MACECalculator

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------
MODEL_PATH = "/home/milias/.cache/mace/dip/MACE_AuFl_compiled.model"
DEVICE     = "cpu"
FMAX       = 0.05           # eV/Å
STEPS      = 200

AU_A       = 4.078          # Au lattice constant (Å)
SIZE       = (4, 4, 4)      # 4x4 surface cell, 4 layers
VACUUM     = 15.0           # Å

ADS_HEIGHT = 2.5            # initial height of Fl above surface (Å)

# QE reference for the isolated Fl atom
E_FL_QE    = -5240.211831   # eV

# ------------------------------------------------------------------
# Setup MACE calculator
# ------------------------------------------------------------------
print("=" * 70)
print("Loading MACE model")
print("=" * 70)
calc = MACECalculator(model_paths=MODEL_PATH, device=DEVICE)

# ------------------------------------------------------------------
# Inspect the model's internal per-element reference energies
# ------------------------------------------------------------------
print("\n" + "=" * 70)
print("MACE model internal atomic reference energies")
print("=" * 70)
try:
    import torch
    model = torch.load(MODEL_PATH, map_location="cpu")
    # MACE stores these under different attribute names in different versions.
    ref_fn = getattr(model, "atomic_energies_fn", None)
    if ref_fn is not None and hasattr(ref_fn, "atomic_energies"):
        print("atomic_energies_fn.atomic_energies:")
        print(ref_fn.atomic_energies)
    elif hasattr(model, "atomic_energies"):
        print("model.atomic_energies:")
        print(model.atomic_energies)
    else:
        print("Could not locate atomic_energies in the model object.")
        print("Model attributes:", [a for a in dir(model) if "energ" in a.lower()])
    # Also print the element order if available
    if hasattr(model, "atomic_numbers"):
        print("atomic_numbers:", model.atomic_numbers)
except Exception as e:
    print(f"Could not inspect model internals: {e}")

# ------------------------------------------------------------------
# Helper: strip non-standard info/arrays so XYZ writer works
# ------------------------------------------------------------------
def clean_atoms(atoms):
    a = atoms.copy()
    a.info = {}
    for key in list(a.arrays.keys()):
        if key not in ('numbers', 'positions'):
            del a.arrays[key]
    return a

# ------------------------------------------------------------------
# 1. Clean Au(111) slab
# ------------------------------------------------------------------
print("\n" + "=" * 70)
print("Optimizing clean Au(111) slab...")
print("=" * 70)

slab = fcc111('Au', size=SIZE, a=AU_A, vacuum=VACUUM)
z = slab.positions[:, 2]
mask = z < z.min() + 1.5
slab.set_constraint(FixAtoms(mask=mask))
slab.calc = calc

opt_slab = BFGS(slab, trajectory='clean_slab.traj', logfile='clean_slab.log')
opt_slab.run(fmax=FMAX, steps=STEPS)

E_slab = slab.get_potential_energy()
print(f"Clean slab energy: {E_slab:.6f} eV")
print(f"  steps taken: {opt_slab.get_number_of_steps()}")

# ------------------------------------------------------------------
# 2a. Isolated Fl energy — MACE (for comparison)
# ------------------------------------------------------------------
print("\n" + "=" * 70)
print("Isolated Fl atom energy (MACE, in 20 Å box)")
print("=" * 70)
fl_box = Atoms('Fl', positions=[[0.0, 0.0, 0.0]])
fl_box.center(vacuum=10.0)
fl_box.calc = calc
E_fl_mace = fl_box.get_potential_energy()
print(f"E(Fl, MACE)  = {E_fl_mace:.6f} eV")

# ------------------------------------------------------------------
# 2b. Isolated Fl energy — QE (reference)
# ------------------------------------------------------------------
E_fl = E_FL_QE
print("\n" + "=" * 70)
print("Isolated Fl atom energy (QE reference)")
print("=" * 70)
print(f"E(Fl, QE)    = {E_fl:.6f} eV")
print(f"Difference E(Fl,MACE) - E(Fl,QE) = {E_fl_mace - E_fl:+.6f} eV")

# ------------------------------------------------------------------
# 3. Fl on hcp site: build, inspect forces, then optimize
# ------------------------------------------------------------------
print("\n" + "=" * 70)
print("Fl on Au(111) hcp site")
print("=" * 70)

slab_ads = slab.copy()
add_adsorbate(slab_ads, 'Fl', height=ADS_HEIGHT, position='hcp')

z = slab_ads.positions[:, 2]
mask = z < z.min() + 1.5
slab_ads.set_constraint(FixAtoms(mask=mask))
slab_ads.calc = calc

# --- forces BEFORE optimization -----------------------------------
print("\nForces BEFORE optimization:")
forces_before = slab_ads.get_forces()
fl_force_before = forces_before[-1]
print(f"  |F(Fl)|  = {np.linalg.norm(fl_force_before):.6f} eV/Å")
print(f"  F(Fl)    = {fl_force_before}")
print(f"  max|F| over all atoms = {np.linalg.norm(forces_before, axis=1).max():.6f} eV/Å")

# Fl height before
fl_z_before = slab_ads.positions[-1, 2]
au_top_z = slab_ads.positions[:-1, 2].max()
print(f"  Fl height before opt = {fl_z_before - au_top_z:.4f} Å")

E_before = slab_ads.get_potential_energy()
print(f"  E(slab+Fl, before opt) = {E_before:.6f} eV")

# --- optimize ------------------------------------------------------
opt_ads = BFGS(slab_ads, trajectory='fl_on_au111_hcp.traj',
               logfile='fl_on_au111_hcp.log')
opt_ads.run(fmax=FMAX, steps=STEPS)

E_total = slab_ads.get_potential_energy()

# --- forces AFTER optimization ------------------------------------
print("\nForces AFTER optimization:")
forces_after = slab_ads.get_forces()
fl_force_after = forces_after[-1]
print(f"  |F(Fl)|  = {np.linalg.norm(fl_force_after):.6f} eV/Å")
print(f"  F(Fl)    = {fl_force_after}")
print(f"  max|F| over all atoms = {np.linalg.norm(forces_after, axis=1).max():.6f} eV/Å")
print(f"  steps taken: {opt_ads.get_number_of_steps()}")

fl_z_after = slab_ads.positions[-1, 2]
print(f"  Fl height after opt = {fl_z_after - au_top_z:.4f} Å")
print(f"  Fl moved in z: {fl_z_after - fl_z_before:+.4f} Å")
print(f"E(slab+Fl, after opt) = {E_total:.6f} eV")

# ------------------------------------------------------------------
# 4a. Adsorption energy using QE Fl reference
# ------------------------------------------------------------------
E_ads_qe = E_total - E_slab - E_fl
# ------------------------------------------------------------------
# 4b. Adsorption energy using MACE Fl reference
# ------------------------------------------------------------------
E_ads_mace = E_total - E_slab - E_fl_mace

print("\n" + "=" * 70)
print("ADSORPTION ENERGY")
print("=" * 70)
print(f"  E(slab+Fl)      = {E_total:.6f} eV")
print(f"  E(slab)         = {E_slab:.6f} eV")
print(f"  E(Fl, QE)       = {E_fl:.6f} eV")
print(f"  E(Fl, MACE)     = {E_fl_mace:.6f} eV")
print(f"  ------------------------------------------")
print(f"  E_ads (QE ref)   = {E_ads_qe:.6f} eV")
print(f"  E_ads (MACE ref) = {E_ads_mace:.6f} eV")
print("=" * 70)

# ------------------------------------------------------------------
# 5. Rigid E vs. height scan (NO relaxation) — key diagnostic
# ------------------------------------------------------------------
print("\n" + "=" * 70)
print("Rigid E vs. Fl height scan (unrelaxed, hcp site)")
print("=" * 70)

# We use the clean slab (fixed bottom two layers) as a base
heights = np.arange(1.6, 5.01, 0.2)
scan_energies = []

# Reference for the scan: interaction energy relative to far-away Fl
for h in heights:
    tmp = slab.copy()
    add_adsorbate(tmp, 'Fl', height=float(h), position='hcp')
    z = tmp.positions[:, 2]
    m = z < z.min() + 1.5
    tmp.set_constraint(FixAtoms(mask=m))
    tmp.calc = calc
    e = tmp.get_potential_energy()
    scan_energies.append(e)
    print(f"  h = {h:5.2f} Å   E = {e:14.6f} eV")

scan_energies = np.array(scan_energies)
# Interaction energy relative to the largest separation
E_ref_far = scan_energies[-1]
E_int = scan_energies - E_ref_far

print("\nInteraction energy relative to largest separation:")
print(f"  (reference E at h = {heights[-1]:.2f} Å = {E_ref_far:.6f} eV)")
for h, e in zip(heights, E_int):
    print(f"  h = {h:5.2f} Å   E_int = {e*1000:10.3f} meV")

# Simple plot
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.figure(figsize=(7, 4.5))
    plt.plot(heights, E_int * 1000.0, "o-")
    plt.xlabel("Fl height above Au(111) (Å)")
    plt.ylabel("Interaction energy (meV)")
    plt.title("Au(111)–Fl rigid scan (hcp site, MACE)")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("Au111_Fl_hcp_scan.png", dpi=200)
    print("\nSaved scan plot to Au111_Fl_hcp_scan.png")
except Exception as e:
    print(f"Could not save plot: {e}")

# ------------------------------------------------------------------
# 6. Save final structures
# ------------------------------------------------------------------
write('clean_slab_final.xyz',      clean_atoms(slab))
write('fl_on_au111_hcp_final.xyz', clean_atoms(slab_ads))
write('clean_slab_final.traj',      slab)
write('fl_on_au111_hcp_final.traj', slab_ads)

print("\nFiles written:")
print("  clean_slab.traj / clean_slab.log")
print("  fl_on_au111_hcp.traj / fl_on_au111_hcp.log")
print("  clean_slab_final.xyz / .traj")
print("  fl_on_au111_hcp_final.xyz / .traj")
print("  Au111_Fl_hcp_scan.png")
print("\nVisualize:  ase gui fl_on_au111_hcp.traj")
