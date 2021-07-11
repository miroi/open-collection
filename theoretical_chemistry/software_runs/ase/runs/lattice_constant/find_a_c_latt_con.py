import numpy as np
from ase.io import Trajectory
from ase.build import bulk

from ase.calculators.emt import EMT
from ase.io import read

# we do the 9 calculations (three values for a and three for c):

a0 = 3.52 / np.sqrt(2)
c0 = np.sqrt(8 / 3.0) * a0

traj = Trajectory('Ni.traj', 'w')

eps = 0.01
for a in a0 * np.linspace(1 - eps, 1 + eps, 3):
    for c in c0 * np.linspace(1 - eps, 1 + eps, 3):
        ni = bulk('Ni', 'hcp', a=a, c=c)

# analysis

