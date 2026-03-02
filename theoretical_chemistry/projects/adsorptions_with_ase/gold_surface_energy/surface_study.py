import numpy as np
import pandas as pd
from ase.build import bulk, surface
from ase.optimize import BFGS
from chgnet.model.dynamics import CHGNetCalculator

# 1. Setup Calculator & Optimize Bulk
calc = CHGNetCalculator()
au_bulk = bulk('Au', 'fcc', a=4.08)
au_bulk.calc = calc
# Relax bulk to find the potential's equilibrium lattice constant
dyn_bulk = BFGS(au_bulk, logfile=None)
dyn_bulk.run(fmax=0.01)
e_bulk_per_atom = au_bulk.get_potential_energy() / len(au_bulk)

def compute_surface_energy(miller, n_layers=4):
    """
    Computes surface energy for any (h, k, l) index.
    Note: n_layers is adjusted for high-index surfaces to ensure thickness.
    """
    # Create slab
    # For very high indices, you might need more layers to ensure bulk-like center
    slab = surface(au_bulk, miller, n_layers)
    slab.center(vacuum=12.0, axis=2)
    
    # Repeat for stability: ensure the lateral dimension is at least ~8-10 Angstroms
    # This prevents self-interaction of atoms with their periodic images
    repeat_x = int(np.ceil(10.0 / np.linalg.norm(slab.get_cell()[0])))
    repeat_y = int(np.ceil(10.0 / np.linalg.norm(slab.get_cell()[1])))
    slab = slab.repeat((repeat_x, repeat_y, 1))
    
    slab.calc = calc
    
    # Relax only positions
    dyn = BFGS(slab, logfile=None)
    dyn.run(fmax=0.05)
    
    e_slab = slab.get_potential_energy()
    area = np.linalg.norm(np.cross(slab.get_cell()[0], slab.get_cell()[1]))
    
    # Formula: (E_slab - n_atoms * E_bulk) / (2 * Area)
    gamma = (e_slab - len(slab) * e_bulk_per_atom) / (2 * area)
    return gamma

# 2. Define a diverse set of Miller Indices
# (111), (100), (110) -> Low index
# (211), (311), (221) -> Stepped surfaces
# (321) -> Kinked surface (highly reactive)
surface_list = [
    (1, 1, 1), (1, 0, 0), (1, 1, 0), 
    (2, 1, 1), (3, 1, 1), (2, 2, 1), 
    (3, 2, 1), (5, 1, 1), (4, 1, 0)
]

results = []

print(f"{'Miller Index':<15} | {'γ (eV/Å²)':<12} | {'Relative to (111)':<10}")
print("-" * 50)

# Reference for (111) to calculate stability ratio
gamma_111 = compute_surface_energy((1,1,1))

for m in surface_list:
    try:
        g = compute_surface_energy(m)
        rel = g / gamma_111
        results.append({"Miller": m, "Gamma": g, "Rel": rel})
        print(f"{str(m):<15} | {g:.6f}     | {rel:.2f}")
    except Exception as e:
        print(f"Error on {m}: {e}")

# 3. (Optional) Save to CSV for analysis
# df = pd.DataFrame(results)
# df.to_csv("gold_surfaces_chgnet.csv", index=False)

