import numpy as np
from ase import Atoms
from quippy.potential import Potential

# 1. Create a simple Silicon dimer structure using ASE (Atomic Number 14)
# Silicon is the native element mapped to the default Stillinger-Weber potential.
distance = 2.4
atoms = Atoms(
    symbols="SiSi", 
    positions=[[0.0, 0.0, 0.0], [0.0, 0.0, distance]], 
    pbc=False
)

try:
    # 2. Use the standard, pre-installed Stillinger-Weber label.
    # Passing 'IP SW' tells QUIP to use its internal silicon descriptor repository.
    calc = Potential(init_args="IP SW")
    atoms.calc = calc

    # 3. Calculate properties
    energy = atoms.get_potential_energy()
    forces = atoms.get_forces()

    # 4. Print results to verify success
    print("\n--- QUIP / ASE Integration Successful ---")
    print(f"Total Potential Energy: {energy:.4f} eV")
    print("\nForces on each atom (eV/A):")
    for i, force in enumerate(forces):
        print(f" Atom {i} ({atoms.symbols[i]}): {force}")

except Exception as e:
    print("\n--- QUIP / ASE Test Failed ---")
    import traceback
    traceback.print_exc()

