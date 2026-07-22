import os
import subprocess
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS

# 1. Intercept and silence MOPAC's stdout at the Python subprocess level
original_popen = subprocess.Popen

def silent_popen(*args, **kwargs):
    # Check if this subprocess call is invoking MOPAC
    if args and isinstance(args[0], list) and any('mopac' in str(arg).lower() for arg in args[0]):
        kwargs['stdout'] = subprocess.DEVNULL  # Silently drop the banner text
    return original_popen(*args, **kwargs)

# Inject our silent handler into the subprocess module
subprocess.Popen = silent_popen

# 2. Set the clean path to your actual MOPAC binary executable
os.environ['ASE_MOPAC_COMMAND'] = 'path/to/mopac'

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

# 7. Print clean, non-blocked structural results
print(f"--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")
print(f"\nOptimization log saved to 'optimization.log'")

