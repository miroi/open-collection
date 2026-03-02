import numpy as np
from ase.build import bulk, surface
from ase.optimize import BFGS
try:
    from chgnet.model.dynamics import CHGNetCalculator
except ImportError:
    print("Error: chgnet not found. Run 'pip install chgnet'")
    raise

# 1. Setup Calculator
calc = CHGNetCalculator()

# 2. Optimize Bulk (Crucial for ML Potentials)
au_bulk = bulk('Au', 'fcc', a=4.08)
au_bulk.calc = calc
dyn_bulk = BFGS(au_bulk, logfile=None)
dyn_bulk.run(fmax=0.01)
e_bulk_per_atom = au_bulk.get_potential_energy() / len(au_bulk)

def compute_surface_energy(miller, n_layers=4):
    # For high-index surfaces, we often need more layers to reach bulk-like center
    # Create slab and add vacuum
    slab = surface(au_bulk, miller, n_layers)
    slab.center(vacuum=12.0, axis=2)
    slab = slab.repeat((2, 2, 1)) # Lateral size for stability
    
    slab.calc = calc
    
    # Relax only the atom positions (keep cell fixed)
    dyn = BFGS(slab, logfile=None)
    dyn.run(fmax=0.05)
    
    e_slab = slab.get_potential_energy()
    
    # Calculate Area
    cell = slab.get_cell()
    area = np.linalg.norm(np.cross(cell[0], cell[1]))
    
    gamma = (e_slab - len(slab) * e_bulk_per_atom) / (2 * area)
    return gamma

# 3. Test various indices
surfaces = [(1,1,1), (1,0,0), (1,1,0), (2,1,1), (3,2,1)]

print(f"{'Miller':<10} | {'γ (eV/Å²)':<10}")
print("-" * 25)

for m in surfaces:
    try:
        g = compute_surface_energy(m)
        print(f"{str(m):<10} | {g:.6f}")
    except Exception as e:
        print(f"Failed {m}: {e}")

