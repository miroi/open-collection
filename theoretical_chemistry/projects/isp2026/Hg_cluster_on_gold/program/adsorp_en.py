from ase.build import fcc111, add_adsorbate
from ase.cluster import Icosahedron
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from chgnet.model.dynamics import CHGNetCalculator

# --- 0. Shared Settings ---
calc = CHGNetCalculator()
fmax_val = 0.05

def get_relaxed_energy(atoms, name):
    atoms.calc = calc
    print(f"Optimizing {name}...")
    dyn = BFGS(atoms, trajectory=f'{name}.traj', logfile=None)
    dyn.run(fmax=fmax_val)
    return atoms.get_potential_energy()

# --- 1. Isolated Hg13 Cluster ---
# Manual latticeconstant fix for Hg
hg13_iso = Icosahedron('Hg', noshells=2, latticeconstant=3.0)
hg13_iso.center(vacuum=10) # Place in a vacuum box
e_cluster = get_relaxed_energy(hg13_iso, "cluster_iso")

# --- 2. Clean Au(111) Slab ---
slab_clean = fcc111('Au', size=(4, 4, 3), vacuum=10.0)
# Fix bottom 2 layers to simulate bulk
mask = [atom.tag < 3 for atom in slab_clean]
slab_clean.set_constraint(FixAtoms(mask=mask))
e_slab = get_relaxed_energy(slab_clean, "slab_clean")

# --- 3. Combined System (Hg13 on Au) ---
# Start fresh to avoid constraint conflicts
system = fcc111('Au', size=(4, 4, 3), vacuum=10.0)
hg13_ads = Icosahedron('Hg', noshells=2, latticeconstant=3.0)
add_adsorbate(system, hg13_ads, height=2.5, position='fcc')
system.set_constraint(FixAtoms(mask=mask)) # Apply same slab constraints
e_total = get_relaxed_energy(system, "total_system")

# --- 4. Final Calculation ---
e_ads = e_total - (e_slab + e_cluster)

print("-" * 30)
print(f"E_total:   {e_total:10.4f} eV")
print(f"E_slab:    {e_slab:10.4f} eV")
print(f"E_cluster: {e_cluster:10.4f} eV")
print(f"Adsorption Energy: {e_ads:10.4f} eV")
print("-" * 30)
if e_ads < 0:
    print("The adsorption is EXOTHERMIC (stable).")
else:
    print("The adsorption is ENDOTHERMIC (unstable).")

