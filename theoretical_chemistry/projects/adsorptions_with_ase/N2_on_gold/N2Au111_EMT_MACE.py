# Adsorption energy calculation with ASE using both EMT and MACE.
# Fixed Atoms object 'get_layers' attribute error.
import pandas as pd
import numpy as np
from ase import Atoms
from ase.build import add_adsorbate, fcc111
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton
from ase.calculators.emt import EMT
from mace.calculators import mace_mp

# Define parameters
h = 1.85
d = 1.10

# Initialize both calculators
calculators = {
    "EMT": EMT(),
    "MACE": mace_mp(
        model="medium", 
        dispersion=False, 
        default_dtype="float64",  # <-- Changed from float32 to float64
        device="cpu"
    ) 
    # Note: change device="cuda" if you have a compatible GPU
}


def assign_layer_tags(atoms, tolerance=0.1):
    """
    Manually group atoms into layers by their Z-coordinates.
    Assigns an integer tag to each atom (0 for bottom layer, 1 for next, etc.)
    """
    z_coords = atoms.positions[:, 2]
    # Find unique Z coordinates within a small tolerance
    unique_z = sorted(list(set(np.round(z_coords / tolerance) * tolerance)))
    
    # Map each position to its closest unique layer Z index
    tags = []
    for z in z_coords:
        layer_idx = np.argmin([abs(z - uz) for uz in unique_z])
        tags.append(layer_idx)
        
    atoms.set_tags(tags)
    return np.array(tags)

def run_adsorption_calculation(name, calc):
    print(f"\n========================================\n Running with {name} Calculator \n========================================")
    
    # 1. Clean gold slab (4 layers thick)
    slab = fcc111('Au', size=(6, 6, 4), vacuum=15.0)
    slab.calc = calc
    
    # --- Relax the clean slab first ---
    # Assign tags manually to the slab atoms
    tags = assign_layer_tags(slab) 
    
    # Freeze bottom two layers (tags 0 and 1) of the clean slab
    slab_constraint = FixAtoms(mask=[tag < 2 for tag in tags])
    slab.set_constraint(slab_constraint)
    
    print(f" Relaxing clean Au(111) slab with {name}...")
    dyn_slab = QuasiNewton(slab, trajectory=f'clean_slab_{name.lower()}.traj', logfile=None)
    dyn_slab.run(fmax=0.02)
    e_slab = slab.get_potential_energy()
    
    # 2. Isolated N2 molecule
    molecule = Atoms('2N', positions=[(0.0, 0.0, 0.0), (0.0, 0.0, d)])
    molecule.calc = calc
    e_N2 = molecule.get_potential_energy()
    
    # 3. Combined system (add N2 to the pre-relaxed slab)
    add_adsorbate(slab, molecule, h, 'ontop')
    
    # 4. Update constraints for the combined system
    # Refresh tags because new adsorbate atoms were appended
    # Non-surface atoms (like Nitrogen) will be assigned separate high layer tags or can be filtered out
    updated_tags = assign_layer_tags(slab)
    
    # Freeze only the gold atoms belonging to the bottom two layers (tag 0 and 1)
    combined_constraint = FixAtoms(mask=[(atom.symbol == 'Au' and tag < 2) for atom, tag in zip(slab, updated_tags)])
    slab.set_constraint(combined_constraint)
    
    # 5. Geometry optimization of the combined system
    traj_filename = f'N2Au_{name.lower()}_relaxed.traj'
    dyn = QuasiNewton(slab, trajectory=traj_filename)
    print(f" Relaxing N2 + top 2 layers of Au(111) with {name}...")
    dyn.run(fmax=0.02)
    
    # 6. Final Energy and Adsorption calculations
    e_combined = slab.get_potential_energy()
    e_ads_pos = e_slab + e_N2 - e_combined
    e_ads_neg = e_combined - (e_slab + e_N2)
    
    return {
        "Calculator": name,
        "E_slab (eV)": round(e_slab, 4),
        "E_N2 (eV)": round(e_N2, 4),
        "E_combined (eV)": round(e_combined, 4),
        "E_ads (+ favorable)": round(e_ads_pos, 4),
        "E_ads (- favorable)": round(e_ads_neg, 4)
    }

# Run the calculation loop
results = []
for name, calc_obj in calculators.items():
    res = run_adsorption_calculation(name, calc_obj)
    results.append(res)

# Print a direct comparison table
df = pd.DataFrame(results)
print("\n=================== FINAL COMPARISON (RELAXED SURFACE) ===================")
print(df.to_string(index=False))

