#!/usr/bin/env python
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
##from dftd4.ase import DFTD4
from ase.io import read, write
from ase.optimize import BFGS
from ase.io.trajectory import Trajectory
#from ase.constraints import FixAtoms
#from ase.filters import UnitCellFilter 
from ase.calculators.mixing import SumCalculator
##from dftd4.interface import DampingParam
##from dftd4.parameters import get_damping_param
import os
import numpy as np
import sys
sys.stdout.flush()

# ==============================================
# 1. Quantum Espresso Input Parameters
# ==============================================
pseudopotentials = {
    'Na': 'Na.upf',
    'Cl': 'Cl.upf'
}

input_data = {
    'control': {
        'prefix': 'NaCl',
        'outdir': './tmp',
        'verbosity': 'low',
        'tstress': True,
        'tprnfor': True,
        'disk_io': 'minimal'
    },
    'system': {
        'input_dft': 'XC-000I-000I-116L-133L-000I-000I',
        'ecutwfc': 90,
        'occupations': 'smearing',
        'smearing': 'gauss',
        'degauss': 0.01,
#       'assume_isolated': '2D',
#        'nosym': True,
#        'noinv': True,
        'ibrav': 0,
        'nat': 8,
        'ntyp': 2,
#        'noncolin': True,
#        'lspinorb': True
    },
    'electrons': {
        'mixing_beta': 0.2,
        'electron_maxstep': 100,
        'diagonalization': 'david',
        'diago_full_acc': True,
        'startingpot': 'atomic',
        'startingwfc': 'atomic+random',
        'conv_thr': 1.0e-9,
    }
}

# ==============================================
# 2. Import atomic structure
# ==============================================
vasp_file = 'nacl.vasp'  

try:
    atoms = read(vasp_file, format='vasp')
    print(f"Successfully read {len(atoms)} atoms from {vasp_file}")
except FileNotFoundError:
    print(f"Error: {vasp_file} not found!")
    sys.exit(1)
except Exception as e:
    print(f"Error reading {vasp_file}: {e}")
    sys.exit(1)

# ==============================================
# 3. Set Constraints
# ==============================================

#fixed_indices = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52]
#constraint = FixAtoms(indices=fixed_indices)
#atoms.set_constraint(constraint)

# ==============================================
# 4. Define Calculator Configuration
# ==============================================
# Set QE bin directory
qe_bin = os.environ["QE"]

# Main QE calculation with full parallelization
#pw_command = f'/lustre/projects/m/milias/work/software/openmpi/openmpi-5.0.9-intelv2025.3.1/install_openmpi-5.0.9-intelv2025.3.1/bin/mpirun -v -np {os.environ["SLURM_NTASKS"]} -machinefile nodes.{os.environ["SLURM_JOB_PARTITION"]}.{os.environ["SLURM_JOB_ID"]} --bind-to core:overload-allowed {qe_bin}/bin/pw.x -npool {os.environ["SLURM_JOB_NUM_NODES"]}'
pw_command = f'mpirun -np {os.environ["SLURM_NTASKS"]} -machinefile nodes.{os.environ["SLURM_JOB_PARTITION"]}.{os.environ["SLURM_JOB_ID"]} {qe_bin}/bin/pw.x -npool {os.environ["SLURM_JOB_NUM_NODES"]}'

profile = EspressoProfile(
    command=pw_command,
    pseudo_dir='./'
)

qe_calc = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials,
    input_data=input_data,
    kpts=(2, 2, 2), 
#    koffset=(1, 1, 0) 
)


atoms.calc = qe_calc 

# ==============================================
# 5. Run Cell Relaxation (Slab, Cell Angles Fixed)
# ==============================================

print("Starting atom relaxation with QE forces via ASE...")

# Create trajectory file
traj = Trajectory('relaxation.traj', 'w', atoms)

# Define optimization (BFGS)
opt = BFGS(atoms, logfile='relaxation.log', trajectory=traj)

try:
    # Run optimization
    opt.run(fmax=0.01)  # Convergence criterion
    
    # Get final relaxed structure
    relaxed_atoms = atoms  # For atomic relaxation, atoms object is updated in-place
    
    # Calculate final energies
    qe_energy = qe_calc.get_potential_energy(relaxed_atoms)
    total_energy = qe_energy
    
    # Print final energies
    print("\n=== Final Relaxation Results ===")
    print(f"\nEnergy Components:")
    print(f"  Total Energy (QE ):  {total_energy:>12.6f} eV", flush=True)
    
    # Get final forces and stress
    forces = opt.atoms.get_forces() # From ASE relaxation steps
    qe_style_forces = relaxed_atoms.get_forces() 
    stress = relaxed_atoms.get_stress() #ASE is using QE+DFT-D4 forces, use QE stress for publication
    
    # Force analysis
    force_norms = np.linalg.norm(forces, axis=1)  # Euclidean norms
    max_force = np.max(force_norms)               # ASE-style max norm
    max_qe_force = np.max(np.abs(qe_style_forces)) # Max component across all atoms/directions
    pressure = -np.sum(stress[:3]) * 1602.1766208 / 3 #kbar
     
    # Print results
    print("\nFinal forces and stress", flush=True)    
    print(f"  ASE-style max force (norm)    : {max_force:>8.6f} eV/Å", flush=True)
    print(f"  QE-style max force            : {max_qe_force:>8.6f} eV/Å", flush=True)
    print(f"  Pressure                      : {pressure:>8.6f} kbar", flush=True)
    
    # Save final structure
    write('final_relaxed_structure.vasp', relaxed_atoms, format='vasp', direct=True)
    print("\n=== Final structure saved to: 'final_relaxed_structure.vasp' ===", flush=True)
    
    # Force final flush
    sys.stdout.flush()

except Exception as e:
    print(f"\nRelaxation failed: {str(e)}")
finally:
    traj.close()
