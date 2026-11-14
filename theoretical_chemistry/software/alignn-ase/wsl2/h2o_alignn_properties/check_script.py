import inspect, traceback
import numpy as np
from ase.build import molecule
from jarvis.core.atoms import ase_to_atoms
from alignn.pretrained import get_prediction, get_all_models

atoms = molecule("H2O"); atoms.center(vacuum=8.0); atoms.pbc = True
jatoms = ase_to_atoms(atoms)

models = get_all_models()
print("type of get_all_models():", type(models))
if isinstance(models, dict):
    print("entry:", models.get("qm9_HOMO_alignn"))

print("\nget_prediction signature:", inspect.signature(get_prediction))
print("\n--- first lines of get_prediction ---")
print("\n".join(inspect.getsource(get_prediction).splitlines()[:40]))

print("\n--- full traceback for HOMO ---")
try:
    print(get_prediction(model_name="qm9_HOMO_alignn", atoms=jatoms))
except Exception:
    traceback.print_exc()
