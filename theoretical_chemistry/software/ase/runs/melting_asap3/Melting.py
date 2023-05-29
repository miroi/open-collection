"Melting a copper cluster."

from asap3 import Atoms, EMT, units
from ase.visualize.primiplotter import PrimiPlotter, PngFile
from ase.lattice.cubic import FaceCenteredCubic
from asap3.md.langevin import Langevin

# Create the atoms
atoms = FaceCenteredCubic(size=(5,5,5), symbol="Cu", pbc=False)


# Associate the EMT potential with the atoms
atoms.set_calculator(EMT())

# Temperature profile
temperatures = (250, 500, 750, 1000, 1250, 1500, 1750)

# How many steps at each temperature
nsteps = 10000

# Interval between plots
plotinterval = 2000

# Make the Langevin dynamics module
dyn = Langevin(atoms, 5*units.fs, units.kB*temperatures[0], 0.002)

# The plotter
plotter = PrimiPlotter(atoms)
# plotter.set_output(X11Window())   # Plot in a window on the screen
plotter.set_output(PngFile("plt"))  # Save plots in files plt0000.gif ...
plotter.set_rotation((10.0, 5.0, 0))
dyn.attach(plotter.plot, interval=plotinterval)

# The main loop
for t in temperatures:
    dyn.set_temperature(units.kB*t)
    for i in range(nsteps//100):
        dyn.run(100)
        print("E_total = %-10.5f  T = %.0f K  (goal: %.0f K, step %d of %d)" %\
              (atoms.get_total_energy()/len(atoms), atoms.get_temperature(),
                   t, i, nsteps//100))
