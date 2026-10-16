#!/usr/bin/env python3
"""
Calculate the adsorption energy of a Fl atom on Au(111) at the hcp site
using a MACE model. Saves optimization trajectories.

The isolated Fl reference energy E_fl is taken from a Quantum ESPRESSO
calculation of the free Fl atom.
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
DEVICE     = "cpu"          # change to "cuda" if available
FMAX       = 0.05           # eV/Å convergence criterion
STEPS      = 200

# Au(111) slab parameters
AU_A       = 4.078          # Au lattice constant (Å)
SIZE       = (4, 4, 4)      # 4x4 surface cell, 4 layers
VACUUM     = 15.0           # Å

# Adsorbate initial position
ADS_HEIGHT = 2.5            # initial height above surface (Å)

# Reference energy for the isolated Fl atom (Quantum ESPRESSO)
E_FL_QE    = -5240.211831   # eV

# ------------------------------------------------------------------
# Setup MACE calculator
# ------------------------------------------------------------------
calc = MACECalculator(model_paths=MODEL_PATH, device=DEVICE)

# ------------------------------------------------------------------
# 1. Build and optimize the clean Au(111) slab
# ------------------------------------------------------------------
print("=" * 60)
print("Optimizing clean Au(111) slab...")
print("=" * 60)

slab = fcc111('Au', size=SIZE, a=AU_A, vacuum=VACUUM)

# Fix the bottom two layers
z = slab.positions[:, 2]
mask = z < z.min() + 1.5
slab.set_constraint(FixAtoms(mask=mask))
slab.calc = calc

opt_slab = BFGS(slab, trajectory='clean_slab.traj', logfile='clean_slab.log')
opt_slab.run(fmax=FMAX, steps=STEPS)

E_slab = slab.get_potential_energy()
print(f"Clean slab energy: {E_slab:.6f} eV")

# ------------------------------------------------------------------
# 2. Isolated Fl reference energy (from Quantum ESPRESSO)
# ------------------------------------------------------------------
E_fl = E_FL_QE
print("\n" + "=" * 60)
print("Isolated Fl reference energy (QE):")
print("=" * 60)
print(f"E(Fl) = {E_fl:.6f} eV")

# ------------------------------------------------------------------
# 3. Add Fl to hcp site and optimize
# ------------------------------------------------------------------
print("\n" + "=" * 60)
print("Optimizing Fl on Au(111) hcp site...")
print("=" * 60)

slab_ads = slab.copy()
add_adsorbate(slab_ads, 'Fl', height=ADS_HEIGHT, position='hcp')

# Re-apply constraint (adsorbate is free, bottom Au layers fixed)
z = slab_ads.positions[:, 2]
mask = z < z.min() + 1.5
slab_ads.set_constraint(FixAtoms(mask=mask))
slab_ads.calc = calc

opt_ads = BFGS(slab_ads, trajectory='fl_on_au111_hcp.traj',
               logfile='fl_on_au111_hcp.log')
opt_ads.run(fmax=FMAX, steps=STEPS)

E_total = slab_ads.get_potential_energy()
print(f"Total energy (slab + Fl): {E_total:.6f} eV")

# ------------------------------------------------------------------
# 4. Compute adsorption energy
# ------------------------------------------------------------------
E_ads = E_total - E_slab - E_fl

print("\n" + "=" * 60)
print("ADSORPTION ENERGY")
print("=" * 60)
print(f"E(slab+Fl)       = {E_total:.6f} eV")
print(f"E(slab)          = {E_slab:.6f} eV")
print(f"E(Fl, QE)        = {E_fl:.6f} eV")
print(f"E_ads            = {E_ads:.6f} eV")
print("=" * 60)

# ------------------------------------------------------------------
# 5. Save final structures (strip problematic info dicts)
# ------------------------------------------------------------------
slab_ads.info.pop('adsorbate_info', None)
slab.info.pop('adsorbate_info', None)

write('clean_slab_final.xyz', slab)
write('fl_on_au111_hcp_final.xyz', slab_ads)

# Save the optimized adsorbate geometry details
fl_pos = slab_ads.positions[-1]
au_surface_z = slab_ads.positions[:-1, 2].max()
print(f"\nFl position (x, y, z) = {fl_pos[0]:.4f}, {fl_pos[1]:.4f}, {fl_pos[2]:.4f}")
print(f"Fl height above surface = {fl_pos[2] - au_surface_z:.4f} Å")

# ------------------------------------------------------------------
# 6. Report trajectory information
# ------------------------------------------------------------------
print("\nTrajectory files saved:")
print("  clean_slab.traj        - clean slab optimization")
print("  fl_on_au111_hcp.traj   - Fl adsorption optimization")
print("\nTo visualize:  ase gui fl_on_au111_hcp.traj")
