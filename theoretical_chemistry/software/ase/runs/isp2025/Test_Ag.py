import os
import numpy as np
from ase import Atoms
from ase.build import add_adsorbate, fcc111
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import write
from ase.calculators.mixing import SumCalculator
from ase.neighborlist import NeighborList

# Create output directories
os.makedirs('vasp_outputs', exist_ok=True)
os.makedirs('ase_outputs', exist_ok=True)
os.makedirs('traj_files', exist_ok=True)

# ==============================================
# 1. Load Slab - Ag(111) with fcc111 function
# ==============================================
element = 'Ag'
size = (4, 4, 3)      # (x, y, z): number of repetitions
vacuum = 10.0          # Å vacuum along z-direction
a = 4.086             # Lattice constant for Ag in Å (FCC)

# Build slab using ASE's built-in function
slab = fcc111(symbol=element, size=size, a=a, vacuum=vacuum, periodic=False)

print(f"Loaded {element}(111) slab with {len(slab)} atoms")
print(f"Lattice vectors:\n{slab.cell}")

# Optional: Fix bottom layers (common in surface simulations)
layer_indices = []
for i, atom in enumerate(slab):
    if atom.position[2] < slab.cell[2, 2] * 0.3:  # Fix atoms below ~30% of height
        layer_indices.append(i)

if layer_indices:
    slab.set_constraint(FixAtoms(indices=layer_indices))
    print(f"Fixed {len(layer_indices)} atoms at the bottom.")

# ==============================================
# 2. Parameters
# ==============================================
# Define cutoffs (Å)
top_layer_cutoff = 0.5   # adjust depending on top layer thickness
top_height = 2.5
bridge_cutoff = 2.9      # set slightly larger than in-plane distance 
bridge_height = 2.0
hollow_cutoff_min = 2.0  
hollow_cutoff_max = 4.0  
hollow_height = 1.8

# List of adsorbates to test
adsorbates = ['C', 'H', 'N', 'O', 'S']

# LJ parameters (adjust based on element)
lj_params = {
    'C': {'epsilon': 0.05, 'sigma': 3.0},
    'H': {'epsilon': 0.02, 'sigma': 2.0},
    'N': {'epsilon': 0.04, 'sigma': 2.7},
    'O': {'epsilon': 0.03, 'sigma': 2.8},
    'S': {'epsilon': 0.06, 'sigma': 3.5}
}

# ==============================================
# 3. Define all unique adsorption sites
# ==============================================
def get_adsorption_sites(slab):
    sites = {}
    
    # Identify top layer
    positions = slab.get_positions()
    z_coords = positions[:, 2]
    top_layer_threshold = np.max(z_coords) - top_layer_cutoff
    
    top_layer_indices = [i for i, z in enumerate(z_coords) if z >= top_layer_threshold]
    print(f"Found {len(top_layer_indices)} top layer atoms: {[i+1 for i in top_layer_indices]}")
    
    # 1. Top sites
    for i in top_layer_indices:
        atom = slab[i]
        sites[f'top_{i+1}'] = {'position': atom.position[:2], 'height': top_height, 'atom_indices': [i]}
    
    # 2. Bridge sites
    for i in top_layer_indices:
        neighbors_found = []
        for j in top_layer_indices:
            if j <= i:
                continue
       
            dist = slab.get_distance(i, j, mic=True)
        
            if dist < bridge_cutoff:
                neighbors_found.append(j+1)
            
                v_ij = slab.get_distance(i, j, mic=True, vector=True)
                pos_i = slab[i].position
                pos_j = pos_i + v_ij
            
                sites[f'bridge_{i+1}-{j+1}'] = {
                    'position': [(pos_i[0] + pos_j[0])/2, (pos_i[1] + pos_j[1])/2],
                    'height': bridge_height,
                    'atom_indices': [i, j]
                }
    
        if neighbors_found:
            print(f"  Atom {i+1}: bridges with {neighbors_found}")
    
    # 3. Hollow sites
    for i, idx_i in enumerate(top_layer_indices):
        for j, idx_j in enumerate(top_layer_indices):
            if idx_j <= idx_i:
                continue
            
            dist_ij = slab.get_distance(idx_i, idx_j, mic=True)
            if dist_ij > hollow_cutoff_max:
                continue
        
            for k, idx_k in enumerate(top_layer_indices):
                if idx_k <= idx_j:
                    continue
            
                dist_jk = slab.get_distance(idx_j, idx_k, mic=True)
                dist_ki = slab.get_distance(idx_k, idx_i, mic=True)
            
                if (hollow_cutoff_min < dist_ij < hollow_cutoff_max and 
                    hollow_cutoff_min < dist_jk < hollow_cutoff_max and 
                    hollow_cutoff_min < dist_ki < hollow_cutoff_max):
                
                    v_ij = slab.get_distance(idx_i, idx_j, mic=True, vector=True)
                    v_ik = slab.get_distance(idx_i, idx_k, mic=True, vector=True)
                
                    cross_product = np.cross(v_ij, v_ik)
                    triangle_area = 0.5 * np.linalg.norm(cross_product)
                
                    pos_i = slab[idx_i].position
                    pos_j = pos_i + v_ij
                    pos_k = pos_i + v_ik
                
                    if triangle_area > 0.1:  # Non-collinear
                        print(f"  Hollow: {idx_i+1}-{idx_j+1}-{idx_k+1} "
                            f"(distances: {dist_ij:.3f}, {dist_jk:.3f}, {dist_ki:.3f} Å, "
                            f"area: {triangle_area:.3f} Å²)")
                    
                        sites[f'hollow_{idx_i+1}-{idx_j+1}-{idx_k+1}'] = {
                            'position': [(pos_i[0]+pos_j[0]+pos_k[0])/3, 
                                (pos_i[1]+pos_j[1]+pos_k[1])/3],
                            'height': hollow_height,
                            'atom_indices': [idx_i, idx_j, idx_k]
                        }
    
    return sites

# ==============================================
# 4. Screening with calculator
# ==============================================
def screen_adsorption_sites(slab, sites, adsorbate_symbol):
    energies = {}
    
    lj_epsilon = lj_params[adsorbate_symbol]['epsilon']
    lj_sigma = lj_params[adsorbate_symbol]['sigma']
    
    adsorbate = Atoms(adsorbate_symbol, positions=[(0, 0, 0)])
    
    for name, site in sites.items():
        slab_with_ads = slab.copy()
        add_adsorbate(slab_with_ads, adsorbate, height=site['height'], position=site['position'])
        
        # Freeze the entire slab
        freeze_indices = list(range(len(slab)))  
        constraint = FixAtoms(indices=freeze_indices)
        slab_with_ads.set_constraint(constraint)
        
        print(f"\nSite {name}:")
        print(f"Fixed {len(freeze_indices)} slab atoms")
        print(f"{adsorbate_symbol} atom index: {len(slab_with_ads)}")
        
        # Calculator setup 
        slab_with_ads.calc = SumCalculator([
            LennardJones(epsilon=lj_epsilon, sigma=lj_sigma, rc=10.0),
        ])
        
        # Relax only adsorbate 
        relax = BFGS(slab_with_ads, trajectory=f'traj_files/{adsorbate_symbol.lower()}_{name}.traj')
        relax.run(fmax=0.05)
        
        energies[name] = slab_with_ads.get_potential_energy()
        
        # Export to VASP 
        write(f'vasp_outputs/{adsorbate_symbol.lower()}_{name}.vasp', slab_with_ads, format='vasp', direct=True)
        
        # Export to ASE 
        with open(f'ase_outputs/{name}.ase', 'w') as f:
            f.write("from ase import Atoms\n\n")
            f.write("atoms = Atoms(\n")

            slab_symbols = [atom.symbol for atom in slab]
            if len(set(slab_symbols)) == 1: 
                slab_symbol = slab[0].symbol
                f.write(f"    symbols=['{slab_symbol}']*{len(slab)} + ['{adsorbate_symbol}'],\n")
            else:  
                f.write(f"    symbols={slab_symbols + [adsorbate_symbol]},\n")
    
            f.write("    positions=[\n")
            for idx, pos in enumerate(slab_with_ads.get_positions(), 1):
                f.write(f"        [{pos[0]:.10f}, {pos[1]:.10f}, {pos[2]:.10f}],\n")
            f.write("    ],\n")
            f.write("    cell=[\n")
            for vec in slab_with_ads.get_cell():
                f.write(f"        [{vec[0]:.10f}, {vec[1]:.10f}, {vec[2]:.10f}],\n")
            f.write("    ],\n")
            f.write(f"    pbc={slab_with_ads.pbc.tolist()}\n")
            f.write(")\n")
    
    return energies


# ==============================================
# 5. Run and Save Results 
# ==============================================
if __name__ == "__main__":
    sites = get_adsorption_sites(slab)
    print(f"\nTesting {len(sites)} adsorption sites (on top layer only)...\n")
    
    # Loop over each adsorbate
    for ad_atom in adsorbates:
        print(f"\n=== Testing adsorption of {ad_atom} ===")
        energies = screen_adsorption_sites(slab, sites, ad_atom)
        
        # Find best site(s) 
        min_energy = min(energies.values())
        best_sites = [site for site, energy in energies.items() if energy == min_energy]
        
        # Write summary file 
        with open(f'adsorption_summary_{ad_atom}.txt', 'w') as f:
            f.write(f"Number of sites tested: {len(sites)}\n")
            f.write(f"Most stable configuration(s): {', '.join(best_sites)}\n")
            f.write(f"Minimum energy: {min_energy:.6f} eV\n\n")
            f.write("Site\t\t\tEnergy (eV)\n")
            f.write("="*40 + "\n")
            for name, energy in sorted(energies.items(), key=lambda x: x[1]):
                f.write(f"{name:30s}\t{energy:.6f}\n")
                if energy == min_energy:
                    f.write(" "*-30 + "\t<--- Most stable\n")
        
        # Console output 
        print(f"Most stable configuration(s): {', '.join(best_sites)}")
        print(f"Minimum energy: {min_energy:.6f} eV\n")
