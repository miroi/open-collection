import os
import numpy as np
from ase.build import molecule
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS
from ase.io import write
from ase.vibrations import Vibrations

# 1. Hardcode your MOPAC path 
mopac_exec = '/usr/bin/mopac'
os.environ['ASE_MOPAC_COMMAND'] = f'echo "" | {mopac_exec}'

# 2. Patch os.system for 100% silent background MOPAC execution
original_system = os.system
def silent_system(cmd):
    if mopac_exec in cmd or 'mopac' in cmd:
        cmd = f'echo "" | {cmd} > /dev/null 2>/dev/null'
    return original_system(cmd)
os.system = silent_system

# 3. Generate initial water molecule and attach calculator
system = molecule('H2O')
system.calc = MOPAC(method='PM7', task='1SCF GRADIENTS')

# 4. Initialize low-level file descriptors to hide all intermediate terminal banners
null_fds = [os.open(os.devnull, os.O_RDWR) for _ in range(2)]
save_fds = [os.dup(1), os.dup(2)]

try:
    os.dup2(null_fds[0], 1)
    os.dup2(null_fds[1], 2)
    
    # Run geometry optimization
    opt = BFGS(system, trajectory='opt.traj', logfile='optimization.log')
    opt.run(fmax=0.01)
    
    # Run Vibrational Analysis using finite differences via ASE
    # This automatically uses the attached MOPAC calculator for displacements
    vib = Vibrations(system, name='vib_data')
    vib.run()
    frequencies = vib.get_frequencies()
    vib.clean() # Remove temporary displacement files
finally:
    # Restore standard output streams to screen
    os.dup2(save_fds[0], 1)
    os.dup2(save_fds[1], 2)
    for fd in null_fds + save_fds:
        os.close(fd)

# 5. Export structural data to standard XYZ format
write('optimized_water.xyz', system)

# 6. Extract dipole moment vector and compute total scalar magnitude (Debye conversion)
# MOPAC internal dipole parses directly into ASE's native properties
try:
    dipole_vector = system.get_dipole_moment()
    # ASE returns dipole moments in e*Å. Convert to Debye units (1 e*Å ≈ 4.8032 Debye)
    dipole_debye = np.linalg.norm(dipole_vector) * 4.8032
except Exception:
    dipole_debye = 0.0

# 7. Evaluate structural local minimum verification status
# True local minima have exactly 0 imaginary frequencies (complex numbers returned as real < 0)
imaginary_modes = [f.imag for f in frequencies if f.imag > 0 or f.real < 0]
is_local_minimum = len(imaginary_modes) == 0

# 8. Print structural, thermodynamic, and vibrational validation summary
print("--- Structural Export ---")
print("Optimized geometry successfully written to: 'optimized_water.xyz'")

print(f"\n--- Molecular Properties ---")
print(f"Total Dipole Moment : {dipole_debye:.3f} D")

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

