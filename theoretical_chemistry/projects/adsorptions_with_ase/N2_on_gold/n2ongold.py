#
#
# Very simple demonstration of computing adsorption energy with ASE.
#
#

from ase import Atoms
from ase.build import add_adsorbate, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton

h = 1.85
d = 1.10

slab = fcc111('Au', size=(6, 6, 4), vacuum=15.0)

slab.calc = EMT()
e_slab = slab.get_potential_energy()

molecule = Atoms('2N', positions=[(0.0, 0.0, 0.0), (0.0, 0.0, d)])
molecule.calc = EMT()
e_N2 = molecule.get_potential_energy()

add_adsorbate(slab, molecule, h, 'ontop')

# freeze the gold slab
constraint = FixAtoms(mask=[a.symbol != 'N' for a in slab])
slab.set_constraint(constraint)

# run own geometry optimization
print("\n Running N2@Au(111) geometru optimization :")
dyn = QuasiNewton(slab, trajectory='N2Au.traj')
dyn.run(fmax=0.02)

# get the output
print('\n Adsorption energy of N2 molecule on gold slab:', e_slab + e_N2 - slab.get_potential_energy(),' eV ')

#  \(N_{2}\) on small gold clusters (\(Au_{n},n=1–6\)) exhibits adsorption energies in the \(0.2–0.9\text{\ eV}\) range.
print('FYI:  N2 on small gold clusters Au_{n},n=1–6 exhibits adsorption energies in the 0.2–0.9 eV range')



