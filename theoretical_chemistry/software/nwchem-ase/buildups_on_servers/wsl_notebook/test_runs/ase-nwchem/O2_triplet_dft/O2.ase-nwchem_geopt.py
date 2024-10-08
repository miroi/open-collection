#
#
#
from ase import Atoms
from ase.calculators.nwchem import NWChem
from ase.optimize import BFGS

calcNW = NWChem(label='calc',
            dft=dict(maxiter=200,mult=3,odft=None,grid=fine, xc='PBE'),
            basis='6-31+G*')

d = 1.5
moleculeO2 = Atoms('2O', [(0., 0., 0.), (0., 0., d)], calculator=calcNW )

opt = BFGS(moleculeO2)
print('\n running geometry optimization of the O2 molecule with the initial distance d(O-O)=',d)
opt.run(fmax=0.02)

# print out optimal internuclear distance
print('NWChem optimized d(O-O)=',moleculeO2.get_distance(0,1))

e_moleculeO2 = moleculeO2.get_total_energy()

print('Oxygen molecule total energy: %5.2f eV' % e_moleculeO2)

