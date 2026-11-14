import io, contextlib
import numpy as np
from ase.build import molecule
from jarvis.core.atoms import ase_to_atoms
from alignn.pretrained import get_prediction

TARGETS = ["HOMO", "LUMO", "gap", "alpha", "ZPVE", "U0", "U", "G"]

def predict(name, cutoff):
    atoms = molecule(name)
    atoms.center(vacuum=8.0)
    atoms.pbc = True
    jatoms = ase_to_atoms(atoms)
    out = {}
    for t in TARGETS:
        with contextlib.redirect_stdout(io.StringIO()):
            v = get_prediction(model_name=f"qm9_{t}_alignn", atoms=jatoms, cutoff=cutoff)
        out[t] = float(np.ravel(v)[0])
    return out

results = {}
for mol in ["CH4", "H2O"]:
    for cutoff in [5.0, 8.0]:
        results[(mol, cutoff)] = predict(mol, cutoff)

print(f"{'target':8s}" + "".join(f"{m}@{c:<4}".rjust(12) for (m, c) in results))
for t in TARGETS:
    print(f"{t:8s}" + "".join(f"{r[t]:12.4f}" for r in results.values()))

# QM9 values for methane from memory (check against the dataset):
# HOMO -0.3877 Ha (-10.55 eV), LUMO 0.1171 Ha (3.19 eV), gap 0.5048 Ha (13.74 eV),
# alpha 13.21 bohr^3, ZPVE 0.0447 Ha (1.22 eV), U0 -40.479 Ha (-1101.5 eV)
