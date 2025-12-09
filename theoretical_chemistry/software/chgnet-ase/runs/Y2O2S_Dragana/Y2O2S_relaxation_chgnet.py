#!/usr/bin/env python
from ase import Atoms
from ase.io import write
from ase.io.trajectory import Trajectory

#
# https://github.com/CederGroupHub/chgnet?tab=readme-ov-file#direct-inference-static-calculation
#
from chgnet.model.model import CHGNet
from pymatgen.core import Structure
from chgnet.model import StructOptimizer
from chgnet.model.dynamics import TrajectoryObserver


import numpy as np
import sys
from ase.filters import UnitCellFilter 

sys.stdout.flush()

chgnet = CHGNet.load()
# ==============================================
# ASE full relxation (unitcell + atom) 
# ==============================================

# symmetry 36
structure = Atoms(
    symbols=['Y']*2 + ['O']*2 + ['S']*2,
    positions=[
        [-2.890196310203E-19,  1.594751693307E-01, -4.918647533201E-01],
        [5.000000000000E-01,  4.726721908980E-02,  2.380357226957E-02],
        [5.000000000000E-01, -9.298341801994E-02, -1.091837670567E-01],
        [-3.347838668088E-20,  3.024088010874E-02, -2.779002192326E-01],
        [-1.571439282610E-19,  1.957210783123E-01,  3.116733984587E-05]
    ],
    cell=[
        [3.51815016, 0.0000000000, 0.0000000000],
        [0.000 , 14.99649783, 0.0000000000],
        [0.0000000000, 0.0000000000, 5.72098960]
    ],
    pbc=[True, True, True]
)

#
# set up calculator
# https://chgnet.lbl.gov/api#method-relax

relaxer = StructOptimizer()
print("\nStarting cell relaxation by ASE", flush=True)

traj=TrajectoryObserver(structure)

result = relaxer.relax(structure,save_path='relaxation_path.traj')
#result = relaxer.relax(structure)

#traj.save('path.trj')
print('traj.compute_energy :',traj.compute_energy() )

print("CHGNet relaxed structure", result["final_structure"])
print("relaxed total energy in eV:", result['trajectory'].energies[-1])

# Save final structure
write('final_relaxed_structure.vasp', structure, format='vasp', direct=False)
print("\nFinal relaxed structure saved to: final_relaxed_structure.vasp", flush=True)

# ==============================================
traj = Trajectory('relaxation.traj', 'w', structure)
