import importlib.util
import numpy as np
from ase.build import molecule
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from jarvis.core.atoms import ase_to_atoms
from alignn.ff.ff import AlignnAtomwiseCalculator, get_figshare_model_ff

FF_MODEL = "alignn_ff_matpes_r2scan"   # best water geometry in your benchmark
DEVICE = "cpu"
T, P = 298.15, 101325.0                # K, Pa

# ---------- 1. ALIGNN-FF: geometry ----------
atoms = molecule("H2O")
atoms.center(vacuum=8.0)
atoms.pbc = True                        # needed by ALIGNN's graph builder
atoms.calc = AlignnAtomwiseCalculator(
    path=get_figshare_model_ff(model_name=FF_MODEL), device=DEVICE, stress_wt=0.0)
BFGS(atoms, logfile=None).run(fmax=0.001, steps=500)
E = atoms.get_potential_energy()

print(f"[ALIGNN-FF {FF_MODEL}]")
print(f"  E            = {E:.4f} eV")
print(f"  r_OH         = {0.5 * (atoms.get_distance(0, 1) + atoms.get_distance(0, 2)):.3f} Å")
print(f"  H-O-H angle  = {atoms.get_angle(1, 0, 2):.2f}°")
print(f"  max |force|  = {np.abs(atoms.get_forces()).max():.2e} eV/Å")

# ---------- 2. ALIGNN-FF: vibrations, ZPE, thermochemistry ----------
vib = Vibrations(atoms, name="vib_h2o", delta=0.02)
vib.run()
energies = np.sort(vib.get_energies().real)    # eV; imaginary modes show as 0
freqs = np.sort(vib.get_frequencies().real)    # cm^-1
internal_e = energies[-3:]                      # the 3 real internal modes of H2O

print("\n  internal modes (cm^-1): bend {:.0f}, sym {:.0f}, asym {:.0f}".format(*freqs[-3:]))
print(f"  largest translation/rotation mode: {np.abs(freqs[:6]).max():.1f} cm^-1 (should be ~0)")
print(f"  ZPE (internal modes) = {0.5 * internal_e.sum():.4f} eV")

# IdealGasThermo requires a non-periodic Atoms object: use a copy
thermo_atoms = atoms.copy()
thermo_atoms.pbc = False
thermo = IdealGasThermo(vib_energies=internal_e, potentialenergy=E, atoms=thermo_atoms,
                        geometry="nonlinear", symmetrynumber=2, spin=0)
H = thermo.get_enthalpy(temperature=T, verbose=False)
S = thermo.get_entropy(temperature=T, pressure=P, verbose=False)
G = thermo.get_gibbs_energy(temperature=T, pressure=P, verbose=False)
print(f"  H({T} K) = {H:.4f} eV,  S = {S * 1000:.3f} meV/K,  G = {G:.4f} eV")
vib.clean()

# ---------- 3. ALIGNN QM9 property models ----------
print("\n[ALIGNN QM9 property models]")
QM9 = ["qm9_HOMO_alignn", "qm9_LUMO_alignn", "qm9_gap_alignn", "qm9_alpha_alignn",
       "qm9_ZPVE_alignn", "qm9_U0_alignn", "qm9_U_alignn", "qm9_G_alignn"]
print("  dipole moment: no ALIGNN dipole model in this install; not available")

has_dgl = importlib.util.find_spec("dgl") is not None
print(f"  DGL installed: {has_dgl}")
if not has_dgl:
    print("  without DGL these calls are expected to fail with KeyError (known issue)")

from alignn.pretrained import get_prediction

jatoms = ase_to_atoms(atoms)
for name in QM9:
    try:
        v = np.ravel(get_prediction(model_name=name, atoms=jatoms))[0]
        print(f"  {name:20s} {v: .4f}   (units: check JARVIS leaderboard)")
    except Exception as e:
        print(f"  {name:20s} failed: {type(e).__name__}: {e}")
