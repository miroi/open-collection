from ase import Atoms
from dftd4.ase import DFTD4
import numpy as np

# 1. Create the H2 molecule in ASE (Positions in Angstrom by default)
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 1.0]])

# 2. Attach the DFTD4 calculator
# You can specify the functional (method) here
calc = DFTD4(method="PBE")
h2.calc = calc

# 3. Get the energy (returned in eV by ASE convention)
energy_ev = h2.get_potential_energy()

# 4. Convert to Hartree (Eh) for comparison with your previous test
from ase.units import Hartree
energy_hartree = energy_ev / Hartree

print(f"Dispersion energy (ASE) : {energy_ev:.10f} eV")
print(f"Dispersion energy (ASE) : {energy_hartree:.10f} Eh")

# 5. You can also easily get forces
forces = h2.get_forces()
print("\nForces (eV/A):")
print(forces)

