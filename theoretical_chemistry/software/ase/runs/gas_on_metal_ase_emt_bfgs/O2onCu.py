from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton
from ase.build import fcc111, add_adsorbate

h = 1.85

d = 1.16 # O-O bond distance in Agstroms (0.116 nm)

slab = fcc111('Cu', size=(4, 4, 2), vacuum=10.0)

# get the energy of the slab
slab.calc = EMT()
e_slab = slab.get_potential_energy()

molecule = Atoms('2O', positions=[(0., 0., 0.), (0., 0., d)])
molecule.calc = EMT()
e_O2 = molecule.get_potential_energy()

# add O2 on copper
add_adsorbate(slab, molecule, h, 'ontop')
# intruduce constraint - fixed adsorbates
constraint = FixAtoms(mask=[a.symbol != 'O' for a in slab])
slab.set_constraint(constraint)

dyn = QuasiNewton(slab, trajectory='O2Cu.traj')
dyn.run(fmax=0.05)

print('Adsorption energy:', e_slab + e_O2 - slab.get_potential_energy())
