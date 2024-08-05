#  https://wiki.fysik.dtu.dk/gpaw/tutorialsexercises/vibrational/vibrations/vibrations.html

from math import cos, pi, sin
from ase import Atoms
from ase.optimize import QuasiNewton
from ase.vibrations import Vibrations
from gpaw import GPAW

# Water molecule:
d = 0.9575
t = pi / 180 * 104.51

h2o = Atoms('H2O',
            positions=[(0, 0, 0),
                       (d, 0, 0),
                       (d * cos(t), d * sin(t), 0)])

h2o.center(vacuum=3.5)

h2o.calc = GPAW(txt='h2o.txt',
                mode='lcao',
                basis='dzp',
                symmetry='off')

QuasiNewton(h2o).run(fmax=0.05)


"""Calculate the vibrational modes of a H2O molecule."""

# Create vibration calculator
vib = Vibrations(h2o)
vib.run()
vib.summary(method='frederiksen')

# Make trajectory files to visualize normal modes:
for mode in range(9):
    vib.write_mode(mode)
