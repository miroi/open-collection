import numpy as np
from ase import Atoms
from ase.build import add_adsorbate
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import read, write, Trajectory

# 1. Load the Gold slab
slab = read('Au48_slab.xyz')

# 2. Automatically Identify Adsorption Sites from Coordinates
# Find the top-most Z-coordinate to identify surface atoms
z_coords = slab.get_positions()[:, 2]
z_max = np.max(z_coords)
surface_indices = [i for i, z in enumerate(z_coords) if z > z_max - 0.5]
surface_atoms = slab[surface_indices]

# Ontop: Use the first surface atom's (x, y)
ontop_pos = surface_atoms.get_positions()[0][:2]

# Bridge: Midpoint between the first and second surface atoms
pos1 = surface_atoms.get_positions()[0][:2]
pos2 = surface_atoms.get_positions()[1][:2]
bridge_pos = (pos1 + pos2) / 2.0

# Hollow: Centroid of the first three surface atoms (forming a triangle)
pos3 = surface_atoms.get_positions()[2][:2]
hollow_pos = (pos1 + pos2 + pos3) / 3.0

sites = {
    'ontop':  ontop_pos,
    'bridge': bridge_pos,
    'hollow': hollow_pos
}

# 3. Define LJ Parameters and Mixing Rules
refs = {'Au': (0.039, 2.90), 'Pb': (0.045, 3.20), 'O': (0.010, 3.00)}

def get_mixed_pair_params(symbols):
    pair_dict = {}
    unique_symbols = list(set(symbols))
    for i, s1 in enumerate(unique_symbols):
        for s2 in unique_symbols[i:]:
            e1, sig1 = refs[s1]
            e2, sig2 = refs[s2]
            pair_dict[f'{s1}-{s2}'] = (np.sqrt(e1 * e2), (sig1 + sig2) / 2.0)
    return pair_dict

# 4. Calculate Reference Energies
all_pair_params = get_mixed_pair_params(['Au', 'Pb', 'O'])

# Slab Reference
slab.calc = LennardJones(pair_params=get_mixed_pair_params(slab.get_chemical_symbols()), rc=10.0)
e_slab = slab.get_potential_energy()

# PbO Molecule Reference (Manual definition)
pbo = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])
pbo.calc = LennardJones(pair_params=get_mixed_pair_params(['Pb', 'O']), rc=10.0)
e_pbo = pbo.get_potential_energy()

# 5. Adsorption Loop
print(f"{'Site':<10} | {'E_ads (eV)':<12}")
print("-" * 25)

for name, pos in sites.items():
    working_system = slab.copy()
    
    # Add PbO molecule (Pb at index 0 faces the calculated site)
    add_adsorbate(working_system, pbo, height=2.5, position=pos, mol_index=0)
    
    # Fix the slab, relax the molecule
    working_system.set_constraint(FixAtoms(indices=list(range(len(slab)))))
    working_system.calc = LennardJones(pair_params=all_pair_params, rc=10.0)
    
    traj_name = f'relax_{name}.traj'
    dyn = BFGS(working_system, trajectory=traj_name, logfile=None)
    dyn.run(fmax=0.05)
    
    e_ads = working_system.get_potential_energy() - (e_slab + e_pbo)
    print(f"{name:<10} | {e_ads:>10.4f}")
    
    # Save files
    write(f'final_{name}.xyz', working_system)
    write(f'POSCAR_{name}', working_system, format='vasp')
    write(f'movie_{name}.xyz', Trajectory(traj_name))

print("\nDone. Sites were calculated dynamically from your XYZ file.")

