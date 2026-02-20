#!/usr/bin/env python
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
import os

# ==============================================
# 1. Quantum Espresso input parameters
# ==============================================
pseudopotentials = {'Si': 'Si.upf'} 

input_data = {
    'control': {
        'calculation': 'scf',
    },
    'system': {
        'ibrav': 0,
        'nat': 2,
        'ntyp': 1,
        'ecutwfc': 30,
        'occupations': 'smearing',
        'smearing': 'gauss',
        'degauss': 0.01

    },
    'electrons': {
        'conv_thr': 1.0e-10
    }
}

# ==============================================
# 2. Atomic Structure 
# ==============================================
atoms = Atoms(
    symbols=['Si']*2,
    positions=[
        [1.3574500000, 4.0723500000, 4.0723500000],
        [0.0000000000, 0.0000000000, 0.0000000000]
    ],
    cell=[
        [0.0000000000, 2.7149000000, 2.7149000000],
        [2.7149000000, 0.0000000000, 2.7149000000],
        [2.7149000000, 2.7149000000, 0.0000000000]
    ],
    pbc=[True, True, True]
)

# ==============================================
# 3. Calculator configuration
# ==============================================
# Set QE bin directory 
#qe_bin = "/home/dsen/work/bin/qe-7.4.1_serial"
qe_bin = "/home/dsen/work/bin/qe-7.4.1"

# Parallel calculation 
#pw_command = f'{qe_bin}/bin/pw.x'
pw_command = f'mpirun -np 4 {qe_bin}/bin/pw.x'

pw_profile = EspressoProfile(
    command=pw_command,
    pseudo_dir='./'
)

# Set k-grids
scf_kpts = (2, 2, 2)

# ==============================================
# 4. SCF calculation
# ==============================================
scf_calc = Espresso(
    profile=pw_profile,
    pseudopotentials=pseudopotentials,
    input_data=input_data,
    kpts=scf_kpts
)

print("\nRunning SCF calculation...", flush=True)
os.makedirs('tmp', exist_ok=True)

atoms.calc = scf_calc
total_energy = atoms.get_potential_energy()
print(f"  Total energy: {total_energy:.6f} eV", flush=True)
fermi_ev = atoms.calc.get_fermi_level()
print(f"  Fermi level: {fermi_ev:.6f} eV", flush=True)