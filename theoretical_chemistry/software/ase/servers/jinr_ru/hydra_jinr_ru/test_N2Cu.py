#
# https://wiki.fysik.dtu.dk/ase/gettingstarted/surface.html
#
from ase import Atoms
from ase.build import add_adsorbate, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton

h = 1.85
d = 1.10

#  build crystals using, for example, the lattice module which returns Atoms objects corresponding to common crystal structures 
# let us make a Cu (111) surface:
slab = fcc111('Cu', size=(4, 4, 2), vacuum=10.0)

slab.calc = EMT()
e_slab = slab.get_potential_energy()

## define a N2 molecule by directly specifying the position of two nitrogen atoms
molecule = Atoms('2N', positions=[(0., 0., 0.), (0., 0., d)])

molecule.calc = EMT()
e_N2 = molecule.get_potential_energy()

## First add the adsorbate to the Cu slab, here in the on-top position
add_adsorbate(slab, molecule, h, 'ontop')

constraint = FixAtoms(mask=[a.symbol != 'N' for a in slab])
slab.set_constraint(constraint)
dyn = QuasiNewton(slab, trajectory='N2Cu.traj')
dyn.run(fmax=0.05)

print('Adsorption energy:', e_slab + e_N2 - slab.get_potential_energy())
