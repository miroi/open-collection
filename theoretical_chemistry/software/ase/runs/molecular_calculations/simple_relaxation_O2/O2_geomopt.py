from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton

d = 2.0 #starting geometry
O2 = Atoms('O2', positions=[[0.0, 0.0, 0.0], [0.0, 0.0, d]])
calc = EMT()
O2.calc = calc

print(" Starting O2 bond distance :", O2.get_distance(0, 1), " Angstrom")

# print the (decreasing) total energy for each iteration until it converges, leaving the file h2.emt.traj in the working directory. Use the command ase gui to view the trajectory file, showing each step of the optimization.
opt = QuasiNewton(O2, trajectory='o2.emt.traj')
# run the optimization algorithm until all atomic forces are below 0.05 eV per Ångström.
opt.run(fmax=0.01)

print(" EMT optimized O2 bond distance :", O2.get_distance(0, 1), " Angstrom")
print("  Experimental bond distance is 1.21 Ang")

