#!/usr/bin/env python3
"""
Extract and save the structure of UO2I2(OH2)2 from Crawford et al. 2003
This is the uranyl core from Figure 2 without the Et2O solvent molecules
"""

import numpy as np
from ase import Atoms
from ase.io import write
from ase.visualize import view

def create_uo2i2_oh2_2():
    """
    Create the UO2I2(OH2)2 molecule from the paper's structural data
    Based on Figure 2 and Table 1 from Crawford et al., Inorg. Chem. 2003
    """
    
    # Bond lengths from the paper (Figure 2 and text)
    # U=O (uranyl): 1.773(3) Å
    # U-OH2: 2.318(4) Å
    # U-I: 3.0267(6) Å
    # O-H: ~0.95 Å (typical for water)
    
    # We'll build the molecule with U at the origin
    # The molecule has D2h symmetry (approximately)
    
    # 1. Uranium at origin
    u_pos = [0.0, 0.0, 0.0]
    
    # 2. Uranyl oxygens (along z-axis, linear O=U=O)
    # U=O bond length = 1.773 Å
    o_uranyl1 = [0.0, 0.0, 1.773]
    o_uranyl2 = [0.0, 0.0, -1.773]
    
    # 3. Iodides (along x-axis, trans)
    # U-I bond length = 3.0267 Å
    i1 = [3.0267, 0.0, 0.0]
    i2 = [-3.0267, 0.0, 0.0]
    
    # 4. Water oxygens (along y-axis, trans)
    # U-OH2 bond length = 2.318 Å
    o_water1 = [0.0, 2.318, 0.0]
    o_water2 = [0.0, -2.318, 0.0]
    
    # 5. Hydrogens for water molecules (tetrahedral geometry)
    # H-O-H angle ~104.5°, O-H bond length ~0.95 Å
    # For water 1 (at y = 2.318)
    oh_dist = 0.95
    h_angle = 104.5 * np.pi / 180.0  # 104.5 degrees in radians
    
    # Water 1 hydrogens (slightly tilted)
    h1 = [
        oh_dist * np.sin(h_angle/2),
        2.318 + oh_dist * np.cos(h_angle/2),
        0.0
    ]
    h2 = [
        -oh_dist * np.sin(h_angle/2),
        2.318 + oh_dist * np.cos(h_angle/2),
        0.0
    ]
    
    # Water 2 hydrogens (opposite side, trans)
    h3 = [
        oh_dist * np.sin(h_angle/2),
        -2.318 - oh_dist * np.cos(h_angle/2),
        0.0
    ]
    h4 = [
        -oh_dist * np.sin(h_angle/2),
        -2.318 - oh_dist * np.cos(h_angle/2),
        0.0
    ]
    
    # Optional: Add a small tilt to water molecules
    # to break perfect symmetry (matching the slight distortion
    # mentioned in the paper)
    tilt = 0.05  # small tilt in Å
    h1[2] += tilt
    h2[2] -= tilt
    h3[2] -= tilt
    h4[2] += tilt
    
    # Create Atoms object
    symbols = ['U', 'O', 'O', 'I', 'I', 'O', 'O', 'H', 'H', 'H', 'H']
    positions = [
        u_pos,
        o_uranyl1, o_uranyl2,
        i1, i2,
        o_water1, o_water2,
        h1, h2, h3, h4
    ]
    
    # Set labels for reference
    labels = ['U1', 'O1', 'O2', 'I1', 'I2', 'O3', 'O4', 'H1', 'H2', 'H3', 'H4']
    
    atoms = Atoms(symbols=symbols, positions=positions)
    atoms.info['labels'] = labels
    
    return atoms

def print_molecule_info(atoms):
    """Print information about the molecule"""
    print("\n" + "="*70)
    print("UO₂I₂(OH₂)₂ - Structural Parameters")
    print("From: Crawford et al., Inorg. Chem. 2003")
    print("="*70)
    
    symbols = atoms.get_chemical_symbols()
    
    print(f"\n📊 Molecule Information:")
    print(f"  Formula: UO₂I₂(OH₂)₂")
    print(f"  Total atoms: {len(atoms)}")
    print(f"  Elements: {set(symbols)}")
    
    print(f"\n🔬 Element Counts:")
    counts = {'U': 1, 'O': 4, 'I': 2, 'H': 4}
    for elem, count in counts.items():
        print(f"  {elem}: {count}")
    
    print(f"\n📐 Bond Lengths (from paper):")
    print(f"  U=O (uranyl): 1.773(3) Å")
    print(f"  U-OH₂: 2.318(4) Å")
    print(f"  U-I: 3.0267(6) Å")
    print(f"  O-H (water): ~0.95 Å")
    
    print(f"\n📐 Bond Angles (from paper):")
    print(f"  O=U=O: 180° (linear)")
    print(f"  I-U-I: 180° (trans)")
    print(f"  O(water)-U-O(water): 180° (trans)")
    print(f"  O(water)-U-I: 90.27(10)°")
    print(f"  O=U-I: 89.0(1)°")
    print(f"  H-O-H: ~104.5°")
    
    print(f"\n🔑 Key Features:")
    print("  • Linear uranyl unit (O=U=O)")
    print("  • Trans iodide ligands")
    print("  • Trans water ligands")
    print("  • Slightly distorted octahedral coordination")
    print("  • First structurally characterized U(VI)-I bond")

def analyze_coordination(atoms):
    """Analyze the coordination geometry"""
    print("\n" + "="*70)
    print("Coordination Geometry Analysis")
    print("="*70)
    
    symbols = atoms.get_chemical_symbols()
    positions = atoms.get_positions()
    
    # Find uranium
    u_idx = symbols.index('U')
    u_pos = positions[u_idx]
    
    print(f"\n🔹 Uranium at: ({u_pos[0]:.3f}, {u_pos[1]:.3f}, {u_pos[2]:.3f})")
    
    # Find all neighbors
    print(f"\n  Coordination shell (distances from U):")
    for i, (sym, pos) in enumerate(zip(symbols, positions)):
        if i != u_idx:
            dist = np.linalg.norm(np.array(pos) - np.array(u_pos))
            label = atoms.info['labels'][i] if 'labels' in atoms.info else f"{sym}{i}"
            print(f"    {label}: {dist:.3f} Å")
    
    # Identify bonding pattern
    print(f"\n  Bonding pattern:")
    print(f"    U=O (uranyl): 2 bonds at ~1.773 Å")
    print(f"    U-OH₂: 2 bonds at ~2.318 Å")
    print(f"    U-I: 2 bonds at ~3.027 Å")
    print(f"    Total coordination number: 8 (distorted octahedral)")

def save_xyz(atoms, filename='uo2i2_oh2_2'):
    """Save to XYZ format"""
    # Add comment line with formula
    comment = "UO2I2(OH2)2 - Uranyl iodide dihydrate core (Crawford et al. 2003)"
    
    # Save as XYZ
    write(f'{filename}.xyz', atoms, comment=comment)
    print(f"\n✓ Saved to {filename}.xyz")
    
    # Also save as extended XYZ with more info
    with open(f'{filename}_extended.xyz', 'w') as f:
        f.write(f"{len(atoms)}\n")
        f.write(f"{comment}\n")
        for i, (sym, pos) in enumerate(zip(atoms.get_chemical_symbols(), atoms.get_positions())):
            label = atoms.info['labels'][i] if 'labels' in atoms.info else sym
            f.write(f"{sym:2s} {pos[0]:12.6f} {pos[1]:12.6f} {pos[2]:12.6f}  # {label}\n")
    
    print(f"✓ Saved to {filename}_extended.xyz (with labels)")

def visualize(atoms):
    """Visualize the molecule"""
    try:
        from ase.visualize import view
        view(atoms)
    except:
        print("\n⚠ Could not visualize. Make sure you have ase.visualize installed.")

def compare_with_cif():
    """Compare with the CIF data we extracted earlier"""
    print("\n" + "="*70)
    print("Comparison with CIF Data")
    print("="*70)
    
    # From the CIF file (compound 1 and 2 mixed)
    cif_data = {
        'U=O': 1.758,     # From compound 1
        'U-OH2': 2.321,   # From compound 1
        'U-I': 2.939,     # From compound 1 (mixed)
    }
    
    # From the paper (compound 2, pure)
    paper_data = {
        'U=O': 1.773,
        'U-OH2': 2.318,
        'U-I': 3.0267,
    }
    
    print(f"\n{'Bond':<15} {'CIF (Mixed)':<15} {'Paper (Pure 2)':<15} {'Difference':<15}")
    print("-"*60)
    for bond in cif_data.keys():
        cif_val = cif_data[bond]
        paper_val = paper_data[bond]
        diff = paper_val - cif_val
        print(f"{bond:<15} {cif_val:<15.3f} {paper_val:<15.3f} {diff:+.3f} Å")
    
    print("\nNote: The CIF data contains a mixture of compounds 1 and 2")
    print("The paper's Figure 2 shows the pure compound 2 structure")

def main():
    """Main function"""
    print("\n" + "="*70)
    print("UO₂I₂(OH₂)₂ Structure from Crawford et al. 2003")
    print("="*70)
    
    # Create the molecule
    atoms = create_uo2i2_oh2_2()
    
    # Print information
    print_molecule_info(atoms)
    analyze_coordination(atoms)
    compare_with_cif()
    
    # Save files
    save_xyz(atoms, 'uo2i2_oh2_2')
    
    # Optional: Visualize
    print("\n" + "="*70)
    print("Visualization")
    print("="*70)
    visualize(atoms)
    
    print("\n" + "="*70)
    print("✓ Done!")
    print("\nFiles created:")
    print("  • uo2i2_oh2_2.xyz - Standard XYZ format")
    print("  • uo2i2_oh2_2_extended.xyz - XYZ with atom labels")
    print("\nTo view the structure:")
    print("  from ase.io import read")
    print("  from ase.visualize import view")
    print("  atoms = read('uo2i2_oh2_2.xyz')")
    print("  view(atoms)")

if __name__ == "__main__":
    main()
