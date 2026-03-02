from openbabel import openbabel
from openbabel import pybel
import numpy as np

def calculate_hg_au_adsorption(slab_file, height=2.5):
    # 1. Load the Gold Slab
    try:
        slab = next(pybel.readfile("xyz", slab_file))
    except StopIteration:
        return "Error: File not found or empty."

    # 2. Setup Force Field (UFF)
    ff = pybel._forcefields["uff"]
    
    # --- Calculate Slab Energy ---
    if not ff.Setup(slab.OBMol):
        return "Error: UFF could not setup slab."
    e_slab = ff.Energy()
    
    # --- Create the Complex (Slab + Hg) ---
    # We clone the slab OBMol to create the combined system
    import openbabel as ob
    combined_obmol = ob.OBMol(slab.OBMol)
    
    # Get surface coordinates to place Hg
    coords = np.array([atom.coords for atom in slab.atoms])
    z_max = np.max(coords[:, 2])
    x_mid = np.mean(coords[:, 0])
    y_mid = np.mean(coords[:, 1])
    
    # Add Mercury atom (Atomic Number 80)
    hg_atom = combined_obmol.NewAtom()
    hg_atom.SetAtomicNum(80)
    hg_atom.SetVector(x_mid, y_mid, z_max + height)
    
    # 3. Calculate Energy of Complex
    combined_mol = pybel.Molecule(combined_obmol)
    if not ff.Setup(combined_mol.OBMol):
        return "Error: UFF could not setup complex."
    
    # We only optimize a few steps to let the Hg find its preferred distance
    ff.ConjugateGradients(100)
    e_complex = ff.Energy()
    
    # 4. Energy of isolated Hg (Single atoms have 0 energy in UFF)
    e_hg = 0 
    
    # 5. Adsorption Energy Calculation
    e_ads = e_complex - (e_slab + e_hg)
    
    return e_ads, e_slab, e_complex

# --- Execution ---
slab_filename = "gold_slab.xyz"

# Generate a dummy slab if you don't have one (requires ASE)
# from ase.build import fcc111; from ase.io import write
# write('gold_slab.xyz', fcc111('Au', size=(2,2,3), vacuum=10.0))

results = calculate_hg_au_adsorption(slab_filename)

if isinstance(results, str):
    print(results)
else:
    e_ads, e_slab, e_comp = results
    print(f"--- Results for Hg on Au ---")
    print(f"Slab Energy:    {e_slab:12.4f} kJ/mol")
    print(f"Complex Energy: {e_comp:12.4f} kJ/mol")
    print(f"Adsorption E:   {e_ads:12.4f} kJ/mol")
    print(f"Adsorption E:   {e_ads / 96.485:12.4f} eV")

