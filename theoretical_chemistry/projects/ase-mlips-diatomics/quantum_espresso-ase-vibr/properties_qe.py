#!/usr/bin/env python3
"""
Diatomic molecule analysis with Quantum ESPRESSO
Using NC SR (ONCVPSP) PBE pseudopotentials
Run with: python properties_qe.py
"""

import os
import sys
import subprocess
import yaml
import numpy as np
import pandas as pd
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.io import write, read
from ase.units import kB, mol
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# OpenMP Thread Control - Keep only MPI parallelization
# ============================================================================
# Set OpenMP threads to 1 before launching Quantum ESPRESSO
# This prevents OpenMP from using multiple threads and interfering with MPI
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"  # Also restricts Intel MKL threads
os.environ["OPENBLAS_NUM_THREADS"] = "1"  # For OpenBLAS
os.environ["NUMEXPR_NUM_THREADS"] = "1"   # For NumExpr

# Optional: Also set these for additional control
os.environ["MKL_DYNAMIC"] = "FALSE"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_DYNAMIC"] = "FALSE"
os.environ["OMP_MAX_ACTIVE_LEVELS"] = "1"
# ============================================================================

class QEDiatomicAnalyzer:
    def __init__(self, config):
        """Initialize with configuration."""
        self.config = config
        self.qe_config = config.get('qe', {})
        self.parallel_config = self.qe_config.get('parallel', {})
        self.pseudo_dir = self.qe_config.get('pseudo_dir', './pseudopotentials/')
        self.pseudopotentials = self.qe_config.get('pseudopotentials', {})
        
        # Build the command with MPI
        self.command = self._build_command()
        
        self.calc = None
        self._setup_directories()
        self._setup_calculator()
    
    def _build_command(self):
        """Build the command string with MPI if enabled."""
        use_mpi = self.parallel_config.get('use_mpi', True)
        nprocs = self.parallel_config.get('nprocs', 4)
        mpi_command = self.parallel_config.get('mpi_command', 'mpirun')
        
        if use_mpi and nprocs > 1:
            # Build MPI command
            # Check if we're on a SLURM system
            if 'SLURM_NTASKS' in os.environ:
                # Use srun if available
                return f'srun -n {nprocs} pw.x'
            else:
                # Use mpirun/mpiexec
                return f'{mpi_command} -np {nprocs} pw.x'
        else:
            # Serial run
            return 'pw.x'
    
    def _setup_directories(self):
        """Create necessary directories."""
        os.makedirs(self.pseudo_dir, exist_ok=True)
        os.makedirs('./tmp/', exist_ok=True)
        os.makedirs(self.config.get('output', {}).get('output_dir', 'results_qe'), exist_ok=True)
    
    def _setup_calculator(self):
        """Setup Quantum ESPRESSO calculator using EspressoProfile."""
        
        # Create profile with command and pseudo_dir
        profile = EspressoProfile(
            command=self.command,
            pseudo_dir=self.pseudo_dir,
        )
        
        # Basic QE parameters in flat format (ASE will put them in correct sections)
        self.input_data = {
            # Control section
            'calculation': 'scf',
            'restart_mode': 'from_scratch',
            'outdir': './tmp/',
            'prefix': 'qe',
            'tprnfor': True,
            'tstress': True,
            'verbosity': 'high',
            
            # System section
            'ecutwfc': self.qe_config.get('ecutwfc', 80.0),
            'ecutrho': self.qe_config.get('ecutrho', 320.0),
            'occupations': 'smearing',
            'smearing': self.qe_config.get('smearing', 'gaussian'),
            'degauss': self.qe_config.get('degauss', 0.01),
            'nspin': 1,
            'ntyp': 1,  # Will be updated per molecule
            
            # Electrons section
            'conv_thr': self.qe_config.get('conv_thr', 1.0e-10),
            'mixing_beta': self.qe_config.get('mixing_beta', 0.7),
            'electron_maxstep': self.qe_config.get('electron_maxstep', 200),
        }
        
        # Setup calculator with profile
        self.calc = Espresso(
            profile=profile,
            pseudopotentials=self.pseudopotentials,
            input_data=self.input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
    
    def get_pseudopotential(self, symbol):
        """Get pseudopotential filename for given element."""
        return self.pseudopotentials.get(symbol, f'{symbol}.upf')
    
    def check_pseudopotential_exists(self, symbol):
        """Check if pseudopotential file exists."""
        pp_file = self.get_pseudopotential(symbol)
        pp_path = os.path.join(self.pseudo_dir, pp_file)
        exists = os.path.exists(pp_path)
        if not exists:
            print(f"  ✗ Pseudopotential {pp_path} not found!")
        return exists
    
    def create_diatomic(self, symbols, distance, cell_size=15.0):
        """Create a diatomic molecule with vacuum cell."""
        # Create molecule
        atoms = Atoms(symbols, positions=[(0, 0, 0), (distance, 0, 0)])
        
        # Add vacuum around molecule
        atoms.center(vacuum=cell_size/2)
        
        # Set cell with enough vacuum
        cell = np.eye(3) * (distance + cell_size)
        atoms.set_cell(cell)
        atoms.set_pbc(True)  # Use PBC but with large vacuum
        
        return atoms
    
    def optimize_geometry(self, atoms, fmax=0.001, steps=100):
        """Optimize geometry using BFGS."""
        atoms.set_calculator(self.calc)
        opt = BFGS(atoms, trajectory='qe_opt.traj', logfile='qe_opt.log')
        opt.run(fmax=fmax, steps=steps)
        return atoms
    
    def get_equilibrium_distance(self, symbols, initial_distance=1.2, fmax=0.001, steps=100):
        """Find equilibrium bond distance."""
        # Check pseudopotentials
        unique_symbols = list(set(symbols))
        all_exist = True
        for sym in unique_symbols:
            if not self.check_pseudopotential_exists(sym):
                all_exist = False
        
        if not all_exist:
            print(f"  ✗ Missing pseudopotentials for {symbols}")
            return initial_distance, None
        
        atoms = self.create_diatomic(symbols, initial_distance)
        
        # Update calculator for this molecule
        self._update_calculator_for_molecule(unique_symbols)
        atoms.set_calculator(self.calc)
        
        opt_atoms = self.optimize_geometry(atoms, fmax, steps)
        return opt_atoms.get_distance(0, 1), opt_atoms
    
    def _update_calculator_for_molecule(self, symbols):
        """Update calculator for specific molecule."""
        # Update pseudopotentials
        pseudo_dict = {sym: self.get_pseudopotential(sym) for sym in symbols}
        self.calc.pseudopotentials = pseudo_dict
        
        # Update ntyp
        self.input_data['ntyp'] = len(symbols)
        
        # Need to recreate calculator with updated input_data
        profile = EspressoProfile(
            command=self.command,
            pseudo_dir=self.pseudo_dir,
        )
        
        # Create new calculator with updated parameters
        self.calc = Espresso(
            profile=profile,
            pseudopotentials=pseudo_dict,
            input_data=self.input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
    
    def _get_mass(self, symbol):
        """Get atomic mass in amu."""
        masses = {
            'H': 1.008, 'N': 14.007, 'O': 15.999,
            'F': 18.998, 'Cl': 35.453
        }
        return masses.get(symbol, 0.0)
    
    def calculate_vibrational_frequencies(self, atoms, delta=0.005, nfree=4):
        """
        Calculate vibrational frequencies using finite differences.
        Returns frequencies in cm^-1.
        """
        try:
            atoms.set_calculator(self.calc)
            
            # Calculate vibrations with optimized parameters
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
            print(f"  Error in vibration calculation: {e}")
            return 0.0
    
    def analyze_molecule(self, molecule_name, properties):
        """Complete analysis of a diatomic molecule."""
        print(f"\n{'='*60}")
        print(f"Analyzing {molecule_name}")
        print(f"{'='*60}")
        
        # Get parameters
        symbols = properties['symbols']
        initial_dist = properties['initial_distance']
        
        # Setup calculator for this molecule
        unique_symbols = list(set(symbols))
        
        # Check pseudopotentials exist
        for sym in unique_symbols:
            if not self.check_pseudopotential_exists(sym):
                print(f"  ✗ Pseudopotential for {sym} not found")
                return None, None
        
        # Update calculator for this molecule
        self._update_calculator_for_molecule(unique_symbols)
        
        # Get equilibrium distance
        fmax = self.config.get('general', {}).get('fmax', 0.001)
        max_steps = self.config.get('general', {}).get('max_steps', 100)
        
        print(f"  Finding equilibrium geometry...")
        eq_dist, opt_atoms = self.get_equilibrium_distance(
            symbols, initial_dist, fmax, max_steps
        )
        
        if opt_atoms is None:
            print(f"  ✗ Optimization failed for {molecule_name}")
            return None, None
        
        print(f"  ✓ Equilibrium bond distance: {eq_dist:.4f} Å")
        
        # Calculate vibrational frequency
        print(f"  Calculating vibrational frequency...")
        delta = self.qe_config.get('delta', 0.005)
        nfree = self.qe_config.get('nfree', 4)
        freq_cm1 = self.calculate_vibrational_frequencies(opt_atoms, delta, nfree)
        print(f"  ✓ Vibrational frequency: {freq_cm1:.2f} cm⁻¹")
        
        # Store results
        results = {
            'molecule': molecule_name,
            'symbols': symbols,
            'calculator': 'Quantum ESPRESSO (ONCVPSP PBE)',
            'equilibrium_distance': eq_dist,
            'vibrational_frequency_cm1': freq_cm1,
        }
        
        return results, opt_atoms

def load_config(config_file='config_qe.yaml'):
    """Load configuration from YAML file."""
    if not os.path.exists(config_file):
        print(f"Error: Config file {config_file} not found!")
        print("Please create config_qe.yaml with your settings.")
        sys.exit(1)
    
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        print(f"✓ Loaded configuration from {config_file}")
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

def save_results(results, config):
    """Save results to files."""
    output_config = config.get('output', {})
    output_dir = output_config.get('output_dir', 'results_qe')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save summary as CSV
    csv_file = os.path.join(output_dir, 'summary.csv')
    with open(csv_file, 'w') as f:
        f.write("Molecule,Symbols,Calculator,d_eq(Å),freq(cm⁻¹)\n")
        for mol_name, mol_result in results.items():
            if mol_result:
                symbols = ''.join(mol_result.get('symbols', []))
                f.write(f"{mol_name},{symbols},Quantum ESPRESSO (ONCVPSP PBE),"
                       f"{mol_result['equilibrium_distance']:.4f},"
                       f"{mol_result['vibrational_frequency_cm1']:.2f}\n")
    
    print(f"✓ Results saved to {csv_file}")

def compare_with_reference(results, config):
    """Compare with reference values from NIST."""
    # Reference values
    reference = {
        'N2': {'d_eq': 1.0977, 'freq': 2358.6},
        'H2': {'d_eq': 0.7414, 'freq': 4401.2},
        'F2': {'d_eq': 1.4119, 'freq': 917.0},
        'O2': {'d_eq': 1.2075, 'freq': 1580.2},
        'Cl2': {'d_eq': 1.9879, 'freq': 559.7}
    }
    
    print("\n" + "="*80)
    print("COMPARISON WITH REFERENCE VALUES (NIST)")
    print("="*80)
    print(f"{'Molecule':<8} {'Property':<15} {'Calculated':<12} {'Reference':<12} {'Error (%)':<10} {'Status'}")
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
        d_eq_marker = "✓" if dist_err < 2 else "⚠" if dist_err < 5 else "✗"
        freq_marker = "✓" if freq_err < 10 else "⚠" if freq_err < 20 else "✗"
        
        print(f"{mol_name:<8} {'d_eq (Å)':<15} {res['equilibrium_distance']:<12.4f} {ref['d_eq']:<12.4f} {dist_err:<10.2f} {d_eq_marker}")
        print(f"{mol_name:<8} {'freq (cm⁻¹)':<15} {res['vibrational_frequency_cm1']:<12.2f} {ref['freq']:<12.2f} {freq_err:<10.2f} {freq_marker}")
        print("-"*80)
    
    # Save comparison to CSV
    if comparisons:
        output_config = config.get('output', {})
        output_dir = output_config.get('output_dir', 'results_qe')
        os.makedirs(output_dir, exist_ok=True)
        df = pd.DataFrame(comparisons)
        df.to_csv(os.path.join(output_dir, 'comparison_with_reference.csv'), index=False)
        print(f"\n✓ Comparison results saved to {output_dir}/comparison_with_reference.csv")
        
        # Print summary statistics
        print("\n" + "="*80)
        print("SUMMARY STATISTICS")
        print("="*80)
        
        if comparisons:
            avg_dist_err = np.mean([c['d_eq_error'] for c in comparisons])
            avg_freq_err = np.mean([c['freq_error'] for c in comparisons if c['freq_error'] < 1000])
            
            print(f"  Average d_eq error: {avg_dist_err:.2f}%")
            print(f"  Average freq error: {avg_freq_err:.2f}%")
            
            # Overall assessment
            if avg_dist_err < 2 and avg_freq_err < 10:
                print("  ✓ Excellent agreement with reference values")
            elif avg_dist_err < 5 and avg_freq_err < 20:
                print("  ✓ Good agreement with reference values")
            else:
                print("  ⚠ Moderate agreement - consider improving convergence parameters")

def check_environment():
    """Check if required executables and files are available."""
    print("\n" + "="*60)
    print("CHECKING ENVIRONMENT")
    print("="*60)
    
    # Display OpenMP thread settings
    print("\n  OpenMP Thread Control:")
    print(f"    OMP_NUM_THREADS = {os.environ.get('OMP_NUM_THREADS', 'Not set')}")
    print(f"    MKL_NUM_THREADS = {os.environ.get('MKL_NUM_THREADS', 'Not set')}")
    print(f"    OPENBLAS_NUM_THREADS = {os.environ.get('OPENBLAS_NUM_THREADS', 'Not set')}")
    
    # Load config to get parallel settings
    config = load_config('config_qe.yaml')
    parallel_config = config.get('qe', {}).get('parallel', {})
    use_mpi = parallel_config.get('use_mpi', True)
    nprocs = parallel_config.get('nprocs', 4)
    mpi_command = parallel_config.get('mpi_command', 'mpirun')
    
    # Check MPI executable
    if use_mpi and nprocs > 1:
        # Check if mpi command exists
        try:
            subprocess.run([mpi_command, '--version'], capture_output=True, check=False)
            print(f"\n  ✓ {mpi_command} found in PATH")
            print(f"    Using {nprocs} processors with MPI")
        except FileNotFoundError:
            print(f"\n  ✗ {mpi_command} not found in PATH")
            print(f"    Will try to use {nprocs} processors with MPI anyway")
    
    # Check QE executables
    qe_exes = ['pw.x', 'ph.x', 'q2r.x', 'matdyn.x']
    all_found = True
    print("\n  Quantum ESPRESSO Executables:")
    for exe in qe_exes:
        found = False
        # Check if in PATH
        for path in os.environ.get('PATH', '').split(':'):
            if os.path.exists(os.path.join(path, exe)):
                found = True
                break
        if found:
            print(f"    ✓ {exe} found in PATH")
        else:
            print(f"    ✗ {exe} not found in PATH")
            all_found = False
    
    # Check pseudopotentials
    print(f"\n  Pseudopotentials in {config.get('qe', {}).get('pseudo_dir', './pseudopotentials/')}:")
    pp_files = ['H.upf', 'N.upf', 'O.upf', 'F.upf', 'Cl.upf']
    pp_dir = config.get('qe', {}).get('pseudo_dir', './pseudopotentials/')
    
    for pp in pp_files:
        pp_path = os.path.join(pp_dir, pp)
        if os.path.exists(pp_path):
            print(f"    ✓ {pp} found")
        else:
            print(f"    ✗ {pp} not found in {pp_dir}")
            all_found = False
    
    if not all_found:
        print("\n  ⚠ Some requirements are missing. The calculation may fail.")
        print("  Make sure:")
        print("    1. Quantum ESPRESSO executables are in your PATH")
        print("    2. Pseudopotential files (.upf) are in the pseudopotentials/ directory")
        if use_mpi and nprocs > 1:
            print(f"    3. {mpi_command} is available for parallel execution")
    
    return all_found

def print_parallel_info():
    """Print information about parallelization settings."""
    print("\n" + "="*60)
    print("PARALLELIZATION INFORMATION")
    print("="*60)
    
    # Read config
    config = load_config('config_qe.yaml')
    parallel_config = config.get('qe', {}).get('parallel', {})
    
    use_mpi = parallel_config.get('use_mpi', True)
    nprocs = parallel_config.get('nprocs', 4)
    mpi_command = parallel_config.get('mpi_command', 'mpirun')
    
    print(f"  MPI enabled: {use_mpi}")
    print(f"  Number of MPI processes: {nprocs}")
    print(f"  MPI command: {mpi_command}")
    
    print("\n  Thread settings (OpenMP disabled for MPI-only parallelization):")
    print(f"    OMP_NUM_THREADS = {os.environ.get('OMP_NUM_THREADS', '1')}")
    print(f"    MKL_NUM_THREADS = {os.environ.get('MKL_NUM_THREADS', '1')}")
    print(f"    OPENBLAS_NUM_THREADS = {os.environ.get('OPENBLAS_NUM_THREADS', '1')}")

def main():
    """Main execution function."""
    print("="*80)
    print("Diatomic Molecule Analysis with Quantum ESPRESSO")
    print("Using NC SR (ONCVPSP) PBE Pseudopotentials")
    print("="*80)
    
    # Print parallelization info
    print_parallel_info()
    
    # Load configuration
    config = load_config('config_qe.yaml')
    
    # Check environment
    env_ok = check_environment()
    
    # Print settings
    general = config.get('general', {})
    print("\n" + "="*60)
    print("CALCULATION SETTINGS")
    print("="*60)
    print(f"  Temperature: {general.get('temperature', 298.15):.2f} K")
    print(f"  Pressure: {general.get('pressure', 101325):.0f} Pa")
    print(f"  Convergence: fmax = {general.get('fmax', 0.001)}")
    
    qe_config = config.get('qe', {})
    parallel_config = qe_config.get('parallel', {})
    
    print(f"\n  Quantum ESPRESSO Settings:")
    print(f"    Pseudo dir: {qe_config.get('pseudo_dir', './pseudopotentials/')}")
    print(f"    ecutwfc: {qe_config.get('ecutwfc', 80.0)} Ry")
    print(f"    ecutrho: {qe_config.get('ecutrho', 320.0)} Ry")
    print(f"    conv_thr: {qe_config.get('conv_thr', 1.0e-10)}")
    print(f"    delta: {qe_config.get('delta', 0.005)} Å")
    print(f"    nfree: {qe_config.get('nfree', 4)}")
    
    if not env_ok:
        print("\n" + "!"*60)
        print("WARNING: Some requirements are missing!")
        print("!"*60)
        response = input("\nContinue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Exiting...")
            sys.exit(1)
    
    # Create analyzer
    print("\n" + "="*60)
    print("RUNNING CALCULATIONS")
    print("="*60)
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
        print("\n" + "="*60)
        print("SAVING RESULTS")
        print("="*60)
        save_results(results, config)
        
        # Compare with reference values
        compare_with_reference(results, config)
    
    # Print final summary
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    output_config = config.get('output', {})
    output_dir = output_config.get('output_dir', 'results_qe')
    print(f"  Results saved in: {output_dir}/")
    print("\n  Files generated:")
    print(f"    - {output_dir}/summary.csv: All calculated properties")
    print(f"    - {output_dir}/comparison_with_reference.csv: Comparison with NIST values")
    print(f"    - {output_dir}/*_qe_opt.xyz: Optimized structures")
    print("    - qe_opt.traj: Optimization trajectory")
    print("    - qe_opt.log: Optimization log")
    print("="*80)

if __name__ == "__main__":
    main()
