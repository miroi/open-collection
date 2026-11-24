import io, os, tempfile, contextlib
import numpy as np
from jarvis.core.atoms import Atoms as JAtoms
from jarvis.db.figshare import data
from alignn.pretrained import get_prediction

TARGETS = ["HOMO", "LUMO", "gap", "alpha", "ZPVE", "U0", "U", "G"]
CUTOFF = 5.0            # matches the cutoff in the models' saved configs
N_FIRST = 3             # first dataset entries (CH4, NH3, H2O)
N_RANDOM = 3            # extra random entries
SEED = 0

# Approximate QM9 mean/std, recalled from memory (eV, except alpha in bohr^3).
# Replace with the exact values from the Faber et al. statistics file when you have them.
CONV = {
    "HOMO":  (-6.5367, 0.5977),
    "LUMO":  ( 0.3220, 1.2748),
    "gap":   ( 6.8587, 1.2843),
    "ZPVE":  ( 4.0568, 0.9017),
    "alpha": (75.19,   8.19),     # slightly off (about 0.2 bohr^3 for CH4)
}

def to_physical(target, z):
    if target not in CONV:
        return None
    mean, std = CONV[target]
    return z * std + mean

def formula(ja):
    counts = ja.composition.to_dict()
    return "".join(f"{el}{n if n != 1 else ''}" for el, n in sorted(counts.items()))

def predict(ja):
    out = {}
    for t in TARGETS:
        with contextlib.redirect_stdout(io.StringIO()):
            v = get_prediction(model_name=f"qm9_{t}_alignn", atoms=ja, cutoff=CUTOFF)
        out[t] = float(np.ravel(v)[0])
    return out

# Run in a temp directory so the qm9_*_alignn config folders do not litter your work dir
workdir = tempfile.TemporaryDirectory()
os.chdir(workdir.name)

print("Loading qm9_std_jctc ...")
with contextlib.redirect_stdout(io.StringIO()):
    d = data("qm9_std_jctc")
print(f"{len(d)} entries; keys: {list(d[0].keys())}")

rng = np.random.default_rng(SEED)
indices = list(range(N_FIRST)) + sorted(rng.choice(np.arange(N_FIRST, len(d)), N_RANDOM, replace=False).tolist())

for i in indices:
    entry = d[i]
    ja = JAtoms.from_dict(entry["atoms"])
    pred = predict(ja)
    print(f"\n#{i}  id={entry.get('id')}  formula={formula(ja)}  SMILES={entry.get('SMILES')}  "
          f"box={np.round(ja.lattice.abc, 1).tolist()}")
    print(f"  {'target':6s} {'stored z':>10s} {'model z':>10s} {'|diff|':>8s}   {'stored (phys)':>14s} {'model (phys)':>13s}")
    for t in TARGETS:
        s, m = float(entry[t]), pred[t]
        ps, pm = to_physical(t, s), to_physical(t, m)
        phys = f"{ps:14.3f} {pm:13.3f}" if ps is not None else f"{'(n/a)':>14s} {'(n/a)':>13s}"
        print(f"  {t:6s} {s:10.4f} {m:10.4f} {abs(s - m):8.4f}   {phys}")
    print(f"  stored mu = {entry.get('mu')} D, R2 = {entry.get('R2')}")

os.chdir("/")
workdir.cleanup()
print("\nNote: most dataset entries were in the training set (110k of ~130k), so a close match "
      "mainly shows the models load and run correctly, not that they generalize.")
