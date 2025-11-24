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

# ==============================================
# 2. Atomic Structure 
# ==============================================
structure = Atoms(
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
