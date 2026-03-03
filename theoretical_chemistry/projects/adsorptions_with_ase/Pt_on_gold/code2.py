from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 1. Isolated Pt atom (Use Atoms, not Atom)
# We place it in a large box to avoid self-interaction
pt_atom = Atoms('Pt', positions=[(0, 0, 0)], cell=[10, 10, 10])
pt_atom.calc = EMT()
e_atom = pt_atom.get_potential_energy()

# 2. Clean Gold (Au) slab
slab = fcc111('Au', size=(3, 3, 3), vacuum=10.0)
slab.calc = EMT()
# Relax the clean slab first
BFGS(slab, logfile=None).run(fmax=0.05)
e_slab = slab.get_potential_energy()

# 3. Combined system (Pt adsorbed on Au)
# Note: add_adsorbate modifies the slab object in place
add_adsorbate(slab, 'Pt', height=2.0, position='ontop')
BFGS(slab, logfile=None).run(fmax=0.05)
e_total = slab.get_potential_energy()

# 4. Adsorption Energy
e_ads = e_total - (e_slab + e_atom)

print(f"Adsorption energy: {e_ads:.3f} eV")

