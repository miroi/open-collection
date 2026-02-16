#
#  https://wiki.fysik.dtu.dk/gpaw/tutorialsexercises/structureoptimization/gettingstarted/gettingstarted.html
#

# creates: h2.emt.traj
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton

system = Atoms('H2', positions=[[0.0, 0.0, 0.0],
                                [0.0, 0.0, 1.0]])
calc = EMT()

system.calc = calc

# print the (decreasing) total energy for each iteration until it converges, leaving the file h2.emt.traj in the working directory. Use the command ase gui to view the trajectory file, showing each step of the optimization.
opt = QuasiNewton(system, trajectory='h2.emt.traj')

# run the optimization algorithm until all atomic forces are below 0.05 eV per Ångström.
opt.run(fmax=0.05)
