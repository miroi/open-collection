#
#
#
from ase import Atoms
from ase.calculators.nwchem import NWChem

#calcNW = NWChem(label='calc/nwchem',
calcNW = NWChem(label='calcnwchem',
              dft=dict(maxiter=200,
                       xc='B3LYP'),
              basis='6-31+G*')

d = 1.1
moleculeN2 = Atoms('2N', [(0., 0., 0.), (0., 0., d)], calculator=calcNW )

#e_moleculeN2 = moleculeN2.get_potential_energy()
e_moleculeN2 = moleculeN2.get_total_energy()

#print('Nitrogen molecule energy: %5.2f eV' % e_moleculeN2)
#print(e_moleculeN2)

