#
# https://github.com/ajjackson/ase-tutorial-symmetry/blob/master/ase-symmetry.md#bravais-lattices
#

import ase.lattice
from ase import Atoms

ag_lattice = ase.lattice.FCC(a=4.09) # Face-centered cubic
print("Made a lattice for Ag: ", type(ag_lattice))

assert isinstance(ag_lattice, ase.lattice.BravaisLattice)

ag_cell = ag_lattice.tocell()
ag_atoms = Atoms('Ag', cell=ag_cell, pbc=True)
print(ag_atoms.cell)
