import numpy as np
from ase import Atoms
from quippy.potential import Potential

# 1. Create a simple Silicon dimer structure using ASE
# Two Si atoms placed 2.4 Angstroms apart along the Z-axis
distance = 2.4
atoms = Atoms(
    symbols="SiSi", 
    positions=[[0, 0, 0], [0, 0, distance]], 
    pbc=False
)

try:
    # 2. Initialize a baseline QUIP potential
    # Note: 'IP SW' initializes a standard Stillinger-Weber potential included in QUIP
    # For a real machine learning potential, you would pass your GAP xml file here instead
    calc = Potential(args="IP SW", param_filename="softpot.xml")
    atoms.calc = calc

    # 3. Calculate properties
    energy = atoms.get_potential_energy()
    forces = atoms.get_forces()

    # 4. Print results to verify success
    print("--- QUIP / ASE Integration Successful ---")
    print(f"Total Potential Energy: {energy:.4f} eV")
    print("\nForces on each atom (eV/A):")
    for i, force in enumerate(forces):
        print(f" Atom {i} ({atoms.symbols[i]}): {force}")

except Exception as e:
    print("--- QUIP / ASE Test Failed ---")
    print(f"Error encountered: {e}")

