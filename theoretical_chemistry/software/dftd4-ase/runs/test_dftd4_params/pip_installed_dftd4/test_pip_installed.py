#!/usr/bin/env python3

from ase import Atoms
from dftd4.ase import DFTD4
import numpy as np

# Create NaCl crystal structure
atoms = Atoms(
    symbols=['Na']*4 + ['Cl']*4,
    positions=[ # positions in Angstrom
        [0.000000000000000, 0.000000000000000, 0.000000000000000],
        [2.810000000000000, 0.000000000000000, 2.810000000000000],
        [2.810000000000000, 2.810000000000000, 2.810000000000000],
        [0.000000000000000, 2.810000000000000, 0.000000000000000],
        [2.810000000000000, 2.810000000000000, 0.000000000000000],
        [0.000000000000000, 2.810000000000000, 2.810000000000000],
        [0.000000000000000, 0.000000000000000, 2.810000000000000],
        [2.810000000000000, 0.000000000000000, 0.000000000000000]
    ],
    cell=[ # cell in Angstrom
        [5.620000000000000, 0.000000000000000, 0.000000000000000],
        [0.000000000000000, 5.620000000000000, 0.000000000000000],
        [0.000000000000000, 0.000000000000000, 5.620000000000000]
    ],
    pbc=[True, True, True]
)

# Test different s8 factors to weaken D4 interaction
print("Testing DFT-D4 with different s8 factors on NaCl crystal:")
print("=" * 60)

for s8_factor in [1.0, 0.8, 0.6, 0.4, 0.2, 0.0]:
    # Create DFT-D4 calculator with custom damping parameters
    calc = DFTD4(
        method="pbe",  # or use None for default parameters
        s8=s8_factor,  # This weakens the interaction!
        s6=1.0,        # Keep s6 at 1.0
        a1=0.4,        # Default parameters
        a2=5.0,        # Default parameters
    )
    
    # Set calculator and calculate
    atoms.calc = calc
    energy = atoms.get_potential_energy()
    forces = atoms.get_forces()
    
    print(f"s8 = {s8_factor:4.1f}:")
    print(f"  Energy = {energy:12.6f} eV")
    print(f"  Max force = {np.max(np.abs(forces)):8.6f} eV/Å")
    print(f"  Mean force = {np.mean(np.abs(forces)):8.6f} eV/Å")
    print()

print("=" * 60)
print("Note: Lower s8 values result in weaker dispersion interaction")
print("s8 = 1.0: Full strength D4 dispersion")
print("s8 = 0.0: No D4 dispersion (only s6 term)")
