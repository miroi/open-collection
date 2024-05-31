from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
from ase.io import write
 
h2 = Atoms('H2',positions=[[0, 0, 0],[0, 0, 0.8]])
h2.calc = NWChem(xc='PBE')
opt = BFGS(h2, trajectory='h2.traj')
opt.run(fmax=0.02)
