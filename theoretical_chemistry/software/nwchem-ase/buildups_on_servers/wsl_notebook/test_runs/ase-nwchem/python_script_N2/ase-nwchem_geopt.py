#
#
#
from ase import Atoms
from ase.calculators.nwchem import NWChem
from ase.optimize import BFGS

#calcNW = NWChem(label='calc/nwchem',
calcNW = NWChem(label='calcnwchem',
              dft=dict(maxiter=200,
                       xc='B3LYP'),
              basis='6-31+G*')

d = 1.1
moleculeN2 = Atoms('2N', [(0., 0., 0.), (0., 0., d)], calculator=calcNW )

opt = BFGS(moleculeN2)
print('\n running geometry optimization of the N2 molecule with the initial distance d(N-N)=',d)
opt.run(fmax=0.02)

# print out optimal internuclear distance
print('NWChem optimized d(N-N)=',moleculeN2.get_distance(0,1))

e_moleculeN2 = moleculeN2.get_total_energy()

print('Nitrogen molecule total energy: %5.2f eV' % e_moleculeN2)

