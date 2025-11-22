#!/usr/bin/env python
from ase import Atoms
from ase.calculators.lj import LennardJones
from ase.io import write
from ase.optimize import BFGS
from ase.calculators.mixing import SumCalculator

import numpy as np
import sys
from ase.filters import UnitCellFilter 

sys.stdout.flush()

# ==============================================
# ASE full relxation (unitcell + atom) 
# ==============================================

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

#
# set up calculator
#
lj_params = {
   'epsilon': 0.025,  # eV
   'sigma': 2.75,     # Å
    'rc': 10.0  }       # Cutoff radius

calc = SumCalculator([LennardJones(**lj_params) ])

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
