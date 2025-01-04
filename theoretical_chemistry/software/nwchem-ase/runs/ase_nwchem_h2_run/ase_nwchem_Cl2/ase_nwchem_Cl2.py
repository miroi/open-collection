from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
from ase.io import write
 
d=2.0 # close to exp.distance 228 pm
cl2 = Atoms('Cl2',positions=[[0, 0, 0],[0, 0, d]])
cl2.calc = NWChem(dft=dict(maxiter=500,xc='B3LYP'),basis='6-31++g')
opt = BFGS(cl2, trajectory='cl2.traj')
opt.run(fmax=0.01)
