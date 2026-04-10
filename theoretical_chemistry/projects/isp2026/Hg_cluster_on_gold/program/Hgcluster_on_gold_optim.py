import os
from ase.build import fcc111, add_adsorbate
from ase.cluster import Icosahedron
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from chgnet.model.dynamics import CHGNetCalculator

# 1. Substrate: Au(111) 4x4 surface with 3 layers
# Vacuum of 10A prevents interaction with periodic images in Z
slab = fcc111('Au', size=(4, 4, 3), vacuum=10.0)

# 2. Cluster: Hg13 Icosahedron
# FIX: Manual latticeconstant=3.0 is REQUIRED for Hg because it is rhombohedral
hg13 = Icosahedron('Hg', noshells=2, latticeconstant=3.0)

# 3. Geometry: Place cluster on the surface
# height=2.5 A is a reasonable initial guess for adsorption
add_adsorbate(slab, hg13, height=2.5, position='fcc')

# 4. Constraints: Fix bottom 2 layers of the Gold slab
# This prevents the whole slab from drifting during optimization
mask = [atom.tag < 3 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# 5. Calculator: Use CHGNet (Machine Learning Universal Potential)
print("Loading CHGNet...")
slab.calc = CHGNetCalculator()

# 6. Optimization: Find the minimum energy structure
print("Starting relaxation...")
dyn = BFGS(slab, trajectory='Hg13_adsorption.traj')
dyn.run(fmax=0.05)

# 7. Results
energy = slab.get_potential_energy()
print(f"Optimization finished!")
print(f"Final Potential Energy: {energy:.4f} eV")

