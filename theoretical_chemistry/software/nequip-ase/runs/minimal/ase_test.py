from ase import Atoms
from ase.calculators.emt import EMT

import nequip

import ase.data
from ase.calculators.calculator import Calculator, all_changes
from ase.stress import full_3x3_to_voigt_6_stress

from nequip.data import AtomicData, AtomicDataDict
from nequip.data.transforms import TypeMapper
import nequip.scripts.deploy

print(nequip)

#  see   https://github.com/mir-group/nequip/blob/main/nequip/ase/nequip_calculator.py

#print(NequIPCalculator)


#atom = Atoms('O', calculator=EMT())
#e_atom = atom.get_potential_energy()
#d = 1.2  # may get proper bond distance
#molecule = Atoms('2O', [(0., 0., 0.), (0., 0., d)])
#molecule.set_calculator(EMT())
#e_molecule = molecule.get_potential_energy()
#e_atomization = e_molecule - 2 * e_atom
#print('Oxygen atom energy: %5.2f eV' % e_atom)
#print('Oxygen molecule energy: %5.2f eV' % e_molecule)
#print('Atomization energy: %5.2f eV' % -e_atomization)

