import os
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS

# 1. Hardcode MOPAC path & pipe an EOF string to auto-respond to the interactive prompt
# This bypasses the interactive "Press (return) to continue" screen at the shell level.
os.environ['ASE_MOPAC_COMMAND'] = 'echo "" | /usr/bin/mopac'

# 2. Generate the initial water molecule
system = molecule('H2O')

# 3. Attach MOPAC calculator
system.calc = MOPAC(method='PM7', task='1SCF GRADIENTS')

# 4. Run optimization and save step information silently to optimization.log
opt = BFGS(system, trajectory='opt.traj', logfile='optimization.log')
opt.run(fmax=0.05)

# 5. Extract structural parameters
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)

# 6. Print clean terminal results
print(f"--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")
print(f"\nOptimization log saved to 'optimization.log'")

