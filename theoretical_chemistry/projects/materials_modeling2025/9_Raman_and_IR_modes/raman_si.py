#!/usr/bin/env python
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
import os
import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import shutil
sys.stdout.flush() 

# ==============================================
# ASE DFPT Raman calculation
# Note: LDA + Norm-conserving psp needed for Raman
# ==============================================

# ==============================================
# 1. Quantum Espresso input parameters
# ==============================================
pseudopotentials = {'Si': 'Si.pz-vbc.UPF'} 

base_input_data = {
    'control': {
        'prefix': 'si_scf',
        'outdir': './tmp',
        'verbosity': 'low',
        'tstress': True,
        'tprnfor': True,
        'disk_io': 'high'
    },
    'system': {
        'ecutwfc': 30,
        'ecutrho': 240,
        'occupations': 'fixed',
        'ibrav': 0,
        'nat': 2,
        'ntyp': 1
    },
    'electrons': {
        'conv_thr': 1.0e-8
    }
}

# ==============================================
# 2. Atomic Structure 
# ==============================================
atoms = Atoms(
    symbols=['Si']*2,
    positions=[ # positions in Angstrom
        [1.3669840665567621, 4.1009521996702860, 4.1009521996702860],
        [0.0000000000000000, 0.0000000000000000, 0.0000000000000000]
    ],
    cell=[ # positions in Angstrom
        [-0.0000000000000000, 2.7339681331135242, 2.7339681331135242],
        [2.7339681331135242, 0.0000000000000000, 2.7339681331135242],
        [2.7339681331135242, 2.7339681331135242, 0.0000000000000000]
    ],
    pbc=[True, True, True]
)

# ==============================================
# 3. Calculator configuration
# ==============================================
# Set QE bin directory 
qe_bin = "/home/dsen/work/bin/qe-7.4.1_serial"
#qe_bin = "/home/dsen/work/bin/qe-7.4.1"

# Parallel calculation 
pw_command = f'{qe_bin}/bin/pw.x'
#pw_command = f'mpirun -np 4 {qe_bin}/bin/pw.x'
ph_command = f'{qe_bin}/bin/ph.x < ph.in > ph.out 2>&1'
#ph_command = f'mpirun -np 4 {qe_bin}/bin/ph.x < ph.in > ph.out 2>&1'

# Serial post-processing commands for fast execution
dynmat_command = f'{qe_bin}/bin/dynmat.x < dynmat.in > dynmat.out 2>&1'

pw_profile = EspressoProfile(
    command=pw_command,
    pseudo_dir='./'
)

# Set k-grids
scf_kpts = (2, 2, 2)

# QE tool 
def run_qe_tool(command, input_file, tool_name):
    """Run QE tool with input file and redirect output to file"""
    try:
        with open(input_file, 'r') as fin:
            subprocess.run(command, shell=True, stdin=fin, check=True)
        print(f"  {tool_name} completed successfully", flush=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running {tool_name}: {e}", flush=True)
        return False

# ==============================================
# 4. SCF calculation
# ==============================================
scf_input_data = base_input_data.copy()
scf_input_data['control']['calculation'] = 'scf'

scf_calc = Espresso(
    profile=pw_profile,
    pseudopotentials=pseudopotentials,
    input_data=scf_input_data,
    kpts=scf_kpts
)

print("\nRunning SCF calculation...", flush=True)
os.makedirs('tmp', exist_ok=True)
atoms.calc = scf_calc
total_energy = atoms.get_potential_energy()
print(f"  Total energy: {total_energy:.6f} eV", flush=True)

# ==============================================
# 5. DFPT phonon calculation (Gamma only)
# ==============================================
print("\nRunning DFPT phonon calculation...", flush=True)

with open('ph.in', 'w') as f:
    f.write(f"""&INPUTPH
   prefix = '{base_input_data['control']['prefix']}',
   outdir = '{base_input_data['control']['outdir']}',
   tr2_ph = 1.0e-12,
   amass(1) = 28.0855,
   epsil = .true.,
   trans = .true.,
   lraman = .true.,
   fildyn = 'si.dyn',
   ldisp = .false.
/
0.0 0.0 0.0
""")

run_qe_tool(ph_command, 'ph.in', 'ph.x')

# ==============================================
# 6. Raman Calculation 
# ==============================================
print("\nCalculating Raman spectra...", flush=True) 

with open('dynmat.in', 'w') as f:
    f.write("""&INPUT
   fildyn = 'si.dyn',
   asr = 'crystal',
/
""")

run_qe_tool(dynmat_command, 'dynmat.in', 'dynmat.x')

# ==============================================
# 7. Clean up and organize files
# ==============================================
print("\nCleaning up and organizing files...", flush=True)
os.makedirs('vibrational_results', exist_ok=True)

# Move all calculation files to results directory
for fname in os.listdir('.'):
    if (fname in ['ph.in', 'ph.out', 'espresso.pwi', 'espresso.pwo', 'espresso.err'] or
        fname.endswith(('.dyn', '.in', '.mold', '.axsf')) or
        fname.startswith(('drho_e'))):
        shutil.move(fname, os.path.join('vibrational_results', fname))

print("  Moved all vibrational calculation files to vibrational_results directory", flush=True)

print("\n=== Raman Calculation Complete ===", flush=True)
print("Generated files:", flush=True)
print("- SCF calculation files: tmp/", flush=True)
print("- Phonon calculation files: vibrational_results/ph.*", flush=True)
print("- Dynamical matrix files: vibrational_results/si.dyn*", flush=True)
print("- Final Raman and IR data: dynmat.out", flush=True)