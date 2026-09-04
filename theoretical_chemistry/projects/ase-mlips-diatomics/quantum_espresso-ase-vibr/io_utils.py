# =============================================================================
# FILE: io_utils.py
# Input/Output utilities for saving results and comparing with reference.
# =============================================================================

import os
import numpy as np
import pandas as pd

def save_results(results, config):
    """Save results to files with all methods compared."""
    output_config = config.get('output', {})
    output_dir = output_config.get('output_dir', 'results_qe')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save detailed summary as CSV
    csv_file = os.path.join(output_dir, 'summary.csv')
    with open(csv_file, 'w') as f:
        f.write("Molecule,Symbols,d_eq_calc(Å),d_eq_exp(Å),d_eq_error(%),"
                "freq_1d(cm⁻¹),time_1d(s),"
                "freq_xonly(cm⁻¹),time_xonly(s),"
                "freq_full(cm⁻¹),time_full(s),"
                "freq_final(cm⁻¹),freq_exp(cm⁻¹),freq_error(%),"
                "Method,Reference,Timestamp\n")
        
        for mol_name, mol_result in results.items():
            if mol_result:
                symbols = ''.join(mol_result.get('symbols', []))
                d_eq_exp = mol_result.get('exp_equilibrium_distance', 'N/A')
                d_eq_error = f"{mol_result.get('d_eq_error_percent', 0):.2f}" if mol_result.get('d_eq_error_percent') is not None else 'N/A'
                freq_exp = mol_result.get('exp_vibrational_frequency', 'N/A')
                freq_error = f"{mol_result.get('freq_error_percent', 0):.2f}" if mol_result.get('freq_error_percent') is not None else 'N/A'
                
                f.write(f"{mol_name},{symbols},"
                       f"{mol_result['equilibrium_distance']:.4f},{d_eq_exp},{d_eq_error},"
                       f"{mol_result.get('freq_1d', 0):.2f},{mol_result.get('time_1d', 0):.1f},"
                       f"{mol_result.get('freq_xonly', 0):.2f},{mol_result.get('time_xonly', 0):.1f},"
                       f"{mol_result.get('freq_full', 0):.2f},{mol_result.get('time_full', 0):.1f},"
                       f"{mol_result.get('vibrational_frequency_cm1', 0):.2f},{freq_exp},{freq_error},"
                       f"{mol_result.get('vibration_method', 'N/A')},"
                       f"{mol_result.get('reference_source', 'N/A')},"
                       f"{mol_result.get('timestamp', 'N/A')}\n")
    
    print(f"✓ Results saved to {csv_file}")
    
    # Create human-readable summary
    txt_file = os.path.join(output_dir, 'summary.txt')
    with open(txt_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("DIATOMIC MOLECULE ANALYSIS SUMMARY\n")
        f.write("="*80 + "\n\n")
        
        for mol_name, mol_result in results.items():
            if mol_result:
                f.write(f"Molecule: {mol_name}\n")
                f.write(f"  Symbols: {mol_result.get('symbols', [])}\n")
                f.write(f"  Equilibrium bond length: {mol_result['equilibrium_distance']:.4f} Å\n")
                
                exp_d_eq = mol_result.get('exp_equilibrium_distance')
                if exp_d_eq is not None:
                    error = mol_result.get('d_eq_error_percent', 0)
                    if error is not None:
                        f.write(f"  Experimental bond length: {exp_d_eq:.4f} Å (error: {error:.2f}%)\n")
                    else:
                        f.write(f"  Experimental bond length: {exp_d_eq:.4f} Å\n")
                
                freq = mol_result.get('vibrational_frequency_cm1', 0)
                if freq > 0:
                    f.write(f"  Vibrational frequency: {freq:.2f} cm⁻¹\n")
                else:
                    f.write(f"  Vibrational frequency: Not calculated\n")
                
                exp_freq = mol_result.get('exp_vibrational_frequency')
                if exp_freq is not None and freq > 0:
                    error = mol_result.get('freq_error_percent', 0)
                    if error is not None:
                        f.write(f"  Experimental frequency: {exp_freq:.2f} cm⁻¹ (error: {error:.2f}%)\n")
                    else:
                        f.write(f"  Experimental frequency: {exp_freq:.2f} cm⁻¹\n")
                
                f.write(f"  Method used: {mol_result.get('vibration_method', 'N/A')}\n")
                
                # Show all method results if available
                if (mol_result.get('freq_1d', 0) > 0 or 
                    mol_result.get('freq_xonly', 0) > 0 or 
                    mol_result.get('freq_full', 0) > 0):
                    f.write(f"  All methods:\n")
                    if mol_result.get('freq_1d', 0) > 0:
                        f.write(f"    1D Scan: {mol_result['freq_1d']:.2f} cm⁻¹ (time: {mol_result.get('time_1d', 0):.1f}s)\n")
                    if mol_result.get('freq_xonly', 0) > 0:
                        f.write(f"    X-Only Hessian: {mol_result['freq_xonly']:.2f} cm⁻¹ (time: {mol_result.get('time_xonly', 0):.1f}s)\n")
                    if mol_result.get('freq_full', 0) > 0:
                        f.write(f"    Full Hessian: {mol_result['freq_full']:.2f} cm⁻¹ (time: {mol_result.get('time_full', 0):.1f}s)\n")
                
                f.write(f"  Reference source: {mol_result.get('reference_source', 'N/A')}\n")
                f.write(f"  Timestamp: {mol_result.get('timestamp', 'N/A')}\n")
                f.write("-"*40 + "\n")
    
    print(f"✓ Human-readable summary saved to {txt_file}")

def compare_with_reference(results, config):
    """Compare with reference values from NIST."""
    print("\n" + "="*80)
    print("COMPARISON WITH EXPERIMENTAL VALUES")
    print("="*80)
    print(f"{'Molecule':<10} {'Property':<15} {'Calculated':<15} {'Experimental':<15} {'Error (%)':<12} {'Status'}")
    print("-"*80)
    
    for mol_name, res in results.items():
        if res is None:
            continue
        
        freq = res.get('vibrational_frequency_cm1', 0)
        exp_d_eq = res.get('exp_equilibrium_distance')
        exp_freq = res.get('exp_vibrational_frequency')
        
        if exp_d_eq is not None:
            dist_err = abs(res['equilibrium_distance'] - exp_d_eq) / exp_d_eq * 100
            d_eq_marker = "✓" if dist_err < 2 else "⚠" if dist_err < 5 else "✗"
            print(f"{mol_name:<10} {'d_eq (Å)':<15} {res['equilibrium_distance']:<15.4f} {exp_d_eq:<15.4f} {dist_err:<12.2f} {d_eq_marker}")
        
        if exp_freq is not None and freq > 0:
            freq_err = abs(freq - exp_freq) / exp_freq * 100
            freq_marker = "✓" if freq_err < 10 else "⚠" if freq_err < 20 else "✗"
            method = res.get('vibration_method', 'N/A')
            print(f"{mol_name:<10} {'freq (cm⁻¹)':<15} {freq:<15.2f} {exp_freq:<15.2f} {freq_err:<12.2f} {freq_marker} ({method})")
        elif exp_freq is not None:
            print(f"{mol_name:<10} {'freq (cm⁻¹)':<15} {'Not calc.':<15} {exp_freq:<15.2f} {'N/A':<12} {'✗'}")
        
        print("-"*80)