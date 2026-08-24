#!/usr/bin/env python3
"""
Final working CIF parser for uranium complex - captures ALL atoms
"""

import re
import numpy as np
from ase import Atoms
from ase.cell import Cell
from ase.io import write
from pathlib import Path

def parse_cif_final(cif_file):
    """Parse CIF and capture ALL atoms - the final working version"""
    
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
    
    # Split into lines and find atom data
    lines = content.split('\n')
    
    symbols = []
    positions = []
    labels = []
    occupancies = []
    
    # We know from the debug output that atom data starts at line 213
    # and continues until line 252
    # Let's search for the pattern of atom lines
    atom_pattern = re.compile(r'^([A-Z][a-z]?\d*)\s+([A-Z][a-z]?)\s+([\d.]+(?:\([\d]+\))?)\s+([\d.]+(?:\([\d]+\))?)\s+([\d.]+(?:\([\d]+\))?)\s+([\d.]+(?:\([\d]+\))?)\s+(\w+)\s+([\d.]+(?:\([\d]+\))?)')
    
    in_atom_section = False
    atom_lines_found = 0
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if this is an atom data line
        # Atom lines in this CIF start with: U1, I1, O1, O2, O5, O6, O7, N1, H1O, H2O, O3, O4, C1, H1A, etc.
        parts = line.split()
        
        # Check if first part is a label like U1, I1, O1, etc.
        if len(parts) >= 5:
            label = parts[0]
            symbol = parts[1] if len(parts) > 1 else ""
            
            # Valid elements in this CIF
            valid_elements = ['U', 'I', 'O', 'N', 'C', 'H']
            
            # Check if this is an atom line
            if symbol in valid_elements:
                try:
                    # Extract coordinates (handle values with parentheses like 0.5000(2))
                    x_str = parts[2].split('(')[0]
                    y_str = parts[3].split('(')[0]
                    z_str = parts[4].split('(')[0]
                    
                    x = float(x_str)
                    y = float(y_str)
                    z = float(z_str)
                    
                    # Check for occupancy (might be in column 7)
                    occupancy = 1.0
                    if len(parts) > 7:
                        try:
                            occ_str = parts[7].split('(')[0]
                            occupancy = float(occ_str)
                        except:
                            pass
                    
                    # Only add if occupancy > 0.01
                    if occupancy > 0.01:
                        symbols.append(symbol)
                        positions.append([x, y, z])
                        labels.append(label)
                        occupancies.append(occupancy)
                        atom_lines_found += 1
                        
                except ValueError:
                    continue
    
    print(f"Found {atom_lines_found} atom lines")
    
    if not symbols:
        raise ValueError("No atoms found in CIF")
    
    # Create Atoms object
    atoms = Atoms(
        symbols=symbols,
        positions=positions,
        cell=atoms_cell,
        pbc=True
    )
    
    # Store additional info
    atoms.info['labels'] = labels
    atoms.info['occupancies'] = occupancies
    
    return atoms

def print_structure_info(atoms):
    """Print detailed structure information"""
    print(f"\n{'='*60}")
    print("Structure Information")
    print("="*60)
    
    symbols = atoms.get_chemical_symbols()
    
    print(f"\n  Total atoms: {len(atoms)}")
    
    # Count elements
    element_counts = {}
    for s in symbols:
        element_counts[s] = element_counts.get(s, 0) + 1
    
    print(f"\n  Element counts:")
    expected = {'U': 1, 'I': 2, 'O': 6, 'N': 1, 'C': 8, 'H': 22}
    for elem in sorted(expected.keys()):
        count = element_counts.get(elem, 0)
        exp = expected.get(elem, 0)
        status = "✓" if count == exp else f"✗ (found {count}, expected {exp})"
        print(f"    {elem}: {count:2d} {status}")
    
    # Check total
    total_expected = sum(expected.values())
    if len(atoms) == total_expected:
        print(f"\n  ✓ All {total_expected} atoms captured correctly!")
    else:
        print(f"\n  ⚠ Expected {total_expected} atoms, found {len(atoms)}")
        print(f"    Missing: {total_expected - len(atoms)} atoms")
    
    # Show first few atoms
    print(f"\n  First 10 atoms:")
    for i in range(min(10, len(atoms))):
        label = atoms.info['labels'][i] if 'labels' in atoms.info else f"{symbols[i]}{i}"
        pos = atoms.get_scaled_positions()[i]
        print(f"    {i:2d} {label}: ({pos[0]:.4f}, {pos[1]:.4f}, {pos[2]:.4f})")

def main():
    print("\n" + "="*60)
    print("Final Working Uranium Complex CIF Parser")
    print("="*60 + "\n")
    
    cif_file = 'ja030260r_2.cif'
    
    if not Path(cif_file).exists():
        print(f"Error: File '{cif_file}' not found!")
        return
    
    try:
        # Parse CIF
        atoms = parse_cif_final(cif_file)
        
        print(f"✓ Successfully parsed CIF!")
        print_structure_info(atoms)
        
        # Save files
        write('structure_final.xyz', atoms)
        write('structure_final.cif', atoms, format='cif')
        print(f"\n✓ Saved to 'structure_final.xyz' and 'structure_final.cif'")
        
        # Test with MACE if model exists
        model_path = Path.home() / '.cache' / 'mace' / 'mace-osaka26-small.model'
        if model_path.exists() and len(atoms) > 0:
            print(f"\n{'='*60}")
            print("Testing with MACE")
            print("="*60)
            
            try:
                from mace.calculators import MACECalculator
                import warnings
                warnings.filterwarnings('ignore')
                
                print(f"  Loading model: {model_path.name}")
                calc = MACECalculator(model_path=str(model_path), device='cpu')
                
                # Check which elements are supported
                elements = set(atoms.get_chemical_symbols())
                print(f"  Elements in structure: {elements}")
                
                # Try calculation
                atoms.calc = calc
                print("\n  Running MACE calculation...")
                energy = atoms.get_potential_energy()
                print(f"  ✓ Energy: {energy:.6f} eV")
                print(f"  ✓ Energy: {energy * 96.485:.2f} kJ/mol")
                
                # Get forces
                forces = atoms.get_forces()
                print(f"  ✓ Forces calculated for {len(forces)} atoms")
                
            except Exception as e:
                print(f"  ✗ MACE calculation failed: {e}")
                print("  This is expected if Uranium is not supported")
        
        print(f"\n{'='*60}")
        print("✓ Done!")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
