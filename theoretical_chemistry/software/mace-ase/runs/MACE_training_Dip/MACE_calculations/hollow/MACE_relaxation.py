#!/usr/bin/env python
from ase import Atoms
from ase.io import read, write
from ase.optimize import BFGS
from ase.io.trajectory import Trajectory
from mace.calculators import MACECalculator
import os
import numpy as np
import sys
sys.stdout.flush()

# ==============================================
# 1. Atomic Structure
# ==============================================
vasp_file = 'hollow.vasp'

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
# 2. Calculator Configuration (MACE)
# ==============================================
model_path = '../../MACE_GrapheneHg_stagetwo.model'

mace_calc = MACECalculator(
    model_paths=model_path,
    device='cpu',          # change to 'cuda' if GPU available
    default_dtype='float64'
)
atoms.calc = mace_calc

# ==============================================
# 3. Atom Relaxation
# ==============================================
print("Starting atom relaxation with MACE forces via ASE...", flush=True)

# Create trajectory file
traj = Trajectory('hollow_MACE.traj', 'w', atoms)

# Define optimization (BFGS)
opt = BFGS(atoms, logfile='hollow_MACE.log', trajectory=traj)

try:
    # Run optimization
    opt.run(fmax=0.01)  # Convergence criterion

    # Calculate final energy
    total_energy = atoms.get_potential_energy()

    # Print final energy
    print("\n=== Final Relaxation Results ===", flush=True)
    print(f"\nEnergy Components:", flush=True)
    print(f"  MACE Total Energy:       {total_energy:>12.6f} eV", flush=True)

    # Get final forces from the optimizer's atoms (fail-safe with filters)
    forces = opt.atoms.get_forces()

    # Force analysis
    force_norms = np.linalg.norm(forces, axis=1)  # Euclidean norms
    max_force = np.max(force_norms)               # ASE-style max norm

    # Print results
    print("\nFinal forces", flush=True)
    print(f"  ASE-style max force (norm)    : {max_force:>8.6f} eV/Å", flush=True)

    # Save final structure
    write('relaxed_hollow_MACE.vasp', atoms, format='vasp', direct=False)
    print("\n=== Final structure saved to: 'relaxed_hollow_MACE.vasp' ===")

except Exception as e:
    print(f"\nRelaxation failed: {str(e)}")
finally:
    traj.close()