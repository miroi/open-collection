import numpy as np
from ase.build import bulk, surface, add_vacuum
from ase.calculators.emt import EMT
from ase.optimize import BFGS

def compute_surface_energy(miller_indices, layers=4):
    # 1. Setup Bulk Reference
    a_lattice = 4.08
    au_bulk = bulk('Au', 'fcc', a=a_lattice)
    au_bulk.calc = EMT()
    e_bulk_per_atom = au_bulk.get_potential_energy() / len(au_bulk)

    # 2. Create the High-Index Surface
    # surface() cuts the crystal along the (h, k, l) plane
    slab = surface(au_bulk, miller_indices, layers)
    
    # Repeat to create a larger supercell for stability (2x2)
    slab = slab.repeat((2, 2, 1))
    
    # Add vacuum (10 Angstroms on both sides)
    slab.center(vacuum=10.0, axis=2)
    
    # 3. Calculate Energy
    slab.calc = EMT()
    dyn = BFGS(slab, logfile=None)
    dyn.run(fmax=0.05)
    
    # 4. Extract Geometry and Energy
    e_slab = slab.get_potential_energy()
    n_atoms = len(slab)
    
    # Area calculation using the cross product of lattice vectors a and b
    cell = slab.get_cell()
    area = np.linalg.norm(np.cross(cell[0], cell[1]))
    
    # Surface Energy formula
    gamma = (e_slab - n_atoms * e_bulk_per_atom) / (2 * area)
    return gamma

# --- Execution ---
high_index_surfaces = [(2, 1, 1), (3, 2, 1), (5, 1, 1)]

print(f"{'Miller Index':<15} | {'Surface Energy (eV/Å²)':<25}")
print("-" * 45)

for indices in high_index_surfaces:
    gamma = compute_surface_energy(indices)
    print(f"{str(indices):<15} | {gamma:.6f}")

