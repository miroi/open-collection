import os
import sys
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS

# 1. Set the environment variable for the MOPAC executable path
#os.environ['ASE_MOPAC_COMMAND'] = 'path/to/mopac'
os.environ['ASE_MOPAC_COMMAND'] = '/home/milias/work/software/mopac/mopac-23.2.3-linux/bin/mopac'

# 2. Generate the initial water molecule
system = molecule('H2O')

# 3. Suppress MOPAC's stdout by redirecting it to devnull during calculation
# Note: MOPAC prints directly to stdout bypasses ASE's logfile controls
sys.stdout = open(os.devnull, 'w')
system.calc = MOPAC(method='PM7', task='1SCF GRADIENTS')

# 4. Run optimization with a clean logfile and restore standard output
# Setting logfile='optimization.log' redirects the BFGS step information
opt = BFGS(system, trajectory='opt.traj', logfile='optimization.log')
opt.run(fmax=0.05)

# Restore standard output to print the final results to the terminal
sys.stdout = sys.__stdout__

# 5. Extract finalized structural parameters
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)

# 6. Print the structural results
print(f"\n--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")
print(f"\nOptimization log saved to 'optimization.log'")

