#
# https://wiki.fysik.dtu.dk/ase/ase/build/surface.html
#

from ase.build import fcc111
from ase import atoms

slab = fcc111('Al', size=(2,2,3), vacuum=10.0)

slab.write("Al_111.in")
