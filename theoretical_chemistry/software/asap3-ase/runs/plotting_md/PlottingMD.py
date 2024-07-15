"""Simple molecular dynamics.

A block of 27 cubic unit cells of Cu is set up, a single atom is given
a significant momentum, and constant energy molecular dynamics is
performed.

"""

from numpy import *
from asap3 import Atoms, EMT, units
from asap3.visualize.primiplotter import *
from ase.lattice.cubic import FaceCenteredCubic
from asap3.md.verlet import VelocityVerlet

# Create the atoms
atoms = FaceCenteredCubic(size=(3,3,3), symbol="Cu", pbc=False)

# Give the first atom a non-zero momentum
atoms[0].momentum = array([0, -11.3, 0])

# Associate the EMT potential with the atoms
atoms.set_calculator(EMT())

# Now do molecular dynamics, printing kinetic, potential and total
# energy every ten timesteps.
dyn = VelocityVerlet(atoms, 5.0*units.fs)

# Set up a plotter
plotter = PrimiPlotter(atoms)
plotter.set_output(X11Window())   # Plot in X11 window on the user's screen
plotter.set_output(PngFile("a"))  # Save as PNG files
# plotter.set_output(PostScriptFile("a"))  # Save as PS files

# Attach it to the dynamics, so it is informed every 25'th time a
# timestep is made.
dyn.attach(plotter.plot, interval=25)

# Now do 1000 timesteps.
dyn.run(1000)
print("The output is in the NetCDF file TrajectoryMD-output.traj")
