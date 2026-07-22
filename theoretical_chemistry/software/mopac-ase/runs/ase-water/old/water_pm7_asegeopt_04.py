import os
import subprocess
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS

# 1. Create a quiet temporary shell wrapper script for MOPAC
wrapper_filename = os.path.abspath('mopac_silent.sh')
with open(wrapper_filename, 'w') as f:
    # Explicitly pass all arguments ($@) but dump stdout to devnull
    f.write('#!/bin/bash\n')
    f.write('/usr/bin/mopac "$@" > /dev/null\n')

# Make the wrapper script executable by the system
os.chmod(wrapper_filename, 0o755)

# 2. Tell ASE to execute our clean wrapper instead of MOPAC directly
os.environ['ASE_MOPAC_COMMAND'] = wrapper_filename

# 3. Generate the initial water molecule
system = molecule('H2O')

# 4. Attach MOPAC calculator
system.calc = MOPAC(method='PM7', task='1SCF GRADIENTS')

# 5. Run optimization with a clean logfile
opt = BFGS(system, trajectory='opt.traj', logfile='optimization.log')
opt.run(fmax=0.05)

# 6. Extract finalized structural parameters
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)

# 7. Print the structural results
print(f"--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")
print(f"\nOptimization log saved to 'optimization.log'")

# 8. Clean up the temporary wrapper script from disk
if os.path.exists(wrapper_filename):
    os.remove(wrapper_filename)

