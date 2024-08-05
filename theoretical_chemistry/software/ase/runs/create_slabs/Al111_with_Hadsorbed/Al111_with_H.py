#
# https://wiki.fysik.dtu.dk/ase/ase/build/surface.html
#

from ase.build import fcc111, add_adsorbate
from ase.visualize import view
slab = fcc111('Al', size=(2,2,3))
add_adsorbate(slab, 'H', 1.5, 'ontop')
slab.center(vacuum=10.0, axis=2)

slab.write("Al111_H.in")

view(slab)


