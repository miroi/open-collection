from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from mace.calculators import mace_mp

# 1. Initialize the ML Potential (MACE-MP)
# 'medium' is usually sufficient for accurate geometry and energy
calc = mace_mp(model="medium", device='cpu') # Use 'cuda' if GPU is available

def get_optimized_energy(atoms):
    atoms.calc = calc
    dyn = BFGS(atoms, logfile=None)
    dyn.run(fmax=0.01) # Relax until forces are small
    return atoms.get_potential_energy()

# 2. Setup the Au(111) Slab
# 4 layers, 3x3 supercell. 
slab = fcc111('Au', size=(3, 3, 4), vacuum=12.0)

# Constraint: Freeze the bottom two layers to simulate bulk
mask = [atom.tag > 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=[not m for m in mask]))

# 3. Reference: Energy of Clean Slab
print("Optimizing Au Slab...")
e_slab = get_optimized_energy(slab)

# 4. Reference: Energy of Isolated Hg Atom
from ase import Atoms
atom_hg = Atoms('Hg', pbc=True)
atom_hg.set_cell([15, 15, 15]) # Large box to avoid self-interaction
atom_hg.center()
e_atom = get_optimized_energy(atom_hg)

# 5. Adsorption: Hg on Au Slab
# Testing the 'hollow' site as it is often most stable for metal-on-metal
add_adsorbate(slab, 'Hg', height=2.5, position='hollow')
print("Optimizing Hg + Au System...")
e_total = get_optimized_energy(slab)

# 6. Final Calculation
e_ads = e_total - (e_slab + e_atom)

print("\n" + "="*30)
print(f"Slab Energy:      {e_slab:10.4f} eV")
print(f"Hg Atom Energy:   {e_atom:10.4f} eV")
print(f"Combined Energy:  {e_total:10.4f} eV")
print("-" * 30)
print(f"Adsorption Energy: {e_ads:10.4f} eV")
print("="*30)

