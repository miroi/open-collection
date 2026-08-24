#!/usr/bin/env python3
"""
Work with the uranium complex structure from the CIF file
"""

import numpy as np
from ase import Atoms
from ase.io import write
from ase.cell import Cell
from pathlib import Path

def create_uranium_complex():
    """Create the uranium complex structure from the CIF data"""
    
    # Cell parameters from the CIF
    cell = Cell.fromcellpar([
        8.8306,   # a
        9.2307,   # b
        10.8926,  # c
        68.412,   # alpha
        67.056,   # beta
        75.297    # gamma
    ])
    
    # All atoms from the structure
    symbols = [
        # Core: Uranium, Iodine, Oxygen, Nitrogen
        'U', 'I', 'O', 'O', 'O', 'O', 'O', 'N',
        # Water molecules
        'H', 'H',
        # Organic ligands
        'O', 'O',
        # Carbon chain 1
        'C', 'H', 'H', 'H',
        # Carbon chain 2
        'C', 'H', 'H',
        # Carbon chain 3
        'C', 'H', 'H',
        # Carbon chain 4
        'C', 'H', 'H', 'H',
        # Carbon chain 5
        'C', 'H', 'H',
        # Carbon chain 6
        'C', 'H', 'H', 'H',
        # Carbon chain 7
        'C', 'H', 'H',
        # Carbon chain 8
        'C', 'H', 'H', 'H'
    ]
    
    # Fractional coordinates from the CIF
    positions = [
        # Core
        [0.5000, 0.5000, 0.0000],  # U
        [0.2356, 0.6403, 0.2048],  # I
        [0.5779, 0.3039, 0.1796],  # O1
        [0.6396, 0.6157, -0.0137], # O2
        [0.2580, 0.7170, 0.0830],  # O5
        [0.3370, 0.5290, 0.2570],  # O6
        [0.1330, 0.7130, 0.3100],  # O7
        [0.2280, 0.6390, 0.2140],  # N1
        # Water molecules
        [0.6580, 0.2940, 0.2090],  # H1O
        [0.5330, 0.2330, 0.2250],  # H2O
        # Organic ligands
        [0.4108, 0.0564, 0.3296],  # O3
        [0.8354, 0.2992, 0.2444],  # O4
        # Carbon chain 1
        [0.2720, 0.1831, 0.5050],  # C1
        [0.1648, 0.1984, 0.5764],  # H1A
        [0.2971, 0.2839, 0.4334],  # H1B
        [0.3588, 0.1411, 0.5486],  # H1C
        # Carbon chain 2
        [0.2649, 0.0722, 0.4404],  # C2
        [0.2473, -0.0316, 0.5117], # H2A
        [0.1696, 0.1094, 0.4054],  # H2B
        # Carbon chain 3
        [0.4146, -0.0496, 0.2597], # C3
        [0.3887, -0.1529, 0.3294], # H3A
        [0.3281, -0.0087, 0.2143], # H3B
        # Carbon chain 4
        [0.5726, -0.0700, 0.1563], # C4
        [0.6558, -0.1251, 0.2024], # H4A
        [0.6044, 0.0330, 0.0931],  # H4B
        [0.5658, -0.1319, 0.1028], # H4C
        # Carbon chain 5
        [0.9854, 0.2460, 0.1560],  # C5
        [1.0703, 0.2213, 0.2020],  # H5A
        [1.0190, 0.3338, 0.0692],  # H5B
        # Carbon chain 6
        [0.9880, 0.1130, 0.1194],  # C6
        [1.1003, 0.0853, 0.0595],  # H6A
        [0.9099, 0.1374, 0.0689],  # H6B
        [0.9569, 0.0243, 0.2043],  # H6C
        # Carbon chain 7
        [0.8280, 0.4280, 0.2880],  # C7
        [0.9097, 0.3968, 0.3378],  # H7A
        [0.8705, 0.5141, 0.2018],  # H7B
        # Carbon chain 8
        [0.7020, 0.4860, 0.3610],  # C8
        [0.7298, 0.5483, 0.4024],  # H8A
        [0.6400, 0.4017, 0.4348],  # H8B
        [0.6335, 0.5529, 0.3031],  # H8C
    ]
    
    # Create Atoms object
    atoms = Atoms(
        symbols=symbols,
        positions=positions,
        cell=cell,
        pbc=True
    )
    
    # Label atoms for reference
    labels = [
        'U1', 'I1', 'O1', 'O2', 'O5', 'O6', 'O7', 'N1',
        'H1O', 'H2O', 'O3', 'O4',
        'C1', 'H1A', 'H1B', 'H1C',
        'C2', 'H2A', 'H2B',
        'C3', 'H3A', 'H3B',
        'C4', 'H4A', 'H4B', 'H4C',
        'C5', 'H5A', 'H5B',
        'C6', 'H6A', 'H6B', 'H6C',
        'C7', 'H7A', 'H7B',
        'C8', 'H8A', 'H8B', 'H8C'
    ]
    atoms.info['labels'] = labels
    
    return atoms

def analyze_structure(atoms):
    """Analyze the structure"""
    print("\n" + "="*60)
    print("Uranium Complex Structure Analysis")
    print("="*60)
    
    symbols = atoms.get_chemical_symbols()
    
    # Count elements
    element_counts = {}
    for s in symbols:
        element_counts[s] = element_counts.get(s, 0) + 1
    
    print(f"\nTotal atoms: {len(atoms)}")
    print(f"\nElement counts:")
    for elem in sorted(element_counts.keys()):
        print(f"  {elem}: {element_counts[elem]}")
    
    # Check cell
    print(f"\nCell parameters:")
    cell = atoms.cell
    print(f"  a = {cell[0][0]:.4f} Å")
    print(f"  b = {cell[1][1]:.4f} Å")
    print(f"  c = {cell[2][2]:.4f} Å")
    print(f"  Volume = {atoms.get_volume():.2f} Å³")
    
    # Find Uranium
    if 'U' in symbols:
        u_idx = symbols.index('U')
        u_pos = atoms.get_scaled_positions()[u_idx]
        print(f"\nUranium position: ({u_pos[0]:.4f}, {u_pos[1]:.4f}, {u_pos[2]:.4f})")
        
        # Find neighbors
        print("\nNearby atoms to Uranium (< 3.0 Å):")
        for i, (s, pos) in enumerate(zip(symbols, atoms.get_scaled_positions())):
            if i != u_idx:
                dist = atoms.get_distance(u_idx, i, mic=True)
                if dist < 3.0:
                    label = atoms.info['labels'][i] if 'labels' in atoms.info else f"{s}{i}"
                    print(f"  {label}: {dist:.3f} Å")
    
    # Check density
    mass = atoms.get_masses().sum() / 6.022e23 * 1000  # grams
    density = mass / (atoms.get_volume() * 1e-24)  # g/cm³
    print(f"\nDensity: {density:.2f} g/cm³")

def main():
    """Main function"""
    print("\n" + "="*60)
    print("Uranium Complex Structure Builder")
    print("="*60)
    
    # Create structure
    atoms = create_uranium_complex()
    
    # Analyze
    analyze_structure(atoms)
    
    # Save files
    write('uranium_complex.xyz', atoms)
    write('uranium_complex.cif', atoms, format='cif')
    print(f"\n✓ Saved to 'uranium_complex.xyz' and 'uranium_complex.cif'")
    
    # Check if MACE can handle it
    print("\n" + "="*60)
    print("Checking MACE Compatibility")
    print("="*60)
    
    model_path = Path.home() / '.cache' / 'mace' / 'mace-osaka26-small.model'
    if model_path.exists():
        try:
            from mace.calculators import MACECalculator
            import warnings
            warnings.filterwarnings('ignore')
            
            # Check which elements are supported
            elements = set(atoms.get_chemical_symbols())
            print(f"\nElements in structure: {sorted(elements)}")
            
            # Load model
            calc = MACECalculator(model_path=str(model_path), device='cpu')
            
            # Get supported elements
            if hasattr(calc, 'atomic_numbers'):
                supported = calc.atomic_numbers
                if hasattr(supported, 'tolist'):
                    supported = supported.tolist()
                
                from ase.data import chemical_symbols
                supported_symbols = [chemical_symbols[int(z)] for z in supported]
                
                unsupported = [e for e in elements if e not in supported_symbols]
                
                if unsupported:
                    print(f"\n⚠ Unsupported elements: {unsupported}")
                    print("  This structure cannot be calculated with this MACE model")
                    print("  Consider using DFT for Uranium-containing systems")
                else:
                    print(f"\n✓ All elements supported!")
                    
                    # Try calculation on small subset
                    print("\nTesting MACE on a small subset (organic part only)...")
                    organic_indices = [i for i, s in enumerate(atoms.get_chemical_symbols()) 
                                      if s not in ['U', 'I']]
                    organic_atoms = atoms[organic_indices]
                    organic_atoms.calc = calc
                    energy = organic_atoms.get_potential_energy()
                    print(f"  Energy: {energy:.6f} eV")
                    
        except Exception as e:
            print(f"Error checking MACE: {e}")
    else:
        print("\nNo MACE model found")
    
    print("\n" + "="*60)
    print("✓ Done!")

if __name__ == "__main__":
    main()
