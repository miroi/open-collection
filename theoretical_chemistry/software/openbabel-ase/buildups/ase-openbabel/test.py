#
# from Google AI querry
#

from ase.io import read
from ase.calculators.openbabel import OpenBabel

# Read a molecule using OpenBabel's SMILES parser
atoms = read('C1=CC=CC=C1', format='smi')

# Attach the OpenBabel UFF calculator
atoms.calc = OpenBabel(forcefield='uff')
energy = atoms.get_potential_energy()

