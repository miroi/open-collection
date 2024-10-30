from ase import Atoms
from ase.calculators.nwchem import NWChem
from ase.io import write
 
d=0.91
hf = Atoms('HF',positions=[[0, 0, 0],[0, 0, d]])

hf.calc = NWChem(xc='PBE',basis='6-311G', property=dict('mulliken'))
#hf.calc = NWChem(xc='PBE',basis='6-311G')

en = hf.get_potential_energy() 

print('HF PBE run, d(HF)=',d,'Ang; Energy=',en,' eV')
#print(hf.calc.get_charges())



