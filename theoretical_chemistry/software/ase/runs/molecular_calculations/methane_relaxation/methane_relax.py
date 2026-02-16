# from Google AI, modified by MI
#

from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 1. Create a molecule (Methane)
atoms = molecule('CH4')

# 2. Set a calculator (Effective Medium Theory - fast for simple systems)
atoms.calc = EMT()

# 3. Optimize the geometry
print(f"Initial energy: {atoms.get_total_energy():.4f} eV")
dyn = BFGS(atoms)
dyn.run(fmax=0.05)  # Optimize until forces are small

# 4. Final results
print(f"Final energy: {atoms.get_total_energy():.4f} eV")
print("Optimization complete.")

