from ase.build import add_adsorbate, molecule
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
import numpy as np

from ase.io import read

# Load the Gold slab from the XYZ file
slab = read('Au48_slab.xyz')

# Define symbols for your system
symbols = ['Au', 'Pb', 'O']

# Define epsilon and sigma for each element in the same order
# (Using your reference values)
epsilons = [0.039, 0.045, 0.010]  # Au, Pb, O
sigmas = [2.90, 3.20, 3.00]      # Au, Pb, O

# Initialize the calculator
# ASE will automatically apply Lorentz-Berthelot mixing rules
calc_lj = LennardJones(epsilon=epsilons, sigma=sigmas)


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

