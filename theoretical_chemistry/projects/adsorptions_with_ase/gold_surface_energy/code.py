import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# 1. Setup Bulk System
# Au FCC lattice constant is ~4.08 Angstroms
a = 4.08
bulk_atom = fcc111('Au', a=a, size=(1, 1, 1), vacuum=0.0)
bulk_atom.calc = EMT()
# Calculate bulk energy per atom
e_bulk = bulk_atom.get_potential_energy()

# 2. Setup Surface Slab
# Create a 4-layer 111 surface with 10 Angstrom vacuum
slab = fcc111('Au', a=a, size=(3, 3, 4), vacuum=10.0)
slab.calc = EMT()

# Fix bottom two layers to simulate bulk, allowing surface relaxation
c = FixAtoms(indices=[atom.index for atom in slab if atom.position[2] < np.mean(slab.positions[:, 2])])
slab.set_constraint(c)

# 3. Relax the surface structure
dyn = BFGS(slab, trajectory='au111.traj', logfile='au111.log')
dyn.run(fmax=0.05)

# 4. Calculate Surface Energy
# Formula: sigma = (E_slab - n*E_bulk) / (2 * Area)
# n is the number of atoms in the slab, 2 is for two surfaces (top+bottom)
e_slab = slab.get_potential_energy()
num_atoms = len(slab)
area = slab.get_cell()[0, 0] * slab.get_cell()[1, 1] # For 111 rectangular cell

# Note: Area calculation might differ based on unit cell setup
# Correct approach using cross product for area of parallelogram:
# a1 = slab.cell[0, :2]
# a2 = slab.cell[1, :2]
# area = np.linalg.norm(np.cross(a1, a2))

surface_energy = (e_slab - (num_atoms * e_bulk)) / (2 * area)

print(f"Bulk energy per atom: {e_bulk:.4f} eV")
print(f"Slab energy: {e_slab:.4f} eV")
print(f"Number of atoms: {num_atoms}")
print(f"Surface Area: {area:.2f} Angstrom^2")
print(f"Gold (111) Surface Energy: {surface_energy:.4f} eV/Angstrom^2")

