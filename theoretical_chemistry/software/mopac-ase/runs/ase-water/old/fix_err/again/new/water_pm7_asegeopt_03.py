import os
import sys
import subprocess
import time
import pty
import select
import signal
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS

# Set environment variable
os.environ['ASE_MOPAC_COMMAND'] = '/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac'

class MOPACInteractive(MOPAC):
    """MOPAC calculator that handles interactive prompt using pty"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mopac_path = '/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac'
        self.command = None
    
    def _run_mopac(self, label):
        """Run MOPAC with proper pty handling"""
        # Fork with pty
        pid, fd = pty.fork()
        
        if pid == 0:
            # Child process - execute MOPAC
            os.execv(self.mopac_path, [self.mopac_path, label])
        else:
            # Parent process
            try:
                # Send Enter key with proper timing
                time.sleep(0.5)
                os.write(fd, b'\n')
                os.write(fd, b'\n')  # Send twice to be safe
                
                # Read output and wait for completion
                output = b''
                timeout = 30
                start_time = time.time()
                
                while time.time() - start_time < timeout:
                    try:
                        r, w, e = select.select([fd], [], [], 0.1)
                        if fd in r:
                            data = os.read(fd, 1024)
                            if not data:
                                break
                            output += data
                    except:
                        break
                
                # Wait for child process
                os.waitpid(pid, 0)
                os.close(fd)
                
                # Check if output file was created
                if os.path.exists(f"{label}.out"):
                    return True
                else:
                    print(f"Output file {label}.out not created")
                    return False
                    
            except Exception as e:
                print(f"Error in pty method: {e}")
                return False
    
    def calculate(self, atoms, properties, system_changes):
        """Override calculate to handle interactive prompt"""
        # Write input file
        super().calculate(atoms, properties, system_changes)
        
        # Get label
        label = self.label or 'mopac'
        
        # Run MOPAC with pty
        success = self._run_mopac(label)
        
        if not success:
            # Try fallback method
            print("PTY method failed, trying fallback...")
            cmd = f"echo '' | {self.mopac_path} {label}"
            subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            # Check again if output file exists
            if not os.path.exists(f"{label}.out"):
                raise RuntimeError(f"MOPAC calculation failed for {label}")
        
        # Read results
        try:
            self.read_results()
        except Exception as e:
            print(f"Error reading results: {e}")
            # Try to read geometry manually
            self._read_geometry_manually(label)

    def _read_geometry_manually(self, label):
        """Read geometry manually if read_results fails"""
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
                    x = float(parts[1])
                    y = float(parts[3])
                    z = float(parts[5])
                    positions.append([x, y, z])
        
        if positions and len(positions) == len(self.atoms):
            print(f"Manually read geometry from {arc_file}")
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
calc = MOPACInteractive(
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
