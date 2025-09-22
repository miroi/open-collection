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
        [0.0000000000000000 , 0.0000470574867644,  7.4267968226954775],
        [-1.2279594963498339, 2.1269347053883405,  7.4267968226954775],
        [2.4560000899999999,  0.0000000000000000,  7.4299244612953963],
        [1.2279589303498339,  2.1269347053883378,  7.4267968226954677],
        [1.2279645054112907,  0.7090065990139333,  7.4284076745439043],
        [-0.0000003780000000,  2.8359033388838224,  7.4284076745439043],
        [3.6840353385887141,  0.7090065990139333,  7.4284076745439043],
        [2.4559997120000001,  2.8359442389999998,  7.4256602058196215],
        [2.4559997120000001,  2.8359442389999998, 11.0788018647677582]
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
#qe_bin = "/usr/bin"
qe_bin = "/home/milias/work/software/qe/q-e-devel/build_gnu_mkl/bin"

# Job commands
#pw_command = f'{qe_bin}/bin/pw.x'
pw_command = f'mpirun -np 6 {qe_bin}/pw.x'

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
    opt.run(fmax=0.001) # Convergence criterion: max force < 0.001 eV/Å
        
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
