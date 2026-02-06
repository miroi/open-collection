from math import cos, pi, sin

from ase import Atoms
from ase.build import add_adsorbate, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixLinearTriatomic
from ase.optimize import BFGS

zpos = cos(134.3 / 2.0 * pi / 180.0) * 1.197
xpos = sin(134.3 / 2.0 * pi / 180.0) * 1.19

# CO2 molecule
co2 = Atoms('COO', positions=[(-xpos + 1.2, 0, -zpos),
                              (-xpos + 1.2, -1.1, -zpos),
                              (-xpos + 1.2, 1.1, -zpos)])

slab = fcc111('Au', size=(2, 2, 4), vacuum=2 * 5, orthogonal=True)
slab.center()
add_adsorbate(slab, co2, 1.5, 'bridge')
slab.set_pbc((True, True, False))

d0 = co2.get_distance(-3, -2)
d1 = co2.get_distance(-3, -1)
d2 = co2.get_distance(-2, -1)

calc = EMT()
slab.calc = calc

slab.set_scaled_positions(slab.get_scaled_positions() % 1.0)
constraint = FixLinearTriatomic(triples=[(-2, -3, -1)])
slab.set_constraint(constraint)

assert slab.get_number_of_degrees_of_freedom() == 53

print("running CO2@Au(111) geometry optimization:")
with BFGS(slab, trajectory='relax_%d.traj' ) as dyn:
      dyn.run(fmax=0.05)

assert abs(slab.get_distance(-3, -2, mic=1) - d0) < 1e-9
assert abs(slab.get_distance(-3, -1, mic=1) - d1) < 1e-9
assert abs(slab.get_distance(-2, -1, mic=1) - d2) < 1e-9

print("",abs(slab.get_distance(-3, -2, mic=1) - d0),abs(slab.get_distance(-3, -1, mic=1) - d1),abs(slab.get_distance(-2, -1, mic=1) - d2))

