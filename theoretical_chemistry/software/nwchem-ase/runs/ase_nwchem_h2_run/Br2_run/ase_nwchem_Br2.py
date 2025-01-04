from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
from ase.io import write
 
d=2.3 # close to exp.distance 228 pm
br2 = Atoms('Br2',positions=[[0, 0, 0],[0, 0, d]])
br2.calc = NWChem(dft=dict(maxiter=500,xc='B3LYP'),basis='6-31+G*')
opt = BFGS(br2, trajectory='br2.traj')
opt.run(fmax=0.02)
