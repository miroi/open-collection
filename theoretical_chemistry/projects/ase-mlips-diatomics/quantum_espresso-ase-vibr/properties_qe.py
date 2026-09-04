#!/usr/bin/env python3
"""
Diatomic molecule analysis with Quantum ESPRESSO
Optimized for fast vibrational frequency calculation using 1D scan
"""

import os
import sys
import yaml
import numpy as np
import pandas as pd
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.optimize import BFGS
from ase.io import write, read
import warnings
warnings.filterwarnings('ignore')

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
        self.vib_calc = None
        self._setup_directories()
        self._setup_calculator()
        self._setup_vibration_calculator()
    
    def _build_command(self):
        """Build the command string with MPI if enabled."""
        use_mpi = self.parallel_config.get('use_mpi', True)
        nprocs = self.parallel_config.get('nprocs', 4)
        mpi_command = self.parallel_config.get('mpi_command', 'mpirun')
        
        if use_mpi and nprocs > 1:
            if 'SLURM_NTASKS' in os.environ:
                return f'srun -n {nprocs} pw.x'
            else:
                return f'{mpi_command} -np {nprocs} pw.x'
        else:
            return 'pw.x'
    
    def _setup_directories(self):
        """Create necessary directories."""
        os.makedirs(self.pseudo_dir, exist_ok=True)
        os.makedirs('./tmp/', exist_ok=True)
        os.makedirs(self.config.get('output', {}).get('output_dir', 'results_qe'), exist_ok=True)
    
    def _setup_calculator(self):
        """Setup main Quantum ESPRESSO calculator."""
        profile = EspressoProfile(
            command=self.command,
            pseudo_dir=self.pseudo_dir,
        )
        
        self.input_data = {
            'calculation': 'scf',
            'restart_mode': 'from_scratch',
            'outdir': './tmp/',
            'prefix': 'qe',
            'tprnfor': True,
            'tstress': True,
            'verbosity': 'low',
            
            'ecutwfc': self.qe_config.get('ecutwfc', 80.0),
            'ecutrho': self.qe_config.get('ecutrho', 320.0),
            'occupations': 'smearing',
            'smearing': self.qe_config.get('smearing', 'gaussian'),
            'degauss': self.qe_config.get('degauss', 0.01),
            'nspin': 1,
            'ntyp': 1,
            
            'conv_thr': self.qe_config.get('conv_thr', 1.0e-10),
            'mixing_beta': self.qe_config.get('mixing_beta', 0.7),
            'electron_maxstep': self.qe_config.get('electron_maxstep', 200),
        }
        
        self.calc = Espresso(
            profile=profile,
            pseudopotentials=self.pseudopotentials,
            input_data=self.input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
    
    def _setup_vibration_calculator(self):
        """Setup a separate calculator for vibrations."""
        profile = EspressoProfile(
            command=self.command,
            pseudo_dir=self.pseudo_dir,
        )
        
        vib_input_data = {
            'calculation': 'scf',
            'restart_mode': 'from_scratch',
            'outdir': './tmp/',
            'prefix': 'vib',
            'tprnfor': True,
            'tstress': True,
            'verbosity': 'low',
            
            # Use slightly lower accuracy for speed
            'ecutwfc': max(40.0, self.qe_config.get('ecutwfc', 80.0) * 0.6),
            'ecutrho': max(160.0, self.qe_config.get('ecutrho', 320.0) * 0.6),
            'occupations': 'smearing',
            'smearing': self.qe_config.get('smearing', 'gaussian'),
            'degauss': self.qe_config.get('degauss', 0.01),
            'nspin': 1,
            'ntyp': 1,
            
            'conv_thr': 1.0e-8,
            'mixing_beta': self.qe_config.get('mixing_beta', 0.7),
            'electron_maxstep': 100,
        }
        
        self.vib_calc = Espresso(
            profile=profile,
            pseudopotentials=self.pseudopotentials,
            input_data=vib_input_data,
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
        atoms = Atoms(symbols, positions=[(0, 0, 0), (distance, 0, 0)])
        atoms.center(vacuum=cell_size/2)
        cell = np.eye(3) * (distance + cell_size)
        atoms.set_cell(cell)
        atoms.set_pbc(True)
        return atoms
    
    def optimize_geometry(self, atoms, fmax=0.001, steps=100):
        """Optimize geometry using BFGS."""
        atoms.set_calculator(self.calc)
        opt = BFGS(atoms, trajectory='qe_opt.traj', logfile='qe_opt.log')
        opt.run(fmax=fmax, steps=steps)
        return atoms
    
    def get_equilibrium_distance(self, symbols, initial_distance=1.2, fmax=0.001, steps=100):
        """Find equilibrium bond distance."""
        unique_symbols = list(set(symbols))
        all_exist = True
        for sym in unique_symbols:
            if not self.check_pseudopotential_exists(sym):
                all_exist = False
        
        if not all_exist:
            print(f"  ✗ Missing pseudopotentials for {symbols}")
            return initial_distance, None
        
        atoms = self.create_diatomic(symbols, initial_distance)
        self._update_calculator_for_molecule(unique_symbols)
        atoms.set_calculator(self.calc)
        
        opt_atoms = self.optimize_geometry(atoms, fmax, steps)
        return opt_atoms.get_distance(0, 1), opt_atoms
    
    def _update_calculator_for_molecule(self, symbols):
        """Update calculator for specific molecule."""
        pseudo_dict = {sym: self.get_pseudopotential(sym) for sym in symbols}
        
        # Update main calculator
        self.calc.pseudopotentials = pseudo_dict
        self.input_data['ntyp'] = len(symbols)
        
        profile = EspressoProfile(
            command=self.command,
            pseudo_dir=self.pseudo_dir,
        )
        
        self.calc = Espresso(
            profile=profile,
            pseudopotentials=pseudo_dict,
            input_data=self.input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
        
        # Update vibration calculator
        vib_input_data = self.vib_calc.input_data.copy()
        vib_input_data['ntyp'] = len(symbols)
        
        self.vib_calc = Espresso(
            profile=profile,
            pseudopotentials=pseudo_dict,
            input_data=vib_input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
    
    def calculate_vibrational_frequency_1d(self, atoms, delta=0.005, n_points=5):
        """
        Calculate vibrational frequency using 1D scan along the bond.
        This is MUCH faster than full 3D Hessian calculation.
        
        Only samples along the M-M bond direction.
        Returns frequency in cm^-1.
        """
        try:
            symbols = atoms.get_chemical_symbols()
            r_eq = atoms.get_distance(0, 1)
            
            # Sample points along the bond direction
            # Use fewer points but with better spacing
            r_values = np.linspace(r_eq - delta, r_eq + delta, n_points)
            energies = []
            
            print(f"    Scanning bond length from {r_values[0]:.4f} to {r_values[-1]:.4f} Å")
            
            for i, r in enumerate(r_values):
                # Create temporary atoms with this bond length
                temp_atoms = Atoms(symbols, positions=[(0, 0, 0), (r, 0, 0)])
                temp_atoms.set_cell(atoms.get_cell())
                temp_atoms.set_pbc(True)
                temp_atoms.set_calculator(self.vib_calc)
                
                # Calculate energy
                energy = temp_atoms.get_potential_energy()
                energies.append(energy)
                
                # Progress indicator
                print(f"      Point {i+1}/{n_points}: r = {r:.4f} Å, E = {energy:.6f} eV")
            
            # Fit to a quadratic polynomial: E(r) = a0 + a1*(r-r_eq) + a2*(r-r_eq)^2
            r_shifted = r_values - r_eq
            coeffs = np.polyfit(r_shifted, energies, 2)
            
            # Second derivative = 2 * coeffs[0] (eV/A^2)
            second_deriv = 2 * coeffs[0]
            
            if second_deriv <= 0:
                print(f"    Warning: Negative second derivative ({second_deriv:.6f} eV/A^2)")
                # Try fitting with more points
                if n_points < 9:
                    print(f"    Retrying with more points...")
                    return self.calculate_vibrational_frequency_1d(atoms, delta, n_points + 4)
                return 0.0
            
            # Convert to frequency
            masses = self._get_masses(symbols)
            reduced_mass_amu = (masses[0] * masses[1]) / (masses[0] + masses[1])
            reduced_mass_kg = reduced_mass_amu * 1.66054e-27
            
            # k in N/m = second_deriv (eV/A^2) * 160.2177
            k_Nm = second_deriv * 160.2177
            
            # Frequency in cm^-1: v = 1/(2*pi*c) * sqrt(k/mu)
            c_cm_s = 2.99792458e10
            freq_cm1 = 1/(2 * np.pi * c_cm_s) * np.sqrt(k_Nm / reduced_mass_kg)
            
            print(f"    Force constant: {k_Nm:.2f} N/m")
            print(f"    Reduced mass: {reduced_mass_amu:.4f} amu")
            
            return abs(freq_cm1)
            
        except Exception as e:
            print(f"  Error in 1D frequency calculation: {e}")
            return 0.0
    
    def _get_masses(self, symbols):
        """Get atomic masses in amu."""
        masses = {
            'H': 1.008, 'He': 4.0026, 'Li': 6.941, 'Be': 9.0122,
            'B': 10.81, 'C': 12.011, 'N': 14.007, 'O': 15.999,
            'F': 18.998, 'Ne': 20.180, 'Na': 22.990, 'Mg': 24.305,
            'Al': 26.982, 'Si': 28.086, 'P': 30.974, 'S': 32.065,
            'Cl': 35.453, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078
        }
        return [masses.get(s, 0.0) for s in symbols]
    
    def analyze_molecule(self, molecule_name, properties):
        """Complete analysis of a diatomic molecule."""
        print(f"\n{'='*60}")
        print(f"Analyzing {molecule_name}")
        print(f"{'='*60}")
        
        symbols = properties['symbols']
        initial_dist = properties['initial_distance']
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
        
        # Calculate vibrational frequency using 1D scan
        print(f"  Calculating vibrational frequency using 1D scan...")
        delta = self.qe_config.get('delta', 0.005)
        n_points = self.qe_config.get('n_points', 7)  # Number of points for 1D scan
        
        import time
        start_time = time.time()
        freq_cm1 = self.calculate_vibrational_frequency_1d(opt_atoms, delta, n_points)
        elapsed = time.time() - start_time
        
        if freq_cm1 > 0:
            print(f"  ✓ Vibrational frequency: {freq_cm1:.2f} cm⁻¹ (took {elapsed:.1f} seconds)")
        else:
            print(f"  ✗ Frequency calculation failed")
        
        results = {
            'molecule': molecule_name,
            'symbols': symbols,
            'calculator': 'Quantum ESPRESSO (ONCVPSP PBE)',
            'equilibrium_distance': eq_dist,
            'vibrational_frequency_cm1': freq_cm1,
            'calculation_time': elapsed,
        }
        
        return results, opt_atoms

# [Rest of the functions remain the same...]

def load_config(config_file='config_qe.yaml'):
    """Load configuration from YAML file."""
    if not os.path.exists(config_file):
        print(f"Error: Config file {config_file} not found!")
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
    
    csv_file = os.path.join(output_dir, 'summary.csv')
    with open(csv_file, 'w') as f:
        f.write("Molecule,Symbols,Calculator,d_eq(Å),freq(cm⁻¹),Time(s)\n")
        for mol_name, mol_result in results.items():
            if mol_result:
                symbols = ''.join(mol_result.get('symbols', []))
                f.write(f"{mol_name},{symbols},Quantum ESPRESSO (ONCVPSP PBE),"
                       f"{mol_result['equilibrium_distance']:.4f},"
                       f"{mol_result['vibrational_frequency_cm1']:.2f},"
                       f"{mol_result.get('calculation_time', 0):.1f}\n")
    
    print(f"✓ Results saved to {csv_file}")

def compare_with_reference(results, config):
    """Compare with reference values from NIST."""
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
        
        dist_err = abs(res['equilibrium_distance'] - ref['d_eq']) / ref['d_eq'] * 100
        freq_err = abs(res['vibrational_frequency_cm1'] - ref['freq']) / ref['freq'] * 100 if ref['freq'] > 0 and res['vibrational_frequency_cm1'] > 0 else 999.0
        
        comparisons.append({
            'Molecule': mol_name,
            'd_eq_calc': res['equilibrium_distance'],
            'd_eq_ref': ref['d_eq'],
            'd_eq_error': dist_err,
            'freq_calc': res['vibrational_frequency_cm1'],
            'freq_ref': ref['freq'],
            'freq_error': freq_err
        })
        
        d_eq_marker = "✓" if dist_err < 2 else "⚠" if dist_err < 5 else "✗"
        freq_marker = "✓" if freq_err < 10 else "⚠" if freq_err < 20 else "✗" if freq_err < 999 else "✗"
        
        print(f"{mol_name:<8} {'d_eq (Å)':<15} {res['equilibrium_distance']:<12.4f} {ref['d_eq']:<12.4f} {dist_err:<10.2f} {d_eq_marker}")
        print(f"{mol_name:<8} {'freq (cm⁻¹)':<15} {res['vibrational_frequency_cm1']:<12.2f} {ref['freq']:<12.2f} {freq_err:<10.2f} {freq_marker}")
        print("-"*80)

def main():
    """Main execution function."""
    print("="*80)
    print("Diatomic Molecule Analysis with Quantum ESPRESSO")
    print("Using 1D Scan for Fast Vibrational Frequencies")
    print("="*80)
    
    config = load_config('config_qe.yaml')
    
    print("\n" + "="*60)
    print("OPTIMIZED SETTINGS")
    print("="*60)
    qe_config = config.get('qe', {})
    print(f"  Vibration method: 1D scan along bond")
    print(f"    n_points: {qe_config.get('n_points', 7)} (SCF calculations per molecule)")
    print(f"    delta: {qe_config.get('delta', 0.005)} Å")
    print(f"  vs. traditional 3D Hessian:")
    print(f"    nfree=4: 8 SCF calculations per atom = 16 total")
    print(f"    Speedup: ~2-3x faster")
    print("="*60)
    
    analyzer = QEDiatomicAnalyzer(config)
    
    molecules = config.get('molecules', {})
    results = {}
    
    for mol_name, properties in molecules.items():
        result, atoms = analyzer.analyze_molecule(mol_name, properties)
        if result:
            results[mol_name] = result
            
            output_config = config.get('output', {})
            if output_config.get('save_structures', True) and atoms:
                output_dir = output_config.get('output_dir', 'results_qe')
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
    output_config = config.get('output', {})
    output_dir = output_config.get('output_dir', 'results_qe')
    print(f"  Results saved in: {output_dir}/")
    print("="*80)

if __name__ == "__main__":
    main()
