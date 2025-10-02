#!/usr/bin/env python
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.io import write
import os
import numpy as np
import sys
sys.stdout.flush()

# ==============================================
# 1. Quantum Espresso Input Parameters
# ==============================================
pseudopotentials = {
    'Se': 'Se_r.upf',
    'Hg': 'Hg_r.upf'
}

input_data = {
    'control': {
        'verbosity': 'low',
        'tstress': True,
        'tprnfor': True,
        'disk_io': 'minimal',
        'etot_conv_thr' : 1.0D-8,
        'forc_conv_thr' : 1.0D-5,
        'calculation': 'relax'
    },
    'system': {
        'ecutwfc': 90,
        'occupations': 'smearing',
        'smearing': 'gauss',
        'degauss': 0.01,
        'assume_isolated': 'martyna-tuckerman',
        'nosym': True,
        'noinv': True,
        'ibrav': 0,
        'nat': 2,
        'ntyp': 2,
        'noncolin': True,
        'lspinorb': True
    },
    'electrons': {
        'mixing_beta': 0.2,
        'electron_maxstep': 100,
        'diagonalization': 'david',
        'diago_full_acc': True,
        'startingpot': 'atomic',
        'startingwfc': 'atomic+random',
        'conv_thr': 1.0e-9
    }
}

# ==============================================
# 2. Distance range parameters
# ==============================================
#min_distance = 2.0  # Angstrom
#max_distance = 5.0  # Angstrom
#num_points = 20
#distances = np.linspace(min_distance, max_distance, num_points)

# ==============================================
# 3. Set up calculator
# ==============================================
# Set QE bin directory
qe_bin = os.environ["qe_bin"]

# Main QE calculation with full parallelization
pw_command = f'mpirun -np {os.environ["SLURM_NTASKS"]} -machinefile nodes.{os.environ["SLURM_JOB_PARTITION"]}.{os.environ["SLURM_JOB_ID"]} {qe_bin}/bin/pw.x -npool {os.environ["SLURM_JOB_NUM_NODES"]}'

profile = EspressoProfile(
    command=pw_command,
    pseudo_dir='./'
)

qe_calc = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials,
    input_data=input_data,
    kpts=(1, 1, 1),  # Gamma point only for molecule
    koffset=(0, 0, 0)
)

# ==============================================
# 4. Loop over distances and calculate energies
# ==============================================
energies = []

print("Starting Hg-Se distance scan with QE (spin-orbit)...", flush=True)

distance = 2.4
# Create Hg-Se dimer in large box
atoms = Atoms(
    symbols=['Hg', 'Se'],
    positions=[
         [0.0, 0.0, 0.0],           # Hg atom at origin
         [distance, 0.0, 0.0]       # Se atom at specified distance along x-axis
        ],
    cell=[20.0, 20.0, 20.0],       # Large box to isolate the dimer
    pbc=[True, True, True]         # Periodic boundary conditions
)
    
# Set calculator and calculate
atoms.calc = qe_calc
    
try:
    energy = atoms.get_potential_energy()
 #   energies.append(energy)
       
    # Print result for this distance
    #print(f"{distance:.6f}\t{energy:.6f}", flush=True)
        
except Exception as e:
    print(f"{distance:.6f}\tFAILED: {str(e)}", flush=True)

# Save raw data to file
print("\n=== Calculation completed ===", flush=True)
#print("Results saved to hg_se_potential_curve.dat", flush=True)
