import numpy as np
from ase import Atoms
from ase.build import add_adsorbate, molecule
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import read, write, Trajectory

# 1. Load the Gold slab
# Ensure 'Au48_slab.xyz' exists in your directory
slab = read('Au48_slab.xyz')

# 2. Define LJ Parameters and Mixing Rules
# Atomic parameters: (epsilon in eV, sigma in Angstrom)
refs = {
    'Au': (0.039, 2.90),
    'Pb': (0.045, 3.20),
    'O':  (0.010, 3.00),
}

def get_mixed_pair_params(symbols):
    """Generates the pair_params dictionary required by ASE LennardJones"""
    pair_dict = {}
    unique_symbols = list(set(symbols))
    for i, s1 in enumerate(unique_symbols):
        for s2 in unique_symbols[i:]:
            e1, sig1 = refs[s1]
            e2, sig2 = refs[s2]
            # Lorentz-Berthelot mixing rules
            eps_mix = np.sqrt(e1 * e2)
            sig_mix = (sig1 + sig2) / 2.0
            pair_dict[f'{s1}-{s2}'] = (eps_mix, sig_mix)
    return pair_dict

# 3. Calculate Reference Energies
# Slab Reference
slab_params = get_mixed_pair_params(slab.get_chemical_symbols())
slab.calc = LennardJones(pair_params=slab_params, rc=10.0)
e_slab = slab.get_potential_energy()

# PbO Molecule Reference
pbo = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])

pbo_params = get_mixed_pair_params(pbo.get_chemical_symbols())
pbo.calc = LennardJones(pair_params=pbo_params, rc=10.0)
e_pbo = pbo.get_potential_energy()

# 4. Adsorption Loop
# High-symmetry sites based on Au(111) geometry
sites = {
    'ontop':  (2.16, 0.41),
    'bridge': (3.60, 0.41),
    'hollow': (2.88, 1.24)
}

# Define all possible pair interactions for the combined system
all_pair_params = get_mixed_pair_params(['Au', 'Pb', 'O'])

print(f"{'Site':<10} | {'E_ads (eV)':<12}")
print("-" * 25)

for name, pos in sites.items():
    # Setup the combined system
    working_system = slab.copy()
    # Add PbO: mol_index=0 (Pb) faces the surface
    add_adsorbate(working_system, pbo, height=2.5, position=pos, mol_index=0)
    
    # Apply Multi-element LJ Calculator
    working_system.calc = LennardJones(pair_params=all_pair_params, rc=10.0)
    
    # Fix bottom two layers (Z < 9.0 A) to keep slab stable
    mask = [atom.position[2] < 9.0 for atom in working_system]
    working_system.set_constraint(FixAtoms(mask=mask))
    
    # Setup Trajectory
    traj_name = f'relax_{name}.traj'
    
    # Run Optimization
    dyn = BFGS(working_system, trajectory=traj_name, logfile=None)
    dyn.run(fmax=0.05)
    
    # Calculate Adsorption Energy
    e_total = working_system.get_potential_energy()
    e_ads = e_total - (e_slab + e_pbo)
    print(f"{name:<10} | {e_ads:>10.4f}")
    
    # 5. Export Files
    # Save final geometry
    write(f'final_{name}.xyz', working_system)
    write(f'POSCAR_{name}', working_system, format='vasp')
    
    # Save optimization movie (XYZ format)
    traj_data = Trajectory(traj_name)
    write(f'movie_{name}.xyz', traj_data)

print("\nTask complete. Trajectories and final geometries saved.")

