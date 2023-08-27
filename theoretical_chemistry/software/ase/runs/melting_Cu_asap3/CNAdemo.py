"Melting a copper cluster."

from numpy import *
from asap3 import Atoms, EMT, units
from asap3.analysis.localstructure import RestrictedCNA 
from asap3.visualize.primiplotter import *
from ase.lattice.cubic import FaceCenteredCubic
from asap3.md.langevin import Langevin

# Create the atoms
atoms = FaceCenteredCubic(size=(6,6,6), symbol="Cu", pbc=False)

# Associate the EMT potential with the atoms
atoms.set_calculator(EMT())

# Temperature profile - brief run at 1750, then lower temperature gradually
t = linspace(1500, 250, 81)
temperatures = 1500 * ones(100)
temperatures[-len(t):] = t
print(temperatures)

# How many steps at each temperature
nsteps_total = 100000
nsteps = nsteps_total // len(temperatures)

# Interval between plots
plotinterval = 2000

# Make the Langevin dynamics module
dyn = Langevin(atoms, 5*units.fs, units.kB*temperatures[0], 0.002)

# The CNA analyser is called every plotinterval timesteps.
cna = RestrictedCNA(atoms)
dyn.attach(cna.analyze, interval=plotinterval)

# The plotter
def invisible_atoms(a):
    """Return True for atoms that should be invisible."""
    r = atoms.get_positions()
    centerofmass = r.sum(axis=0) / len(atoms)
    return (r[:,2] < centerofmass[2])

plotter = PrimiPlotter(atoms)
plotter.set_invisibility_function(invisible_atoms)
plotter.set_colors({0: (1.0, 1.0, 1.0), 1: (1.0, 0.0, 0.0), 2: (0.3, 0.3, 1.0)}) # Map tags to colors
# plotter.set_output(X11Window())   # Plot in a window on the screen
plotter.set_output(PngFile("plt"))  # Save plots in files plt0000.png ...
plotter.set_rotation((10.0, 5.0, 0))

# Attach the plotter to the RestrictedCNA object.  That guarantees
# that the plotter is called AFTER the CNA analysis has been done.
# Similarly, a Trajectory should be attached to the RestricedCNA
# object.  By using interval=1 (the default), the plotter is called
# every time RestrictedCNA is called, i.e. every plotinterval
# timesteps.
cna.attach(plotter.plot)

# The main loop
for t in temperatures:
    dyn.set_temperature(units.kB*t)
    for i in range(nsteps//100):
        dyn.run(100)
        print("E_total = %-10.5f  T = %.0f K  (goal: %.0f K, step %d of %d)" %\
          (atoms.get_total_energy()/len(atoms), atoms.get_temperature(), t, i, nsteps/100))
