#!/usr/bin/env python
from ase import Atoms
from ase.io import read,write
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

structure=read('../files/mikami.vasp',format='vasp')

#
# set up calculator
# https://chgnet.lbl.gov/api#method-relax

relaxer = StructOptimizer()
print("\nStarting cell relaxation by ASE", flush=True)

traj=TrajectoryObserver(structure)

result = relaxer.relax(structure,save_path='relaxation_path.traj')
#result = relaxer.relax(structure)


print("CHGNet relaxed structure", result["final_structure"])
print("relaxed total energy in eV:", result['trajectory'].energies[-1])

# Save final structure
write('Y2O2S_chgnet_relaxed_structure.vasp', structure, format='vasp', direct=False)
print("\nFinal relaxed structure saved to: final_relaxed_structure.vasp", flush=True)



# ==============================================
#traj = Trajectory('relaxation.traj', 'w', structure)
