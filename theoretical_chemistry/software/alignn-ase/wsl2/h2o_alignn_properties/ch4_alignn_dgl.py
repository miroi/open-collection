import io, contextlib
import numpy as np
from ase.build import molecule
from jarvis.core.atoms import ase_to_atoms, Atoms as JAtoms
from alignn.pretrained import get_prediction

TARGETS = ["HOMO", "LUMO", "gap", "alpha", "ZPVE", "U0", "U", "G"]

def predict(jatoms, cutoff=5.0):
    out = {}
    for t in TARGETS:
        with contextlib.redirect_stdout(io.StringIO()):
            v = get_prediction(model_name=f"qm9_{t}_alignn", atoms=jatoms, cutoff=cutoff)
        out[t] = float(np.ravel(v)[0])
    return out

# --- A. Does the box size change the answer? (methane) ---
print("A. CH4 vs vacuum size")
rows = {}
for vac in [3.0, 5.0, 8.0, 12.0]:
    a = molecule("CH4"); a.center(vacuum=vac); a.pbc = True
    rows[vac] = predict(ase_to_atoms(a))
print(f"{'target':8s}" + "".join(f"vac={v:<5}".rjust(12) for v in rows))
for t in TARGETS:
    print(f"{t:8s}" + "".join(f"{r[t]:12.4f}" for r in rows.values()))

# --- B. Feed a structure from the training dataset itself ---
print("\nB. First entries of qm9_std_jctc (stored target vs model prediction)")
from jarvis.db.figshare import data
d = data("qm9_std_jctc")
print("entry keys:", list(d[0].keys()))
for entry in d[:3]:
    ja = JAtoms.from_dict(entry["atoms"])
    print("\nformula:", ja.composition.reduced_formula, " lattice abc:", np.round(ja.lattice.abc, 2))
    pred = predict(ja)
    for t in TARGETS:
        stored = entry.get(t, entry.get(t.lower(), "n/a"))
        print(f"  {t:6s} stored = {stored}   model = {pred[t]:.4f}")
