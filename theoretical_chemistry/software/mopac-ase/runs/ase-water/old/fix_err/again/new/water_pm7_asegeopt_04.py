import os
import sys
import subprocess
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS

# Use the wrapper script
wrapper_path = os.path.abspath('./mopac_wrapper.sh')
os.environ['ASE_MOPAC_COMMAND'] = wrapper_path

# Verify wrapper exists and is executable
if not os.path.exists(wrapper_path):
    print(f"ERROR: Wrapper not found at {wrapper_path}")
    print("Please create mopac_wrapper.sh")
    sys.exit(1)

if not os.access(wrapper_path, os.X_OK):
    print(f"ERROR: Wrapper is not executable. Run: chmod +x {wrapper_path}")
    sys.exit(1)

print(f"Using MOPAC wrapper: {wrapper_path}")

# Generate water molecule
system = molecule('H2O')

# Print initial geometry
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)
print(f"\n--- ASE prepared H2O molecule geometry ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")

# Set up calculator with a label
calc = MOPAC(
    method='PM7',
    task='1SCF GRADIENTS',
    label='water_opt'
)

system.calc = calc

# Run optimization
print("\nStarting geometry optimization...")
opt = BFGS(system, trajectory='opt.traj', logfile='optimization.log')

try:
    opt.run(fmax=0.01)
except Exception as e:
    print(f"Optimization failed: {e}")
    
    # Debug output
    print("\n--- Debugging Information ---")
    for fname in ['water_opt.mop', 'water_opt.out', 'water_opt.arc']:
        if os.path.exists(fname):
            print(f"\n=== {fname} (last 30 lines) ===")
            with open(fname, 'r') as f:
                lines = f.readlines()
                print(''.join(lines[-30:]))
        else:
            print(f"{fname} not found")
    sys.exit(1)

# Extract results
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)

print(f"\n--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")
print(f"\nOptimization log saved to 'optimization.log'")
print(f"Trajectory saved to 'opt.traj'")
