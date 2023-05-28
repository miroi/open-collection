import sys
from ase.io import read
from ase.calculators.acemolecule import ACE

label = sys.argv[1]
mol= read('H2.xyz')
basic_list = {'Cell' : 12.0}
ace = ACE(label=label, BasicInformation = basic_list)
mol.calc = ace
print (mol.get_potential_energy())

