import os
import re
from pathlib import Path
from ase.build import molecule
from quippy.potential import Potential

# 1. Locate CH.xml via absolute path (no os.chdir needed)
gap_xml = Path("gap_files/CH.xml").resolve()
gap_dir = gap_xml.parent

print("=== GAP Potential File Verification ===")
print(f"XML Parameter File : {gap_xml} (exists={gap_xml.is_file()}, size={gap_xml.stat().st_size / 1e6:.2f} MB)")

# 2. Parse CH.xml to find all referenced sparseX files and descriptors
xml_text = gap_xml.read_text(errors="ignore")
sparse_refs = sorted(set(re.findall(r'sparseX_filename="([^"]+)"', xml_text)))
descriptors = sorted(set(re.findall(r'<descriptor[^>]*>([^<]+)</descriptor>', xml_text)))

print(f"Descriptors in XML : {descriptors if descriptors else 'Parsed inside GAP_params'}")
print(f"Required sparseX   : {len(sparse_refs)} files referenced")

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

# 3. Initialize QUIP/GAP calculator (verifies soap_turbo support in quippy)
print("\n=== Initializing quippy Potential ===")
calc = Potential(param_filename=str(gap_xml))
print("Calculator loaded  :", calc.name)

# 4. Run single-point energy and force evaluation on C2H4
atoms = molecule("C2H4")
atoms.center(vacuum=10.0)
atoms.calc = calc

energy = atoms.get_potential_energy()
forces = atoms.get_forces()
max_force = abs(forces).max()

print("\n=== Test Evaluation (C2H4) ===")
print(f"Potential Energy   : {energy:.6f} eV ({energy / len(atoms):.6f} eV/atom)")
print(f"Max Force Component: {max_force:.6f} eV/A")
print("Forces (eV/A):\n", forces)

