import os
import sys
import subprocess
import numpy as np
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS
from ase.io import write
from ase.vibrations import Vibrations

# 1. Hardcode your clean MOPAC path 
mopac_exec = '/usr/bin/mopac'
os.environ['ASE_MOPAC_COMMAND'] = mopac_exec

# 2. Patch subprocess.run globally to safely force MOPAC into a headless execution mode
original_run = subprocess.run

def silent_run(args, *extra_args, **kwargs):
    # Detect if the execution call targets our MOPAC execution path string
    is_mopac = False
    if isinstance(args, str) and mopac_exec in args:
        is_mopac = True
    elif isinstance(args, list) and any(mopac_exec in str(a) for a in args):
        is_mopac = True
        
    if is_mopac:
        # Route output streams away from terminal to achieve 100% silence
        kwargs['stdout'] = subprocess.DEVNULL
        kwargs['stderr'] = subprocess.DEVNULL
        # Closing standard input feeds an immediate EOF, bypassing the "Press Return" hang
        kwargs['stdin'] = subprocess.DEVNULL
        
    return original_run(args, *extra_args, **kwargs)

# Inject our process supervisor globally into Python's subprocess core engine
subprocess.run = silent_run

# 3. Generate the initial water molecule
system = molecule('H2O')

# 4. Attach MOPAC calculator 
system.calc = MOPAC(method='PM7', task='1SCF GRADIENTS')

# 5. Initialize the optimizer (step information outputs cleanly to optimization.log)
opt = BFGS(system, trajectory='opt.traj', logfile='optimization.log')

# 6. Run the geometry optimization and vibrational frequency displacement calculations
# This block runs completely headlessly and silently now.
opt.run(fmax=0.01)

vib = Vibrations(system, name='vib_data')
vib.run()
frequencies = vib.get_frequencies()
vib.clean()  # Remove temporary displacement calculation files

# 7. Extract finalized structural parameters
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)

# Save the finalized structural model to a standard file format
xyz_filename = 'optimized_water.xyz'
write(xyz_filename, system)

# 8. Parse the MOPAC output file safely
mopac_version = "Unknown Version"
heat_of_formation = "Unknown"
dipole_debye = "Unknown"
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
                
        if "DIPOLE" in line and "DEBYE" in line:
            parts = line.split()
            if "TOTAL" in parts:
                dipole_debye = parts[parts.index("TOTAL") + 1] + " D"
            
        if "NET ATOMIC CHARGES" in line:
            charges = []
            for charge_line in lines[idx + 3 : idx + 3 + len(system)]:
                parts = charge_line.split()
                if len(parts) >= 3:
                    atom_index = parts[0]
                    atom_symbol = parts[1]
                    partial_charge = parts[2]
                    charges.append((atom_index, atom_symbol, partial_charge))

# 9. Evaluate structural local minimum verification status
# True local minima have exactly 0 imaginary/negative modes.
imaginary_modes = [f for f in frequencies if f.imag > 0 or f.real < 0]
is_local_minimum = len(imaginary_modes) == 0

# 10. Print clean terminal results and parsed quantum data
print("--- Computational Environment ---")
print(f"MOPAC Executable : {mopac_exec}")
print(f"MOPAC Version    : {mopac_version}")

print(f"\n--- Structural Export ---")
print(f"Optimized geometry successfully written to : '{xyz_filename}'")

print(f"\n--- Thermodynamic & Electrical Properties ---")
print(f"Heat of Formation: {heat_of_formation}")
print(f"Dipole Moment    : {dipole_debye}")

print(f"\n--- Net Atomic Charges ---")
for idx, sym, chg in charges:
    print(f"Atom {idx:>2} ({sym:<2}) : {chg:>8} e")

print(f"\n--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")

print(f"\n--- Vibrational Stability Check ---")
print("Calculated Normal Modes (cm⁻¹):")
for idx, freq in enumerate(frequencies):
    if freq.imag > 0 or freq.real < 0:
        val = freq.imag if freq.imag > 0 else abs(freq.real)
        print(f"  Mode {idx}: {val:>8.1f}i cm⁻¹ (IMAGINARY MODE)")
    else:
        print(f"  Mode {idx}: {freq.real:>8.1f}  cm⁻¹")

print(f"\nStructure verification status:")
if is_local_minimum:
    print("SUCCESS: 0 Imaginary modes found. Structure is a valid LOCAL MINIMUM.")
else:
    print(f"WARNING: {len(imaginary_modes)} Imaginary modes detected. Structure is a TRANSITION STATE.")

print(f"\nOptimization log saved to 'optimization.log'")

