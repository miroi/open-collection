from ase.build import molecule
from ase import Atoms
from ase.collections import g2
from ase.visualize import view

# Get a list of names from the g2 database
molecule_names = g2.names
print(f"Available molecules in g2: {len(molecule_names)} - {molecule_names}")

# Create a water molecule object
water = molecule('H2O')
print(f"Created molecule: {water}")

# Accessing experimental atomization energy for a molecule (requires ase.data.g2)
from ase.data.g2 import get_atomization_energy
h2o_energy = get_atomization_energy('H2O')
print(f"Experimental atomization energy of H2O: {h2o_energy} eV")

ch3oh_energy = get_atomization_energy('CH3OH')
print(f"Experimental atomization energy of CH3OH: {ch3oh_energy} eV")

