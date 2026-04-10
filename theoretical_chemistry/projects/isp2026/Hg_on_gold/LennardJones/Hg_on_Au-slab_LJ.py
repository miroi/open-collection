#
# ase adsorption energy of Hg on gold slab write code
#
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS

# 1. Setup Parameters
adsorbate_element = 'Hg'
slab_element = 'Au'
vacuum_size = 10.0

# 2. Create the Au(111) Slab (4 layers, 3x3 supercell)
slab = fcc111(slab_element, size=(3, 3, 4), vacuum=vacuum_size)

# --- IMPORTANT: Replace LennardJones with a real DFT calculator ---
# Example: slab.calc = GPAW(mode='pw', xc='PBE')
slab.calc = LennardJones() 

# 3. Calculate Energy of the Clean Slab
print("Optimizing clean slab...")
dyn_slab = BFGS(slab, logfile=None)
dyn_slab.run(fmax=0.05)
e_slab = slab.get_potential_energy()

# 4. Calculate Energy of the Isolated Hg Atom
atom = Atoms(adsorbate_element, pbc=True)
atom.set_cell([20, 20, 20]) # Large box to simulate vacuum
atom.center()
atom.calc = LennardJones()
e_atom = atom.get_potential_energy()

# 5. Create the Adsorption System (Hg on Au)
# We place Hg on a 'ontop' site 2.5 Angstroms above the surface
add_adsorbate(slab, adsorbate_element, height=2.5, position='ontop')

# 6. Calculate Energy of the Combined System
print("Optimizing combined system...")
dyn_total = BFGS(slab, logfile=None)
dyn_total.run(fmax=0.05)
e_total = slab.get_potential_energy()

# 7. Calculate Adsorption Energy
e_ads = e_total - (e_slab + e_atom)

print("-" * 30)
print(f"Energy of Slab: {e_slab:.4f} eV")
print(f"Energy of Atom: {e_atom:.4f} eV")
print(f"Total Energy:   {e_total:.4f} eV")
print(f"Adsorption Energy (E_ads): {e_ads:.4f} eV")
print("-" * 30)

