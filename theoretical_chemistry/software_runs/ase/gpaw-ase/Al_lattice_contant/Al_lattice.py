#
# https://wiki.fysik.dtu.dk/gpaw/tutorials/lattice_constants/lattice_constants.html#fcc-aluminium
#
import numpy as np
from ase.build import bulk
from gpaw import GPAW, PW

a0 = 4.04
al = bulk('Al', 'fcc', a=a0)
cell0 = al.cell

for ecut in range(200, 501, 50):
    al.calc = GPAW(mode=PW(ecut),
                   xc='PBE',
                   kpts=(8, 8, 8),
                   parallel={'band': 1},
                   basis='dzp',
                   txt='Al-%d.txt' % ecut)
    for eps in np.linspace(-0.02, 0.02, 5):
        al.cell = (1 + eps) * cell0
        al.get_potential_energy()

