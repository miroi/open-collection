import os
import numpy as np
from ase import Atoms, io
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# --- MLIP Calculators ---
from chgnet.model.dynamics import CHGNetCalculator

# Try-except block to handle MACE installation issues
try:
    from mace.calculators import mace_mp
    HAS_MACE = True
except ImportError:
    print("MACE not found. Install it with: pip install mace-torch")
    HAS_MACE = False

# 1. Setup Environment
output_dir = "adsorption_dual_results"
os.makedirs(output_dir, exist_ok=True)

# Initialize Calculators
print("Initializing Calculators...")
calculators = {"CHGNet": CHGNetCalculator()}

if HAS_MACE:
    # mace_mp loads the universal Materials Project foundation model
    #calculators["MACE"] = mace_mp(model="medium", device='cuda', default_dtype="float32")

    # Change this line:
    calculators["MACE"] = mace_mp(model="medium", device='cpu', default_dtype="float32")


def get_pbo_molecule(orientation='Pb-down'):
    """
    Creates PbO molecule with specific orientations.
    Pb is index 0, O is index 1.
    """
    mol = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])
    if orientation == 'O-down': mol.rotate(180, 'x')
    elif orientation == 'horizontal': mol.rotate(90, 'x')
    elif orientation == 'slant-Pb-down': mol.rotate(45, 'x')
    elif orientation == 'slant-O-down': mol.rotate(135, 'x')
    return mol

# Define Search Space
sites = ['ontop', 'bridge', 'fcc', 'hcp']
orientations = ['Pb-down', 'O-down', 'horizontal', 'slant-Pb-down', 'slant-O-down']

# 2. Main Comparison Loop
for calc_name, calc in calculators.items():
    print(f"\n" + "="*50)
    print(f"RUNNING CALCULATOR: {calc_name}")
    print("="*50)
    
    best_energy = float('inf')
    best_atoms = None
    
    for s in sites:
        for o in orientations:
            try:
                # Build Au(111) Slab
                slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
                pbo = get_pbo_molecule(o)
                add_adsorbate(slab, pbo, height=2.5, position=s)
                
                slab.calc = calc
                # Fix bottom layers (tags 3 & 4)
                c = FixAtoms(indices=[atom.index for atom in slab if atom.tag > 2])
                slab.set_constraint(c)

                name = f"{calc_name}_{s}_{o}"
                dyn = BFGS(slab, logfile=f"{output_dir}/{name}.log")
                dyn.run(fmax=0.05)
                
                energy = slab.get_potential_energy()
                print(f"Site: {s:<8} | Orient: {o:<13} | E: {energy:>10.4f} eV")

                # Remove metadata that triggers warnings in .xyz
                if 'adsorbate_info' in slab.info: 
                    del slab.info['adsorbate_info']

                # Save structures
                io.write(f"{output_dir}/{name}_converged.xyz", slab)
                io.write(f"{output_dir}/{name}_converged.vasp", slab, format='vasp', direct=True)

                if energy < best_energy:
                    best_energy = energy
                    best_atoms = slab.copy()
                    best_name = name

            except Exception as e:
                print(f"Failed {s}_{o} with {calc_name}: {e}")

    # Save summary for each calculator
    if best_atoms:
        print(f"\n{calc_name} Best: {best_name} at {best_energy:.4f} eV")
        io.write(f"BEST_{calc_name}_STABLE.vasp", best_atoms, format='vasp', direct=True)

print(f"\nAll results saved to '{output_dir}/'")

