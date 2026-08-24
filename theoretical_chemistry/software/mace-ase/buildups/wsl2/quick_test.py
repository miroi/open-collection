# Save as quick_test.py
from mace.calculators import MACECalculator
from ase.build import molecule
from pathlib import Path
import time

model = Path.home() / '.cache' / 'mace' / 'macempa0mediummodel'
calc = MACECalculator(model_path=str(model), device='cpu')

print("MACE Quick Test\n" + "="*40)
for mol in ['H2O', 'CH4', 'NH3', 'CO2', 'C6H6']:
    atoms = molecule(mol)
    atoms.calc = calc
    start = time.time()
    e = atoms.get_potential_energy()
    t = time.time() - start
    print(f"{mol:>8}: {e:10.6f} eV ({t:.3f}s)")
