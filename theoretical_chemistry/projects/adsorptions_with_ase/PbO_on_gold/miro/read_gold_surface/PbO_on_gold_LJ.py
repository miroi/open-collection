from ase import Atoms
from ase.build import add_adsorbate, molecule
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
from ase.io import read
import numpy as np

# 1. Load Slab
slab = read('Au48_slab.xyz')

# 2. Define standard parameters per element
# Key: (Symbol1, Symbol2)
# Value: (epsilon, sigma)
# We use Lorentz-Berthelot mixing rules: sigma_ab = (s_a + s_b)/2, eps_ab = sqrt(e_a * e_b)
raw_params = {
    'Au': (0.039, 2.90),
    'Pb': (0.045, 3.20),
    'O':  (0.010, 3.00)
}

def get_pair_params(symbols):
    """Generates the MoralesRetamar dictionary for all pairs in the system"""
    p = {}
    for s1 in symbols:
        for s2 in symbols:
            e1, sig1 = raw_params[s1]
            e2, sig2 = raw_params[s2]
            # Mixing rules
            eps_mix = np.sqrt(e1 * e2)
            sig_mix = (sig1 + sig2) / 2.0
            p[f'{s1}-{s2}'] = (eps_mix, sig_mix)
    return p

# 3. Setup Calculator for Slab
# The 'vasp' format/XYZ might not have symbols stored correctly, ensure they are set
slab_symbols = list(set(slab.get_chemical_symbols()))
calc_slab = LennardJones(pair_params=get_pair_params(slab_symbols), rc=10.0)
slab.calc = calc_slab
e_slab = slab.get_potential_energy()

# 4. Setup PbO Molecule
try:
    pbo = molecule('PbO')
except:
    pbo = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])

mol_symbols = list(set(pbo.get_chemical_symbols()))
calc_pbo = LennardJones(pair_params=get_pair_params(mol_symbols), rc=10.0)
pbo.calc = calc_pbo
e_pbo = pbo.get_potential_energy()

# 5. Adsorption Loop
sites = {'ontop': (2.16, 0.41), 'hollow': (2.88, 1.24)}
all_symbols = ['Au', 'Pb', 'O']
total_pair_params = get_pair_params(all_symbols)

print(f"{'Site':<10} | {'E_ads (eV)':<15}")
for name, pos in sites.items():
    working_system = slab.copy()
    add_adsorbate(working_system, pbo, height=2.5, position=pos)
    
    # Use the comprehensive pair parameter dictionary
    working_system.calc = LennardJones(pair_params=total_pair_params, rc=10.0)
    
    dyn = BFGS(working_system, logfile=None)
    dyn.run(fmax=0.05)
    
    e_ads = working_system.get_potential_energy() - (e_slab + e_pbo)
    print(f"{name:<10} | {e_ads:>10.4f}")

