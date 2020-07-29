from ase import Atoms
from gpaw import GPAW

d = 0.74
a = 6.0

atoms = Atoms('H2',
              positions=[(0, 0, 0),
                         (0, 0, d)],
              cell=(a, a, a))
atoms.center()

#calc = GPAW(nbands=2, txt='h2.txt')

calc = GPAW(nbands=1, xc='PBE',gpts=(24, 24, 24), txt='h2_pbe.out')

atoms.set_calculator(calc)
print(atoms.get_forces())

