from ase import Atoms
from ase.calculators.nwchem import NWChem
from ase.io import write
 
d=0.91
hf = Atoms('HF',positions=[[0, 0, 0],[0, 0, d]])
hf.calc = NWChem(xc='PBE',basis='6-31G')


