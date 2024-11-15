from ase import Atoms
from ase.calculators.emt import EMT

#from nequip import nequip.dynamics
#import logging
#from nequip.models import ForceModel

atom = Atoms('O', calculator=EMT())
e_atom = atom.get_potential_energy()

d = 1.2  # may get proper bond distance
molecule = Atoms('2O', [(0., 0., 0.), (0., 0., d)])
molecule.set_calculator(EMT())
e_molecule = molecule.get_potential_energy()

e_atomization = e_molecule - 2 * e_atom

print('Oxygen atom energy: %5.2f eV' % e_atom)
print('Oxygen molecule energy: %5.2f eV' % e_molecule)
print('Atomization energy: %5.2f eV' % -e_atomization)
