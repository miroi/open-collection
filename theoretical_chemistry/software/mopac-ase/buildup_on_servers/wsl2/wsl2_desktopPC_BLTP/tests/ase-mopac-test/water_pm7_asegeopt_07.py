import os
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS

# 1. Hardcode MOPAC path & pipe an EOF string to auto-respond to interactive prompts
mopac_exec = '/usr/bin/mopac'
os.environ['ASE_MOPAC_COMMAND'] = f'echo "" | {mopac_exec}'

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

# 6. Parse the MOPAC output file for version, heat of formation, and partial charges
mopac_version = "Unknown Version"
heat_of_formation = "Unknown"
charges = []
out_filename = 'mopac.out'

if os.path.exists(out_filename):
    with open(out_filename, 'r') as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines):
        # Extract version
        if "Version" in line or "MOPAC" in line and any(yr in line for yr in ["2012", "2016", "2022", "v"]):
            if mopac_version == "Unknown Version":
                mopac_version = line.strip()
        
        # Extract Heat of Formation
        if "FINAL HEAT OF FORMATION" in line:
            # Splits row to capture the numeric value right after the '=' sign
            heat_of_formation = line.split('=')[1].strip().split()[0] + " kcal/mol"
            
        # Extract Mulliken/ESP Partial Charges
        if "NET ATOMIC CHARGES" in line:
            charges = [] # Clear any previous optimization step entries
            # Skip the table header rows to start parsing structural values
            for charge_line in lines[idx + 3 : idx + 3 + len(system)]:
                parts = charge_line.split()
                if len(parts) >= 3:
                    atom_index = parts[0]
                    atom_symbol = parts[1]
                    partial_charge = parts[2]
                    charges.append((atom_index, atom_symbol, partial_charge))

# 7. Print clean terminal results and parsed quantum data
print(f"--- Computational Environment ---")
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

