from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from chgnet.model.dynamics import CHGNetCalculator

# 1. Initialize CHGNet Calculator
# CHGNet will automatically download pre-trained weights on first run
calc = CHGNetCalculator()

def get_optimized_energy(atoms):
    atoms.calc = calc
    # fmax=0.05 is usually sufficient for adsorption energy trends
    dyn = BFGS(atoms, logfile=None)
    dyn.run(fmax=0.05)
    return atoms.get_potential_energy()

# 2. Setup Au(111) Slab
# A 3x3 supercell with 4 layers is a good balance for MLIP speed/accuracy
slab = fcc111('Au', size=(3, 3, 4), vacuum=12.0)

# Constraint: Freeze the bottom two layers (indices based on Z-coordinate)
# This simulates the bulk underneath the surface
c = FixAtoms(indices=[atom.index for atom in slab if atom.tag > 2])
slab.set_constraint(c)

# 3. Calculate Clean Slab Energy
print("Optimizing clean Au slab...")
e_slab = get_optimized_energy(slab)

# 4. Calculate Isolated Hg Atom Energy
# We place it in a large periodic box to simulate gas phase
atom_hg = Atoms('Hg', pbc=True)
atom_hg.set_cell([15, 15, 15])
atom_hg.center()
print("Calculating isolated Hg atom energy...")
e_atom = get_optimized_energy(atom_hg)

# 5. Calculate Adsorption at different sites
# We test 'fcc' and 'ontop' as they are the most likely candidates
sites = ['fcc', 'ontop']
results = {}

for site in sites:
    # Reset slab for each calculation
    working_slab = fcc111('Au', size=(3, 3, 4), vacuum=12.0)
    working_slab.set_constraint(c)
    
    print(f"Optimizing Hg at {site} site...")
    add_adsorbate(working_slab, 'Hg', height=2.5, position=site)
    
    e_total = get_optimized_energy(working_slab)
    e_ads = e_total - (e_slab + e_atom)
    results[site] = e_ads

# 6. Output Results
print("\n" + "="*40)
print(f"{'Site':<10} | {'E_total (eV)':<15} | {'E_ads (eV)':<10}")
print("-" * 40)
for site, e_ads in results.items():
    # We use a placeholder for total energy logic here
    print(f"{site:<10} | {'Done':<15} | {e_ads:10.4f} eV")
print("="*40)
print("Note: A negative E_ads indicates stable adsorption.")

