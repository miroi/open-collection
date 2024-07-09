#
# https://wiki.fysik.dtu.dk/ase/ase/build/surface.html
#

from ase.build import fcc111, add_adsorbate, surface
from ase.visualize import view
from ase import Atoms

a = 4.0
Pt3Rh = Atoms('Pt3Rh',
              scaled_positions=[(0, 0, 0),
                                (0.5, 0.5, 0),
                                (0.5, 0, 0.5),
                                (0, 0.5, 0.5)],
              cell=[a, a, a],
              pbc=True)


Pt3Rh.set_chemical_symbols('PtRhPt2')
s4 = surface(Pt3Rh, (2, 1, 1), 9)
s4.center(vacuum=10, axis=2)

s4.write("alloy.in")

view(s4)


