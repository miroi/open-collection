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
    
    # Get enabled molecules
    molecules_to_calc = config.get('molecules_to_calculate', {})
    enabled_molecules = [m for m, enabled in molecules_to_calc.items() if enabled]
    
    # Check which enabled molecules have only_geometry_optimization enabled
    molecules = config.get('molecules', {})
    geometry_only_molecules = []
    full_analysis_molecules = []
    
    for mol_name in enabled_molecules:
        if mol_name in molecules:
            if molecules[mol_name].get('only_geometry_optimization', False):
                geometry_only_molecules.append(mol_name)
            else:
                full_analysis_molecules.append(mol_name)
    
    if geometry_only_molecules:
        print(f"  🔧 GEOMETRY ONLY MODE: {', '.join(geometry_only_molecules)}")
    if full_analysis_molecules:
        print(f"  📊 FULL ANALYSIS MODE: {', '.join(full_analysis_molecules)}")
    
    if not enabled_molecules:
        print("  ⚠ No molecules selected for calculation!")
        print("  Please enable molecules in molecules_to_calculate section")
        return
    
    qe_config = config.get('qe', {})
    vib_method = qe_config.get('vibration_method', '1d')
    
    if full_analysis_molecules:
        print(f"  Vibration method: {vib_method}")
        print(f"    Options: 1d, xonly, full, 1d+xonly, 1d+full, xonly+full, all")
        
        if '1d' in vib_method:
            print(f"    1D Scan: n_points={qe_config.get('1d_settings', {}).get('n_points', 9)}, delta={qe_config.get('1d_settings', {}).get('delta', 0.001)} Å")
        if 'xonly' in vib_method:
            print(f"    X-Only Hessian: nfree={qe_config.get('xonly_settings', {}).get('nfree', 2)}, delta={qe_config.get('xonly_settings', {}).get('delta', 0.001)} Å")
        if 'full' in vib_method:
            print(f"    Full Hessian: nfree={qe_config.get('full_settings', {}).get('nfree', 2)}, delta={qe_config.get('full_settings', {}).get('delta', 0.001)} Å")
    
    # Check if any enabled molecule has eq_distance pre-computed
    for mol_name in enabled_molecules:
        if mol_name in molecules and 'eq_distance' in molecules[mol_name]:
            print(f"  Note: {mol_name} has pre-computed eq_distance={molecules[mol_name]['eq_distance']:.4f} Å (will skip geometry optimization)")
    
    print(f"\n  Molecules to calculate: {', '.join(enabled_molecules) if enabled_molecules else 'None'}")
    print("="*60)
    
    # Setup directories
    output_config = config.get('output', {})
    output_dir = output_config.get('output_dir', 'results_qe')
    pseudo_dir = qe_config.get('pseudo_dir', './pseudopotentials/')
    setup_directories(pseudo_dir, output_dir)
    
    analyzer = MoleculeAnalyzer(config)
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
        
        # Check if any calculated molecule had full analysis (frequencies calculated)
        any_full_analysis = any(not r.get('only_geometry', True) for r in results.values() if r)
        if any_full_analysis:
            compare_with_reference(results, config)
        else:
            print("\n  ⏭ Skipping comparison with reference (all calculated molecules in geometry-only mode)")
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print(f"  Results saved in: {output_dir}/")
    print("\n  Files generated:")
    print(f"    - {output_dir}/summary.csv: All calculated properties")
    print(f"    - {output_dir}/summary.txt: Human-readable summary")
    print(f"    - {output_dir}/*_qe_opt.xyz: Optimized structures")
    if any(not r.get('only_geometry', True) for r in results.values() if r):
        print("    - *_opt.traj: Per-molecule optimization trajectories")
        print("    - *_opt.log: Per-molecule optimization logs")
    if any(not r.get('only_geometry', True) for r in results.values() if r) and ('full' in vib_method or 'xonly' in vib_method):
        print("    - vib/*.json: Vibration displacement files")
        print("    - vib/*.traj: Vibrational mode trajectories")
    print("="*80)

if __name__ == "__main__":
    main()
