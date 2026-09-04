import os
import yaml
import numpy as np
import pandas as pd
from ase import Atoms
from ase.calculators.espresso import Espresso
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.io import write, read
from ase.units import kB, mol
import warnings
warnings.filterwarnings('ignore')

class QEDiatomicAnalyzer:
    def __init__(self, config):
        """Initialize with configuration."""
        self.config = config
        self.qe_config = config.get('qe', {})
        self.pseudopotentials = self.qe_config.get('pseudopotentials', {})
        self.calc = None
        self._setup_calculator()
    
    def _setup_calculator(self):
        """Setup Quantum ESPRESSO calculator."""
        # Basic QE parameters
        input_params = {
            'control': {
                'calculation': 'scf',
                'restart_mode': 'from_scratch',
                'pseudo_dir': './pseudopotentials/',
                'outdir': './tmp/',
                'prefix': 'qe',
                'tprnfor': True,
                'tstress': True,
                'verbosity': 'high',
            },
            'system': {
                'ibrav': 0,  # Free coordinates
                'nat': 2,
                'ntyp': 1,
                'ecutwfc': self.qe_config.get('ecutwfc', 50.0),
                'ecutrho': self.qe_config.get('ecutrho', 200.0),
                'occupations': 'smearing',
                'smearing': self.qe_config.get('smearing', 'gaussian'),
                'degauss': self.qe_config.get('degauss', 0.01),
                'nspin': 1,
                'tot_charge': 0,
            },
            'electrons': {
                'conv_thr': self.qe_config.get('conv_thr', 1.0e-8),
                'mixing_beta': self.qe_config.get('mixing_beta', 0.7),
                'electron_maxstep': self.qe_config.get('electron_maxstep', 100),
            }
        }
        
        # Setup calculator
        self.calc = Espresso(
            pseudopotentials=self.pseudopotentials,
            input_data=input_params,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
            pw_path=self.qe_config.get('pw_path', 'pw.x'),
            ph_path=self.qe_config.get('ph_path', 'ph.x'),
            q2r_path=self.qe_config.get('q2r_path', 'q2r.x'),
            matdyn_path=self.qe_config.get('matdyn_path', 'matdyn.x'),
        )
    
    def get_pseudopotential(self, symbol):
        """Get pseudopotential for given element."""
        return self.pseudopotentials.get(symbol, f'{symbol}.pbe-rrkjus.UPF')
    
    def create_diatomic(self, symbols, distance, cell_size=15.0):
        """Create a diatomic molecule with vacuum cell."""
        # Create molecule
        atoms = Atoms(symbols, positions=[(0, 0, 0), (distance, 0, 0)])
        
        # Add vacuum around molecule
        atoms.center(vacuum=cell_size/2)
        atoms.set_pbc(False)
        
        # Set cell with enough vacuum
        cell = np.eye(3) * (distance + cell_size)
        atoms.set_cell(cell)
        atoms.set_pbc(True)  # Use PBC but with large vacuum
        
        return atoms
    
    def optimize_geometry(self, atoms, fmax=0.001, steps=100):
        """Optimize geometry using BFGS."""
        # Set calculator
        atoms.set_calculator(self.calc)
        
        opt = BFGS(atoms, trajectory='qe_opt.traj', logfile='qe_opt.log')
        opt.run(fmax=fmax, steps=steps)
        
        return atoms
    
    def get_equilibrium_distance(self, symbols, initial_distance=1.2, fmax=0.001, steps=100):
        """Find equilibrium bond distance."""
        atoms = self.create_diatomic(symbols, initial_distance)
        opt_atoms = self.optimize_geometry(atoms, fmax, steps)
        return opt_atoms.get_distance(0, 1), opt_atoms
    
    def calculate_vibrational_frequencies(self, atoms, delta=0.01, nfree=2):
        """
        Calculate vibrational frequencies using finite differences.
        Returns frequencies in cm^-1.
        """
        try:
            # Set calculator for vibrations
            atoms.set_calculator(self.calc)
            
            # Calculate vibrations
            vib = Vibrations(atoms, indices=[0, 1], delta=delta, nfree=nfree)
            vib.run()
            
            # Get frequencies in cm^-1
            frequencies = vib.get_frequencies()
            
            # For diatomic, take the first non-zero frequency
            valid_freqs = [f for f in frequencies if abs(f) > 1.0]
            
            if len(valid_freqs) > 0:
                freq_cm1 = abs(valid_freqs[0])
            else:
                freq_cm1 = 0.0
            
            # Clean up
            try:
                vib.clean()
            except:
                pass
            
            return freq_cm1
            
        except Exception as e:
            print(f"Error in vibration calculation: {e}")
            return 0.0
    
    def analyze_molecule(self, molecule_name, properties):
        """Complete analysis of a diatomic molecule."""
        print(f"\n{'='*60}")
        print(f"Analyzing {molecule_name} with Quantum ESPRESSO")
        print(f"{'='*60}")
        
        # Get parameters
        symbols = properties['symbols']
        initial_dist = properties['initial_distance']
        
        # Setup pseudopotentials for this molecule
        unique_symbols = list(set(symbols))
        pseudos = {sym: self.get_pseudopotential(sym) for sym in unique_symbols}
        self.calc.pseudopotentials = pseudos
        
        # Update system ntyp
        self.calc.input_data['system']['ntyp'] = len(unique_symbols)
        
        # Get equilibrium distance
        eq_dist, opt_atoms = self.get_equilibrium_distance(
            symbols, initial_dist, 
            fmax=self.config.get('general', {}).get('fmax', 0.001),
            steps=self.config.get('general', {}).get('max_steps', 100)
        )
        
        print(f"✓ Equilibrium bond distance: {eq_dist:.4f} Å")
        
        # Calculate vibrational frequency
        freq_cm1 = self.calculate_vibrational_frequencies(
            opt_atoms, 
            delta=self.config.get('advanced', {}).get('vibrations', {}).get('delta', 0.01),
            nfree=self.config.get('advanced', {}).get('vibrations', {}).get('nfree', 2)
        )
        print(f"✓ Vibrational frequency: {freq_cm1:.2f} cm⁻¹")
        
        # Store results
        results = {
            'molecule': molecule_name,
            'calculator': 'Quantum ESPRESSO',
            'equilibrium_distance': eq_dist,
            'vibrational_frequency_cm1': freq_cm1,
            'd_eq_error': 0.0,
            'freq_error': 0.0
        }
        
        return results, opt_atoms

def load_config(config_file='config_qe.yaml'):
    """Load configuration from YAML file."""
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        print(f"Loaded configuration from {config_file}")
        return config
    except FileNotFoundError:
        print(f"Config file {config_file} not found.")
        return None
    except Exception as e:
        print(f"Error loading config: {e}")
        return None

def save_results(results, config):
    """Save results to files."""
    output_config = config.get('output', {})
    output_dir = output_config.get('output_dir', 'results_qe')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save summary as CSV
    csv_file = os.path.join(output_dir, 'summary.csv')
    with open(csv_file, 'w') as f:
        f.write("Molecule,Calculator,d_eq(Å),freq(cm⁻¹)\n")
        for mol_name, mol_result in results.items():
            if mol_result:
                f.write(f"{mol_name},Quantum ESPRESSO,"
                       f"{mol_result['equilibrium_distance']:.4f},"
                       f"{mol_result['vibrational_frequency_cm1']:.2f}\n")
    
    print(f"Results saved to {csv_file}")

def compare_with_reference(results, config):
    """Compare with reference values from NIST."""
    # Reference values
    reference = {
        'N2': {'d_eq': 1.0977, 'freq': 2358.6},
        'H2': {'d_eq': 0.7414, 'freq': 4401.2},
        'F2': {'d_eq': 1.4119, 'freq': 917.0},
        'O2': {'d_eq': 1.2075, 'freq': 1580.2}
    }
    
    print("\n" + "="*80)
    print("COMPARISON WITH REFERENCE VALUES (NIST)")
    print("="*80)
    print(f"{'Molecule':<8} {'Property':<15} {'Calculated':<12} {'Reference':<12} {'Error (%)':<10}")
    print("-"*80)
    
    comparisons = []
    
    for mol_name, ref in reference.items():
        if mol_name not in results:
            continue
            
        res = results[mol_name]
        if res is None:
            continue
        
        # Calculate errors
        dist_err = abs(res['equilibrium_distance'] - ref['d_eq']) / ref['d_eq'] * 100
        freq_err = abs(res['vibrational_frequency_cm1'] - ref['freq']) / ref['freq'] * 100 if ref['freq'] > 0 else 0
        
        comparisons.append({
            'Molecule': mol_name,
            'd_eq_calc': res['equilibrium_distance'],
            'd_eq_ref': ref['d_eq'],
            'd_eq_error': dist_err,
            'freq_calc': res['vibrational_frequency_cm1'],
            'freq_ref': ref['freq'],
            'freq_error': freq_err
        })
        
        # Print results with indicators
        d_eq_marker = "✓" if dist_err < 5 else "⚠" if dist_err < 20 else "✗"
        freq_marker = "✓" if freq_err < 10 else "⚠" if freq_err < 30 else "✗"
        
        print(f"{mol_name:<8} {'d_eq (Å)':<15} {res['equilibrium_distance']:<12.4f} {ref['d_eq']:<12.4f} {dist_err:<10.2f}{d_eq_marker}")
        print(f"{mol_name:<8} {'freq (cm⁻¹)':<15} {res['vibrational_frequency_cm1']:<12.2f} {ref['freq']:<12.2f} {freq_err:<10.2f}{freq_marker}")
        print("-"*80)
    
    # Save comparison to CSV
    if comparisons:
        output_config = config.get('output', {})
        output_dir = output_config.get('output_dir', 'results_qe')
        os.makedirs(output_dir, exist_ok=True)
        df = pd.DataFrame(comparisons)
        df.to_csv(os.path.join(output_dir, 'comparison_with_reference.csv'), index=False)
        print(f"\nComparison results saved to {output_dir}/comparison_with_reference.csv")
        
        # Print summary statistics
        print("\n" + "="*80)
        print("SUMMARY STATISTICS")
        print("="*80)
        
        if comparisons:
            avg_dist_err = np.mean([c['d_eq_error'] for c in comparisons])
            avg_freq_err = np.mean([c['freq_error'] for c in comparisons if c['freq_error'] < 1000])
            
            print(f"Average d_eq error: {avg_dist_err:.2f}%")
            print(f"Average freq error: {avg_freq_err:.2f}%")

def main():
    """Main execution function."""
    # Load configuration
    config = load_config('config_qe.yaml')
    
    if config is None:
        print("Please create config_qe.yaml file")
        return
    
    # Print settings
    general = config.get('general', {})
    print("Diatomic Molecule Analysis with Quantum ESPRESSO")
    print("="*60)
    print(f"Temperature: {general.get('temperature', 298.15):.2f} K")
    print(f"Pressure: {general.get('pressure', 101325):.0f} Pa")
    print(f"Convergence: fmax = {general.get('fmax', 0.001)}")
    
    # Print QE settings
    qe_config = config.get('qe', {})
    print(f"QE pseudopotential path: {qe_config.get('pseudo_dir', './pseudopotentials/')}")
    print(f"QE ecutwfc: {qe_config.get('ecutwfc', 50.0)} Ry")
    print(f"QE ecutrho: {qe_config.get('ecutrho', 200.0)} Ry")
    print("="*60)
    
    # Create analyzer
    analyzer = QEDiatomicAnalyzer(config)
    
    # Run analysis for each molecule
    molecules = config.get('molecules', {})
    results = {}
    
    for mol_name, properties in molecules.items():
        result, atoms = analyzer.analyze_molecule(mol_name, properties)
        if result:
            results[mol_name] = result
            
            # Save optimized structure
            output_config = config.get('output', {})
            if output_config.get('save_structures', True) and atoms:
                output_dir = output_config.get('output_dir', 'results_qe')
                os.makedirs(output_dir, exist_ok=True)
                write(f"{output_dir}/{mol_name}_qe_opt.xyz", atoms)
    
    # Save results
    if results:
        save_results(results, config)
    
    # Compare with reference values
    compare_with_reference(results, config)
    
    # Print final summary
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    output_config = config.get('output', {})
    output_dir = output_config.get('output_dir', 'results_qe')
    print(f"Results saved in: {output_dir}/")
    print("Files generated:")
    print("  - summary.csv: All calculated properties")
    print("  - comparison_with_reference.csv: Comparison with NIST reference values")
    print("  - *_qe_opt.xyz: Optimized structures")
    print("  - qe_opt.traj: Optimization trajectory")
    print("  - qe_opt.log: Optimization log")
    print("="*80)

if __name__ == "__main__":
    main()
