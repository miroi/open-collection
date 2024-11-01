from ase import Atoms
from ase.calculators.nwchem import NWChem
from ase.io import write
 
d=0.91
hf = Atoms('HF',positions=[[0, 0, 0],[0, 0, d]])

hf.calc = NWChem(xc='PBE',basis='6-311G', property=dict(mulliken=None, dipole=None),task='property')

en = hf.get_potential_energy() 
print('HF PBE run, d(HF)=',d,'Ang; Energy=',en,' eV')
print('total energy =',hf.get_total_energy() )

print(hf.calc)

print('atomic numbers array:',hf.get_atomic_numbers() )

#print('atomic charges :',hf.get_charges())

print('dipole moment :',hf.get_dipole_moment() )

print('chemical formula :',hf.get_chemical_formula(mode='all') )

print('atomic mulliken charges :',hf.get_charges())

