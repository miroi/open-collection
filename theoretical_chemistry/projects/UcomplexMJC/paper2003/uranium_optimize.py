#!/usr/bin/env python3
"""
MACE Geometry Optimization for Uranium-Containing Structures
Reads structure from CIF/XYZ and performs optimization with MACE
"""

import os
import sys
import numpy as np
import warnings
from pathlib import Path
from datetime import datetime
from ase.io import read, write
from ase.optimize import BFGS, LBFGS, FIRE
from ase.constraints import FixAtoms
from ase.visualize import view
from ase.cell import Cell
from ase.io.trajectory import Trajectory

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

class UraniumMACE:
    """Class for uranium structure optimization with MACE"""
    
    def __init__(self, model_path=None, device='cpu'):
        """Initialize with MACE model"""
        self.model_path = model_path or self.find_model()
        self.device = device
        self.calc = None
        self.atoms = None
        self.initial_energy = None
        self.final_energy = None
        self.trajectory = None
        self.optimizer = None
        
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
    
    def read_structure(self, filename, format=None):
        """Read structure from file"""
        if not Path(filename).exists():
            print(f"{Colors.RED}✗ File not found: {filename}{Colors.NC}")
            return False
        
        try:
            self.atoms = read(filename, format=format)
            print(f"{Colors.GREEN}✓ Structure loaded from {filename}{Colors.NC}")
            print(f"  Atoms: {len(self.atoms)}")
            print(f"  Elements: {set(self.atoms.get_chemical_symbols())}")
            return True
        except Exception as e:
            print(f"{Colors.RED}✗ Failed to read structure: {e}{Colors.NC}")
            return False
    
    def create_structure_from_fragments(self):
        """Create the uranium complex structure from fragments"""
        from ase import Atoms
        from ase.cell import Cell
        
        # This is the full structure we built earlier
        cell = Cell.fromcellpar([
            8.8306, 9.2307, 10.8926, 68.412, 67.056, 75.297
        ])
        
        symbols = [
            'U', 'I', 'O', 'O', 'O', 'O', 'O', 'N',
            'H', 'H', 'O', 'O',
            'C', 'H', 'H', 'H',
            'C', 'H', 'H',
            'C', 'H', 'H',
            'C', 'H', 'H', 'H',
            'C', 'H', 'H',
            'C', 'H', 'H', 'H',
            'C', 'H', 'H',
            'C', 'H', 'H', 'H'
        ]
        
        positions = [
            [0.5000, 0.5000, 0.0000],
            [0.2356, 0.6403, 0.2048],
            [0.5779, 0.3039, 0.1796],
            [0.6396, 0.6157, -0.0137],
            [0.2580, 0.7170, 0.0830],
            [0.3370, 0.5290, 0.2570],
            [0.1330, 0.7130, 0.3100],
            [0.2280, 0.6390, 0.2140],
            [0.6580, 0.2940, 0.2090],
            [0.5330, 0.2330, 0.2250],
            [0.4108, 0.0564, 0.3296],
            [0.8354, 0.2992, 0.2444],
            [0.2720, 0.1831, 0.5050],
            [0.1648, 0.1984, 0.5764],
            [0.2971, 0.2839, 0.4334],
            [0.3588, 0.1411, 0.5486],
            [0.2649, 0.0722, 0.4404],
            [0.2473, -0.0316, 0.5117],
            [0.1696, 0.1094, 0.4054],
            [0.4146, -0.0496, 0.2597],
            [0.3887, -0.1529, 0.3294],
            [0.3281, -0.0087, 0.2143],
            [0.5726, -0.0700, 0.1563],
            [0.6558, -0.1251, 0.2024],
            [0.6044, 0.0330, 0.0931],
            [0.5658, -0.1319, 0.1028],
            [0.9854, 0.2460, 0.1560],
            [1.0703, 0.2213, 0.2020],
            [1.0190, 0.3338, 0.0692],
            [0.9880, 0.1130, 0.1194],
            [1.1003, 0.0853, 0.0595],
            [0.9099, 0.1374, 0.0689],
            [0.9569, 0.0243, 0.2043],
            [0.8280, 0.4280, 0.2880],
            [0.9097, 0.3968, 0.3378],
            [0.8705, 0.5141, 0.2018],
            [0.7020, 0.4860, 0.3610],
            [0.7298, 0.5483, 0.4024],
            [0.6400, 0.4017, 0.4348],
            [0.6335, 0.5529, 0.3031],
        ]
        
        self.atoms = Atoms(symbols=symbols, positions=positions, cell=cell, pbc=True)
        print(f"{Colors.GREEN}✓ Created uranium complex structure{Colors.NC}")
        print(f"  Atoms: {len(self.atoms)}")
        print(f"  Elements: {set(self.atoms.get_chemical_symbols())}")
        return True
    
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
    
    def setup_optimization(self, optimizer='BFGS', fmax=0.05, steps=100, 
                           constrain_uranium=True, fix_com=False):
        """Setup geometry optimization"""
        if self.atoms is None:
            print(f"{Colors.RED}✗ No structure loaded{Colors.NC}")
            return False
        
        if self.calc is None:
            if not self.load_model():
                return False
        
        # Check model support
        self.check_model_support()
        
        # Apply constraints if requested
        constraints = []
        
        if constrain_uranium:
            # Find uranium atoms
            u_indices = [i for i, s in enumerate(self.atoms.get_chemical_symbols()) 
                        if s == 'U']
            if u_indices:
                constraint = FixAtoms(indices=u_indices)
                constraints.append(constraint)
                print(f"{Colors.BLUE}✓ Constraining Uranium atoms (indices: {u_indices}){Colors.NC}")
        
        if fix_com:
            # Fix center of mass
            from ase.constraints import FixCenterOfMass
            constraints.append(FixCenterOfMass())
            print(f"{Colors.BLUE}✓ Fixing center of mass{Colors.NC}")
        
        if constraints:
            self.atoms.set_constraint(constraints)
        
        # Set calculator
        self.atoms.calc = self.calc
        
        # Setup optimizer
        optimizers = {
            'BFGS': BFGS,
            'LBFGS': LBFGS,
            'FIRE': FIRE
        }
        
        opt_class = optimizers.get(optimizer, BFGS)
        self.optimizer = opt_class(self.atoms, trajectory='optimization.traj')
        
        print(f"{Colors.GREEN}✓ Optimization setup complete{Colors.NC}")
        print(f"  Optimizer: {optimizer}")
        print(f"  fmax: {fmax}")
        print(f"  Max steps: {steps}")
        print(f"  Uranium constrained: {constrain_uranium}")
        
        return True
    
    def optimize(self, fmax=0.05, steps=100, save_interval=10):
        """Run geometry optimization"""
        if self.optimizer is None:
            print(f"{Colors.RED}✗ Optimization not set up{Colors.NC}")
            return False
        
        print(f"\n{Colors.CYAN}{'='*60}{Colors.NC}")
        print(f"{Colors.BOLD}Starting Geometry Optimization{Colors.NC}")
        print(f"{Colors.CYAN}{'='*60}{Colors.NC}")
        print(f"\n{'Step':>6} {'Energy (eV)':>15} {'Max Force (eV/Å)':>20} {'Time (s)':>10}")
        print("-"*55)
        
        # Initial energy
        try:
            self.initial_energy = self.atoms.get_potential_energy()
            print(f"{'Init':>6} {self.initial_energy:>15.6f} {'':>20} {'':>10}")
        except:
            pass
        
        # Run optimization
        import time
        start_time = time.time()
        
        try:
            self.optimizer.run(fmax=fmax, steps=steps)
            
            # Final energy
            self.final_energy = self.atoms.get_potential_energy()
            elapsed = time.time() - start_time
            
            print("-"*55)
            print(f"{'Final':>6} {self.final_energy:>15.6f} {'':>20} {elapsed:>10.1f}")
            
            # Energy change
            if self.initial_energy is not None:
                delta_e = self.final_energy - self.initial_energy
                print(f"\n{Colors.GREEN}✓ Optimization complete!{Colors.NC}")
                print(f"  Initial energy: {self.initial_energy:.6f} eV")
                print(f"  Final energy:   {self.final_energy:.6f} eV")
                print(f"  Energy change:  {delta_e:.6f} eV")
                print(f"  Time elapsed:   {elapsed:.1f} seconds")
            
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Optimization failed: {e}{Colors.NC}")
            import traceback
            traceback.print_exc()
            return False
    
    def save_results(self, prefix='optimized'):
        """Save optimization results"""
        if self.atoms is None:
            return
        
        # Save final structure
        write(f'{prefix}.xyz', self.atoms)
        write(f'{prefix}.cif', self.atoms, format='cif')
        write(f'{prefix}.traj', self.atoms)
        
        # Save optimization summary
        with open(f'{prefix}_summary.txt', 'w') as f:
            f.write(f"MACE Geometry Optimization Summary\n")
            f.write(f"{'='*60}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Model: {self.model_path}\n")
            f.write(f"Device: {self.device}\n")
            f.write(f"Atoms: {len(self.atoms)}\n")
            f.write(f"Elements: {set(self.atoms.get_chemical_symbols())}\n\n")
            
            if self.initial_energy is not None:
                f.write(f"Initial energy: {self.initial_energy:.6f} eV\n")
            if self.final_energy is not None:
                f.write(f"Final energy:   {self.final_energy:.6f} eV\n")
                if self.initial_energy is not None:
                    f.write(f"Energy change:  {self.final_energy - self.initial_energy:.6f} eV\n")
        
        print(f"\n{Colors.GREEN}✓ Results saved:{Colors.NC}")
        print(f"  {prefix}.xyz - Final structure (XYZ)")
        print(f"  {prefix}.cif - Final structure (CIF)")
        print(f"  {prefix}.traj - Trajectory file")
        print(f"  {prefix}_summary.txt - Optimization summary")
    
    def run(self, structure_file=None, optimizer='BFGS', fmax=0.05, steps=100,
            constrain_uranium=True, save_results=True):
        """Complete workflow: load/create structure, setup, optimize, save"""
        
        print(f"\n{Colors.GREEN}{'='*60}{Colors.NC}")
        print(f"{Colors.GREEN}{Colors.BOLD}  Uranium Complex MACE Optimization  {Colors.NC}")
        print(f"{Colors.GREEN}{'='*60}{Colors.NC}\n")
        
        # Load model
        if not self.load_model():
            return False
        
        # Load or create structure
        if structure_file and Path(structure_file).exists():
            if not self.read_structure(structure_file):
                return False
        else:
            if not self.create_structure_from_fragments():
                return False
        
        # Setup optimization
        if not self.setup_optimization(optimizer=optimizer, fmax=fmax, 
                                       steps=steps, constrain_uranium=constrain_uranium):
            return False
        
        # Run optimization
        if not self.optimize(fmax=fmax, steps=steps):
            return False
        
        # Save results
        if save_results:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.save_results(prefix=f'optimized_{timestamp}')
        
        return True

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='MACE optimization for uranium structures')
    parser.add_argument('--input', type=str, help='Input structure file (XYZ, CIF, etc.)')
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
                       help='Do not constrain uranium atoms')
    parser.add_argument('--visualize', action='store_true',
                       help='Visualize structure after optimization')
    
    args = parser.parse_args()
    
    # Create optimizer
    optimizer = UraniumMACE(model_path=args.model, device=args.device)
    
    # Run optimization
    success = optimizer.run(
        structure_file=args.input,
        optimizer=args.optimizer,
        fmax=args.fmax,
        steps=args.steps,
        constrain_uranium=not args.no_constrain_uranium,
        save_results=True
    )
    
    if success and args.visualize and optimizer.atoms is not None:
        print(f"\n{Colors.CYAN}Visualizing optimized structure...{Colors.NC}")
        view(optimizer.atoms)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
