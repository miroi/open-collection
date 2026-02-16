from ase.build import molecule
from ase import Atoms
from ase.collections import g2
from ase.visualize import view

# Get a list of names from the g2 database
molecule_names = g2.names
#print(f"Available molecules in g2: {len(molecule_names)} - {molecule_names}")

# Create a water molecule object
water = molecule('H2O')
print(f"Created molecule: {water}")

# Visualize the molecule
view(water)

