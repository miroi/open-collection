from ase.build import add_adsorbate, molecule
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
import numpy as np

from ase.io import read

# Load the Gold slab from the XYZ file
slab = read('Au48_slab.xyz')

# 1. Define LJ Parameters (example values in eV and Angstrom)
# Note: In a real study, these should be fitted to DFT or experimental data.
refs = {
    ('Au', 'Au'): {'epsilon': 0.039, 'sigma': 2.90},
    ('Pb', 'Pb'): {'epsilon': 0.045, 'sigma': 3.20},
    ('O', 'O'):   {'epsilon': 0.010, 'sigma': 3.00},
}

# Mixing rules (Lorentz-Berthelot) for cross-interactions
def get_mix(a, b):
    eps = np.sqrt(refs[(a, a)]['epsilon'] * refs[(b, b)]['epsilon'])
    sig = (refs[(a, a)]['sigma'] + refs[(b, b)]['sigma']) / 2.0
    return eps, sig

# 2. Setup the LJ Calculator
# We must define interactions for all unique pairs in the system
pairs = [('Au', 'Au'), ('Pb', 'Pb'), ('O', 'O'), ('Au', 'Pb'), ('Au', 'O'), ('Pb', 'O')]
lj_params = {}
for p1, p2 in pairs:
    if (p1, p2) in refs:
        e, s = refs[(p1, p2)]['epsilon'], refs[(p1, p2)]['sigma']
    else:
        e, s = get_mix(p1, p2)
    lj_params[f'{p1}-{p2}'] = (e, s)

calc_lj = LennardJones(parameters=lj_params)

# 3. Calculate Reference Energies
# Energy of isolated slab
slab.calc = calc_lj
e_slab = slab.get_potential_energy()

# Energy of isolated PbO molecule
pbo = molecule('PbO')
pbo.calc = calc_lj
e_pbo = pbo.get_potential_energy()

# 4. Loop through adsorption sites
sites = ['ontop', 'fcc', 'hcp']
results = {}

for site in sites:
    # Create a copy of the slab for this site
    working_slab = slab.copy()
    working_slab.calc = calc_lj
    
    # Add PbO molecule (Pb atom at index 0 is positioned at the site)
    # height=2.5A is a standard starting point
    add_adsorbate(working_slab, pbo, height=2.5, position=site, mol_index=0)
    
    # Relax the system (keeping bottom layers fixed if constraints are set)
    dyn = BFGS(working_slab, logfile=None)
    dyn.run(fmax=0.05)
    
    # Calculate Adsorption Energy
    e_total = working_slab.get_potential_energy()
    e_ads = e_total - (e_slab + e_pbo)
    results[site] = e_ads
    print(f"Site: {site:6} | Adsorption Energy: {e_ads:.4f} eV")

