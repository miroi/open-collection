import numpy as np
from ase.build import molecule
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from alignn.ff.ff import AlignnAtomwiseCalculator, get_figshare_model_ff

MODELS = ["alignn_ff_mptrj", "alignn_ff_matpes_pbe",
          "alignn_ff_matpes_r2scan", "alignn_ff_omat24_1m"]
DEVICE = "cpu"

# Approximate reference values for gas-phase H2O (check against your own DFT/CCSD(T))
REF_R = 0.9572                           # Å, experiment
REF_ANGLE = 104.52                       # degrees, experiment
REF_FREQ = np.array([1649, 3832, 3943])  # cm^-1, harmonic: bend, sym, asym

def run(model_name):
    model_dir = get_figshare_model_ff(model_name=model_name)
    atoms = molecule("H2O")
    atoms.center(vacuum=8.0)
    atoms.pbc = True
    atoms.calc = AlignnAtomwiseCalculator(path=model_dir, device=DEVICE, stress_wt=0.0)
    BFGS(atoms, logfile=None).run(fmax=0.001, steps=500)
    r = 0.5 * (atoms.get_distance(0, 1) + atoms.get_distance(0, 2))
    ang = atoms.get_angle(1, 0, 2)
    vib = Vibrations(atoms, name=f"vib_{model_name}", delta=0.02)
    vib.run()
    freqs = np.sort(vib.get_frequencies().real)   # imaginary modes show as ~0 here
    vib.clean()
    return r, ang, freqs[-3:], freqs[:6]          # last 3 = real internal modes

rows = []
for m in MODELS:
    try:
        r, ang, f, low = run(m)
    except Exception as e:
        print(f"{m}: failed ({e})")
        continue
    # Arbitrary combined score: 0.01 Å, 1 degree and 50 cm^-1 each count as 1 unit
    score = abs(r - REF_R) / 0.01 + abs(ang - REF_ANGLE) + np.mean(np.abs(f - REF_FREQ)) / 50
    rows.append((score, m, r, ang, f, np.abs(low).max()))

print(f"{'model':28s} {'r_OH':>7s} {'angle':>7s} {'bend':>7s} {'sym':>7s} {'asym':>7s} {'max|low|':>9s} {'score':>6s}")
for score, m, r, ang, f, lowmax in sorted(rows):
    print(f"{m:28s} {r:7.3f} {ang:7.2f} {f[0]:7.0f} {f[1]:7.0f} {f[2]:7.0f} {lowmax:9.1f} {score:6.2f}")
print("\nBest by score:", sorted(rows)[0][1])
