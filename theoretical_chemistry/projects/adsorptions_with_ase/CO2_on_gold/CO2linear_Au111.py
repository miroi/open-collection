#
# Simple program on adsorption
#
# From ASE test suite
#
from math import cos, pi, sin

from ase import Atoms
from ase.build import add_adsorbate, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixLinearTriatomic
from ase.optimize import BFGS
from ase.visualize import view

zpos = cos(134.3 / 2.0 * pi / 180.0) * 1.197
xpos = sin(134.3 / 2.0 * pi / 180.0) * 1.19

print('xpos=',xpos,' zpos=',zpos)

#CO2 molecule
co2 = Atoms('COO', positions=[(-xpos + 1.2, 0, -zpos),
                              (-xpos + 1.2, -1.1, -zpos),
                              (-xpos + 1.2, +1.1, -zpos)])

# ** define Au111 slab **
# slab = fcc111('Au', size=(2, 2, 4), vacuum=2 * 5, orthogonal=True)
slab = fcc111('Au', size=(6, 6, 4), vacuum=2 * 10, orthogonal=True)
slab.center()

# add adsorbate
#add_adsorbate(slab, co2, 1.5, 'bridge')
pos_shift = 5.0
add_adsorbate(slab, co2, 1.5, position=(pos_shift,pos_shift))

# control view of prepared slab
view(slab)

slab.set_pbc((True, True, False))

d0 = co2.get_distance(-3, -2)
d1 = co2.get_distance(-3, -1)
d2 = co2.get_distance(-2, -1)
print("CO2 interatomic distances:",d0,d1,d2)

calc = EMT()
slab.calc = calc

slab.set_scaled_positions(slab.get_scaled_positions() % 1.0)

# set constrains
constraint = FixLinearTriatomic(triples=[(-2, -3, -1)])
slab.set_constraint(constraint)

#assert slab.get_number_of_degrees_of_freedom() == 53
print(" Number of degrees of freedom =", slab.get_number_of_degrees_of_freedom() )

print("running CO2@Au(111) geometry optimization:")
with BFGS(slab, trajectory='relaxation.traj' ) as dyn:
      dyn.run(fmax=0.05)

# check that O-C-O bond distances are kept frozen
assert abs(slab.get_distance(-3, -2, mic=1) - d0) < 1e-9
assert abs(slab.get_distance(-3, -1, mic=1) - d1) < 1e-9
assert abs(slab.get_distance(-2, -1, mic=1) - d2) < 1e-9

print("aasertion on CO2 interatomic distances:",abs(slab.get_distance(-3, -2, mic=1) - d0),abs(slab.get_distance(-3, -1, mic=1) - d1),abs(slab.get_distance(-2, -1, mic=1) - d2))

