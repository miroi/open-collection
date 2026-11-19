import re
from pathlib import Path
from ase.build import molecule
from ase.optimize import BFGS
from ase.units import kJ, mol
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
for d in descriptors:
    desc_type = d.strip().split()[0]
    print(f"  - {desc_type}: {d.strip()}")

print(f"\nRequired sparseX   : {len(sparse_refs)} files referenced")
missing_files = []
for fname in sparse_refs:
    fpath = gap_dir / fname
    if fpath.is_file():
        print(f"  [OK]      {fname} ({fpath.stat().st_size / 1e6:.2f} MB)")
    else:
        print(f"  [MISSING] {fname}")
        missing_files.append(fname)

if missing_files:
    raise FileNotFoundError(f"Missing {len(missing_files)} required sparseX files in {gap_dir}")

# 3. Initialize QUIP/GAP calculator
print("\n=== Initializing quippy Potential ===")
calc = Potential(param_filename=str(gap_xml))
print(f"Calculator loaded  : {type(calc).__name__} (max XML cutoff = {max_cutoff:.2f} A)")

# 4. Helper function to relax a molecule with BFGS
def relax_molecule(name, fmax=0.005):
    atoms = molecule(name)
    atoms.center(vacuum=12.0)  # > 2 * max_cutoff to prevent periodic self-interaction
    atoms.calc = calc
    e_init = atoms.get_potential_energy()
    opt = BFGS(atoms, logfile=None)
    opt.run(fmax=fmax)
    e_final = atoms.get_potential_energy()
    return atoms, e_init, e_final, opt.nsteps

# 5. Relax reactants (C2H4, H2) and product (C2H6)
print("\n=== Geometry Optimization (BFGS, fmax = 0.005 eV/A) ===")
results = {}
for species in ["C2H4", "H2", "C2H6"]:
    atoms, e_init, e_final, steps = relax_molecule(species)
    results[species] = (atoms, e_final)
    print(f"{species:<6} | steps={steps:<3} | E_init={e_init:10.6f} eV | E_opt={e_final:10.6f} eV")

# 6. Check relaxed key bond distances against PBE DFT benchmarks
d_hh = results["H2"][0].get_distance(0, 1)
d_cc_ene = results["C2H4"][0].get_distance(0, 1)
d_cc_ane = results["C2H6"][0].get_distance(0, 1)

print("\n=== Relaxed Bond Lengths vs. PBE DFT Reference ===")
print(f"H-H  in H2         : {d_hh:.4f} A  (PBE ref: ~0.750 A)")
print(f"C=C  in C2H4       : {d_cc_ene:.4f} A  (PBE ref: ~1.331 A)")
print(f"C-C  in C2H6       : {d_cc_ane:.4f} A  (PBE ref: ~1.530 A)")

# 7. Calculate electronic reaction energy: C2H4 + H2 -> C2H6
e_c2h4 = results["C2H4"][1]
e_h2 = results["H2"][1]
e_c2h6 = results["C2H6"][1]

delta_e_ev = e_c2h6 - (e_c2h4 + e_h2)
delta_e_kj = delta_e_ev / (kJ / mol)

print("\n=== Ethene Hydrogenation Benchmark: C2H4 + H2 -> C2H6 ===")
print(f"GAP dE_rxn         : {delta_e_ev:.4f} eV  ({delta_e_kj:.2f} kJ/mol)")
print("PBE DFT ref (0 K)  : ~ -1.75 to -1.80 eV (-169 to -174 kJ/mol, electronic dE without ZPE)")
print("Expt. dH_rxn (298K):   -1.41 eV (-136.3 kJ/mol, includes ZPE + thermal corrections)")

