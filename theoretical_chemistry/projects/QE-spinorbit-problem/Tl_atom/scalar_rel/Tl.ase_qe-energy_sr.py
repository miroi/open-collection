#!/usr/bin/env python
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
#from dftd4.ase import DFTD4
from ase.io import write
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import os
import sys
sys.stdout.flush()  # Force immediate output

# ==============================================
# 1. Quantum Espresso Input Parameters
# ==============================================
pseudopotentials = {
    'Tl': 'Tl.upf'
}

input_data = {
    'control': {
        'verbosity': 'high',
        'disk_io': 'minimal'
    },
    'system': {
        'ecutwfc': 90,
        'occupations': 'smearing',
        'smearing' : 'gaussian',
        'degauss' : 0.02,
        'assume_isolated': 'martyna-tuckerman',
        'nosym': True,
        'ibrav': 0,
        'nat': 1,
        'ntyp': 1,
        'noncolin': False,
        'lspinorb': False 
    },
    'electrons': {
        'mixing_beta': 0.2,
        'electron_maxstep': 100,
        'diagonalization': 'david',
        'diago_full_acc': True,
        'startingpot': 'atomic',
        'startingwfc': 'atomic+random',
        'conv_thr': 1.0e-10
    }
}

# ==============================================
# 2. Cluster-Specific Command Setup
# ==============================================
# Set QE bin directory
#qe_bin = "/lustre/home/user/m/milias/work/software/quantum-espresso/qe-develop/q-e/build_inteloneapimpi_mkl_scalapack"
qe_bin = os.environ["qe_bin"]

# Main QE calculation with full parallelization
pw_command = f'mpirun -np {os.environ["SLURM_NTASKS"]} -machinefile nodes.{os.environ["SLURM_JOB_PARTITION"]}.{os.environ["SLURM_JOB_ID"]} {qe_bin}/bin/pw.x -npool {os.environ["SLURM_JOB_NUM_NODES"]}'

profile = EspressoProfile(
    command=pw_command,
    pseudo_dir='./'
)

# ==============================================
# 3. Atomic Structure and Cell Parameters
# ==============================================
atoms = Atoms(
    symbols=['Tl'],
    positions=[ # positions in Angstrom
        [10.0000000000, 10.0000000000, 10.0000000000],
    ],
    cell=[ # positions in Angstrom
        [20.0000000000, 0.0000000000, 0.0000000000],
        [0.0000000000, 20.0000000000, 0.0000000000],
        [0.0000000000, 0.0000000000, 20.0000000000]
    ],
    pbc=[True, True, True]
)
# ==============================================
# 4. Set Constraints
# ==============================================

#fixed_indices = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52]
#constraint = FixAtoms(indices=fixed_indices)
#atoms.set_constraint(constraint)

# ==============================================
# 4. Define Calculator Configuration
# ==============================================
qe_calc = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials,
    input_data=input_data,
    kpts=(1, 1, 1), 
    koffset=(0, 0, 0) 
)


#dftd4_calc = DFTD4(
#    method="PBE",
#    verbose=True,
#)
#from ase.calculators.mixing import SumCalculator
#combined_calc = SumCalculator([qe_calc, dftd4_calc])
#atoms.calc = combined_calc

# ==============================================
# 5. Run SCF Calculation
# ==============================================

#print("\nStarting SCF total energy calculation with QE+D4...", flush=True)
print("\nStarting SCF total energy calculation with QE...", flush=True)

# Get total energy (QE+D4) from combined calculator
#total_energy = combined_calc.get_potential_energy(atoms)

# Get individual components
qe_energy = qe_calc.get_potential_energy(atoms)
#d4_energy = dftd4_calc.get_potential_energy(atoms)

# Verify sum matches combined energy
#tolerance = 1e-6  # eV
#sum_energy = qe_energy + d4_energy
#energy_diff = abs(total_energy - sum_energy)

print("\nSCF Energy Results:", flush=True)
print(f"  QE Electronic Energy: {qe_energy:.6f} eV", flush=True)
#print(f"  DFT-D4 Dispersion:    {d4_energy:.6f} eV", flush=True)
#print(f"  Sum (QE + D4):        {sum_energy:.6f} eV", flush=True)
#print(f"  Total Energy (QE+D4): {total_energy:.6f} eV", flush=True)

# Force final flush
sys.stdout.flush()
