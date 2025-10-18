#!/usr/bin/env python
from ase import Atoms
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS
from ase.io.trajectory import Trajectory
from ase.io import read, write
import os
import numpy as np
import sys
sys.stdout.flush()

# ==============================================
# 1. Read atomic Structure
# ==============================================
pdb_file = '1IYT_geopt_pm7water_geo-arc.pdb'

try:
    atoms = read(pdb_file)
    print(f"Successfully read {len(atoms)} atoms from {pdb_file}")
except FileNotFoundError:
    print(f"Error: {pdb_file} not found!")
    sys.exit(1)
except Exception as e:
    print(f"Error reading {pdb_file}: {e}")
    sys.exit(1)

# ==============================================
# 2. Define Calculator Configuration
# ==============================================
# Set MOPAC executable path
mopac_command = f'OMP_NUM_THREADS={os.environ["SLURM_NTASKS"]} MKL_NUM_THREADS={os.environ["SLURM_NTASKS"]} {os.environ["mopac_bin"]}/bin/mopac PREFIX.mop > mopac.log 2>&1'

mopac_calc = MOPAC(
    command=mopac_command,
    label='pm7water',
    task='1SCF gradient',
    method='pm7', 
    charge=0
)

# Set calculator
atoms.calc = mopac_calc

# ==============================================
# 3. Run Geometry Optimization
# ==============================================
print("\nStarting MOPAC optimization...", flush=True)
print("Note: MOPAC reports gradients in kcal/mol·Å; ASE converts to eV/Å", flush=True)

# Create trajectory file to monitor progress
traj = Trajectory('relaxation.traj', 'w', atoms)

# Define optimization (BFGS)
opt = BFGS(atoms, logfile='relaxation.log', trajectory=traj)

try:
    # Run optimization
    opt.run(fmax=0.1)  # Convergence criterion (eV/Å)
    
    # Get final results
    final_HoF = atoms.get_potential_energy()
    final_forces = atoms.get_forces()
    
    # Force analysis
    force_norms = np.linalg.norm(final_forces, axis=1)
    max_force = np.max(force_norms)
    rms_force = np.sqrt(np.mean(force_norms**2))
    
    # Print final results
    print("\n=== Final Results ===", flush=True)
    print(f"Heat of Formation: {final_HoF:.6f} eV", flush=True)
    print(f"Maximum Force: {max_force:.6f} eV/Å", flush=True)
    print(f"RMS Force: {rms_force:.6f} eV/Å", flush=True)
    
    # Save final structure
    xyz_file = f'{mopac_calc.label}_optimized.xyz'
    pdb_file = f'{mopac_calc.label}_optimized.pdb'

    write(xyz_file, atoms, format='xyz')
    write(pdb_file, atoms, format='proteindatabank')
    
    print("\n=== Final structures saved ===", flush=True)
    print(f"  {xyz_file} - XYZ format")
    print(f"  {pdb_file} - PDB format") 

except Exception as e:
    print(f"\nRelaxation failed: {str(e)}")
finally:
    traj.close()