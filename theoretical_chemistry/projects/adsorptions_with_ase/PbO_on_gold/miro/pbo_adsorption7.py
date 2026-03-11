import os
import numpy as np
from ase import Atoms, io
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from chgnet.model.dynamics import CHGNetCalculator

# 1. Setup Environment
output_dir = "adsorption_results"
os.makedirs(output_dir, exist_ok=True)

print("Initializing CHGNet...")
calc = CHGNetCalculator()

def get_pbo_molecule(orientation='Pb-down'):
    """
    Creates PbO molecule with specific orientations.
    Pb is index 0, O is index 1. Bond length ~1.92 A.
    """
    mol = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])
    
    # Standard Orientations
    if orientation == 'O-down':
        mol.rotate(180, 'x')
    elif orientation == 'horizontal':
        mol.rotate(90, 'x')
    
    # Slanted Orientations
    elif orientation == 'slant-Pb-down':
        # Tilted 45 degrees, Pb remains closer to surface
        mol.rotate(45, 'x')
    elif orientation == 'slant-O-down':
        # Tilted 135 degrees, O remains closer to surface
        mol.rotate(135, 'x')
        
    return mol

# Variables to track the most stable configuration
best_energy = float('inf')
best_atoms = None
best_name = ""

# Define Expanded Search Space
sites = ['ontop', 'bridge', 'fcc', 'hcp']
orientations = [
    'Pb-down', 
    'O-down', 
    'horizontal', 
    'slant-Pb-down', 
    'slant-O-down'
]

print(f"\n{'Site':<10} | {'Orientation':<15} | {'Energy (eV)':<12}")
print("-" * 45)

# 2. Main Optimization Loop
for s in sites:
    for o in orientations:
        try:
            # Build Au(111) Slab (3x3 supercell, 4 layers)
            slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
            
            # Create and add PbO
            pbo = get_pbo_molecule(o)
            # height=2.5 is the distance from surface to the first atom (index 0)
            add_adsorbate(slab, pbo, height=2.5, position=s)
            
            slab.calc = calc
            
            # Fix bottom two layers (tags 3 and 4)
            c = FixAtoms(indices=[atom.index for atom in slab if atom.tag > 2])
            slab.set_constraint(c)

            # Run Optimization
            name = f"{s}_{o}"
            dyn = BFGS(slab, logfile=f"{output_dir}/{name}.log")
            dyn.run(fmax=0.05)
            
            energy = slab.get_potential_energy()
            print(f"{s:<10} | {o:<15} | {energy:>12.4f}")

            # CLEANUP: Remove unhashable info for XYZ writing
            if 'adsorbate_info' in slab.info:
                del slab.info['adsorbate_info']

            # Save Converged Structures
            io.write(f"{output_dir}/{name}_converged.xyz", slab)
            io.write(f"{output_dir}/{name}_converged.vasp", slab, format='vasp', direct=True)

            # Track Global Minimum
            if energy < best_energy:
                best_energy = energy
                best_atoms = slab.copy()
                best_name = name

        except Exception as e:
            print(f"{s:<10} | {o:<15} | Failed: {e}")

# 3. Final Summary Output
if best_atoms:
    print(f"\n" + "="*45)
    print(f"STABILITY WINNER: {best_name}")
    print(f"POTENTIAL ENERGY: {best_energy:.4f} eV")
    print("="*45)
    
    io.write("MOST_STABLE_PbO_Au.vasp", best_atoms, format='vasp', direct=True)
    io.write("MOST_STABLE_PbO_Au.xyz", best_atoms)
    print(f"\nResults saved in '{output_dir}/'")

