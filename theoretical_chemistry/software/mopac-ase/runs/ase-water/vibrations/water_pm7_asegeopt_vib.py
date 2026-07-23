import os
import sys
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS
from ase.io import write
from ase.vibrations import Vibrations

# 1. Set the environment variable for the MOPAC executable path
#os.environ['ASE_MOPAC_COMMAND'] = 'path/to/mopac'
#os.environ['ASE_MOPAC_COMMAND'] = '/home/milias/work/software/mopac/mopac-23.2.3-linux/bin/mopac'
#os.environ['ASE_MOPAC_COMMAND'] = '/usr/bin/mopac'
#os.environ['ASE_MOPAC_COMMAND'] = '/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac'
mopac_exec='/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac'
#os.environ['ASE_MOPAC_COMMAND'] = '/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac  PREFIX.mop '
os.environ['ASE_MOPAC_COMMAND'] = '/home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac  PREFIX.mop  > /dev/null 2>&1 '

# 2. Generate the initial water molecule
system = molecule('H2O')
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)
print(f"\n--- ASE prepared H2O molecule geometry  ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")

# 3. Suppress MOPAC's stdout by redirecting it to devnull during calculation
# Note: MOPAC prints directly to stdout bypasses ASE's logfile controls
system.calc = MOPAC(method='PM7', task='1SCF GRADIENTS')

# 4. Run optimization with a clean logfile and restore standard output
# Setting logfile='optimization.log' redirects the BFGS step information
opt = BFGS(system, trajectory='opt.traj', logfile='optimization.log')
opt.run(fmax=0.01)

vib = Vibrations(system, name='vib_data')
vib.run()
frequencies = vib.get_frequencies()
vib.clean()  # Remove temporary displacement calculation files


# 5. Extract finalized structural parameters
r_oh1 = system.get_distance(0, 1)
r_oh2 = system.get_distance(0, 2)
angle_hoh = system.get_angle(1, 0, 2)

# Save the finalized structural model to a standard file format
xyz_filename = 'optimized_water.xyz'
write(xyz_filename, system)


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

# 9. Evaluate structural local minimum verification status
# True local minima have exactly 0 imaginary/negative modes.
imaginary_modes = [f for f in frequencies if f.imag > 0 or f.real < 0]
is_local_minimum = len(imaginary_modes) == 0


# 8. Print clean terminal results and parsed quantum data
print("--- Computational Environment ---")
print(f"MOPAC Executable : {mopac_exec}")
print(f"MOPAC Version    : {mopac_version}")

print(f"\n--- Thermodynamic Results ---")
print(f"Heat of Formation: {heat_of_formation}")

print(f"\n--- Net Atomic Charges ---")
for idx, sym, chg in charges:
    print(f"Atom {idx:>2} ({sym:<2}) : {chg:>8} e")


# 6. Print the structural results
print(f"\n--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")
print(f"\nOptimization log saved to 'optimization.log'")

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

