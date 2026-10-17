#!/usr/bin/env python3
"""
Calculate and plot the AuFl diatomic potential energy curve using a MACE model.
"""

import numpy as np
import matplotlib.pyplot as plt
from ase import Atoms
from mace.calculators import MACECalculator   # <-- corrected import

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------
MODEL_PATH = "/home/milias/.cache/mace/dip/MACE_AuFl_compiled.model"
ELEMENT1 = "Au"
ELEMENT2 = "Fl"
DEVICE   = "cpu"

#R_MIN, R_MAX, N_POINTS = 1.5, 8.0, 100
R_MIN, R_MAX, N_POINTS = 0.5, 5.0, 60

# ------------------------------------------------------------------
# Setup MACE calculator
# ------------------------------------------------------------------
calc = MACECalculator(model_paths=MODEL_PATH, device=DEVICE)  # <-- MACECalculator

# ------------------------------------------------------------------
# Scan the potential
# ------------------------------------------------------------------
distances = np.linspace(R_MIN, R_MAX, N_POINTS)
energies  = np.zeros_like(distances)

for i, r in enumerate(distances):
    atoms = Atoms(ELEMENT1 + ELEMENT2,
                  positions=[[0.0, 0.0, 0.0], [0.0, 0.0, r]])
    atoms.calc = calc
    energies[i] = atoms.get_potential_energy()
    print(f"r = {r:6.3f} Å   E = {energies[i]:12.6f} eV")

# ------------------------------------------------------------------
# Shift and find equilibrium
# ------------------------------------------------------------------
E_min = energies.min()
energies_shifted = energies - E_min
i_min = np.argmin(energies)
r_eq  = distances[i_min]

print(f"\nEquilibrium distance r_eq = {r_eq:.4f} Å")
print(f"Minimum energy (raw)      = {E_min:.6f} eV")

# ------------------------------------------------------------------
# Plot
# ------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(distances, energies_shifted, "-", lw=2, color="navy")
plt.axvline(r_eq, ls="--", color="red", alpha=0.6,
            label=f"$r_{{eq}}$ = {r_eq:.3f} Å")
plt.axhline(0.0, ls=":", color="gray", alpha=0.5)

plt.xlabel("Distance r (Å)", fontsize=12)
plt.ylabel("Energy (eV, shifted)", fontsize=12)
plt.title(f"{ELEMENT1}–{ELEMENT2} diatomic potential (MACE)", fontsize=13)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("AuFl_potential.png", dpi=200)
plt.show()
