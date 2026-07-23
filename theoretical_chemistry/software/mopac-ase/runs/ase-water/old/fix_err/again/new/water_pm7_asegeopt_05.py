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
    
    def calculate(self, atoms, properties, system_changes):
        """Run MOPAC as subprocess"""
        # Write input file
        self.atoms = atoms
        label = self.label or 'mopac'
        
        # Write input using parent method
        super().calculate(atoms, properties, system_changes)
        
        # Try to run MOPAC with automatic Enter
        # Use a temporary file to store the input for MOPAC
        input_content = ""
        
        # Read the .mop file
        with open(f"{label}.mop", 'r') as f:
            input_content = f.read()
        
        # Run MOPAC with the input piped in
        # This ensures MOPAC gets the Enter key
        cmd = f"echo '' | {self.mopac_path} {label}"
        
        # Run the command
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )
        
        # Check if output exists
        if not os.path.exists(f"{label}.out"):
            # Try alternative method
            cmd2 = f"printf '\\n' | {self.mopac_path} {label}"
            result2 = subprocess.run(
                cmd2,
                shell=True,
                capture_output=True,
                text=True
            )
            
            if not os.path.exists(f"{label}.out"):
                raise RuntimeError(f"MOPAC calculation failed for {label}")
        
        # Read results
        try:
            self.read_results()
        except Exception as e:
            print(f"Error reading results: {e}")
            # Try to manually read geometry
            self._read_geometry_manually(label)
    
    def _read_geometry_manually(self, label):
        """Read geometry manually"""
        arc_file = f"{label}.arc"
        if not os.path.exists(arc_file):
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
                if len(parts) >= 5 and parts[0] in ['O', 'H']:
                    x = float(parts[1])
                    y = float(parts[3])
                    z = float(parts[5])
                    positions.append([x, y, z])
        
        if positions and len(positions) == len(self.atoms):
            self.atoms.set_positions(positions)

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
