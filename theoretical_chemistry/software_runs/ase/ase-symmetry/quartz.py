#
#
#

import ase.spacegroup
import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms

quartz = ase.spacegroup.crystal(symbols=['O', 'Si'],
                                basis=[[0.413, 0.2711, 0.2172],
                                       [0.4673, 0, 0.3333]],
                                spacegroup=152,
                                cellpar=[4.9019, 4.9019, 5.3988, 90, 90, 120])
fig, ax = plt.subplots()
plot_atoms(quartz)


