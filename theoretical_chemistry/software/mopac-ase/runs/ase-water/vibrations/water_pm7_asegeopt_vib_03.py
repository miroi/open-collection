import os
import sys
import numpy as np
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS
from ase.io import write
from ase.vibrations import Vibrations

# 1. Set the environment variable for the MOPAC executable path
mopac_exec = '/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac'
os.environ['ASE_MOPAC_COMMAND'] = f'{mopac_exec} PREFIX.mop > /dev/null 2>&1'

# 2. Generate the initial water molecule
system = molecule('H2O')
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)
print(f"\n--- ASE prepared H2O molecule geometry ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")

# 3. Set up the calculator
calc = MOPAC(method='PM7', task='1SCF GRADIENTS')
system.calc = calc

# 4. Run optimization with tighter convergence
print("\nStarting geometry optimization...")
opt = BFGS(system, trajectory='opt.traj', logfile='optimization.log')
opt.run(fmax=0.0001)  # Tighter convergence for vibrational analysis

# 5. Extract optimized geometry
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)
print(f"\n--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")

# 6. Save optimized structure
xyz_filename = 'optimized_water.xyz'
write(xyz_filename, system)
print(f"\nOptimized structure saved to '{xyz_filename}'")

# 7. Run vibrational analysis with the SAME calculator
print("\n--- Running Vibrational Analysis ---")
vib = Vibrations(system, name='vib_data')
vib.run()

# 8. Get frequencies
frequencies = vib.get_frequencies()
vib.clean()  # Remove temporary files

# 9. Parse MOPAC output for additional info
heat_of_formation = "Unknown"
charges = []
out_filename = 'mopac.out'

if os.path.exists(out_filename):
    with open(out_filename, 'r') as f:
        lines = f.readlines()
    
    for idx, line in enumerate(lines):
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

# 10. Evaluate vibrational stability with threshold
# Frequencies below 10 cm^-1 are considered numerical noise
THRESHOLD = 10.0  # cm^-1

imaginary_modes = []
for idx, freq in enumerate(frequencies):
    if freq.imag > 0 or freq.real < 0:
        val = freq.imag if freq.imag > 0 else abs(freq.real)
        if val > THRESHOLD:  # Only count significant imaginary modes
            imaginary_modes.append((idx, val))
        else:
            # These are just numerical noise, treat as zero
            # We'll keep the frequency but note it's negligible
            pass

is_local_minimum = len(imaginary_modes) == 0

# 11. Print results
print(f"\n--- Computational Environment ---")
print(f"MOPAC Executable : {mopac_exec}")

print(f"\n--- Thermodynamic Results ---")
print(f"Heat of Formation: {heat_of_formation}")

print(f"\n--- Net Atomic Charges ---")
for idx, sym, chg in charges:
    print(f"Atom {idx:>2} ({sym:<2}) : {chg:>8} e")

print(f"\n--- Vibrational Stability Check ---")
print("Calculated Normal Modes (cm⁻¹):")
for idx, freq in enumerate(frequencies):
    if freq.imag > 0 or freq.real < 0:
        val = freq.imag if freq.imag > 0 else abs(freq.real)
        if val > THRESHOLD:
            print(f"  Mode {idx}: {val:>8.1f}i cm⁻¹ (IMAGINARY MODE)")
        else:
            print(f"  Mode {idx}: {val:>8.1f}i cm⁻¹ (negligible - numerical noise)")
    else:
        print(f"  Mode {idx}: {freq.real:>8.1f}  cm⁻¹")

print(f"\nStructure verification status:")
if is_local_minimum:
    print("✓ SUCCESS: No significant imaginary modes (>10 cm⁻¹) found.")
    print("  Structure is a valid LOCAL MINIMUM.")
else:
    print(f"⚠ WARNING: {len(imaginary_modes)} significant imaginary modes detected.")
    print("  Structure may be a TRANSITION STATE.")
    print("\nTo resolve imaginary modes:")
    print("  1. Use a different optimizer: LBFGS or FIRE")
    print("  2. Try a larger displacement for the vibrational analysis")
    print("  3. The imaginary modes might indicate the molecule is floppy")

# 12. Save frequencies to file
with open('frequencies.txt', 'w') as f:
    f.write("# Vibrational frequencies (cm^-1)\n")
    f.write("# Mode  Frequency\n")
    for idx, freq in enumerate(frequencies):
        if freq.imag > 0 or freq.real < 0:
            val = freq.imag if freq.imag > 0 else abs(freq.real)
            if val > THRESHOLD:
                f.write(f"{idx:>4}  {val:>8.1f}i\n")
            else:
                f.write(f"{idx:>4}  {val:>8.1f}i (negligible)\n")
        else:
            f.write(f"{idx:>4}  {freq.real:>8.1f}\n")
    f.write("\n")
    f.write(f"Is local minimum: {is_local_minimum}\n")
    f.write(f"Number of significant imaginary modes: {len(imaginary_modes)}\n")
    f.write(f"Threshold used: {THRESHOLD} cm^-1\n")

print(f"\nFrequencies saved to 'frequencies.txt'")

# 13. Clean up MOPAC temporary files if desired
# Comment out if you want to keep them for inspection
# for ext in ['.mop', '.out', '.arc', '.aux']:
#     if os.path.exists(f'mopac{ext}'):
#         os.remove(f'mopac{ext}')
