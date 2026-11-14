import numpy as np
from ase.build import molecule
from ase.optimize import BFGS
from jarvis.core.atoms import ase_to_atoms
from alignn.ff.ff import AlignnAtomwiseCalculator, get_figshare_model_ff
from alignn.pretrained import get_prediction, get_all_models

# --- 1. Geometry with ALIGNN-FF (best geometry in your benchmark) ---
atoms = molecule("H2O")
atoms.center(vacuum=8.0)
atoms.pbc = True
atoms.calc = AlignnAtomwiseCalculator(
    path=get_figshare_model_ff(model_name="alignn_ff_matpes_r2scan"),
    device="cpu", stress_wt=0.0)
BFGS(atoms, logfile=None).run(fmax=0.001, steps=500)
print(f"r_OH = {atoms.get_distance(0, 1):.3f} Å, angle = {atoms.get_angle(1, 0, 2):.1f}°")

# --- 2. Find the QM9 property models available in this install ---
available = [n for n in get_all_models() if "qm9" in n.lower()]
print("QM9 models found:")
for n in sorted(available):
    print("  ", n)

# --- 3. Property predictions on the relaxed structure ---
# Targets and (assumed) units; check the printed model names and the leaderboard pages
TARGETS = {"mu": "dipole moment (Debye)", "homo": "HOMO", "lumo": "LUMO",
           "gap": "HOMO-LUMO gap", "alpha": "polarizability", "zpve": "ZPVE", "U0": "U0"}

jatoms = ase_to_atoms(atoms)
print("\nPredictions (raw model output):")
for key, label in TARGETS.items():
    names = [n for n in available if f"_{key}_" in n.lower() or n.lower().endswith(f"_{key}")]
    if not names:
        print(f"  {label:25s} no matching model")
        continue
    try:
        value = get_prediction(model_name=names[0], atoms=jatoms)
        print(f"  {label:25s} {np.ravel(value)[0]: .4f}   ({names[0]})")
    except Exception as e:
        print(f"  {label:25s} failed: {e}")
