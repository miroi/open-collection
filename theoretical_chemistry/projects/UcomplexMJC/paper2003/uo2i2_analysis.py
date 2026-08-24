#!/usr/bin/env python3
"""
Extract and analyze the structure of UO2I2(OH2)2·4Et2O from Crawford et al. 2003
Paper: Synthesis and Structure of UO2I2(OH2)2·4Et2O
DOI: 10.1021/ic034267v (or similar)
"""

import numpy as np
from ase import Atoms
from ase.cell import Cell
from ase.io import write
from ase.visualize import view
from ase.data import chemical_symbols, covalent_radii

class UO2I2Structure:
    """Class representing the UO2I2(OH2)2·4Et2O structure from the paper"""
    
    def __init__(self):
        """Initialize with structural parameters from the paper"""
        # Cell parameters from the paper (triclinic, P-1)
        self.cell = Cell.fromcellpar([
            8.8306,   # a (Å)
            9.2307,   # b (Å)
            10.8926,  # c (Å)
            68.412,   # alpha (degrees)
            67.056,   # beta (degrees)
            75.297    # gamma (degrees)
        ])
        
        # Space group: P-1 (No. 2)
        self.space_group = 'P-1'
        self.z = 2  # molecules per unit cell
        
        # Key bond lengths from Figure 2 and text
        self.bond_lengths = {
            'U=O (uranyl)': 1.773,      # Å
            'U-OH2': 2.318,             # Å
            'U-I': 3.0267,              # Å
            'O-H (water)': 0.95,        # Å (typical)
        }
        
        # Key bond angles from Figure 2
        self.bond_angles = {
            'O=U=O': 180.0,             # degrees (linear)
            'I-U-I': 180.0,             # degrees (trans)
            'O(water)-U-O(water)': 180.0, # degrees (trans)
            'O(water)-U-I': 90.27,       # degrees
            'O=U-I': 89.0,              # degrees
        }
        
        # Build the molecule (fractional coordinates)
        self.build_molecule()
        
    def build_molecule(self):
        """Build the UO2I2(OH2)2 molecule from the structural data"""
        
        # The U atom at the center of symmetry (inversion center)
        # In the P-1 space group, U is at a special position (0,0,0) in fractional coords
        # For this structure, U is at (0.5, 0.5, 0) in the cif, but we'll center it
        
        # Start with U at origin
        u_pos = np.array([0.0, 0.0, 0.0])
        
        # The molecule is centrosymmetric, so atoms come in pairs
        # We'll build one half and then mirror it
        
        # Half of the molecule (fractional coordinates relative to U)
        # Using the bond lengths and angles from the paper
        
        # 1. Uranyl oxygens (O=U=O linear, along z-axis)
        o_uranyl_pos = np.array([0.0, 0.0, self.bond_lengths['U=O (uranyl)']])
        
        # 2. Water oxygens (equatorial plane, trans)
        # O(water)-U-O(water) = 180°, so they are opposite
        # O(water)-U-I = 90.27°, so they are slightly off the I-U-I axis
        o_water_pos = np.array([self.bond_lengths['U-OH2'], 0.0, 0.0])
        
        # 3. Iodides (trans, along x-axis)
        i_pos = np.array([self.bond_lengths['U-I'], 0.0, 0.0])
        
        # 4. Hydrogens on water (approximate positions)
        # Water geometry: H-O-H ~104.5°, O-H ~0.95 Å
        h_angle = 104.5 * np.pi / 180.0
        h_distance = 0.95  # Å
        h1_pos = o_water_pos + np.array([
            h_distance * np.sin(h_angle/2),
            h_distance * np.cos(h_angle/2),
            0.0
        ])
        h2_pos = o_water_pos + np.array([
            h_distance * np.sin(h_angle/2),
            -h_distance * np.cos(h_angle/2),
            0.0
        ])
        
        # 5. Create the full molecule (centrosymmetric)
        # Uranium
        symbols = ['U']
        positions = [u_pos]
        
        # Add uranyl oxygens (both sides)
        symbols.extend(['O', 'O'])
        positions.extend([o_uranyl_pos, -o_uranyl_pos])
        
        # Add water oxygens (both sides)
        symbols.extend(['O', 'O'])
        positions.extend([o_water_pos, -o_water_pos])
        
        # Add iodides (both sides)
        symbols.extend(['I', 'I'])
        positions.extend([i_pos, -i_pos])
        
        # Add hydrogens (both sides, 2 each water)
        symbols.extend(['H', 'H', 'H', 'H'])
        positions.extend([h1_pos, h2_pos, -h1_pos, -h2_pos])
        
        # 6. Convert to fractional coordinates using the cell
        # We'll place the molecule at a special position in the cell
        # For P-1 with Z=2, molecules are at (0,0,0) and (0.5,0.5,0)
        # We'll put the first molecule at (0,0,0) and the second at (0.5,0.5,0)
        
        all_symbols = []
        all_positions = []
        
        # First molecule (at 0,0,0)
        for sym, pos in zip(symbols, positions):
            all_symbols.append(sym)
            all_positions.append(pos)
        
        # Second molecule (at 0.5, 0.5, 0)
        translation = np.array([0.5, 0.5, 0.0])
        for sym, pos in zip(symbols, positions):
            all_symbols.append(sym)
            all_positions.append(pos + translation)
        
        # Convert to fractional coordinates
        self.atoms = Atoms(
            symbols=all_symbols,
            positions=all_positions,
            cell=self.cell,
            pbc=True
        )
        
        # Scale to fractional coordinates
        frac_pos = self.atoms.get_scaled_positions()
        self.atoms.set_scaled_positions(frac_pos)
        
    def print_structure_info(self):
        """Print all structural information from the paper"""
        print("\n" + "="*70)
        print("UO₂I₂(OH₂)₂·4Et₂O - Structural Parameters")
        print("From: Crawford et al., Inorg. Chem. 2003")
        print("="*70)
        
        print("\n📐 Cell Parameters:")
        print(f"  Crystal system: Triclinic")
        print(f"  Space group: {self.space_group}")
        print(f"  Z: {self.z}")
        print(f"  a = {self.cell[0][0]:.4f} Å")
        print(f"  b = {self.cell[1][1]:.4f} Å")
        print(f"  c = {self.cell[2][2]:.4f} Å")
        print(f"  α = 68.412°")
        print(f"  β = 67.056°")
        print(f"  γ = 75.297°")
        print(f"  Volume = {self.atoms.get_volume():.2f} Å³")
        
        print("\n🔬 Bond Lengths (Å):")
        for label, value in self.bond_lengths.items():
            print(f"  {label}: {value:.4f}")
        
        print("\n📐 Bond Angles (degrees):")
        for label, value in self.bond_angles.items():
            print(f"  {label}: {value:.2f}")
        
        print("\n🧪 Molecular Formula:")
        print("  UO₂I₂(OH₂)₂·4Et₂O")
        print("  U: 1, O: 8 (2 uranyl + 2 water + 4 ether), I: 2, C: 8, H: 22")
        
        print("\n📊 Element Counts in Asymmetric Unit:")
        counts = {'U': 1, 'O': 8, 'I': 2, 'C': 8, 'H': 22}
        for elem, count in counts.items():
            print(f"  {elem}: {count}")
        
        print("\n🔑 Key Features:")
        print("  • Linear O=U=O unit (180°)")
        print("  • Trans iodides (I-U-I = 180°)")
        print("  • Trans water ligands (OH2-U-OH2 = 180°)")
        print("  • Slightly distorted D₂h structure")
        print(f"  • U-I bond length: 3.0267(6) Å (first structurally characterized U(VI)-I bond)")
        print("  • Thermally unstable: decomposes above -28°C")
        
        print("\n📝 References:")
        print("  Crawford, M.-J.; Ellern, A.; Nöth, H.; Suter, M.")
        print("  Inorg. Chem. 2003, 42, 4, 1332-1334")
        print("  DOI: 10.1021/ic034267v")
    
    def analyze_coordination(self):
        """Analyze the coordination around uranium"""
        print("\n" + "="*70)
        print("Uranium Coordination Analysis")
        print("="*70)
        
        # Find uranium positions
        symbols = self.atoms.get_chemical_symbols()
        u_indices = [i for i, s in enumerate(symbols) if s == 'U']
        
        for idx, u_idx in enumerate(u_indices):
            print(f"\n🔹 Uranium {idx+1} at position {u_idx}:")
            pos = self.atoms.get_scaled_positions()[u_idx]
            print(f"  Fractional: ({pos[0]:.4f}, {pos[1]:.4f}, {pos[2]:.4f})")
            
            # Find all neighbors
            neighbors = []
            for i, (sym, pos2) in enumerate(zip(symbols, self.atoms.get_scaled_positions())):
                if i != u_idx:
                    dist = self.atoms.get_distance(u_idx, i, mic=True)
                    if dist < 4.0:
                        neighbors.append((i, sym, dist))
            
            # Sort by distance
            neighbors.sort(key=lambda x: x[2])
            
            print(f"\n  Coordination shell (< 4.0 Å):")
            for i, sym, dist in neighbors[:12]:
                if sym == 'O':
                    if dist < 2.0:
                        type_str = "Uranyl O"
                    else:
                        type_str = "Water O"
                elif sym == 'I':
                    type_str = "Iodide"
                else:
                    type_str = "Other"
                print(f"    {sym}{i}: {dist:.3f} Å ({type_str})")
            
            print(f"\n  Coordination number (bonds < 3.5 Å): {len([n for n in neighbors if n[2] < 3.5])}")
            print("  Coordination geometry: Distorted octahedral")
    
    def save_structure(self, filename='uo2i2_structure'):
        """Save the structure to various formats"""
        write(f'{filename}.xyz', self.atoms)
        write(f'{filename}.cif', self.atoms, format='cif')
        print(f"\n✓ Saved to {filename}.xyz and {filename}.cif")
    
    def visualize(self):
        """Visualize the structure"""
        view(self.atoms)

def compare_with_compound_1():
    """Compare compounds 1 and 2 from the paper"""
    print("\n" + "="*70)
    print("Comparison of Compounds 1 and 2")
    print("="*70)
    
    # Compound 1: Mixed UO2I1.38(NO3)0.62
    compound1 = {
        'formula': 'UO₂I₁.₃₈(NO₃)₀.₆₂',
        'U=O': 1.758,
        'U-OH2': 2.321,
        'U-I': 2.939,
        'U-ONO3': 2.65-2.68,
        'U-I (avg)': 2.939,
        'stability': 'Decomposes at 0°C',
        'iodine:nitrate': '69:31'
    }
    
    # Compound 2: UO2I2(OH2)2·4Et2O
    compound2 = {
        'formula': 'UO₂I₂(OH₂)₂·4Et₂O',
        'U=O': 1.773,
        'U-OH2': 2.318,
        'U-I': 3.0267,
        'U-I (avg)': 3.0267,
        'stability': 'Decomposes at -28°C',
        'iodine:nitrate': '100:0'
    }
    
    print(f"\n{'Property':<20} {'Compound 1':<25} {'Compound 2':<25}")
    print("-"*70)
    for key in ['formula', 'U=O', 'U-OH2', 'U-I', 'U-I (avg)', 'stability', 'iodine:nitrate']:
        print(f"{key:<20} {str(compound1.get(key, '')):<25} {str(compound2.get(key, '')):<25}")

def main():
    """Main function"""
    print("\n" + "="*70)
    print("UO₂I₂(OH₂)₂·4Et₂O Structure Analysis")
    print("Crawford et al., Inorg. Chem. 2003")
    print("="*70)
    
    # Create structure
    structure = UO2I2Structure()
    
    # Print all information
    structure.print_structure_info()
    structure.analyze_coordination()
    compare_with_compound_1()
    
    # Save files
    structure.save_structure('uo2i2_complex')
    
    print("\n" + "="*70)
    print("✓ Done!")
    print("\nTo visualize the structure:")
    print("  from ase.io import read")
    print("  from ase.visualize import view")
    print("  atoms = read('uo2i2_complex.xyz')")
    print("  view(atoms)")

if __name__ == "__main__":
    main()
