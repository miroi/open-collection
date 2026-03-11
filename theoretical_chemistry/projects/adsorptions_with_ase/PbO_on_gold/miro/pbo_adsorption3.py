import numpy as np
from ase import Atoms, io
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from chgnet.model.dynamics import CHGNetCalculator
import os

# Create a directory for the results
output_dir = "adsorption_results"
os.makedirs(output_dir, exist_ok=True)

# Initialize Calculator
calc = CHGNetCalculator()

def get_pbo_molecule(orientation='Pb-down'):
    mol = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])
    if orientation == 'O-down':
        mol.rotate(180, 'x')
    elif orientation == 'horizontal':
        mol.rotate(90, 'x')
    return mol

def run_adsorption(site, orientation):
    # 1. Build Slab
    slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
    
    # 2. Add Adsorbate
    pbo = get_pbo_molecule(orientation)
    add_adsorbate(slab, pbo, height=2.5, position=site)

    # 3. Setup Calculator & Constraints
    slab.calc = calc
    from ase.constraints import FixAtoms
    c = FixAtoms(indices=[atom.index for atom in slab if atom.tag > 2])
    slab.set_constraint(c)

    # 4. Optimize
    filename = f"{site}_{orientation}"
    dyn = BFGS(slab, logfile=f"{output_dir}/{filename}.log")
    dyn.run(fmax=0.05)

    # 5. Write out the converged structure to XYZ
    io.write(f"{output_dir}/{filename}_converged.xyz", slab)
    
    return slab.get_potential_energy()

# Execution Loop
sites = ['ontop', 'bridge', 'fcc', 'hcp']
orientations = ['Pb-down', 'O-down', 'horizontal']

print(f"{'Site':<10} | {'Orientation':<12} | {'Energy (eV)':<12}")
print("-" * 40)

for s in sites:
    for o in orientations:
        try:
            energy = run_adsorption(s, o)
            print(f"{s:<10} | {o:<12} | {energy:>12.4f}")
        except Exception as e:
            print(f"{s:<10} | {o:<12} | Failed: {e}")

print(f"\nDone! Converged structures are in the '{output_dir}' folder.")

