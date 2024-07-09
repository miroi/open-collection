#
#
#
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS


atom = Atoms('N', calculator=EMT())
e_atom = atom.get_potential_energy()

d = 1.1 # this is the N2 experimental bond length (in Angs)
molecule = Atoms('2N', [(0., 0., 0.), (0., 0., d)], calculator=EMT() )

opt = BFGS(molecule)
print('\n running geometry optimization of the N2 molecule with the initial distance d(N-N)=',d)
opt.run(fmax=0.02)

# print out optimal internuclear distance
print('d(N-N)optimiz=',molecule.get_distance(0,1))

e_molecule = molecule.get_potential_energy()

e_atomization = e_molecule - 2 * e_atom

print('\n Nitrogen atom energy: %5.2f eV' % e_atom)
print('Nitrogen molecule energy: %5.2f eV' % e_molecule)
print('Atomization energy: %5.2f eV' % -e_atomization)

