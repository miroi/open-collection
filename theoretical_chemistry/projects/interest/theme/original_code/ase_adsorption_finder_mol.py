#!/usr/bin/env python
import os
import numpy as np
from ase import Atoms
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
from ase.constraints import FixAtoms, FixInternals
from ase.io import write

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
# Surface parameters
top_layer_cutoff = 0.5 #increase for buckled layers
top_height = 2.5
bridge_height = 2.0 
hollow_height = 1.8
bridge_cutoff = 2.9
hollow_cutoff_min = 2.0
hollow_cutoff_max = 4.0

# Molecular structure
molecule = Atoms(
    symbols=['O']*1 + ['H']*2,
    positions=[ # positions in Angstrom
        [9.309999943, 13.081400394, 10.709600449],
        [10.224800110, 12.905000448, 10.477399826], 
        [9.215599895, 13.076800108, 11.664999723]
    ],
    cell=[ # values in Angstrom
        [20.0, 0.00, 0.00],
        [0.00, 20.0, 0.00],
        [0.00, 0.00, 20.0]
    ],
    pbc=[True, True, True]
)
molecule_name = 'H2O'
anchor_atom_index = 2  # 1-based index

# Molecular constraints (1-BASED indexing, list all bond lengths and bond angles to constrain)
molecule_bonds = [(1, 2), (1, 3)]
molecule_angles = [(2, 1, 3)]

# Rotation sampling
rotation_angles = [0, 60, 120, 180, 240, 300]

# LJ parameters
lj_epsilon = 0.01
lj_sigma = 2.5

# Optimization parameters
max_optimization_steps = 50
force_tolerance = 0.02

# ==============================================
# 3. Molecular Functions
# ==============================================
def create_molecule(anchor_position, rotation_angle=0):
    """Create molecule with specified anchor position and rotation"""
    mol = molecule.copy()
    
    # Center on anchor atom
    current_anchor_pos = mol[anchor_atom_index - 1].position.copy()
    shift = anchor_position - current_anchor_pos
    mol.translate(shift)
    
    # Rotate around surface normal (z-axis) through anchor atom
    if rotation_angle != 0:
        mol.rotate(rotation_angle, 'z', center=anchor_position)
    
    return mol

def place_molecule_on_surface(slab, site_position, site_height, rotation_angle):
    """Place molecule on surface site with specified rotation"""
    # Find the top layer height
    positions = slab.get_positions()
    top_layer_z = np.max(positions[:, 2])
    
    # Calculate 3D position for anchor atom: site_position + top_layer_z + height
    anchor_position_3d = np.array([site_position[0], site_position[1], top_layer_z + site_height])
    
    # Create molecule
    mol = create_molecule(anchor_position_3d, rotation_angle)
    
    # Combine slab and molecule
    system = slab.copy()
    system.extend(mol)
    
    return system

def apply_constraints(system, slab_length):
    """Apply constraints: freeze slab and fix specified molecular geometry"""
    # Freeze slab atoms
    freeze_indices = list(range(slab_length))
    
    # Get molecule indices
    mol_indices = list(range(slab_length, len(system)))
    
    # Create constraints list
    constraints = [FixAtoms(indices=freeze_indices)]
    
    # Only add molecular constraints if we have a molecule
    if len(mol_indices) > 0 and (molecule_bonds or molecule_angles):
        bonds = []
        angles = []
        
        # Add specified bonds
        for bond in molecule_bonds:
            i, j = bond
            # Adjust indices for the combined system 
            i_adj = (i - 1) + slab_length
            j_adj = (j - 1) + slab_length
            
            # Use ASE's built-in get_distance function with MIC
            dist = system.get_distance(i_adj, j_adj, mic=True)
            bonds.append([dist, [i_adj, j_adj]])
            print(f"  Constraining bond: {system[i_adj].symbol}{i_adj+1}-{system[j_adj].symbol}{j_adj+1} = {dist:.3f} Å")
        
        # Add specified angles
        for angle in molecule_angles:
            i, j, k = angle
            # Adjust indices for the combined system
            i_adj = (i - 1) + slab_length
            j_adj = (j - 1) + slab_length
            k_adj = (k - 1) + slab_length
            
            # Use ASE's built-in get_angle function with MIC
            angle_deg = system.get_angle(i_adj, j_adj, k_adj, mic=True)
            angles.append([angle_deg, [i_adj, j_adj, k_adj]])
            print(f"  Constraining angle: {system[i_adj].symbol}{i_adj+1}-{system[j_adj].symbol}{j_adj+1}-{system[k_adj].symbol}{k_adj+1} = {angle_deg:.1f}°")
        
        # Create FixInternals constraint
        fix_internals = FixInternals(
            bonds=bonds if bonds else None,
            angles_deg=angles if angles else None
        )
        constraints.append(fix_internals)
        print(f"  Applied constraints: {len(bonds)} bonds, {len(angles)} angles")
    
    system.set_constraint(constraints)
    
    return system

# ==============================================
# 4. Define all unique adsorption sites
# ==============================================
def get_adsorption_sites(slab):
    sites = {}
    
    # Identify top layer
    positions = slab.get_positions()
    z_coords = positions[:, 2]
    top_layer_z = np.max(z_coords)
    top_layer_threshold = top_layer_z - top_layer_cutoff
    
    top_layer_indices = [i for i, z in enumerate(z_coords) if z >= top_layer_threshold]
    print(f"\nFound {len(top_layer_indices)} top layer atoms: {[i+1 for i in top_layer_indices]}")
    print(f" Top layer height: {top_layer_z:.3f} Å")
    
    # 1. Top sites
    for i in top_layer_indices:
        atom = slab[i]
        sites[f'top_{i+1}'] = {'position': atom.position[:2], 'height': top_height, 'atom_indices': [i]}
    
    # 2. Bridge sites
    print(f"\nFound bridge sites:")
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
                pos_j = pos_i + v_ij
            
                sites[f'bridge_{i+1}-{j+1}'] = {
                    'position': [(pos_i[0] + pos_j[0])/2, (pos_i[1] + pos_j[1])/2],
                    'height': bridge_height,
                    'atom_indices': [i, j]
                }
    
        if neighbors_found:
            print(f" Atom {i+1}: bridges with {neighbors_found}")
    
    # 3. Hollow sites
    print(f"\nFound hollow sites:")
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
                
                    if triangle_area > 0.1:
                        print(f" Hollow: {idx_i+1}-{idx_j+1}-{idx_k+1} "
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
# 5. Screening with calculator
# ==============================================
def screen_adsorption_sites(slab, sites):
    energies = {}
    convergence_info = {}  # Track convergence status
    
    # Find top layer height for reference
    positions = slab.get_positions()
    top_layer_z = np.max(positions[:, 2])
    
    for name, site in sites.items():
        for rotation_angle in rotation_angles:
            config_name = f"{name}_rot{rotation_angle:03d}"
            
            # Place molecule on surface
            system = place_molecule_on_surface(slab, site['position'], site['height'], rotation_angle)
                     
            # Apply constraints: freeze slab and fix molecular geometry
            system = apply_constraints(system, len(slab))
            
            # Calculator setup - using simple LJ for now
            system.calc = LennardJones(epsilon=lj_epsilon, sigma=lj_sigma, rc=10.0)
            
            # Use ASE's built-in optimization with step limit
            relax = BFGS(system, 
                        trajectory=f'traj_files/{molecule_name}_{config_name}.traj')
            
            print(f"  Starting BFGS optimization (max {max_optimization_steps} steps)...")
            
            # ASE automatically handles step limits and convergence
            relax.run(fmax=force_tolerance, steps=max_optimization_steps)
            
            # Get energy and convergence info using ASE's built-in methods
            energy = system.get_potential_energy()
            n_steps = relax.get_number_of_steps()
            energies[config_name] = energy
            
            # Check convergence using ASE's built-in method
            if relax.converged():
                convergence_info[config_name] = f"Converged ({n_steps} steps)"
            else:
                convergence_info[config_name] = f"Not converged ({n_steps} steps)"
            
            # Export structures using ASE's writers
            write(f'vasp_outputs/{molecule_name}_{config_name}.vasp', system, format='vasp', direct=True)
            
            with open(f'ase_outputs/{config_name}.ase', 'w') as f:
                f.write("from ase import Atoms\n\n")
                f.write("atoms = Atoms(\n")
                
                symbols = [atom.symbol for atom in system]
                f.write(f"    symbols={symbols},\n")
                
                f.write("    positions=[\n")
                for pos in system.get_positions():
                    f.write(f"        [{pos[0]:.10f}, {pos[1]:.10f}, {pos[2]:.10f}],\n")
                f.write("    ],\n")
                f.write("    cell=[\n")
                for vec in system.get_cell():
                    f.write(f"        [{vec[0]:.10f}, {vec[1]:.10f}, {vec[2]:.10f}],\n")
                f.write("    ],\n")
                f.write(f"    pbc={system.pbc.tolist()}\n")
                f.write(")\n")
    
    return energies, convergence_info

# ==============================================
# 6. Run and Save Results
# ==============================================
if __name__ == "__main__":
    print(f"Testing {molecule_name} adsorption")
    print(f"\nAnchor atom: {molecule.get_chemical_symbols()[anchor_atom_index - 1]} (1-based index {anchor_atom_index})")
    print(f"Rotation angles: {rotation_angles}")
    print(f"Constrained bonds: {molecule_bonds}")
    print(f"Constrained angles: {molecule_angles}")
    print(f"\nLJ Parameters: ε = {lj_epsilon}, σ = {lj_sigma}")
    print(f"BFGS settings: fmax={force_tolerance}, max_steps={max_optimization_steps}")
    
    sites = get_adsorption_sites(atoms)
    total_configs = len(sites) * len(rotation_angles)
    print(f"\nTesting {total_configs} configurations ({len(sites)} sites × {len(rotation_angles)} rotations)...\n")
    
    energies, convergence_info = screen_adsorption_sites(atoms, sites)
    
    # Count converged vs non-converged using ASE's status
    converged_count = sum(1 for status in convergence_info.values() if "Converged" in status)
    not_converged_count = total_configs - converged_count
    
    # Find best configuration (only among converged ones)
    converged_energies = {k: v for k, v in energies.items() if "Converged" in convergence_info[k]}
    
    if converged_energies:
        min_energy = min(converged_energies.values())
        best_configs = [config for config, energy in converged_energies.items() if energy == min_energy]
    else:
        min_energy = None
        best_configs = []
    
    # Write summary file
    with open('adsorption_summary.txt', 'w') as f:
        f.write(f"Molecule: {molecule_name}\n")
        f.write(f"Anchor atom: {molecule.get_chemical_symbols()[anchor_atom_index - 1]} (1-based index {anchor_atom_index})\n")
        f.write(f"Rotation angles tested: {rotation_angles}\n")
        f.write(f"Constraint: Fixed Bond Lengths and Angles (geometry preserved)\n")
        f.write(f"Constrained bonds: {molecule_bonds}\n")
        f.write(f"Constrained angles: {molecule_angles}\n")
        f.write(f"LJ Parameters: ε = {lj_epsilon}, σ = {lj_sigma}\n")
        f.write(f"BFGS settings: fmax={force_tolerance}, max_steps={max_optimization_steps}\n")
        f.write(f"Total configurations tested: {total_configs}\n")
        f.write(f"Successfully converged: {converged_count}\n")
        f.write(f"Not converged: {not_converged_count}\n")
        
        if best_configs:
            f.write(f"Most stable configuration(s): {', '.join(best_configs)}\n")
            f.write(f"Minimum energy: {min_energy:.6f} eV\n\n")
        else:
            f.write(f"Most stable configuration(s): NONE (no converged calculations)\n")
            f.write(f"Minimum energy: N/A\n\n")
        
        f.write("Configuration\t\t\tEnergy (eV)\tConvergence\n")
        f.write("="*70 + "\n")
        for name, energy in sorted(energies.items(), key=lambda x: x[1]):
            f.write(f"{name:40s}\t{energy:.6f}\t{convergence_info[name]}")
            if name in best_configs and min_energy is not None and energy == min_energy:
                f.write(" <--- Most stable")
            f.write("\n")
    
    # Console output
    print(f"\nOptimization Summary:")
    print(f"Successfully converged: {converged_count}/{total_configs}")
    print(f"Not converged: {not_converged_count}/{total_configs}")
    
    if best_configs:
        print(f"\nMost stable configuration(s): {', '.join(best_configs)}")
        print(f"Minimum energy: {min_energy:.6f} eV")
    else:
        print(f"\nWARNING: No configurations converged successfully!")
    
    # List non-converged configurations
    if not_converged_count > 0:
        print(f"\nNon-converged configurations:")
        for name, status in convergence_info.items():
            if "Not converged" in status:
                print(f"  {name}: {status}")
    
    print(f"\nComplete energy table:")
    print("Configuration\t\t\tEnergy (eV)\tConvergence")
    print("="*70)
    for name, energy in sorted(energies.items(), key=lambda x: x[1]):
        print(f"{name:40s}\t{energy:.6f}\t{convergence_info[name]}", end="")
        if name in best_configs and min_energy is not None and energy == min_energy:
            print(" <--- Most stable", end="")
        print()