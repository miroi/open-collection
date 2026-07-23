import os
import sys
import contextlib
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS

# Redirect MOPAC output
os.environ['ASE_MOPAC_COMMAND'] = '/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac PREFIX.mop 2> /dev/null'

# Suppress MOPAC's stdout messages
with contextlib.redirect_stdout(open(os.devnull, 'w')):
    system = molecule('H2O')
    system.calc = MOPAC(method='PM7', task='1SCF GRADIENTS')
    opt = BFGS(system, trajectory='opt.traj', logfile='optimization.log')
    opt.run(fmax=0.01)

# Print results
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)

print(f"\n--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")
