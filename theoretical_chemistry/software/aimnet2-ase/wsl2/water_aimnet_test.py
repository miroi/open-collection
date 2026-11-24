from ase.build import molecule
from aimnet.calculators import AIMNet2ASE

# Create a water molecule
atoms = molecule("H2O")

# Attach AIMNet2 calculator
atoms.calc = AIMNet2ASE("aimnet2")

# Calculate energy and forces
energy = atoms.get_potential_energy()
forces = atoms.get_forces()

print(f"Energy: {energy} eV")
print(f"Forces: {forces}")
