#!/usr/bin/env python3
"""
MACE Energy and Force Calculator
Usage: python mace_calc.py [molecule] [model] [--device cpu|cuda]

Examples:
  python mace_calc.py H2O
  python mace_calc.py CH4 ~/.cache/mace/20231210mace128L0_energy_epoch249model
  python mace_calc.py C2H5OH ~/.cache/mace/macempa0mediummodel --device cuda
"""

import sys
import argparse
from mace.calculators import MACECalculator
from ase.build import molecule
from pathlib import Path
import time

def get_available_models():
    """Get list of available models"""
    model_dir = Path.home() / '.cache' / 'mace'
    return list(model_dir.glob('*model'))

def calculate_energy(molecule_name, model_path, device='cpu'):
    """Calculate energy and forces for a molecule"""
    
    # Resolve model path
    model_path = Path(model_path).expanduser()
    
    if not model_path.exists():
        print(f"✗ Model not found: {model_path}")
        return None
    
    try:
        print(f"\n{'='*60}")
        print(f"Molecule: {molecule_name}")
        print(f"Model: {model_path.name}")
        print(f"Device: {device}")
        print(f"{'='*60}\n")
        
        # Setup calculator
        start_time = time.time()
        calc = MACECalculator(model_path=str(model_path), device=device)
        atoms = molecule(molecule_name)
        atoms.calc = calc
        
        # Calculate
        energy = atoms.get_potential_energy()
        forces = atoms.get_forces()
        calc_time = time.time() - start_time
        
        # Results
        print(f"✓ Calculation completed in {calc_time:.3f} seconds")
        print(f"\nEnergy:")
        print(f"  {energy:.8f} eV")
        print(f"  {energy * 96.485:.4f} kJ/mol")
        print(f"  {energy * 23.0605:.4f} kcal/mol")
        
        print(f"\nForces (eV/Å):")
        for i, (atom, force) in enumerate(zip(atoms, forces)):
            symbol = atom.symbol
            print(f"  {symbol}{i}: [{force[0]:.6f}, {force[1]:.6f}, {force[2]:.6f}]")
        
        # Force magnitudes
        print(f"\nForce magnitudes (eV/Å):")
        for i, (atom, force) in enumerate(zip(atoms, forces)):
            magnitude = (force[0]**2 + force[1]**2 + force[2]**2)**0.5
            print(f"  {atom.symbol}{i}: {magnitude:.6f}")
        
        return energy, forces
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Calculate energy with MACE models')
    parser.add_argument('molecule', type=str, nargs='?', default='H2O',
                       help='Molecule name (e.g., H2O, CH4, NH3)')
    parser.add_argument('model', type=str, nargs='?', 
                       default='~/.cache/mace/macempa0mediummodel',
                       help='Path to MACE model')
    parser.add_argument('--device', type=str, default='cpu',
                       choices=['cpu', 'cuda'],
                       help='Device to use (cpu or cuda)')
    parser.add_argument('--list', action='store_true',
                       help='List available models')
    
    args = parser.parse_args()
    
    if args.list:
        models = get_available_models()
        print("\nAvailable models:")
        for model in models:
            size = model.stat().st_size / (1024 * 1024)
            print(f"  {model.name} ({size:.1f} MB)")
        return
    
    calculate_energy(args.molecule, args.model, args.device)

if __name__ == "__main__":
    main()
