#!/usr/bin/env python
import os
import numpy as np
from ase import Atoms
from ase.build import add_adsorbate
from ase.calculators.lj import LennardJones
#from dftd4.ase import DFTD4
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
# 1. Load Slab
# ==============================================
atoms = Atoms(
    symbols=['Au']*48,
    positions=[ # positions in Angstrom 
        [2.162792418, 0.416273963, 5.000027010],
        [-0.720892382, 2.081170159, 7.354685128],
        [0.720950007, 1.248722043, 9.709145886],
        [5.046592448, 0.416273963, 5.000027010],
        [2.162907605, 2.081170159, 7.354685128],
        [3.604750037, 1.248722043, 9.709145886],
        [7.930392134, 0.416273963, 5.000027010],
        [5.046707978, 2.081170159, 7.354685128],
        [6.488550067, 1.248722043, 9.709145886],
        [10.814192164, 0.416273963, 5.000027010],
        [7.930508008, 2.081170159, 7.354685128],
        [9.372350097, 1.248722043, 9.709145886],
        [0.720892425, 2.913718011, 5.000027010],
        [-2.162792397, 4.578614244, 7.354685128],
        [-0.720950007, 3.746166128, 9.709145886],
        [3.604692455, 2.913718011, 5.000027010],
        [0.721007590, 4.578614244, 7.354685128],
        [2.162850022, 3.746166128, 9.709145886],
        [6.488492141, 2.913718011, 5.000027010],
        [3.604807963, 4.578614244, 7.354685128],
        [5.046650052, 3.746166128, 9.709145886],
        [9.372292170, 2.913718011, 5.000027010],
        [6.488607993, 4.578614244, 7.354685128],
        [7.930450082, 3.746166128, 9.709145886],
        [-0.721007762, 5.411162394, 5.000027010],
        [-3.604692240, 7.076058032, 7.354685128],
        [-2.162850022, 6.243610213, 9.709145886],
        [2.162792268, 5.411162394, 5.000027010],
        [-0.720892253, 7.076058032, 7.354685128],
        [0.720950007, 6.243610213, 9.709145886],
        [5.046591954, 5.411162394, 5.000027010],
        [2.162908120, 7.076058032, 7.354685128],
        [3.604750037, 6.243610213, 9.709145886],
        [7.930391984, 5.411162394, 5.000027010],
        [5.046708150, 7.076058032, 7.354685128],
        [6.488550067, 6.243610213, 9.709145886],
        [-2.162907777, 7.908606479, 5.000027010],
        [-5.046592255, 9.573502117, 7.354685128],
        [-3.604750037, 8.741054298, 9.709145886],
        [0.720892253, 7.908606479, 5.000027010],
        [-2.162792268, 9.573502117, 7.354685128],
        [-0.720950007, 8.741054298, 9.709145886],
        [3.604691939, 7.908606479, 5.000027010],
        [0.721008106, 9.573502117, 7.354685128],
        [2.162850022, 8.741054298, 9.709145886],
        [6.488491969, 7.908606479, 5.000027010],
        [3.604808135, 9.573502117, 7.354685128],
        [5.046650052, 8.741054298, 9.709145886]
    ],
    cell=[ # values in Angstrom
        [11.5352001190, 0.0000000000, 0.0000000000],
        [-5.7676000595, 9.9897763408, 0.0000000000],
        [0.0000000000, 0.0000000000, 19.7091999054]
    ],
    pbc=[True, True, True]
)

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
    
# Specify adsorbate 
adsorbate_symbol = 'O'  

# LJ parameters 
lj_epsilon = 0.03        # Adjust depending on your system
lj_sigma = 2.80          # Adjust depending on your system

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
            
                # Get MIC-corrected vector and positions
                v_ij = slab.get_distance(i, j, mic=True, vector=True)
                pos_i = slab[i].position
                pos_j = pos_i + v_ij  # Corrected position in same periodic image
            
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
            
                # Check if all distances are reasonable for a hollow site
                if (hollow_cutoff_min < dist_ij < hollow_cutoff_max and 
                    hollow_cutoff_min < dist_jk < hollow_cutoff_max and 
                    hollow_cutoff_min < dist_ki < hollow_cutoff_max):
                
                    # Get the minimum image vectors
                    v_ij = slab.get_distance(idx_i, idx_j, mic=True, vector=True)
                    v_ik = slab.get_distance(idx_i, idx_k, mic=True, vector=True)
                
                    cross_product = np.cross(v_ij, v_ik)
                    triangle_area = 0.5 * np.linalg.norm(cross_product)
                
                    # Center the coordinate system
                    pos_i = slab[idx_i].position
                    pos_j = pos_i + v_ij
                    pos_k = pos_i + v_ik
                
                    # Only accept if area is significant (non-collinear)
                    if triangle_area > 0.1:  # Minimum area threshold
                        print(f"  Hollow: {idx_i+1}-{idx_j+1}-{idx_k+1} "
                            f"(distances: {dist_ij:.3f}, {dist_jk:.3f}, {dist_ki:.3f} Å, "
                            f"area: {triangle_area:.3f} Å²)")
                    
                        sites[f'hollow_{idx_i+1}-{idx_j+1}-{idx_k+1}'] = {
                            'position': [(pos_i[0]+pos_j[0]+pos_k[0])/3, 
                                (pos_i[1]+pos_j[1]+pos_k[1])/3],
                            'height': hollow_height,
                            'atom_indices': [idx_i, idx_j, idx_k]
                        }
                    else:
                        print(f"  Rejected collinear hollow: {idx_i+1}-{idx_j+1}-{idx_k+1} "
                            f"(area: {triangle_area:.3f} Å²)")
    
    return sites

# ==============================================
# 4. Screening with calculator
# ==============================================
def screen_adsorption_sites(slab, sites):
    energies = {}
    
    adsorbate = Atoms(adsorbate_symbol, positions=[(0, 0, 0)])
    
    for name, site in sites.items():
        slab_with_ads = slab.copy()
        add_adsorbate(slab_with_ads, adsorbate, height=site['height'], position=site['position'])
        
        # Freeze the entire slab
        freeze_indices = list(range(len(slab)))  
        constraint = FixAtoms(indices=freeze_indices)
        slab_with_ads.set_constraint(constraint)
        
        # Debug print 
        print(f"\nSite {name}:")
        print(f"Fixed {len(freeze_indices)} slab atoms (VESTA indices: 1-{len(slab)})")
        print(f"{adsorbate_symbol} atom index: {len(slab_with_ads)} (VESTA numbering)")
        
        # Calculator setup 
        slab_with_ads.calc = SumCalculator([
            LennardJones(epsilon=lj_epsilon, sigma=lj_sigma, rc=10.0),
        #    DFTD4(method="PBE")
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
    sites = get_adsorption_sites(atoms)
    print(f"\nTesting {len(sites)} adsorption sites (on top layer only)...\n")
    energies = screen_adsorption_sites(atoms, sites)  
    
    # Find best site(s) 
    min_energy = min(energies.values())
    best_sites = [site for site, energy in energies.items() if energy == min_energy]
    
    # Write summary file 
    with open('adsorption_summary.txt', 'w') as f:
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
    print(f"\nMost stable configuration(s): {', '.join(best_sites)}")
    print(f"Minimum energy: {min_energy:.6f} eV\n")
    print("Complete energy table:")
    print("Site\t\t\tEnergy (eV)")
    print("="*50)
    for name, energy in sorted(energies.items(), key=lambda x: x[1]):
        print(f"{name:30s}\t{energy:.6f}", end="")
        if energy == min_energy:
            print(" <--- Most stable", end="")
        print()