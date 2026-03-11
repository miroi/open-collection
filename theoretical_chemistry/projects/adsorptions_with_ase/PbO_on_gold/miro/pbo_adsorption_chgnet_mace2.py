import os
import torch
import numpy as np
from ase import Atoms, io
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# --- MLIP Calculators ---
from chgnet.model.dynamics import CHGNetCalculator
try:
    from mace.calculators import mace_mp
    HAS_MACE = True
except ImportError:
    print("MACE not found. Install it with: pip install mace-torch")
    HAS_MACE = False

# 1. Setup Environment & Device
output_dir = "adsorption_dual_results"
os.makedirs(output_dir, exist_ok=True)
device = "cuda" if torch.cuda.is_available() else "cpu"

def get_pbo_molecule(orientation='Pb-down'):
    """Creates PbO molecule. Bond length approx 1.92 A."""
    mol = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])
    if orientation == 'O-down': mol.rotate(180, 'x')
    elif orientation == 'horizontal': mol.rotate(90, 'x')
    elif orientation == 'slant-Pb-down': mol.rotate(45, 'x')
    elif orientation == 'slant-O-down': mol.rotate(135, 'x')
    return mol

# Initialize Calculators
calculators = {"CHGNet": CHGNetCalculator()}
if HAS_MACE:
    calculators["MACE"] = mace_mp(model="medium", device=device, default_dtype="float32")

# Define Search Space
sites = ['ontop', 'bridge', 'fcc', 'hcp']
orientations = ['Pb-down', 'O-down', 'horizontal', 'slant-Pb-down', 'slant-O-down']

# 2. Main Comparison Loop
for calc_name, calc in calculators.items():
    print(f"\n" + "="*60)
    print(f"CALCULATOR: {calc_name} | DEVICE: {device}")
    print("="*60)
    
    # --- REFERENCE CALCULATIONS FOR ADSORPTION ENERGY ---
    # 1. Clean Slab Energy
    slab_ref = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
    slab_ref.calc = calc
    e_slab_ref = slab_ref.get_potential_energy()
    
    # 2. Isolated Molecule Energy (in a large vacuum box)
    mol_ref = get_pbo_molecule()
    mol_ref.set_cell([15, 15, 15])
    mol_ref.center()
    mol_ref.calc = calc
    e_mol_ref = mol_ref.get_potential_energy()
    
    print(f"Reference Energies | Slab: {e_slab_ref:.4f} eV | PbO: {e_mol_ref:.4f} eV")

    best_e_ads = float('inf')
    best_atoms = None
    
    for s in sites:
        for o in orientations:
            try:
                # Build System
                slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
                pbo = get_pbo_molecule(o)
                add_adsorbate(slab, pbo, height=2.5, position=s)
                slab.calc = calc
                
                # Fix bottom two layers (tags 3 and 4)
                c = FixAtoms(indices=[atom.index for atom in slab if atom.tag > 2])
                slab.set_constraint(c)

                name = f"{calc_name}_{s}_{o}"
                traj_file = f"{output_dir}/{name}.traj"
                
                # BFGS with Trajectory saving
                dyn = BFGS(slab, logfile=f"{output_dir}/{name}.log", trajectory=traj_file)
                dyn.run(fmax=0.05)
                
                # Calculate Adsorption Energy
                e_total = slab.get_potential_energy()
                e_ads = e_total - (e_slab_ref + e_mol_ref)
                
                print(f"Site: {s:<8} | Orient: {o:<13} | E_ads: {e_ads:>10.4f} eV")

                # Clean up and save final structure
                if 'adsorbate_info' in slab.info: del slab.info['adsorbate_info']
                io.write(f"{output_dir}/{name}_final.vasp", slab, format='vasp', direct=True)

                if e_ads < best_e_ads:
                    best_e_ads = e_ads
                    best_atoms = slab.copy()
                    best_name = name

            except Exception as e:
                print(f"Failed {s}_{o} with {calc_name}: {e}")

    if best_atoms:
        print(f"\n>>> {calc_name} BEST: {best_name}")
        print(f">>> Lowest Adsorption Energy: {best_e_ads:.4f} eV")
        io.write(f"BEST_{calc_name}_STABLE.vasp", best_atoms, format='vasp', direct=True)

print(f"\nAll trajectories and structures saved to '{output_dir}/'")

