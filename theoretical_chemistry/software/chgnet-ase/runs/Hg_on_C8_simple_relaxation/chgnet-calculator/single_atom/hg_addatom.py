#!/usr/bin/env python
from ase import Atoms
from ase.io import write

from chgnet.model.model import CHGNet
from pymatgen.core import Structure
from chgnet.model import StructOptimizer
from chgnet.model.dynamics import TrajectoryObserver
import os

# ==============================================
# 2. Atomic Structure 
# ==============================================
hg_atom = Atoms(
    symbols=['Hg'],
    positions=[ # positions in Angstrom
        [10.0000000000, 10.0000000000, 10.0000000000],
    ],
    cell=[ # positions in Angstrom
        [20.0000000000, 0.0000000000, 0.0000000000],
        [0.0000000000, 20.0000000000, 0.0000000000],
        [0.0000000000, 0.0000000000, 20.0000000000]
    ],
    pbc=[True, True, True]
)

relaxer = StructOptimizer()
result = relaxer.relax(hg_atom)

print("CHGNet relaxed structure", result["final_structure"])
print("relaxed total energy in eV:", result['trajectory'].energies[-1])

# Save final structure
write('final_relaxed_structure.vasp', hg_atom, format='vasp', direct=False)
print("\nFinal relaxed structure saved to: final_relaxed_structure.vasp", flush=True)

total_energy = hg_atom.get_potential_energy()
print(f"  Total energy: {total_energy:.6f} eV", flush=True)
