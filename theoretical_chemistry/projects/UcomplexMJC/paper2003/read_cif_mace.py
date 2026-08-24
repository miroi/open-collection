#!/usr/bin/env python3
"""
Fixed CIF parser - captures ALL atoms from the CIF file
"""

import re
import numpy as np
from ase import Atoms
from ase.cell import Cell
from ase.io import write
from pathlib import Path

def parse_cif_all_atoms(cif_file):
    """Parse CIF file and capture ALL atoms"""
    with open(cif_file, 'r') as f:
        content = f.read()
    
    # Extract cell parameters
    cell_params = {}
    patterns = {
        '_cell_length_a': r'_cell_length_a\s+([\d.]+)',
        '_cell_length_b': r'_cell_length_b\s+([\d.]+)',
        '_cell_length_c': r'_cell_length_c\s+([\d.]+)',
        '_cell_angle_alpha': r'_cell_angle_alpha\s+([\d.]+)',
        '_cell_angle_beta': r'_cell_angle_beta\s+([\d.]+)',
        '_cell_angle_gamma': r'_cell_angle_gamma\s+([\d.]+)',
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            cell_params[key] = float(match.group(1))
    
    # Create cell
    atoms_cell = Cell.fromcellpar([
        cell_params.get('_cell_length_a', 1.0),
        cell_params.get('_cell_length_b', 1.0),
        cell_params.get('_cell_length_c', 1.0),
        cell_params.get('_cell_angle_alpha', 90.0),
        cell_params.get('_cell_angle_beta', 90.0),
        cell_params.get('_cell_angle_gamma', 90.0)
    ])
    
    # Find the atom_site loop
    loop_pattern = r'loop_\s*\n.*?_atom_site_label.*?\n(.*?)(?=\n\s*loop_|\n\s*_|\n\s*#|\Z)'
    match = re.search(loop_pattern, content, re.DOTALL)
    
    if not match:
        raise ValueError("Could not find atom_site loop")
    
    atom_lines = match.group(1).strip().split('\n')
    
    symbols = []
    positions = []
    labels = []
    occupancies = []
    
    # Valid element symbols (all elements)
    valid_elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 
                      'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 
                      'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 
                      'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 
                      'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 
                      'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 
                      'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 
                      'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 
                      'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 
                      'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
    
    for line in atom_lines:
        line = line.strip()
        if not line or line.startswith('_'):
            continue
        
        parts = line.split()
        
        # Need at least label, symbol, x, y, z
        if len(parts) >= 5:
            label = parts[0]
            symbol = parts[1]
            
            # Check if symbol is a valid element (or starts with valid element)
            # For labels like "I1", "O1", etc.
            element = symbol
            # If symbol is like "O1", extract "O"
            if not symbol in valid_elements and len(symbol) > 0:
                # Check if first 1-2 characters are an element
                for length in [2, 1]:
                    if symbol[:length] in valid_elements:
                        element = symbol[:length]
                        break
            
            if element in valid_elements:
                try:
                    x = float(parts[2]) if len(parts) > 2 else 0
                    y = float(parts[3]) if len(parts) > 3 else 0
                    z = float(parts[4]) if len(parts) > 4 else 0
                    
                    # Check for occupancy
                    occupancy = 1.0
                    if len(parts) > 7:  # occupancy is usually in column 7
                        try:
                            # Extract occupancy from parts[7] (e.g., "0.685(5)")
                            occ_str = parts[7].split('(')[0]
                            occupancy = float(occ_str)
                        except:
                            pass
                    
                    symbols.append(element)
                    positions.append([x, y, z])
                    labels.append(label)
                    occupancies.append(occupancy)
                except ValueError:
                    continue
    
    if not symbols:
        raise ValueError("No atoms found in CIF")
    
    print(f"Found {len(symbols)} atoms total")
    
    # Print summary by element
    element_counts = {}
    for symbol in symbols:
        element_counts[symbol] = element_counts.get(symbol, 0) + 1
    
    print("\nElement counts:")
    for elem, count in sorted(element_counts.items()):
        print(f"  {elem}: {count}")
    
    # Create Atoms object with all atoms
    atoms = Atoms(symbols=symbols, positions=positions, cell=atoms_cell, pbc=True)
    
    # Store additional info in info dict
    atoms.info['labels'] = labels
    atoms.info['occupancies'] = occupancies
    atoms.info['original_cif'] = cif_file
    
    return atoms

def main():
    """Main function"""
    print("\n" + "="*60)
    print("CIF Parser - Capturing ALL Atoms")
    print("="*60 + "\n")
    
    cif_file = 'ja030260r_2.cif'
    
    if not Path(cif_file).exists():
        print(f"Error: File '{cif_file}' not found!")
        return
    
    try:
        atoms = parse_cif_all_atoms(cif_file)
        
        print(f"\n✓ Successfully parsed CIF!")
        print(f"  Total atoms: {len(atoms)}")
        print(f"  Chemical formula: {atoms.get_chemical_formula()}")
        print(f"  Elements: {set(atoms.get_chemical_symbols())}")
        
        # Check for Uranium
        symbols = atoms.get_chemical_symbols()
        if 'U' in symbols:
            u_indices = [i for i, s in enumerate(symbols) if s == 'U']
            print(f"\n✓ Uranium found at positions: {u_indices}")
            u_pos = atoms.get_scaled_positions()[u_indices[0]]
            print(f"  U position (fractional): ({u_pos[0]:.4f}, {u_pos[1]:.4f}, {u_pos[2]:.4f})")
        
        # Check for Iodine
        if 'I' in symbols:
            i_indices = [i for i, s in enumerate(symbols) if s == 'I']
            print(f"✓ Iodine found: {len(i_indices)} atoms")
        
        # Check for Oxygen
        if 'O' in symbols:
            o_indices = [i for i, s in enumerate(symbols) if s == 'O']
            print(f"✓ Oxygen found: {len(o_indices)} atoms")
        
        # Save to XYZ
        write('structure.xyz', atoms)
        print(f"\n✓ Saved to 'structure.xyz' for visualization")
        
        # Also save to CIF format that ASE can read
        from ase.io import write as ase_write
        ase_write('structure_cleaned.cif', atoms, format='cif')
        print(f"✓ Saved to 'structure_cleaned.cif'")
        
        # Now test with MACE
        print(f"\n{'-'*60}")
        print("Testing with MACE (if model available):")
        print("  from mace.calculators import MACECalculator")
        print("  from pathlib import Path")
        print("  model_path = Path.home() / '.cache' / 'mace' / 'mace-osaka26-small.model'")
        print("  calc = MACECalculator(model_path=str(model_path), device='cpu')")
        print("  atoms.calc = calc")
        print("  energy = atoms.get_potential_energy()")
        
        # Actually try the MACE calculation if model exists
        model_path = Path.home() / '.cache' / 'mace' / 'mace-osaka26-small.model'
        if model_path.exists():
            print(f"\n✓ MACE model found! Running test calculation...")
            try:
                from mace.calculators import MACECalculator
                import warnings
                warnings.filterwarnings('ignore')
                
                calc = MACECalculator(model_path=str(model_path), device='cpu')
                atoms.calc = calc
                
                # Make sure atoms are not too close (needs vacuum)
                # For periodic systems, this is fine
                energy = atoms.get_potential_energy()
                print(f"  ✓ Energy: {energy:.6f} eV")
                print(f"  ✓ Energy: {energy * 96.485:.2f} kJ/mol")
                
                # Get forces
                forces = atoms.get_forces()
                print(f"  ✓ Forces calculated for {len(forces)} atoms")
                
            except Exception as e:
                print(f"  ✗ MACE calculation failed: {e}")
                print("  This might be because the model doesn't support Uranium")
                print("  Elements in structure:", set(atoms.get_chemical_symbols()))
                print("  Elements supported by Osaka model: 97 elements including U")
        
    except Exception as e:
        print(f"✗ Error parsing CIF: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
