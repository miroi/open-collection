#
#
#
import numpy as np
from ase.build import molecule
from ase.calculators.mixing import SumCalculator
from dftd4.ase import DFTD4

# 1. Initialize a molecule geometry
atoms = molecule('H2O')

# 2. Attach the DFT-D4 calculator (specifying the functional mapping)
# The calculator evaluates standalone dispersion or mixes with QM engines
d4_calc = DFTD4(method="PBE")
atoms.calc = d4_calc

# 3. Compute dispersion energy and gradients (forces)
disp_energy = atoms.get_potential_energy()
disp_forces = atoms.get_forces()

print(f"DFT-D4 Dispersion Energy: {disp_energy:.6f} eV")
print(f"DFT-D4 Dispersion Forces:\n{disp_forces}")

