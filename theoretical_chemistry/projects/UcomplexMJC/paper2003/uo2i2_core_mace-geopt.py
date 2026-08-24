#!/usr/bin/env python3
"""
UO2I2(OH2)2 Structure from Crawford et al. 2003 with MACE Optimization
Extracts structure, performs MACE geometry optimization, and compares results
"""

import os
import sys
import numpy as np
import warnings
from pathlib import Path
from datetime import datetime
from ase import Atoms
from ase.io import write, read
from ase.optimize import BFGS, LBFGS, FIRE
from ase.constraints import FixAtoms, FixBondLengths
from ase.visualize import view
from ase.data import covalent_radii

# Suppress warnings
warnings.filterwarnings('ignore')
os.environ['TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD'] = '1'
os.environ['PYTHONWARNINGS'] = 'ignore'

# Color codes for terminal output
class Colors:
    GREEN = '\033[0;32m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;35m'
    NC = '\033[0m'
    BOLD = '\033[1m'

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
    atoms.info['reference'] = 'Crawford et al., Inorg. Chem. 2003'
    
    return atoms

class UO2I2Optimizer:
    """Class for optimizing UO2I2(OH2)2 with MACE"""
    
    def __init__(self, model_path=None, device='cpu'):
        """Initialize with MACE model"""
        self.model_path = model_path or self.find_model()
        self.device = device
        self.calc = None
        self.atoms = None
        self.initial_atoms = None
        self.optimized_atoms = None
        self.bond_lengths_paper = {}
        self.bond_lengths_initial = {}
        self.bond_lengths_optimized = {}
        self.bond_angles_paper = {}
        self.bond_angles_initial = {}
        self.bond_angles_optimized = {}
        
    def find_model(self):
        """Find MACE model in common locations"""
        common_paths = [
            Path.home() / '.cache' / 'mace' / 'mace-osaka26-small.model',
            Path.home() / '.cache' / 'mace' / 'macempa0mediummodel',
            Path.home() / '.cache' / 'mace' / 'mace-mp-0b3-medium.model',
            Path.home() / '.cache' / 'mace' / '20231210mace128L0_energy_epoch249model',
        ]
        
        for path in common_paths:
            if path.exists():
                print(f"{Colors.GREEN}✓ Found model: {path.name}{Colors.NC}")
                return str(path)
        
        # Try to find any .model file
        model_dir = Path.home() / '.cache' / 'mace'
        if model_dir.exists():
            models = list(model_dir.glob('*.model'))
            if models:
                print(f"{Colors.GREEN}✓ Found model: {models[0].name}{Colors.NC}")
                return str(models[0])
        
        print(f"{Colors.YELLOW}⚠ No MACE model found. Please specify path.{Colors.NC}")
        return None
    
    def load_model(self):
        """Load the MACE calculator"""
        if not self.model_path or not Path(self.model_path).exists():
            print(f"{Colors.RED}✗ Model not found: {self.model_path}{Colors.NC}")
            return False
        
        try:
            from mace.calculators import MACECalculator
            self.calc = MACECalculator(model_path=self.model_path, device=self.device)
            print(f"{Colors.GREEN}✓ MACE model loaded successfully{Colors.NC}")
            return True
        except Exception as e:
            print(f"{Colors.RED}✗ Failed to load MACE: {e}{Colors.NC}")
            return False
    
    def check_model_support(self):
        """Check if the model supports all elements in the structure"""
        if self.atoms is None or self.calc is None:
            return False
        
        elements = set(self.atoms.get_chemical_symbols())
        
        # Get supported elements from model
        if hasattr(self.calc, 'atomic_numbers'):
            supported = self.calc.atomic_numbers
            if hasattr(supported, 'tolist'):
                supported = supported.tolist()
            
            from ase.data import chemical_symbols
            supported_symbols = [chemical_symbols[int(z)] for z in supported]
            
            unsupported = [e for e in elements if e not in supported_symbols]
            
            if unsupported:
                print(f"{Colors.YELLOW}⚠ Unsupported elements: {unsupported}{Colors.NC}")
                print(f"  MACE may not work correctly for these elements")
                return False
            else:
                print(f"{Colors.GREEN}✓ All elements supported by model{Colors.NC}")
                return True
        
        return False
    
    def setup_atoms(self, atoms=None):
        """Setup atoms for optimization"""
        if atoms is None:
            self.atoms = create_uo2i2_oh2_2()
        else:
            self.atoms = atoms.copy()
        
        self.initial_atoms = self.atoms.copy()
        print(f"\n{Colors.BLUE}Structure information:{Colors.NC}")
        print(f"  Atoms: {len(self.atoms)}")
        print(f"  Elements: {set(self.atoms.get_chemical_symbols())}")
        
        return True
    
    def setup_optimization(self, constrain_uranium=True):
        """Setup geometry optimization with constraints"""
        if self.atoms is None:
            print(f"{Colors.RED}✗ No structure loaded{Colors.NC}")
            return False
        
        if self.calc is None:
            if not self.load_model():
                return False
        
        # Check model support
        self.check_model_support()
        
        # Set calculator
        self.atoms.calc = self.calc
        
        # Apply constraints
        constraints = []
        
        if constrain_uranium:
            # Find uranium atom
            u_indices = [i for i, s in enumerate(self.atoms.get_chemical_symbols()) 
                        if s == 'U']
            if u_indices:
                constraint = FixAtoms(indices=u_indices)
                constraints.append(constraint)
                print(f"{Colors.BLUE}✓ Constraining Uranium atom (index: {u_indices[0]}){Colors.NC}")
        
        if constraints:
            self.atoms.set_constraint(constraints)
        
        print(f"{Colors.GREEN}✓ Optimization setup complete{Colors.NC}")
        return True
    
    def calculate_bond_lengths(self, atoms, label):
        """Calculate key bond lengths"""
        symbols = atoms.get_chemical_symbols()
        pos = atoms.get_positions()
        u_idx = symbols.index('U')
        
        bonds = {}
        
        # Find U=O (uranyl) - should be O atoms at ~1.77 Å
        # U-I bonds
        # U-O (water) bonds
        
        for i, (sym, p) in enumerate(zip(symbols, pos)):
            if i != u_idx:
                dist = np.linalg.norm(np.array(p) - np.array(pos[u_idx]))
                if sym == 'O' and dist < 2.5:
                    # Check if it's uranyl or water oxygen
                    # Uranyl oxygens are along z-axis
                    if abs(p[2]) > 1.0:  # Along z-axis
                        bonds[f'U=O_{i}'] = dist
                    else:
                        bonds[f'U-OH2_{i}'] = dist
                elif sym == 'I':
                    bonds[f'U-I_{i}'] = dist
                elif sym == 'H':
                    # Find the O-H bond for water
                    for j, (sym2, p2) in enumerate(zip(symbols, pos)):
                        if sym2 == 'O' and j != u_idx:
                            oh_dist = np.linalg.norm(np.array(p) - np.array(p2))
                            if oh_dist < 1.5:
                                bonds[f'O-H_{j}_{i}'] = oh_dist
        
        # Calculate averages
        avg_bonds = {}
        uo_bonds = [v for k, v in bonds.items() if 'U=O' in k]
        if uo_bonds:
            avg_bonds['U=O (avg)'] = np.mean(uo_bonds)
        u_oh2_bonds = [v for k, v in bonds.items() if 'U-OH2' in k]
        if u_oh2_bonds:
            avg_bonds['U-OH2 (avg)'] = np.mean(u_oh2_bonds)
        u_i_bonds = [v for k, v in bonds.items() if 'U-I' in k]
        if u_i_bonds:
            avg_bonds['U-I (avg)'] = np.mean(u_i_bonds)
        oh_bonds = [v for k, v in bonds.items() if 'O-H' in k]
        if oh_bonds:
            avg_bonds['O-H (avg)'] = np.mean(oh_bonds)
        
        return avg_bonds
    
    def calculate_bond_angles(self, atoms, label):
        """Calculate key bond angles"""
        symbols = atoms.get_chemical_symbols()
        pos = atoms.get_positions()
        u_idx = symbols.index('U')
        u_pos = pos[u_idx]
        
        angles = {}
        
        # Find uranyl oxygens
        uo_indices = []
        water_o_indices = []
        i_indices = []
        
        for i, (sym, p) in enumerate(zip(symbols, pos)):
            if i != u_idx:
                dist = np.linalg.norm(np.array(p) - np.array(u_pos))
                if sym == 'O':
                    if dist < 2.0:  # Uranyl oxygen
                        uo_indices.append(i)
                    else:  # Water oxygen
                        water_o_indices.append(i)
                elif sym == 'I':
                    i_indices.append(i)
        
        # Calculate angles
        def get_angle(p1, p2, p3):
            v1 = np.array(p1) - np.array(p2)
            v2 = np.array(p3) - np.array(p2)
            dot = np.dot(v1, v2)
            norm = np.linalg.norm(v1) * np.linalg.norm(v2)
            return np.arccos(dot/norm) * 180 / np.pi
        
        # O=U=O angle
        if len(uo_indices) >= 2:
            angle = get_angle(pos[uo_indices[0]], u_pos, pos[uo_indices[1]])
            angles['O=U=O'] = angle
        
        # I-U-I angle
        if len(i_indices) >= 2:
            angle = get_angle(pos[i_indices[0]], u_pos, pos[i_indices[1]])
            angles['I-U-I'] = angle
        
        # O(water)-U-O(water) angle
        if len(water_o_indices) >= 2:
            angle = get_angle(pos[water_o_indices[0]], u_pos, pos[water_o_indices[1]])
            angles['O(water)-U-O(water)'] = angle
        
        # O(water)-U-I angle
        if water_o_indices and i_indices:
            angle = get_angle(pos[water_o_indices[0]], u_pos, pos[i_indices[0]])
            angles['O(water)-U-I'] = angle
        
        # O=U-I angle
        if uo_indices and i_indices:
            angle = get_angle(pos[uo_indices[0]], u_pos, pos[i_indices[0]])
            angles['O=U-I'] = angle
        
        return angles
    
    def print_geometry_comparison(self):
        """Print comparison of paper, initial, and optimized geometries"""
        print(f"\n{Colors.CYAN}{'='*80}{Colors.NC}")
        print(f"{Colors.BOLD}Geometry Comparison: Paper vs Initial vs MACE Optimized{Colors.NC}")
        print(f"{Colors.CYAN}{'='*80}{Colors.NC}")
        
        # Paper values
        paper_bonds = {
            'U=O (avg)': 1.773,
            'U-OH2 (avg)': 2.318,
            'U-I (avg)': 3.0267,
            'O-H (avg)': 0.95,
        }
        
        paper_angles = {
            'O=U=O': 180.0,
            'I-U-I': 180.0,
            'O(water)-U-O(water)': 180.0,
            'O(water)-U-I': 90.27,
            'O=U-I': 89.0,
        }
        
        print(f"\n{Colors.BOLD}Bond Lengths (Å):{Colors.NC}")
        print(f"{'Bond':<20} {'Paper':<12} {'Initial':<12} {'Optimized':<12} {'Difference':<15}")
        print("-"*75)
        
        for bond in paper_bonds.keys():
            paper_val = paper_bonds[bond]
            initial_val = self.bond_lengths_initial.get(bond, 0)
            optimized_val = self.bond_lengths_optimized.get(bond, 0)
            
            if initial_val > 0 and optimized_val > 0:
                diff_paper_opt = optimized_val - paper_val
                diff_init_opt = optimized_val - initial_val
                status = "✓" if abs(diff_paper_opt) < 0.1 else "⚠"
                print(f"{bond:<20} {paper_val:<12.4f} {initial_val:<12.4f} {optimized_val:<12.4f} {diff_paper_opt:+7.4f} Å  {status}")
        
        print(f"\n{Colors.BOLD}Bond Angles (degrees):{Colors.NC}")
        print(f"{'Angle':<25} {'Paper':<12} {'Initial':<12} {'Optimized':<12} {'Difference':<15}")
        print("-"*80)
        
        for angle in paper_angles.keys():
            paper_val = paper_angles[angle]
            initial_val = self.bond_angles_initial.get(angle, 0)
            optimized_val = self.bond_angles_optimized.get(angle, 0)
            
            if initial_val > 0 and optimized_val > 0:
                diff_paper_opt = optimized_val - paper_val
                diff_init_opt = optimized_val - initial_val
                status = "✓" if abs(diff_paper_opt) < 2.0 else "⚠"
                print(f"{angle:<25} {paper_val:<12.2f} {initial_val:<12.2f} {optimized_val:<12.2f} {diff_paper_opt:+7.2f}°  {status}")
        
        # Summary
        print(f"\n{Colors.BOLD}Summary:{Colors.NC}")
        if abs(self.bond_lengths_optimized.get('U=O (avg)', 0) - 1.773) < 0.1:
            print(f"  {Colors.GREEN}✓ U=O bond length matches paper within 0.1 Å{Colors.NC}")
        else:
            print(f"  {Colors.YELLOW}⚠ U=O bond length differs from paper by > 0.1 Å{Colors.NC}")
        
        if abs(self.bond_lengths_optimized.get('U-I (avg)', 0) - 3.0267) < 0.1:
            print(f"  {Colors.GREEN}✓ U-I bond length matches paper within 0.1 Å{Colors.NC}")
        else:
            print(f"  {Colors.YELLOW}⚠ U-I bond length differs from paper by > 0.1 Å{Colors.NC}")
    
    def optimize(self, fmax=0.05, steps=100, optimizer_name='BFGS'):
        """Run geometry optimization"""
        if self.atoms is None:
            print(f"{Colors.RED}✗ No structure loaded{Colors.NC}")
            return False
        
        if self.calc is None:
            if not self.load_model():
                return False
        
        # Calculate initial geometry
        self.bond_lengths_initial = self.calculate_bond_lengths(self.atoms, 'Initial')
        self.bond_angles_initial = self.calculate_bond_angles(self.atoms, 'Initial')
        
        print(f"\n{Colors.CYAN}{'='*80}{Colors.NC}")
        print(f"{Colors.BOLD}Running Geometry Optimization{Colors.NC}")
        print(f"{Colors.CYAN}{'='*80}{Colors.NC}")
        print(f"\n{'Step':>6} {'Energy (eV)':>15} {'Max Force (eV/Å)':>20} {'Time (s)':>10}")
        print("-"*55)
        
        # Setup optimizer
        optimizers = {
            'BFGS': BFGS,
            'LBFGS': LBFGS,
            'FIRE': FIRE
        }
        
        opt_class = optimizers.get(optimizer_name, BFGS)
        optimizer = opt_class(self.atoms, trajectory='optimization_uo2i2.traj')
        
        import time
        start_time = time.time()
        
        # Run optimization
        try:
            # Print initial energy
            initial_energy = self.atoms.get_potential_energy()
            print(f"{'Init':>6} {initial_energy:>15.6f} {'':>20} {'':>10}")
            
            # Run optimization
            optimizer.run(fmax=fmax, steps=steps)
            
            # Final energy
            final_energy = self.atoms.get_potential_energy()
            elapsed = time.time() - start_time
            
            print("-"*55)
            print(f"{'Final':>6} {final_energy:>15.6f} {'':>20} {elapsed:>10.1f}")
            print(f"\n{Colors.GREEN}✓ Optimization complete!{Colors.NC}")
            print(f"  Initial energy: {initial_energy:.6f} eV")
            print(f"  Final energy:   {final_energy:.6f} eV")
            print(f"  Energy change:  {final_energy - initial_energy:.6f} eV")
            print(f"  Time elapsed:   {elapsed:.1f} seconds")
            
            # Calculate optimized geometry
            self.optimized_atoms = self.atoms.copy()
            self.bond_lengths_optimized = self.calculate_bond_lengths(self.optimized_atoms, 'Optimized')
            self.bond_angles_optimized = self.calculate_bond_angles(self.optimized_atoms, 'Optimized')
            
            # Print geometry comparison
            self.print_geometry_comparison()
            
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Optimization failed: {e}{Colors.NC}")
            import traceback
            traceback.print_exc()
            return False
    
    def save_results(self, prefix='uo2i2_optimized'):
        """Save optimization results"""
        # Save the paper-based initial structure
        paper_atoms = create_uo2i2_oh2_2()
        write(f'uo2i2_paper_initial.xyz', paper_atoms)
        print(f"✓ Paper-based initial structure: uo2i2_paper_initial.xyz")
        
        # Save the initial structure (before optimization)
        if self.initial_atoms:
            write(f'uo2i2_initial.xyz', self.initial_atoms)
            print(f"✓ Initial structure (before optimization): uo2i2_initial.xyz")
        
        # Save the optimized structure
        if self.optimized_atoms:
            write(f'{prefix}.xyz', self.optimized_atoms)
            write(f'{prefix}.cif', self.optimized_atoms, format='cif')
            print(f"✓ Optimized structure: {prefix}.xyz and {prefix}.cif")
        
        # Save comparison summary
        with open(f'{prefix}_comparison.txt', 'w') as f:
            f.write("UO2I2(OH2)2 Geometry Comparison\n")
            f.write("="*70 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Model: {self.model_path}\n")
            f.write(f"Device: {self.device}\n\n")
            
            f.write("Bond Lengths (Å):\n")
            f.write(f"{'Bond':<20} {'Paper':<12} {'Initial':<12} {'Optimized':<12}\n")
            f.write("-"*60 + "\n")
            
            for bond in ['U=O (avg)', 'U-OH2 (avg)', 'U-I (avg)', 'O-H (avg)']:
                paper = 1.773 if bond == 'U=O (avg)' else 2.318 if bond == 'U-OH2 (avg)' else 3.0267 if bond == 'U-I (avg)' else 0.95
                initial = self.bond_lengths_initial.get(bond, 0)
                optimized = self.bond_lengths_optimized.get(bond, 0)
                f.write(f"{bond:<20} {paper:<12.4f} {initial:<12.4f} {optimized:<12.4f}\n")
            
            f.write("\nBond Angles (degrees):\n")
            f.write(f"{'Angle':<25} {'Paper':<12} {'Initial':<12} {'Optimized':<12}\n")
            f.write("-"*65 + "\n")
            
            for angle in ['O=U=O', 'I-U-I', 'O(water)-U-O(water)', 'O(water)-U-I', 'O=U-I']:
                paper = 180.0 if angle in ['O=U=O', 'I-U-I', 'O(water)-U-O(water)'] else 90.27 if angle == 'O(water)-U-I' else 89.0
                initial = self.bond_angles_initial.get(angle, 0)
                optimized = self.bond_angles_optimized.get(angle, 0)
                f.write(f"{angle:<25} {paper:<12.2f} {initial:<12.2f} {optimized:<12.2f}\n")
    
    def run(self, optimizer='BFGS', fmax=0.05, steps=100, constrain_uranium=True):
        """Complete workflow"""
        print(f"\n{Colors.GREEN}{'='*80}{Colors.NC}")
        print(f"{Colors.GREEN}{Colors.BOLD}  UO₂I₂(OH₂)₂ MACE Optimization  {Colors.NC}")
        print(f"{Colors.GREEN}{'='*80}{Colors.NC}")
        
        # Create structure
        if not self.setup_atoms():
            return False
        
        # Load model
        if not self.load_model():
            return False
        
        # Setup optimization
        if not self.setup_optimization(constrain_uranium=constrain_uranium):
            return False
        
        # Run optimization
        if not self.optimize(optimizer_name=optimizer, fmax=fmax, steps=steps):
            return False
        
        # Save results
        self.save_results()
        
        return True

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='UO2I2(OH2)2 MACE optimization')
    parser.add_argument('--model', type=str, help='Path to MACE model file')
    parser.add_argument('--device', type=str, default='cpu', choices=['cpu', 'cuda'],
                       help='Device to use (cpu or cuda)')
    parser.add_argument('--optimizer', type=str, default='BFGS',
                       choices=['BFGS', 'LBFGS', 'FIRE'],
                       help='Optimizer to use')
    parser.add_argument('--fmax', type=float, default=0.05,
                       help='Maximum force convergence criteria (eV/Å)')
    parser.add_argument('--steps', type=int, default=100,
                       help='Maximum optimization steps')
    parser.add_argument('--no-constrain-uranium', action='store_true',
                       help='Do not constrain uranium atom')
    parser.add_argument('--visualize', action='store_true',
                       help='Visualize structure after optimization')
    
    args = parser.parse_args()
    
    # Create optimizer
    optimizer = UO2I2Optimizer(model_path=args.model, device=args.device)
    
    # Run optimization
    success = optimizer.run(
        optimizer=args.optimizer,
        fmax=args.fmax,
        steps=args.steps,
        constrain_uranium=not args.no_constrain_uranium
    )
    
    if success and args.visualize and optimizer.optimized_atoms is not None:
        print(f"\n{Colors.CYAN}Visualizing optimized structure...{Colors.NC}")
        view(optimizer.optimized_atoms)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
