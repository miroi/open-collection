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

# Initialize CHGNet (Loading once outside the loop for speed)
print("Initializing CHGNet...")
calc = CHGNetCalculator()

def get_pbo_molecule(orientation='Pb-down'):
    """
    Creates PbO molecule with specific orientations.
    Pb is index 0, O is index 1.
    """
    # Using approx bond length 1.92 A
    mol = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])
    if orientation == 'O-down':
        mol.rotate(180, 'x')
    elif orientation == 'horizontal':
        mol.rotate(90, 'x')
    return mol

# Variables to track the most stable configuration
best_energy = float('inf')
best_atoms = None
best_name = ""

# Define Search Space
sites = ['ontop', 'bridge', 'fcc', 'hcp']
orientations = ['Pb-down', 'O-down', 'horizontal']

print(f"\n{'Site':<10} | {'Orientation':<12} | {'Energy (eV)':<12}")
print("-" * 40)

# 2. Main Optimization Loop
for s in sites:
    for o in orientations:
        try:
            # Build Au(111) Slab (3x3 supercell, 4 layers)
            slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
            
            # Create and add PbO
            pbo = get_pbo_molecule(o)
            add_adsorbate(slab, pbo, height=2.5, position=s)
            
            # Assign Calculator
            slab.calc = calc
            
            # Fix bottom two layers (ASE tags layers 1-4 for fcc111)
            # Higher tag = deeper layer
            c = FixAtoms(indices=[atom.index for atom in slab if atom.tag > 2])
            slab.set_constraint(c)

            # Run Optimization
            name = f"{s}_{o}"
            dyn = BFGS(slab, logfile=f"{output_dir}/{name}.log")
            dyn.run(fmax=0.05)
            
            # Get Energy
            energy = slab.get_potential_energy()
            print(f"{s:<10} | {o:<12} | {energy:>12.4f}")

            # CLEANUP: Remove unhashable info that triggers XYZ UserWarnings
            if 'adsorbate_info' in slab.info:
                del slab.info['adsorbate_info']

            # Save Converged Structures
            # .xyz for visualization; .vasp for DFT/Selective Dynamics
            io.write(f"{output_dir}/{name}_converged.xyz", slab)
            io.write(f"{output_dir}/{name}_converged.vasp", slab, format='vasp', direct=True)

            # Track Global Minimum
            if energy < best_energy:
                best_energy = energy
                best_atoms = slab.copy()
                best_name = name

        except Exception as e:
            print(f"{s:<10} | {o:<12} | Failed: {e}")

# 3. Final Summary Output
if best_atoms:
    print(f"\n" + "="*40)
    print(f"STABILITY WINNER: {best_name}")
    print(f"POTENTIAL ENERGY: {best_energy:.4f} eV")
    print("="*40)
    
    # Save the absolute winner to the main directory
    io.write("MOST_STABLE_PbO_Au.vasp", best_atoms, format='vasp', direct=True)
    io.write("MOST_STABLE_PbO_Au.xyz", best_atoms)
    print(f"\nAll structures saved in '{output_dir}/'")
    print("Most stable structure saved as 'MOST_STABLE_PbO_Au.vasp/xyz'")
else:
    print("\nNo calculations completed successfully.")

