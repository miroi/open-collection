#
# from Google AI querry
#

from ase.io import read
#from ase.calculators.openbabel import OpenBabel
#from openbabel import OpenBabel
from openbabel import pybel, openbabel

# Read a molecule using OpenBabel's SMILES parser
#atoms = read('C1=CC=CC=C1', format='smi')
atoms =  pybel.readstring("smi",'C1=CC=CC=C1')

# Attach the OpenBabel UFF calculator
#atoms.calc = OpenBabel(forcefield='uff')
atoms.calc = openbabel(forcefield='uff')
energy = atoms.get_potential_energy()

