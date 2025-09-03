#!/usr/bin/env python
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.io import write
from ase.optimize import BFGS
import numpy as np
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import os
import sys
sys.stdout.flush()

# ==============================================
# ASE full relxation (unitcell + atom) 
# ==============================================

# ==============================================
# 1. Quantum Espresso Input Parameters
# ==============================================
pseudopotentials = {
    'C': 'C.upf',
    'Hg': 'Hg.upf'
}

input_data = {
    'control': {
        'prefix': 'c_hg',
        'outdir': './tmp',
        'verbosity': 'low',
        'tstress': True,
        'tprnfor': True
    },
    'system': {
        'ecutwfc': 65,
        'occupations': 'smearing',
        'smearing': 'gauss',
        'degauss': 0.01,
        'ibrav': 0,
        'nat': 9,
        'ntyp': 2,
        'assume_isolated': '2D',
        'vdw_corr' : 'DFT-D3'
    },
    'electrons': {
        'conv_thr': 1.0e-10
    }
}

# ==============================================
# 2. Atomic Structure 
# ==============================================
atoms = Atoms(
    symbols=['C']*8 + ['Hg']*1,
    positions=[
		[0.0000000000, 0.0001343939, 7.4560906485],
		[-1.2278839620, 2.1268909992, 7.4560906485],
		[2.4560000900, 0.0000000000, 7.4626892201],
		[1.2278833960, 2.1268909992, 7.4560906485],
		[1.2279287268, 0.7090272405, 7.4599693934],
		[-0.0000003780, 2.8358620390, 7.4599693934],
		[3.6840711172, 0.7090272405, 7.4599693934],
		[2.4559997120, 2.8359442390, 7.4509300145],
		[2.4559997120, 2.8359442390, 10.8382002815]
    ],
    cell=[
		[4.91200017930000, 0.00000000000000, 0.00000000000000],
		[-2.45600065610000, 4.25391661160000, 0.00000000000000],
		[0.00000000000000, 0.00000000000000, 15.00000000000000]
    ],
    pbc=[True, True, True]
)

# ==============================================
# 3. Calculator Configuration
# ==============================================
# Set QE bin directory 
#qe_bin = "/home/dsen/work/bin/qe-7.4.1_serial"
#qe_bin = "/home/dsen/work/bin/qe-7.4.1"
qe_bin = "/usr/bin"

# Job commands
#pw_command = f'{qe_bin}/bin/pw.x'
#pw_command = f'mpirun -np 8 {qe_bin}/bin/pw.x'
pw_command = f'mpirun -np 4 {qe_bin}/pw.x'

pw_profile = EspressoProfile(
    command=pw_command,
    pseudo_dir='./'
)

scf_calc = Espresso(
    profile=pw_profile,
    pseudopotentials=pseudopotentials,
    input_data=input_data,
    #kpts=(1,1,1)  # Fixed k-points
    kpts=(2,2,1)  # Fixed k-points
)

atoms.calc = scf_calc

# ==============================================
# 4. SCF Calculation 
# ==============================================
print("\nRunning SCF calculation...", flush=True)
os.makedirs('tmp', exist_ok=True)

atoms.calc = scf_calc
total_energy = atoms.get_potential_energy()
print(f"  Total energy: {total_energy:.6f} eV", flush=True)

# ==============================================
# 5. Vibrational Analysis
# ==============================================
print("\nStarting vibrational analysis...")

# Run vibrations (focusing only on speific atoms, 0 based index)
vib_atom_index = [8]  
vib = Vibrations(atoms, indices=vib_atom_index, name='vib', delta=0.01)
vib.run()

# Extract frequencies and ensure they're real-valued
all_frequencies = vib.get_frequencies() * 0.001  # in eV
real_frequencies = np.array([freq.real for freq in all_frequencies if freq.imag == 0 and freq.real > 0])
imaginary_frequencies = np.array([freq for freq in all_frequencies if freq.imag != 0 or freq.real <= 0])

print("\nVibrational frequencies (eV):", flush=True)
for i, freq in enumerate(real_frequencies):
    print(f"Mode {i+1}: {freq:.6f} eV", flush=True)

# Warn if there are imaginary frequencies
if len(imaginary_frequencies) > 0:
    print("\n ***WARNING***: Imaginary frequencies detected (indicates possible instability):", flush=True)
    for i, freq in enumerate(imaginary_frequencies):
        print(f"  Mode {i+1}: {np.abs(freq):.6f} eV (i.e., {-freq:.6f} eV imaginary)", flush=True)
    print("\nProceeding with only real frequencies for thermodynamics.\n", flush=True)

# Check if we have valid frequencies
if len(real_frequencies) == 0:
    raise ValueError("No real vibrational frequencies found!")
    
# These are all possible and indicate instability:
#(-5.0 + 0.0j)    # Negative real, zero imaginary → unstable
#(-2.5 + 1.5j)    # Negative real, non-zero imaginary → unstable
#(0.0 + 4.0j)     # Zero real, non-zero imaginary → unstable (pure imaginary)
#(3.0 + 0.0j)     # Positive real, zero imaginary → STABLE (only good case)
    
# ==============================================
# 6. Thermodynamic Analysis
# ==============================================
# Initialize with vibrational frequencies
thermo = HarmonicThermo(vib_energies=np.real(real_frequencies))

# Temperature range and steps
temperatures = np.arange(0, 501, 10)

# Get electronic energy (from prior SCF)
electronic_energy = atoms.get_potential_energy()

print("\nComplete Energy Analysis:", flush=True)
print("="*65, flush=True)
print("Temp(K)   ZPE(eV)   F_thermal(eV)   F_vib(eV)   E_elec(eV)   E_total(eV)", flush=True)
print("-"*65, flush=True)

results = []
for T in temperatures:
    # Calculate components
    zpe = thermo.get_ZPE_correction()
    
    if T == 0:
        F_vib = zpe
        F_thermal = 0.0
    else:
        with np.errstate(divide='ignore', invalid='ignore'):
            F_vib = thermo.get_helmholtz_energy(T, verbose=False)
            F_thermal = F_vib - zpe
    
    total_energy = electronic_energy + F_vib
    results.append([T, zpe, F_thermal, F_vib, electronic_energy, total_energy])
    
    # Print formatted table
    print(f"{T:5.0f}   {zpe:7.6f}   {F_thermal:12.6f}   {F_vib:9.6f}   "
          f"{electronic_energy:10.6f}   {total_energy:10.6f}", flush=True)
         
print("\n=== Thermodynamic Analysis Complete ===", flush=True)
sys.stdout.flush()          
