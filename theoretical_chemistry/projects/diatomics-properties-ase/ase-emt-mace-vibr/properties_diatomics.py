import os
import yaml
import numpy as np
import pandas as pd
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS, FIRE
from ase.vibrations import Vibrations
from ase.io import write, read
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Import MACE if available
MACE_AVAILABLE = False
try:
    from mace.calculators import MACECalculator
    MACE_AVAILABLE = True
except ImportError:
    pass

class DiatomicAnalyzer:
    def __init__(self, calculator_name='EMT', calculator_params=None):
        """Initialize with calculator type and parameters."""
        self.calculator_name = calculator_name
        self.calculator_params = calculator_params or {}
        self.calculator = None
        self.supported_elements = []
        self._initialize_calculator()
    
    def _initialize_calculator(self):
        """Initialize the calculator with proper error handling."""
        if self.calculator_name == 'EMT':
            try:
                self.calculator = EMT()
                # EMT supports a limited set of elements
                self.supported_elements = ['H', 'N', 'O', 'Cu', 'Ag', 'Au', 'Ni', 'Pd', 'Pt', 'Al']
                print(f"EMT calculator initialized. Supports: {self.supported_elements}")
            except Exception as e:
                print(f"Error initializing EMT: {e}")
                self.calculator = None
                
        elif self.calculator_name == 'MACE' and MACE_AVAILABLE:
            try:
                model = self.calculator_params.get('model', 'MACE')
                device = self.calculator_params.get('device', 'cpu')
                model_path = self.calculator_params.get('model_path', None)
                
                if model_path:
                    self.calculator = MACECalculator(model_paths=model_path, device=device)
                else:
                    self.calculator = MACECalculator(model=model, device=device)
                
                # MACE supports many elements
                self.supported_elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 
                                          'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 
                                          'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 
                                          'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 
                                          'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 
                                          'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 
                                          'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 
                                          'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 
                                          'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 
                                          'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 
                                          'Pb', 'Bi', 'Po', 'At', 'Rn']
                print(f"MACE calculator initialized with model: {model}")
                
            except Exception as e:
                print(f"Error initializing MACE: {e}")
                self.calculator = None
                self.supported_elements = []
        else:
            if self.calculator_name == 'MACE' and not MACE_AVAILABLE:
                print("MACE not available. Please install: pip install mace-torch")
            self.calculator = None
            self.supported_elements = []
    
    def supports_element(self, symbol):
        """Check if the calculator supports a given element."""
        if self.calculator is None:
            return False
        return symbol in self.supported_elements
    
    def create_diatomic(self, symbols, distance):
        """Create a diatomic molecule at the given distance."""
        atoms = Atoms(symbols, positions=[(0, 0, 0), (distance, 0, 0)])
        if self.calculator:
            atoms.set_calculator(self.calculator)
        return atoms
    
    def optimize_geometry(self, atoms, fmax=0.001, steps=100):
        """Optimize geometry using BFGS or FIRE."""
        if self.calculator is None:
            print("No calculator available for optimization")
            return atoms
        
        # Get optimization algorithm from config
        opt_algorithm = self.calculator_params.get('optimization', {}).get('algorithm', 'BFGS')
        
        if opt_algorithm == 'FIRE':
            opt = FIRE(atoms, trajectory=f'{self.calculator_name}_opt.traj', logfile=None)
        else:
            opt = BFGS(atoms, trajectory=f'{self.calculator_name}_opt.traj', logfile=None)
        
        try:
            opt.run(fmax=fmax, steps=steps)
        except Exception as e:
            print(f"Optimization failed: {e}")
        return atoms
    
    def get_equilibrium_distance(self, symbols, initial_distance=1.2, fmax=0.001, steps=100):
        """Find equilibrium bond distance."""
        # Check if calculator supports the elements
        for symbol in symbols:
            if not self.supports_element(symbol):
                print(f"Warning: {self.calculator_name} does not support element {symbol}")
                return initial_distance, None
        
        atoms = self.create_diatomic(symbols, initial_distance)
        opt_atoms = self.optimize_geometry(atoms, fmax, steps)
        
        if opt_atoms:
            return opt_atoms.get_distance(0, 1), opt_atoms
        return initial_distance, None
    
    def calculate_vibrational_frequency(self, atoms, delta=0.01, nfree=2):
        """
        Calculate vibrational frequency using ASE's Vibrations class (Full Hessian).
        This method uses FORCES to compute the Hessian, which is much more accurate
        than using energy differences.
        
        Returns frequency in cm^-1.
        """
        if atoms is None or self.calculator is None:
            return 0.0
        
        try:
            print(f"    Using ASE Vibrations (Full Hessian) with delta={delta}, nfree={nfree}")
            
            # Set calculator
            atoms.set_calculator(self.calculator)
            
            # Create Vibrations object - only vibrate atoms 0 and 1
            vib = Vibrations(
                atoms, 
                indices=[0, 1],  # Only vibrate the two atoms
                name='vib',      # Name for output files
                delta=delta,     # Displacement for finite differences
                nfree=nfree      # Number of displacements per direction
            )
            
            # Run the calculations
            total_calcs = 2 * nfree * 3 * 2  # 2 atoms × 3 directions × 2 displacements
            print(f"    Running {total_calcs} displacement calculations...")
            vib.run()
            
            # Get frequencies in cm^-1
            frequencies = vib.get_frequencies()
            
            # Get energies in eV
            energies = vib.get_energies()
            
            # Print summary for debugging
            print(f"\n    {'='*50}")
            print(f"    FULL HESSIAN RESULTS")
            print(f"    {'='*50}")
            print(f"    {'Mode':<6} {'Energy (eV)':<15} {'Frequency (cm⁻¹)':<15} {'Type'}")
            print(f"    {'-'*50}")
            
            # Classify modes and find the stretching mode
            stretching_mode = None
            stretching_freq = 0.0
            stretching_energy = 0.0
            
            for i, (freq, energy) in enumerate(zip(frequencies, energies)):
                freq_abs = abs(freq)
                energy_abs = abs(energy)
                
                # Classify mode type
                if freq_abs < 1.0:
                    mode_type = "Translation"
                elif freq_abs < 100.0:
                    mode_type = "Rotation (numerical noise)"
                else:
                    mode_type = "STRETCHING ✓"
                    # Store the stretching mode (highest frequency non-zero mode)
                    if freq_abs > stretching_freq:
                        stretching_freq = freq_abs
                        stretching_energy = energy_abs
                        stretching_mode = i
                
                # Print each mode
                freq_str = f"{freq:.2f}" if freq_abs > 0.01 else "0.00"
                print(f"    {i:<6} {energy_abs:<15.4f} {freq_str:<15} {mode_type}")
            
            print(f"    {'='*50}")
            
            # Now we have the stretching mode
            if stretching_mode is not None:
                print(f"\n    ✓ Stretching mode identified: Mode {stretching_mode}")
                print(f"      Frequency: {stretching_freq:.2f} cm⁻¹")
                print(f"      Energy: {stretching_energy:.4f} eV")
                
                # Write the stretching mode to a trajectory file for visualization
                try:
                    vib.write_mode(stretching_mode)
                    print(f"    ✓ Mode written to vib.{stretching_mode}.traj")
                except:
                    pass
                
                # Get zero-point energy (all modes)
                try:
                    vib_data = vib.get_vibrations()
                    zero_point = vib_data.get_zero_point_energy()
                    print(f"    Total zero-point energy: {zero_point:.4f} eV")
                except:
                    pass
                
            else:
                stretching_freq = 0.0
                print(f"    ⚠ No stretching mode found!")
            
            # Clean up
            try:
                vib.clean()
            except:
                pass
            
            return stretching_freq
            
        except Exception as e:
            print(f"  Error in vibration calculation: {e}")
            return 0.0
    
    def analyze_molecule(self, molecule_name, properties, config):
        """Complete analysis of a diatomic molecule - bond distance and frequency."""
        print(f"\n{'='*60}")
        print(f"Analyzing {molecule_name} with {self.calculator_name}")
        print(f"{'='*60}")
        
        # Check if calculator supports the elements
        symbols = properties['symbols']
        for symbol in symbols:
            if not self.supports_element(symbol):
                print(f"✗ {self.calculator_name} does not support element {symbol}")
                print(f"  Skipping {molecule_name} analysis")
                return None, None
        
        # Get parameters from config
        general = config.get('general', {})
        fmax = general.get('fmax', 0.001)
        max_steps = general.get('max_steps', 100)
        
        # Get advanced settings
        advanced = config.get('advanced', {})
        opt_settings = advanced.get('optimization', {})
        fmax = opt_settings.get('fmax', fmax)
        max_steps = opt_settings.get('max_steps', max_steps)
        
        # Get vibration parameters
        vib_settings = advanced.get('vibrations', {})
        delta = vib_settings.get('delta', 0.01)
        nfree = vib_settings.get('nfree', 2)
        
        # Check if equilibrium distance is provided in config
        eq_distance_from_config = properties.get('eq_distance', None)
        
        if eq_distance_from_config is not None:
            print(f"✓ Using pre-computed equilibrium bond distance: {eq_distance_from_config:.4f} Å")
            print(f"  (Skipping geometry optimization)")
            eq_dist = eq_distance_from_config
            
            # Create atoms at the pre-computed equilibrium distance
            opt_atoms = self.create_diatomic(symbols, eq_dist)
            opt_atoms.set_calculator(self.calculator)
        else:
            # Get equilibrium geometry
            initial_dist = properties['initial_distance']
            eq_dist, opt_atoms = self.get_equilibrium_distance(
                symbols, initial_dist, fmax, max_steps)
            
            if opt_atoms is None:
                print(f"✗ Optimization failed for {molecule_name}")
                return None, None
        
        print(f"✓ Equilibrium bond distance: {eq_dist:.4f} Å")
        
        # Calculate vibrational frequency using ASE Vibrations (Full Hessian)
        print(f"\n  Calculating vibrational frequency...")
        freq_cm1 = self.calculate_vibrational_frequency(opt_atoms, delta, nfree)
        
        if freq_cm1 > 0:
            print(f"✓ Vibrational frequency: {freq_cm1:.2f} cm⁻¹")
        else:
            print(f"⚠ Vibrational frequency calculation failed")
        
        # Store results
        results = {
            'molecule': molecule_name,
            'calculator': self.calculator_name,
            'equilibrium_distance': eq_dist,
            'vibrational_frequency_cm1': freq_cm1,
            'vibration_method': 'full_hessian',
            'delta': delta,
            'nfree': nfree
        }
        
        return results, opt_atoms

def load_config(config_file='config.yaml'):
    """Load configuration from YAML file."""
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        print(f"Loaded configuration from {config_file}")
        return config
    except FileNotFoundError:
        print(f"Config file {config_file} not found. Using default settings.")
        return get_default_config()
    except Exception as e:
        print(f"Error loading config: {e}")
        return get_default_config()

def get_default_config():
    """Return default configuration."""
    return {
        'general': {
            'fmax': 0.001,
            'max_steps': 100,
            'compare_with_reference': True,
            'verbose': True
        },
        'molecules': {
            'N2': {'symbols': ['N', 'N'], 'initial_distance': 1.2, 
                   'spin': 0, 'symmetry': 2, 'geometry': 'linear'},
            'H2': {'symbols': ['H', 'H'], 'initial_distance': 0.8,
                   'spin': 0, 'symmetry': 2, 'geometry': 'linear'},
            'F2': {'symbols': ['F', 'F'], 'initial_distance': 1.4,
                   'spin': 0, 'symmetry': 2, 'geometry': 'linear'},
            'O2': {'symbols': ['O', 'O'], 'initial_distance': 1.3,
                   'spin': 1, 'symmetry': 2, 'geometry': 'linear'}
        },
        'calculators': {
            'EMT': {'enabled': True},
            'MACE': {'enabled': False, 'model': 'MACE', 'device': 'cpu'}
        },
        'output': {
            'save_structures': True,
            'save_trajectories': True,
            'verbose': True,
            'output_dir': 'results'
        },
        'advanced': {
            'vibrations': {
                'delta': 0.01,   # Displacement for finite differences (Å)
                'nfree': 2       # Number of displacements per direction
            },
            'optimization': {
                'algorithm': 'BFGS',
                'max_steps': 100,
                'fmax': 0.0005
            }
        }
    }

def save_results(all_results, config):
    """Save results to files."""
    output_config = config.get('output', {})
    output_dir = output_config.get('output_dir', 'results')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save summary as CSV
    csv_file = os.path.join(output_dir, 'summary.csv')
    with open(csv_file, 'w') as f:
        # Write header
        f.write("Molecule,Calculator,d_eq(Å),freq(cm⁻¹),method,delta(Å),nfree\n")
        
        for calc_name, calc_results in all_results.items():
            for mol_name, mol_result in calc_results.items():
                if mol_result:
                    freq = mol_result.get('vibrational_frequency_cm1', 0.0)
                    if freq is None or np.isnan(freq):
                        freq = 0.0
                    f.write(f"{mol_name},{calc_name},"
                           f"{mol_result['equilibrium_distance']:.4f},"
                           f"{freq:.2f},"
                           f"{mol_result.get('vibration_method', 'N/A')},"
                           f"{mol_result.get('delta', 0.01)},"
                           f"{mol_result.get('nfree', 2)}\n")
    
    print(f"Results saved to {csv_file}")

def compare_with_reference_combined(config, all_results):
    """Compare both MACE and EMT with reference values in a combined table."""
    print("\n" + "="*80)
    print("COMPARISON WITH REFERENCE VALUES (NIST)")
    print("="*80)
    
    # Reference values from NIST
    reference = {
        'N2': {'d_eq': 1.0977, 'freq': 2358.6},
        'H2': {'d_eq': 0.7414, 'freq': 4401.2},
        'F2': {'d_eq': 1.4119, 'freq': 917.0},
        'O2': {'d_eq': 1.2075, 'freq': 1580.2}
    }
    
    # Collect results from all calculators
    all_comparisons = []
    
    for mol_name in config['molecules'].keys():
        if mol_name not in reference:
            continue
            
        ref = reference[mol_name]
        print(f"\n{mol_name} Reference: d_eq={ref['d_eq']:.4f} Å, freq={ref['freq']:.1f} cm⁻¹")
        print("-"*80)
        print(f"{'Calculator':<12} {'d_eq (Å)':<15} {'Error %':<10} "
              f"{'freq (cm⁻¹)':<15} {'Error %':<10} {'Method':<10}")
        print("-"*80)
        
        for calc_name, calc_results in all_results.items():
            if mol_name not in calc_results:
                continue
                
            res = calc_results[mol_name]
            if res is None:
                continue
                
            freq_calc = res.get('vibrational_frequency_cm1', 0.0)
            if freq_calc is None or np.isnan(freq_calc):
                freq_calc = 0.0
                
            # Calculate errors
            dist_err = abs(res['equilibrium_distance'] - ref['d_eq']) / ref['d_eq'] * 100
            freq_err = abs(freq_calc - ref['freq']) / ref['freq'] * 100 if ref['freq'] > 0 and freq_calc > 0 else 999.0
            
            # Store for CSV
            all_comparisons.append({
                'Molecule': mol_name,
                'Calculator': calc_name,
                'd_eq_calc': res['equilibrium_distance'],
                'd_eq_ref': ref['d_eq'],
                'd_eq_error': dist_err,
                'freq_calc': freq_calc,
                'freq_ref': ref['freq'],
                'freq_error': freq_err,
                'freq_method': res.get('vibration_method', 'N/A')
            })
            
            # Determine best performance indicators
            d_eq_marker = "✓" if dist_err < 5 else "⚠" if dist_err < 20 else "✗"
            freq_marker = "✓" if freq_err < 10 else "⚠" if freq_err < 30 else "✗" if freq_err < 999 else "✗"
            
            print(f"{calc_name:<12} {res['equilibrium_distance']:<15.4f} "
                  f"{dist_err:<10.2f}{d_eq_marker} "
                  f"{freq_calc:<15.2f} "
                  f"{freq_err:<10.2f}{freq_marker} "
                  f"{res.get('vibration_method', 'N/A'):<10}")
    
    # Save comparison to CSV
    if all_comparisons:
        output_config = config.get('output', {})
        output_dir = output_config.get('output_dir', 'results')
        os.makedirs(output_dir, exist_ok=True)
        comparison_file = os.path.join(output_dir, 'comparison_with_reference.csv')
        df = pd.DataFrame(all_comparisons)
        df.to_csv(comparison_file, index=False)
        print(f"\nComparison results saved to {comparison_file}")
        
        # Print summary statistics
        print("\n" + "="*80)
        print("SUMMARY STATISTICS")
        print("="*80)
        
        for calc_name in all_results.keys():
            calc_data = [c for c in all_comparisons if c['Calculator'] == calc_name]
            if calc_data:
                valid_data = [c for c in calc_data if c['freq_error'] < 999]
                avg_dist_err = np.mean([c['d_eq_error'] for c in calc_data])
                if valid_data:
                    avg_freq_err = np.mean([c['freq_error'] for c in valid_data])
                else:
                    avg_freq_err = 999.0
                
                print(f"\n{calc_name}:")
                print(f"  Average d_eq error: {avg_dist_err:.2f}%")
                if avg_freq_err < 999:
                    print(f"  Average freq error: {avg_freq_err:.2f}%")
                else:
                    print(f"  Average freq error: N/A (failed calculations)")

def run_analysis(config):
    """Run the complete analysis based on configuration."""
    # Get enabled calculators
    calc_config = config.get('calculators', {})
    enabled_calculators = []
    for calc_name, calc_settings in calc_config.items():
        if calc_settings.get('enabled', False):
            enabled_calculators.append(calc_name)
    
    if not enabled_calculators:
        print("No calculators enabled. Please enable at least one calculator in the config.")
        return {}
    
    print(f"\nEnabled calculators: {', '.join(enabled_calculators)}")
    
    all_results = {}
    molecules = config.get('molecules', {})
    
    for calc_name in enabled_calculators:
        print(f"\n{'#'*60}")
        print(f"Using {calc_name} calculator")
        print(f"{'#'*60}")
        
        # Get calculator parameters
        calc_params = config.get('calculators', {}).get(calc_name, {})
        
        # Merge advanced settings into calculator params
        advanced = config.get('advanced', {})
        calc_params['vibrations'] = advanced.get('vibrations', {})
        calc_params['optimization'] = advanced.get('optimization', {})
        
        analyzer = DiatomicAnalyzer(calc_name, calc_params)
        
        results = {}
        for mol_name, properties in molecules.items():
            result, atoms = analyzer.analyze_molecule(mol_name, properties, config)
            if result:
                results[mol_name] = result
                
                # Save optimized structure
                output_config = config.get('output', {})
                if output_config.get('save_structures', True) and atoms:
                    output_dir = output_config.get('output_dir', 'results')
                    os.makedirs(output_dir, exist_ok=True)
                    write(f"{output_dir}/{mol_name}_{calc_name}_opt.xyz", atoms)
        
        all_results[calc_name] = results
        
        # Print summary table
        if results:
            print(f"\n{'='*60}")
            print(f"Summary for {calc_name}")
            print(f"{'='*60}")
            print(f"{'Molecule':<8} {'d_eq (Å)':<10} {'freq (cm⁻¹)':<12} {'Method':<10}")
            print("-"*45)
            for mol, res in results.items():
                freq = res.get('vibrational_frequency_cm1', 0.0)
                if freq is None or np.isnan(freq):
                    freq = 0.0
                print(f"{mol:<8} {res['equilibrium_distance']:<10.4f} "
                      f"{freq:<12.2f} "
                      f"{res.get('vibration_method', 'N/A'):<10}")
        else:
            print(f"\nNo results obtained for {calc_name}")
    
    return all_results

def main():
    """Main execution function."""
    # Load configuration
    config = load_config('config.yaml')
    
    # Get general settings
    general = config.get('general', {})
    
    # Print settings
    print("Diatomic Molecule Analysis with ASE")
    print("="*60)
    print(f"Convergence: fmax = {general.get('fmax', 0.001)}")
    
    # Print advanced settings
    advanced = config.get('advanced', {})
    vib_settings = advanced.get('vibrations', {})
    print(f"Vibration delta: {vib_settings.get('delta', 0.01)} Å")
    print(f"Vibration nfree: {vib_settings.get('nfree', 2)}")
    print("="*60)
    
    # Check MACE availability
    if MACE_AVAILABLE:
        print("✓ MACE is available")
        # Check if MACE is enabled in config
        calc_config = config.get('calculators', {})
        if calc_config.get('MACE', {}).get('enabled', False):
            print("  MACE is enabled in configuration")
            print(f"  MACE model: {calc_config.get('MACE', {}).get('model', 'MACE')}")
            print(f"  MACE device: {calc_config.get('MACE', {}).get('device', 'cpu')}")
        else:
            print("  MACE is disabled in configuration (enable in config.yaml)")
    else:
        print("✗ MACE is not available (install with: pip install mace-torch)")
    
    # Run analysis
    all_results = run_analysis(config)
    
    # Save results
    if all_results:
        save_results(all_results, config)
    
    # Compare with reference values (both calculators)
    compare_ref = general.get('compare_with_reference', True)
    if compare_ref and all_results:
        compare_with_reference_combined(config, all_results)
    
    # Print final summary
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    output_config = config.get('output', {})
    output_dir = output_config.get('output_dir', 'results')
    print(f"Results saved in: {output_dir}/")
    print("Files generated:")
    print("  - summary.csv: All calculated properties")
    print("  - comparison_with_reference.csv: Comparison with NIST reference values")
    print("  - *_opt.xyz: Optimized structures for each molecule and calculator")
    print("  - *_opt.traj: Optimization trajectories")
    print("  - vib/*.json: Vibration displacement files")
    print("  - vib.*.traj: Vibrational mode trajectories")
    print("="*80)

if __name__ == "__main__":
    main()
