import io, os, tempfile, contextlib
import numpy as np
from ase.build import molecule
from ase.optimize import BFGS
from jarvis.core.atoms import Atoms as JAtoms, ase_to_atoms
from jarvis.db.figshare import data
from alignn.ff.ff import AlignnAtomwiseCalculator, get_figshare_model_ff
from alignn.pretrained import get_prediction

FF_MODEL = "alignn_ff_matpes_r2scan"   # ALIGNN-FF model used for the relaxation
DEVICE = "cpu"
CUTOFF = 5.0                            # matches the QM9 models' saved configs
BOX = 60.0                              # QM9 training structures use 60 Å cubic boxes
TARGETS = ["HOMO", "LUMO", "gap", "alpha", "ZPVE", "U0", "U", "G"]

# Approximate QM9 mean/std recalled from memory (eV; alpha in bohr^3; mu in D).
# Replace with exact values from the Faber et al. statistics file when you have them.
CONV = {
    "HOMO":  (-6.5367, 0.5977),
    "LUMO":  ( 0.3220, 1.2748),
    "gap":   ( 6.8587, 1.2843),
    "ZPVE":  ( 4.0568, 0.9017),
    "alpha": (75.19,   8.19),     # about 0.2 bohr^3 low for CH4
    "mu":    ( 2.72,   1.53),     # fitted so CH4 comes out ~0 D; unverified otherwise
}
UNITS = {"HOMO": "eV", "LUMO": "eV", "gap": "eV", "ZPVE": "eV", "alpha": "bohr^3"}

def to_phys(t, z):
    mean, std = CONV[t]
    return z * std + mean

def water_geometry(a):
    sym = a.get_chemical_symbols()
    o = sym.index("O")
    hs = [i for i, s in enumerate(sym) if s == "H"]
    r = np.mean([a.get_distance(o, h, mic=True) for h in hs])
    ang = a.get_angle(hs[0], o, hs[1], mic=True)
    return r, ang

def embed(atoms, box=BOX):
    a = atoms.copy()
    a.set_cell([box, box, box])
    a.pbc = True
    a.center()
    return a

def predict_qm9(ase_atoms):
    ja = ase_to_atoms(embed(ase_atoms))
    out = {}
    for t in TARGETS:
        with contextlib.redirect_stdout(io.StringIO()):
            v = get_prediction(model_name=f"qm9_{t}_alignn", atoms=ja, cutoff=CUTOFF)
        out[t] = float(np.ravel(v)[0])
    return out

# get_prediction writes qm9_*_alignn config folders into the current directory
workdir = tempfile.TemporaryDirectory()
os.chdir(workdir.name)

# ---------- 1. Relax water with ALIGNN-FF ----------
ff = molecule("H2O")
ff.center(vacuum=8.0)
ff.pbc = True
ff.calc = AlignnAtomwiseCalculator(
    path=get_figshare_model_ff(model_name=FF_MODEL), device=DEVICE, stress_wt=0.0)
BFGS(ff, logfile=None).run(fmax=0.001, steps=500)
ff.calc = None
r_ff, ang_ff = water_geometry(ff)

# ---------- 2. Water from the QM9 dataset (stored B3LYP values + geometry) ----------
print("Loading qm9_std_jctc ...")
with contextlib.redirect_stdout(io.StringIO()):
    d = data("qm9_std_jctc")
entry = None
for e in d[:200]:
    ja = JAtoms.from_dict(e["atoms"])
    if sorted(ja.composition.to_dict().items()) == [("H", 2), ("O", 1)]:
        entry = e
        break
if entry is None:
    raise SystemExit("H2O not found among the first 200 dataset entries")
qm9_atoms = JAtoms.from_dict(entry["atoms"]).ase_converter()
r_q, ang_q = water_geometry(qm9_atoms)

# ---------- 3. QM9 models on both geometries ----------
pred_qm9_geom = predict_qm9(qm9_atoms)
pred_ff_geom = predict_qm9(ff)

# ---------- 4. Report ----------
print(f"\nWater: dataset entry id={entry.get('id')}, SMILES={entry.get('SMILES')}")
print(f"  geometry      r_OH (Å)   H-O-H (°)")
print(f"  QM9 (B3LYP)   {r_q:8.3f}   {ang_q:8.2f}")
print(f"  ALIGNN-FF     {r_ff:8.3f}   {ang_ff:8.2f}   ({FF_MODEL})")

print("\nPhysical properties (converted with approximate constants)")
print(f"  {'target':6s} {'unit':7s} {'stored B3LYP':>13s} {'model@QM9 geom':>15s} {'model@FF geom':>14s}")
for t in ["HOMO", "LUMO", "gap", "ZPVE", "alpha"]:
    s = to_phys(t, float(entry[t]))
    print(f"  {t:6s} {UNITS[t]:7s} {s:13.3f} {to_phys(t, pred_qm9_geom[t]):15.3f} "
          f"{to_phys(t, pred_ff_geom[t]):14.3f}")
mu = to_phys("mu", float(entry["mu"]))
print(f"  {'mu':6s} {'D':7s} {mu:13.3f} {'(no model)':>15s} {'(no model)':>14s}")

print("\nEnergies (standardized z-scores, atomization-type quantities; not converted)")
print(f"  {'target':6s} {'stored':>10s} {'model@QM9':>10s} {'model@FF':>10s}")
for t in ["U0", "U", "G"]:
    print(f"  {t:6s} {float(entry[t]):10.4f} {pred_qm9_geom[t]:10.4f} {pred_ff_geom[t]:10.4f}")

os.chdir("/")
workdir.cleanup()
