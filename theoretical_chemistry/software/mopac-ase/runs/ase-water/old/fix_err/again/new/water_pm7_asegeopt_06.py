import os
import sys
import subprocess
import time
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS
from ase.io import read

class MOPACSubprocess(MOPAC):
    """MOPAC calculator that runs as subprocess with proper input handling"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mopac_path = '/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac'
        # IMPORTANT: Set command to None to prevent ASE from trying to execute it
        self.command = None
    
    def calculate(self, atoms, properties, system_changes):
        """Run MOPAC as subprocess"""
        # Store atoms
        self.atoms = atoms
        label = self.label or 'mopac'
        
        # Write input using parent method (this creates the .mop file)
        super().calculate(atoms, properties, system_changes)
        
        # Run MOPAC with automatic Enter key
        # Try multiple methods to ensure it works
        success = False
        
        # Method 1: echo with pipe
        cmd = f"echo '' | {self.mopac_path} {label}"
        print(f"Running: {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if os.path.exists(f"{label}.out"):
            success = True
        else:
            # Method 2: printf with newline
            print("Method 1 failed, trying printf...")
            cmd2 = f"printf '\\n' | {self.mopac_path} {label}"
            result2 = subprocess.run(cmd2, shell=True, capture_output=True, text=True)
            
            if os.path.exists(f"{label}.out"):
                success = True
            else:
                # Method 3: Use yes command
                print("Method 2 failed, trying yes...")
                cmd3 = f"yes '' | head -n 1 | {self.mopac_path} {label}"
                result3 = subprocess.run(cmd3, shell=True, capture_output=True, text=True)
                
                if os.path.exists(f"{label}.out"):
                    success = True
        
        if not success:
            # Print debug information
            print(f"ERROR: All MOPAC execution methods failed for {label}")
            print(f"STDOUT from last attempt: {result.stdout[:500] if 'result' in locals() else 'N/A'}")
            print(f"STDERR from last attempt: {result.stderr[:500] if 'result' in locals() else 'N/A'}")
            
            # Check if the .mop file exists
            if os.path.exists(f"{label}.mop"):
                print(f".mop file exists, content:")
                with open(f"{label}.mop", 'r') as f:
                    print(f.read())
            
            raise RuntimeError(f"MOPAC calculation failed for {label}")
        
        # Read results
        try:
            self.read_results()
        except Exception as e:
            print(f"Error reading results: {e}")
            # Try to manually read geometry
            self._read_geometry_manually(label)
    
    def _read_geometry_manually(self, label):
        """Read geometry manually from arc file"""
        arc_file = f"{label}.arc"
        if not os.path.exists(arc_file):
            print(f"ARC file {arc_file} not found")
            return
        
        with open(arc_file, 'r') as f:
            lines = f.readlines()
        
        positions = []
        found_geometry = False
        
        for line in lines:
            if "FINAL GEOMETRY OBTAINED" in line:
                found_geometry = True
                continue
            if found_geometry and line.strip():
                parts = line.split()
                if len(parts) >= 5 and parts[0] in ['O', 'H', 'C', 'N', 'S']:
                    try:
                        x = float(parts[1])
                        y = float(parts[3])
                        z = float(parts[5])
                        positions.append([x, y, z])
                    except:
                        continue
        
        if positions and len(positions) == len(self.atoms):
            print(f"Manually read geometry from {arc_file}")
            self.atoms.set_positions(positions)
        else:
            print(f"Could not read geometry from {arc_file}")

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

# Set up calculator
calc = MOPACSubprocess(
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
