#!/usr/bin/env python3
# =============================================================================
# FILE: main.py
# Diatomic molecule analysis with Quantum ESPRESSO
# Main entry point for the application
# =============================================================================

import os
import sys
from ase.io import write
from datetime import datetime

from config_loader import load_config
from calculator import QECalculatorSetup
from vibration import VibrationCalculator
from analysis import MoleculeAnalyzer
from io_utils import save_results, compare_with_reference
from utils import setup_directories

# ============================================================================
# OpenMP Thread Control - Keep only MPI parallelization
# ============================================================================
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["MKL_DYNAMIC"] = "FALSE"
os.environ["OMP_DYNAMIC"] = "FALSE"
os.environ["OMP_MAX_ACTIVE_LEVELS"] = "1"
# ============================================================================

def main():
    """Main execution function."""
    print("="*80)
    print("Diatomic Molecule Analysis with Quantum ESPRESSO")
    print("Full Vibrational Analysis with Multiple Methods")
    print("="*80)
    
    config = load_config('config_qe.yaml')
    
    print("\n" + "="*60)
    print("CALCULATION SETTINGS")
    print("="*60)
    qe_config = config.get('qe', {})
    vib_method = qe_config.get('vibration_method', '1d')
    
    print(f"  Vibration method: {vib_method}")
    print(f"    Options: 1d, xonly, full, 1d+xonly, 1d+full, xonly+full, all")
    
    if '1d' in vib_method:
        print(f"    1D Scan: n_points={qe_config.get('1d_settings', {}).get('n_points', 7)}, delta={qe_config.get('1d_settings', {}).get('delta', 0.005)} Å")
    if 'xonly' in vib_method:
        print(f"    X-Only Hessian: nfree={qe_config.get('xonly_settings', {}).get('nfree', 2)}, delta={qe_config.get('xonly_settings', {}).get('delta', 0.005)} Å")
    if 'full' in vib_method:
        print(f"    Full Hessian: nfree={qe_config.get('full_settings', {}).get('nfree', 2)}, delta={qe_config.get('full_settings', {}).get('delta', 0.005)} Å")
    
    molecules_to_calc = config.get('molecules_to_calculate', {})
    selected_molecules = [m for m, enabled in molecules_to_calc.items() if enabled]
    print(f"\n  Molecules to calculate: {', '.join(selected_molecules) if selected_molecules else 'None'}")
    print("="*60)
    
    # Setup directories
    output_config = config.get('output', {})
    output_dir = output_config.get('output_dir', 'results_qe')
    pseudo_dir = qe_config.get('pseudo_dir', './pseudopotentials/')
    setup_directories(pseudo_dir, output_dir)
    
    analyzer = MoleculeAnalyzer(config)
    
    molecules = config.get('molecules', {})
    results = {}
    
    for mol_name, properties in molecules.items():
        if not molecules_to_calc.get(mol_name, False):
            print(f"\n⏭ Skipping {mol_name} (disabled in config)")
            continue
        
        result, atoms = analyzer.analyze_molecule(mol_name, properties)
        if result:
            results[mol_name] = result
            
            if output_config.get('save_structures', True) and atoms:
                os.makedirs(output_dir, exist_ok=True)
                write(f"{output_dir}/{mol_name}_qe_opt.xyz", atoms)
    
    if results:
        print("\n" + "="*60)
        print("SAVING RESULTS")
        print("="*60)
        save_results(results, config)
        compare_with_reference(results, config)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print(f"  Results saved in: {output_dir}/")
    print("\n  Files generated:")
    print(f"    - {output_dir}/summary.csv: All calculated properties")
    print(f"    - {output_dir}/summary.txt: Human-readable summary")
    print(f"    - {output_dir}/*_qe_opt.xyz: Optimized structures")
    print("    - *_opt.traj: Per-molecule optimization trajectories")
    print("    - *_opt.log: Per-molecule optimization logs")
    if 'full' in vib_method or 'xonly' in vib_method:
        print("    - vib/*.json: Vibration displacement files")
        print("    - vib/*.traj: Vibrational mode trajectories")
    print("="*80)

if __name__ == "__main__":
    main()