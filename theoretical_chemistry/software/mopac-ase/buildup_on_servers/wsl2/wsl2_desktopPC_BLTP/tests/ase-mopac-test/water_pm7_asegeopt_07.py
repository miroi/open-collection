import os
import sys
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS

# 1. Hardcode your clean MOPAC path 
mopac_exec = '/usr/bin/mopac'
# We append echo to handle any lingering internal interactive requirements
os.environ['ASE_MOPAC_COMMAND'] = f'echo "" | {mopac_exec}'

# 2. Generate the initial water molecule
system = molecule('H2O')

# 3. Attach MOPAC calculator 
system.calc = MOPAC(method='PM7', task='1SCF GRADIENTS')

# 4. Initialize the optimizer
opt = BFGS(system, trajectory='opt.traj', logfile='optimization.log')

# 5. Low-level descriptor manipulation to force 100% terminal silence
# This physically detaches the script from the terminal screen during the run
null_fds = [os.open(os.devnull, os.O_RDWR) for _ in range(2)]
save_fds = [os.dup(1), os.dup(2)]

try:
    # Redirect stdout (1) and stderr (2) at the operating system file descriptor level
    os.dup2(null_fds[0], 1)
    os.dup2(null_fds[1], 2)
    
    # Run the optimization completely headlessly
    opt.run(fmax=0.01)
finally:
    # Restore original terminal streams so python can print the final summary block
    os.dup2(save_fds[0], 1)
    os.dup2(save_fds[1], 2)
    for fd in null_fds + save_fds:
        os.close(fd)

# 6. Extract finalized structural parameters
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)

# 7. Parse the MOPAC output file safely
mopac_version = "Unknown Version"
heat_of_formation = "Unknown"
charges = []
out_filename = 'mopac.out'

if os.path.exists(out_filename):
    with open(out_filename, 'r') as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines):
        if "Version" in line or "MOPAC" in line:
            if "MOPAC v" in line or "MOPAC2" in line:
                mopac_version = line.strip()
        
        if "FINAL HEAT OF FORMATION" in line:
            parts = line.split('=')
            if len(parts) > 1:
                heat_of_formation = parts[1].split()[0] + " kcal/mol"
            
        if "NET ATOMIC CHARGES" in line:
            charges = []
            for charge_line in lines[idx + 3 : idx + 3 + len(system)]:
                parts = charge_line.split()
                if len(parts) >= 3:
                    atom_index = parts[0]
                    atom_symbol = parts[1]
                    partial_charge = parts[2]
                    charges.append((atom_index, atom_symbol, partial_charge))

# 8. Print clean terminal results and parsed quantum data
print("--- Computational Environment ---")
print(f"MOPAC Executable : {mopac_exec}")
print(f"MOPAC Version    : {mopac_version}")

print(f"\n--- Thermodynamic Results ---")
print(f"Heat of Formation: {heat_of_formation}")

print(f"\n--- Net Atomic Charges ---")
for idx, sym, chg in charges:
    print(f"Atom {idx:>2} ({sym:<2}) : {chg:>8} e")

print(f"\n--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")
print(f"\nOptimization log saved to 'optimization.log'")

