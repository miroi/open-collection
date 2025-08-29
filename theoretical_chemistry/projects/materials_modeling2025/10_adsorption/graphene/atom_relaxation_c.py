#!/usr/bin/env python
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.io import write
from ase.optimize import BFGS
import numpy as np
import sys
from ase.filters import UnitCellFilter 
sys.stdout.flush()

# ==============================================
# ASE full relxation (unitcell + atom) 
# ==============================================

# ==============================================
# 1. Quantum Espresso Input Parameters
# ==============================================
pseudopotentials = {
    'C': 'C.upf'
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
        'nat': 8,
        'ntyp': 1,
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
    symbols=['C']*8,
    positions=[
        [0.000000000, 0.000000000, 7.500000000],
        [-1.228000328, 2.126958306, 7.500000000],
        [2.456000090, 0.000000000, 7.500000000],
        [1.227999762, 2.126958306, 7.500000000],
        [1.227999877, 0.708986060, 7.500000000],
        [-0.000000378, 2.835944239, 7.500000000],
        [3.683999967, 0.708986060, 7.500000000],
        [2.455999712, 2.835944239, 7.500000000]
    ],
    cell=[
        [4.9120001793, 0.0000000000, 0.0000000000],
        [-2.4560006561 , 4.2539166116, 0.0000000000],
        [0.0000000000, 0.0000000000, 15.0000000000]
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
pw_command = f'mpirun -np 10 {qe_bin}/pw.x'

pw_profile = EspressoProfile(
    command=pw_command,
    pseudo_dir='./'
)

calc = Espresso(
    profile=pw_profile,
    pseudopotentials=pseudopotentials,
    input_data=input_data,
    #kpts=(1,1,1)  # Fixed k-points
    kpts=(2,2,1)  # Fixed k-points
)

atoms.calc = calc

# ==============================================
# 4. Cell Relaxation
# ==============================================
print("\nStarting cell relaxation by ASE", flush=True)

# Create a trajectory file to store relaxation steps
from ase.io.trajectory import Trajectory
traj = Trajectory('relaxation.traj', 'w', atoms)

# Pass the Trajectory object to BFGS 
opt = BFGS(atoms, trajectory=traj, logfile='relaxation.log')

try:
    opt.run(fmax=0.01) # Convergence criterion: max force < 0.01 eV/Å
        
    # Get final results
    final_energy = atoms.get_potential_energy()
    forces = opt.atoms.get_forces()
    qe_style_forces = atoms.get_forces() 
    stress = atoms.get_stress()
     
    # Analysis
    force_norms = np.linalg.norm(forces, axis=1)  # Euclidean norms
    max_force = np.max(force_norms)               # ASE-style max norm
    max_qe_force = np.max(np.abs(qe_style_forces)) # Max component across all atoms/directions
    pressure = -np.sum(stress[:3]) * 1602.1766208 / 3

    # Print results
    print("\nFinal results", flush=True)    
    print(f"  Total Energy                  : {final_energy:>12.6f} eV", flush=True)
    print(f"  ASE-style max force (norm)    : {max_force:>8.6f} eV/Å", flush=True)
    print(f"  QE-style max force            : {max_qe_force:>8.6f} eV/Å", flush=True)
    print(f"  Pressure                      : {pressure:>8.6f} kbar", flush=True)

    # Save final structure
    write('final_relaxed_structure.vasp', atoms, format='vasp', direct=False)
    print("\nFinal relaxed structure saved to: final_relaxed_structure.vasp", flush=True)

except Exception as e:
    print(f"\nRelaxation failed: {str(e)}", flush=True)
    print("Check output files for error details", flush=True)
finally:
    traj.close()
    print("\nRelaxation complete", flush=True)
