from ase import Atoms
from ase.calculators.emt import EMT

import nequip

import ase.data
from ase.calculators.calculator import Calculator, all_changes
from ase.stress import full_3x3_to_voigt_6_stress

from nequip.data import AtomicData, AtomicDataDict
from nequip.data.transforms import TypeMapper
import nequip.scripts.deploy

#  https://github.com/mir-group/nequip/discussions/115#discussioncomment-1722946

from nequip.ase import NequIPCalculator
#atoms.calc = NequIPCalculator.from_deployed_model(
Atoms.calc = NequIPCalculator.from_deployed_model(
    model_path="deployed_model.pth",
 #   species_to_type_name = {
 #      "C": "NequIPTypeNameForCarbon",
 #      "H": "NequIPTypeNameForHydrogen"
 #   }
)

print(nequip)

d = 1.2  # may get proper bond distance
moleculeO2 = Atoms('2O', [(0., 0., 0.), (0., 0., d)])

#moleculeO2.set_calculator(Atoms.calc())
#moleculeO2.get_potential_energy()

#  see   https://github.com/mir-group/nequip/blob/main/nequip/ase/nequip_calculator.py

#print(NequIPCalculator)


#atomO = Atoms('O', calculator=EMT())
#e_atom = atomO.get_potential_energy()
#d = 1.2  # may get proper bond distance
#molecule = Atoms('2O', [(0., 0., 0.), (0., 0., d)])
#molecule.set_calculator(EMT())
#e_molecule = molecule.get_potential_energy()
#e_atomization = e_molecule - 2 * e_atom
#print('Oxygen atom energy: %5.2f eV' % e_atom)
#print('Oxygen molecule energy: %5.2f eV' % e_molecule)
#print('Atomization energy: %5.2f eV' % -e_atomization)

