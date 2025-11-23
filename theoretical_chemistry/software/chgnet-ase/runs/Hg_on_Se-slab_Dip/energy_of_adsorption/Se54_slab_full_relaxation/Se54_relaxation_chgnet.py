#!/usr/bin/env python
from ase import Atoms
from ase.io import write, read
from ase.io.trajectory import Trajectory

#
# https://github.com/CederGroupHub/chgnet?tab=readme-ov-file#direct-inference-static-calculation
#
from chgnet.model.model import CHGNet
from pymatgen.core import Structure
from chgnet.model import StructOptimizer
from pymatgen.io.ase import AseAtomsAdaptor
#from chgnet.model.dynamics import TrajectoryObserver


import numpy as np
import sys
from ase.filters import UnitCellFilter 

sys.stdout.flush()

chgnet = CHGNet.load()

# ==============================================
# 2. Atomic Structure 
# ==============================================
inpgeomfile='Se54_QE.vasp'
print("\n  Read in QE preoptimized structure ",inpgeomfile)
structure = Structure.from_file(inpgeomfile)
#
# set up calculator
# https://chgnet.lbl.gov/api#method-relax

relaxer = StructOptimizer()
print("\nStarting cell relaxation by ASE", flush=True)

#traj=TrajectoryObserver(structure)
result = relaxer.relax(structure,save_path='relaxation_path.traj')
#result = relaxer.relax(structure)

#traj.save('path.trj')
#print('traj.compute_energy :',traj.compute_energy() )

# Convert to ASE Atoms object
#ase_atoms = AseAtomsAdaptor.get_atoms(structure)
ase_atoms = AseAtomsAdaptor.get_atoms(result["final_structure"])

print("CHGNet relaxed structure", result["final_structure"])
print("relaxed total energy in eV:", result['trajectory'].energies[-1])

# Save final structure
write('Se54_final_relaxed_structure.vasp', ase_atoms, format='vasp', direct=False)
print("\nFinal relaxed structure saved to: final_relaxed_structure.vasp", flush=True)

# ==============================================
#traj = Trajectory('relaxation.traj', 'w', structure)
