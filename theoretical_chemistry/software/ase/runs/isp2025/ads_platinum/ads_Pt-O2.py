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
# 1. Load Slab  Pf fcc(111), from ase gui, put in a(exp)
# ==============================================
atoms = Atoms(
    symbols=['Pt']*48,
    positions=[ # positions in Angstrom 
  [1.38592929, 0.80016665, 10.0],
[4.15778787, 0.80016665, 10.0],
[6.92964646, 0.80016665, 10.0],
[9.70150504, 0.80016665, 10.0],
[2.77185858, 3.2006666, 10.0],
[5.54371716, 3.2006666, 10.0],
[8.31557575, 3.2006666, 10.0],
[11.08743433, 3.2006666, 10.0],
[4.15778787, 5.60116655, 10.0],
[6.92964646, 5.60116655, 10.0],
[9.70150504, 5.60116655, 10.0],
[12.47336362, 5.60116655, 10.0],
[5.54371716, 8.00166649, 10.0],
[8.31557575, 8.00166649, 10.0],
[11.08743433, 8.00166649, 10.0],
[13.85929291, 8.00166649, 10.0],
[0, 1.6003333, 12.26321306],
[2.77185858, 1.6003333, 12.26321306],
[5.54371716, 1.6003333, 12.26321306],
[8.31557575, 1.6003333, 12.26321306],
[1.38592929, 4.00083325, 12.26321306],
[4.15778787, 4.00083325, 12.26321306],
[6.92964646, 4.00083325, 12.26321306],
[9.70150504, 4.00083325, 12.26321306],
[2.77185858, 6.40133319, 12.26321306],
[5.54371716, 6.40133319, 12.26321306],
[8.31557575, 6.40133319, 12.26321306],
[11.08743433, 6.40133319, 12.26321306],
[4.15778787, 8.80183314, 12.26321306],
[6.92964646, 8.80183314, 12.26321306],
[9.70150504, 8.80183314, 12.26321306],
[12.47336362, 8.80183314, 12.26321306],
[0.0, 0.0, 14.52642611],
[2.77185858, 0.0, 14.52642611],
[5.54371716, 0.0, 14.52642611],
[8.31557575, 0.0, 14.52642611],
[1.38592929, 2.40049995, 14.52642611],
[4.15778787, 2.40049995, 14.52642611],
[6.92964646, 2.40049995, 14.52642611],
[9.70150504, 2.40049995, 14.52642611],
[2.77185858, 4.8009999, 14.52642611],
[5.54371716, 4.8009999, 14.52642611],
[8.31557575, 4.8009999, 14.52642611],
[11.08743433, 4.8009999, 14.52642611],
[4.15778787, 7.20149984, 14.52642611],
[6.92964646, 7.20149984, 14.52642611],
[9.70150504, 7.20149984, 14.52642611],
[12.47336362, 7.20149984, 14.52642611]
    ],
    cell=[ # values in Angstrom
       [11.0874343290, 0.0000000000, 0.0000000000],
       [5.5437171645, 9.6019997917, 0.0000000000],
       [0.0000000000, 0.0000000000, 24.5264261104]
    ],
    pbc=[True, True, True]
)

# ==============================================
# 2. Parameters
# ==============================================
# Define cutoffs (Å)
top_layer_cutoff = 0.5   # thickness of the top layer, adjust if needed
top_height = 2.5         # height threshold for top layer atoms
bridge_cutoff = 3.0      # bridge neighbors cutoff, slightly above 2.77 Å (Pt NN dist)
bridge_height = 2.5      # height cutoff for bridge sites
hollow_cutoff_min = 2.0  # minimum distance for hollow site consideration
hollow_cutoff_max = 3.8  # can be slightly lowered if needed
hollow_height = 1.8      # vertical cutoff for hollow sites
    
# Specify adsorbate 
adsorbate_symbol = 'O'  

# LJ parameters 
lj_epsilon = 0.570        # Adjust depending on your system
lj_sigma = 1.98           # Adjust depending on your system

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
