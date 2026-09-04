# =============================================================================
# FILE: analysis.py
# Molecule analysis for diatomic systems.
# =============================================================================

import time
from datetime import datetime
from ase.optimize import BFGS
from calculator import QECalculatorSetup
from vibration import VibrationCalculator
from utils import create_diatomic, parse_vibration_methods

class MoleculeAnalyzer:
    """Analyze diatomic molecules with Quantum ESPRESSO."""
    
    def __init__(self, config):
        """Initialize with configuration."""
        self.config = config
        self.qe_config = config.get('qe', {})
        self.calc_setup = QECalculatorSetup(config)
        self.vibration_calc = VibrationCalculator(
            self.calc_setup.vib_calc, 
            self.qe_config
        )
    
    def optimize_geometry(self, atoms, mol_name, fmax=0.001, steps=100):
        """Optimize geometry using BFGS with per-molecule naming."""
        traj_file = f'{mol_name}_opt.traj'
        log_file = f'{mol_name}_opt.log'
        
        atoms.set_calculator(self.calc_setup.calc)
        opt = BFGS(atoms, trajectory=traj_file, logfile=log_file)
        opt.run(fmax=fmax, steps=steps)
        return atoms
    
    def get_equilibrium_distance(self, symbols, mol_name, initial_distance=1.2, 
                                 fmax=0.001, steps=100):
        """Find equilibrium bond distance."""
        unique_symbols = list(set(symbols))
        all_exist = True
        
        for sym in unique_symbols:
            if not self.calc_setup.check_pseudopotential_exists(sym):
                all_exist = False
        
        if not all_exist:
            print(f"  ✗ Missing pseudopotentials for {symbols}")
            return initial_distance, None
        
        atoms = create_diatomic(symbols, initial_distance)
        self.calc_setup.update_for_molecule(unique_symbols)
        atoms.set_calculator(self.calc_setup.calc)
        
        opt_atoms = self.optimize_geometry(atoms, mol_name, fmax, steps)
        return opt_atoms.get_distance(0, 1), opt_atoms
    
    def analyze_molecule(self, molecule_name, properties):
        """Complete analysis of a diatomic molecule."""
        print(f"\n{'='*60}")
        print(f"Analyzing {molecule_name}")
        print(f"{'='*60}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        symbols = properties['symbols']
        initial_dist = properties['initial_distance']
        unique_symbols = list(set(symbols))
        
        # Check pseudopotentials exist
        for sym in unique_symbols:
            if not self.calc_setup.check_pseudopotential_exists(sym):
                print(f"  ✗ Pseudopotential for {sym} not found")
                return None, None
        
        # Update calculator for this molecule
        self.calc_setup.update_for_molecule(unique_symbols)
        
        # Get equilibrium distance
        fmax = self.config.get('general', {}).get('fmax', 0.001)
        max_steps = self.config.get('general', {}).get('max_steps', 100)
        
        print(f"  Finding equilibrium geometry...")
        print(f"  Log files: {molecule_name}_opt.log, {molecule_name}_opt.traj")
        eq_dist, opt_atoms = self.get_equilibrium_distance(
            symbols, molecule_name, initial_dist, fmax, max_steps
        )
        
        if opt_atoms is None:
            print(f"  ✗ Optimization failed for {molecule_name}")
            return None, None
        
        print(f"  ✓ Equilibrium bond distance: {eq_dist:.4f} Å")
        
        # Parse the vibration method
        vib_method = self.qe_config.get('vibration_method', '1d')
        methods_to_run = parse_vibration_methods(vib_method)
        
        # Dictionary to store results
        freq_results = {}
        method_names = {
            '1d': '1D Scan',
            'xonly': 'X-Only Hessian',
            'full': 'Full 3D Hessian'
        }
        
        # Run each method
        if '1d' in methods_to_run:
            print(f"\n  Method 1: 1D Scan (quadratic fit along bond)")
            delta = self.qe_config.get('1d_settings', {}).get('delta', 0.005)
            n_points = self.qe_config.get('1d_settings', {}).get('n_points', 7)
            
            start_time = time.time()
            freq_1d = self.vibration_calc.calculate_1d_scan(
                opt_atoms, molecule_name, delta, n_points
            )
            elapsed_1d = time.time() - start_time
            
            if freq_1d > 0:
                print(f"    ✓ 1D Scan: {freq_1d:.2f} cm⁻¹ (took {elapsed_1d:.1f}s, {n_points} SCF)")
            freq_results['1d'] = {'freq': freq_1d, 'time': elapsed_1d, 'scf': n_points}
        
        if 'xonly' in methods_to_run:
            print(f"\n  Method 2: X-Only Hessian (manual, only along bond)")
            delta = self.qe_config.get('xonly_settings', {}).get('delta', 0.005)
            nfree = self.qe_config.get('xonly_settings', {}).get('nfree', 2)
            scf_count = 2 * nfree
            
            start_time = time.time()
            freq_xonly = self.vibration_calc.calculate_xonly_hessian(
                opt_atoms, molecule_name, delta, nfree
            )
            elapsed_xonly = time.time() - start_time
            
            if freq_xonly > 0:
                print(f"    ✓ X-Only Hessian: {freq_xonly:.2f} cm⁻¹ (took {elapsed_xonly:.1f}s, {scf_count} SCF)")
            freq_results['xonly'] = {'freq': freq_xonly, 'time': elapsed_xonly, 'scf': scf_count}
        
        if 'full' in methods_to_run:
            print(f"\n  Method 3: Full 3D Hessian (all directions)")
            delta = self.qe_config.get('full_settings', {}).get('delta', 0.005)
            nfree = self.qe_config.get('full_settings', {}).get('nfree', 2)
            scf_count = 2 * nfree * 3 * 2
            
            start_time = time.time()
            freq_full = self.vibration_calc.calculate_full_hessian(
                opt_atoms, molecule_name, delta, nfree
            )
            elapsed_full = time.time() - start_time
            
            if freq_full > 0:
                print(f"    ✓ Full Hessian: {freq_full:.2f} cm⁻¹ (took {elapsed_full:.1f}s, {scf_count} SCF)")
            freq_results['full'] = {'freq': freq_full, 'time': elapsed_full, 'scf': scf_count}
        
        # Print comparison table if multiple methods were run
        if len(freq_results) > 1:
            print(f"\n  {'='*55}")
            print(f"  VIBRATION METHOD COMPARISON")
            print(f"  {'='*55}")
            print(f"  {'Method':<18} {'Frequency (cm⁻¹)':<20} {'Time (s)':<12} {'SCF count':<12}")
            print(f"  {'-'*55}")
            
            for method, data in freq_results.items():
                freq = data['freq']
                freq_str = f"{freq:.2f}" if freq > 0 else "Failed"
                print(f"  {method_names[method]:<18} {freq_str:<20} {data['time']:<12.1f} {data['scf']:<12}")
            
            print(f"  {'='*55}")
        
        # Select primary method
        if 'xonly' in freq_results and freq_results['xonly']['freq'] > 0:
            primary_method = 'xonly'
            final_freq = freq_results['xonly']['freq']
        elif 'full' in freq_results and freq_results['full']['freq'] > 0:
            primary_method = 'full'
            final_freq = freq_results['full']['freq']
        elif '1d' in freq_results and freq_results['1d']['freq'] > 0:
            primary_method = '1d'
            final_freq = freq_results['1d']['freq']
        else:
            primary_method = 'none'
            final_freq = 0.0
        
        # Get experimental reference
        ref_data = properties.get('reference', {})
        exp_freq = ref_data.get('freq')
        exp_d_eq = ref_data.get('d_eq')
        
        # Calculate errors
        d_eq_error = None
        freq_error = None
        
        if exp_d_eq and eq_dist > 0:
            d_eq_error = abs(eq_dist - exp_d_eq) / exp_d_eq * 100
        
        if exp_freq and final_freq > 0:
            freq_error = abs(final_freq - exp_freq) / exp_freq * 100
        
        results = {
            'molecule': molecule_name,
            'symbols': symbols,
            'equilibrium_distance': eq_dist,
            'exp_equilibrium_distance': exp_d_eq,
            'd_eq_error_percent': d_eq_error,
            'vibrational_frequency_cm1': final_freq,
            'exp_vibrational_frequency': exp_freq,
            'freq_error_percent': freq_error,
            'vibration_method': primary_method,
            'freq_1d': freq_results.get('1d', {}).get('freq', 0),
            'freq_xonly': freq_results.get('xonly', {}).get('freq', 0),
            'freq_full': freq_results.get('full', {}).get('freq', 0),
            'time_1d': freq_results.get('1d', {}).get('time', 0),
            'time_xonly': freq_results.get('xonly', {}).get('time', 0),
            'time_full': freq_results.get('full', {}).get('time', 0),
            'reference_source': ref_data.get('source', 'Unknown'),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Print comparison with experiment
        print(f"\n  {'='*50}")
        print(f"  COMPARISON WITH EXPERIMENT")
        print(f"  {'='*50}")
        if exp_d_eq:
            print(f"    Bond length: {eq_dist:.4f} Å (exp: {exp_d_eq:.4f} Å, error: {d_eq_error:.2f}%)")
        if exp_freq and final_freq > 0:
            print(f"    Frequency: {final_freq:.2f} cm⁻¹ (exp: {exp_freq:.2f} cm⁻¹, error: {freq_error:.2f}%)")
            print(f"    Method used: {primary_method}")
        elif exp_freq:
            print(f"    ⚠ Frequency not calculated")
        print(f"  {'='*50}")
        
        return results, opt_atoms