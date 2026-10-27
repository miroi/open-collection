from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from mace.calculators import mace_mp

# 1. Initialize the ML Potential (MACE-MP)
calc = mace_mp(model="medium", device='cpu')  # Use 'cuda' if GPU is available

def get_optimized_energy(atoms):
    atoms.calc = calc
    dyn = BFGS(atoms, logfile=None)
    dyn.run(fmax=0.01)
    return atoms.get_potential_energy()

# 2. Setup the Au(111) Slab
slab = fcc111('Au', size=(4, 4, 4), vacuum=12.0)

# Constraint: freeze ONLY the bottom layer (tag == 1 in fcc111)
#slab.set_constraint(FixAtoms(mask=[atom.tag == 1 for atom in slab]))

# 3. Reference: Energy of Clean Slab
print("Optimizing Au Slab...")
e_slab = get_optimized_energy(slab)

# 4. Reference: Energy of Isolated Hg Atom
from ase import Atoms
atom_hg = Atoms('Hg', pbc=True)
atom_hg.set_cell([15, 15, 15])
atom_hg.center()
e_atom = get_optimized_energy(atom_hg)

# 5. Adsorption: Hg on Au Slab
# Work on a copy so 'slab' stays clean for reference / later sites
slab_ads = slab.copy()
add_adsorbate(slab_ads, 'Hg', height=2.5, position='bridge')
print("Optimizing Hg + Au System...")
e_total = get_optimized_energy(slab_ads)

# 6. Final Calculation
e_ads = e_total - (e_slab + e_atom)

print("\n" + "="*30)
print(f"Slab Energy:      {e_slab:10.4f} eV")
print(f"Hg Atom Energy:   {e_atom:10.4f} eV")
print(f"Combined Energy:  {e_total:10.4f} eV")
print("-" * 30)
print(f"Adsorption Energy: {e_ads:10.4f} eV")
print("="*30)
