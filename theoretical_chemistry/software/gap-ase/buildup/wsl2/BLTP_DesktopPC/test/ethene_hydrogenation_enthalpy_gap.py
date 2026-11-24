import re
import shutil
from pathlib import Path
from ase.build import molecule
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase.units import kJ, mol, invcm
from quippy.potential import Potential

# 1. Locate CH.xml via absolute path (no os.chdir needed)
gap_xml = Path("gap_files/CH.xml").resolve()
gap_dir = gap_xml.parent

print("=== GAP Potential File Verification ===")
print(f"XML Parameter File : {gap_xml} (exists={gap_xml.is_file()}, size={gap_xml.stat().st_size / 1e6:.2f} MB)")

# 2. Parse CH.xml to find all referenced sparseX files, descriptors, and cutoffs
xml_text = gap_xml.read_text(errors="ignore")
sparse_refs = sorted(set(re.findall(r'sparseX_filename="([^"]+)"', xml_text)))
descriptors = sorted(set(re.findall(r'<descriptor[^>]*>([^<]+)</descriptor>', xml_text)))
cutoffs = [float(c) for c in re.findall(r'(?:cutoff|rcut_hard)=([0-9.]+)', xml_text)]
max_cutoff = max(cutoffs) if cutoffs else 0.0

print(f"\nDescriptors in XML : {len(descriptors)} active (max cutoff = {max_cutoff:.2f} A)")
print(f"Required sparseX   : {len(sparse_refs)} files referenced")
missing_files = [f for f in sparse_refs if not (gap_dir / f).is_file()]
if missing_files:
    raise FileNotFoundError(f"Missing {len(missing_files)} required sparseX files in {gap_dir}")

# 3. Initialize QUIP/GAP calculator
print("\n=== Initializing quippy Potential ===")
calc = Potential(param_filename=str(gap_xml))
print(f"Calculator loaded  : {type(calc).__name__} (max XML cutoff = {max_cutoff:.2f} A)")

# 4. Helper function to relax tightly before Hessian evaluation
def relax_molecule(name, fmax=0.0005):
    atoms = molecule(name)
    atoms.center(vacuum=12.0)
    atoms.calc = calc
    opt = BFGS(atoms, logfile=None)
    opt.run(fmax=fmax)
    return atoms, atoms.get_potential_energy(), opt.nsteps

# 5. Helper function to compute harmonic vibrations, ZPE, and 298.15 K enthalpy
def analyze_vibrations(name, atoms, e_pot, geometry, symmetrynumber):
    vib_dir = Path(f"vib_{name}")
    if vib_dir.exists():
        shutil.rmtree(vib_dir)

    vib = Vibrations(atoms, name=str(vib_dir), delta=0.01)
    vib.run()
    vib_energies = vib.get_energies()
    zpe = vib.get_zero_point_energy()
    vib.clean()
    if vib_dir.exists():
        shutil.rmtree(vib_dir)

    # Filter out 5 (linear) or 6 (nonlinear) translational/rotational modes
    n_tr = 5 if geometry == "linear" else 6
    internal_energies = vib_energies[n_tr:]
    internal_cm1 = [e.real / invcm for e in internal_energies]

    thermo = IdealGasThermo(
        vib_energies=internal_energies,
        potentialenergy=e_pot,
        atoms=atoms,
        geometry=geometry,
        symmetrynumber=symmetrynumber,
        spin=0,
    )
    h_298 = thermo.get_enthalpy(temperature=298.15, verbose=False)
    return internal_cm1, zpe, h_298

# 6. Run relaxation + vibrational analysis for reactants and product
specs = {
    "H2": ("linear", 2),
    "C2H4": ("nonlinear", 4),
    "C2H6": ("nonlinear", 6),
}

print("\n=== Tight Geometry Optimization & Harmonic Vibrations (delta = 0.01 A) ===")
results = {}
for name, (geom, sym) in specs.items():
    atoms, e_opt, steps = relax_molecule(name, fmax=0.0005)
    freqs_cm1, zpe, h_298 = analyze_vibrations(name, atoms, e_opt, geom, sym)
    results[name] = {
        "e_opt": e_opt,
        "zpe": zpe,
        "h_298": h_298,
        "freqs": freqs_cm1,
    }
    print(f"\n[{name}] (BFGS steps={steps}, E_opt={e_opt:.6f} eV, ZPE={zpe:.4f} eV)")
    print("  Internal frequencies (cm^-1):", ", ".join(f"{f:.1f}" for f in freqs_cm1))

# 7. Reaction energetics summary: C2H4 + H2 -> C2H6
dE_elec = results["C2H6"]["e_opt"] - (results["C2H4"]["e_opt"] + results["H2"]["e_opt"])
dZPE = results["C2H6"]["zpe"] - (results["C2H4"]["zpe"] + results["H2"]["zpe"])
dE_0K = dE_elec + dZPE
dH_298 = results["C2H6"]["h_298"] - (results["C2H4"]["h_298"] + results["H2"]["h_298"])

print("\n=== Hydrogenation Thermochemistry Summary: C2H4 + H2 -> C2H6 ===")
print(f"Electronic dE_rxn  : {dE_elec:8.4f} eV  ({dE_elec / (kJ / mol):8.2f} kJ/mol)")
print(f"Zero-Point dZPE    : {dZPE:+8.4f} eV  ({dZPE / (kJ / mol):+8.2f} kJ/mol)  [Expt/DFT ref: ~ +0.34 eV (+33 kJ/mol)]")
print(f"ZPE-Corr dE_0K     : {dE_0K:8.4f} eV  ({dE_0K / (kJ / mol):8.2f} kJ/mol)")
print(f"Enthalpy dH_298K   : {dH_298:8.4f} eV  ({dH_298 / (kJ / mol):8.2f} kJ/mol)  [Expt ref: -1.41 eV (-136.3 kJ/mol)]")

