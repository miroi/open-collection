#
#
#

import ase

mystery_atoms = ase.io.read('mystery.cell')
ase.spacegroup.get_spacegroup(mystery_atoms)
