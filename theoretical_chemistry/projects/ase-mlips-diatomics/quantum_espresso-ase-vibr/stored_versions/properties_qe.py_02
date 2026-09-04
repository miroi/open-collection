#!/usr/bin/env python3
"""
Diatomic molecule analysis with Quantum ESPRESSO
Full vibrational analysis using ASE Vibrations class
Optimized for diatomics with per-molecule logging
"""

import os
import sys
import yaml
import numpy as np
import pandas as pd
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.optimize import BFGS
from ase.vibrations import Vibrations, VibrationsData
from ase.io import write, read
from ase.units import invcm
from datetime import datetime
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
        self.molecules_to_calculate = config.get('molecules_to_calculate', {})
        
        # Build the command with MPI
        self.command = self._build_command()
        
        # Store input data as dictionaries
        self.main_input_data = None
        self.vib_input_data = None
        
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
        os.makedirs('./vib/', exist_ok=True)
        os.makedirs(self.config.get('output', {}).get('output_dir', 'results_qe'), exist_ok=True)
    
    def _setup_calculator(self):
        """Setup main Quantum ESPRESSO calculator."""
        profile = EspressoProfile(
            command=self.command,
            pseudo_dir=self.pseudo_dir,
        )
        
        self.main_input_data = {
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
            input_data=self.main_input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
    
    def _setup_vibration_calculator(self):
        """Setup a separate calculator for vibrations."""
        profile = EspressoProfile(
            command=self.command,
            pseudo_dir=self.pseudo_dir,
        )
        
        self.vib_input_data = {
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
            input_data=self.vib_input_data,
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
    
    def optimize_geometry(self, atoms, mol_name, fmax=0.001, steps=100):
        """Optimize geometry using BFGS with per-molecule naming."""
        traj_file = f'{mol_name}_opt.traj'
        log_file = f'{mol_name}_opt.log'
        
        atoms.set_calculator(self.calc)
        opt = BFGS(atoms, trajectory=traj_file, logfile=log_file)
        opt.run(fmax=fmax, steps=steps)
        return atoms
    
    def get_equilibrium_distance(self, symbols, mol_name, initial_distance=1.2, fmax=0.001, steps=100):
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
        
        opt_atoms = self.optimize_geometry(atoms, mol_name, fmax, steps)
        return opt_atoms.get_distance(0, 1), opt_atoms
    
    def _update_calculator_for_molecule(self, symbols):
        """Update calculator for specific molecule."""
        pseudo_dict = {sym: self.get_pseudopotential(sym) for sym in symbols}
        
        # Update main calculator
        self.main_input_data['ntyp'] = len(symbols)
        
        profile = EspressoProfile(
            command=self.command,
            pseudo_dir=self.pseudo_dir,
        )
        
        self.calc = Espresso(
            profile=profile,
            pseudopotentials=pseudo_dict,
            input_data=self.main_input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
        
        # Update vibration calculator
        self.vib_input_data['ntyp'] = len(symbols)
        
        self.vib_calc = Espresso(
            profile=profile,
            pseudopotentials=pseudo_dict,
            input_data=self.vib_input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
    
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
    
    def calculate_vibrational_frequency_full(self, atoms, mol_name, delta=0.005, nfree=2):
        """
        Calculate vibrational frequencies using ASE Vibrations class.
        This does a full 3D Hessian calculation for all atoms.
        For diatomics, we only vibrate the two atoms.
        """
        try:
            print(f"    Using ASE Vibrations with delta={delta}, nfree={nfree}")
            
            # Set the vibration calculator
            atoms.set_calculator(self.vib_calc)
            
            # Create Vibrations object - only vibrate atoms 0 and 1
            vib_name = f'vib/{mol_name}'
            vib = Vibrations(
                atoms, 
                indices=[0, 1],  # Only vibrate the two atoms
                name=vib_name,
                delta=delta,
                nfree=nfree
            )
            
            # Run the calculations
            print(f"    Running {2 * nfree * 2} displacement calculations...")
            vib.run()
            
            # Get frequencies in cm^-1
            frequencies = vib.get_frequencies()
            
            # Filter out near-zero frequencies (translations and rotations)
            valid_freqs = [f for f in frequencies if abs(f) > 1.0]
            
            if len(valid_freqs) > 0:
                # For diatomic, the first non-zero frequency is the stretching mode
                freq_cm1 = abs(valid_freqs[0])
                print(f"    Found {len(valid_freqs)} non-zero modes")
                print(f"    Stretching mode: {freq_cm1:.2f} cm⁻¹")
                
                # Get summary
                vib.summary()
                
                # Write the mode to a trajectory file for visualization
                try:
                    vib.write_mode(-1)  # Write last mode
                    print(f"    Mode written to {vib_name}.8.traj")
                except:
                    pass
                
                # Get detailed vibrational data
                vib_data = vib.get_vibrations()
                energies = vib_data.get_energies()
                zero_point = vib_data.get_zero_point_energy()
                print(f"    Zero-point energy: {zero_point:.4f} eV")
                
            else:
                freq_cm1 = 0.0
                print(f"    No non-zero modes found")
            
            # Clean up
            try:
                vib.clean()
            except:
                pass
            
            return freq_cm1
            
        except Exception as e:
            print(f"  Error in full vibration calculation: {e}")
            return 0.0
    
    def calculate_vibrational_frequency_1d(self, atoms, mol_name, delta=0.005, n_points=7):
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
            r_values = np.linspace(r_eq - delta, r_eq + delta, n_points)
            energies = []
            
            print(f"    Scanning bond length from {r_values[0]:.4f} to {r_values[-1]:.4f} Å")
            
            # Get the cell from the optimized atoms
            cell = atoms.get_cell()
            
            for i, r in enumerate(r_values):
                # Create temporary atoms with this bond length
                temp_atoms = Atoms(symbols, positions=[(0, 0, 0), (r, 0, 0)])
                temp_atoms.set_cell(cell)
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
                if n_points < 11:
                    print(f"    Retrying with more points...")
                    return self.calculate_vibrational_frequency_1d(atoms, mol_name, delta, n_points + 2)
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
            if not self.check_pseudopotential_exists(sym):
                print(f"  ✗ Pseudopotential for {sym} not found")
                return None, None
        
        # Update calculator for this molecule
        self._update_calculator_for_molecule(unique_symbols)
        
        # Get equilibrium distance with per-molecule naming
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
        
        # Choose frequency calculation method
        vib_method = self.qe_config.get('vibration_method', '1d')
        
        print(f"  Calculating vibrational frequency using method: {vib_method}")
        delta = self.qe_config.get('delta', 0.005)
        
        import time
        start_time = time.time()
        
        if vib_method == 'full':
            # Use full ASE Vibrations class
            nfree = self.qe_config.get('nfree', 2)
            freq_cm1 = self.calculate_vibrational_frequency_full(opt_atoms, molecule_name, delta, nfree)
        else:
            # Use 1D scan (default, faster)
            n_points = self.qe_config.get('n_points', 7)
            freq_cm1 = self.calculate_vibrational_frequency_1d(opt_atoms, molecule_name, delta, n_points)
        
        elapsed = time.time() - start_time
        
        if freq_cm1 > 0:
            print(f"  ✓ Vibrational frequency: {freq_cm1:.2f} cm⁻¹ (took {elapsed:.1f} seconds)")
        else:
            print(f"  ✗ Frequency calculation failed")
        
        # Get experimental reference values
        ref_data = properties.get('reference', {})
        exp_d_eq = ref_data.get('d_eq', None)
        exp_freq = ref_data.get('freq', None)
        ref_source = ref_data.get('source', 'Unknown')
        
        # Calculate errors if experimental values exist
        d_eq_error = abs(eq_dist - exp_d_eq) / exp_d_eq * 100 if exp_d_eq else None
        freq_error = abs(freq_cm1 - exp_freq) / exp_freq * 100 if exp_freq and freq_cm1 > 0 else None
        
        results = {
            'molecule': molecule_name,
            'symbols': symbols,
            'calculator': 'Quantum ESPRESSO (ONCVPSP PBE)',
            'equilibrium_distance': eq_dist,
            'exp_equilibrium_distance': exp_d_eq,
            'd_eq_error_percent': d_eq_error,
            'vibrational_frequency_cm1': freq_cm1,
            'exp_vibrational_frequency': exp_freq,
            'freq_error_percent': freq_error,
            'reference_source': ref_source,
            'vibration_method': vib_method,
            'calculation_time': elapsed,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Print comparison with experiment
        print(f"\n  Comparison with experiment:")
        if exp_d_eq:
            print(f"    Bond length: {eq_dist:.4f} Å (exp: {exp_d_eq:.4f} Å, error: {d_eq_error:.2f}%)")
        if exp_freq and freq_cm1 > 0:
            print(f"    Frequency: {freq_cm1:.2f} cm⁻¹ (exp: {exp_freq:.2f} cm⁻¹, error: {freq_error:.2f}%)")
        
        return results, opt_atoms

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
    
    # Save detailed summary as CSV
    csv_file = os.path.join(output_dir, 'summary.csv')
    with open(csv_file, 'w') as f:
        # Write header with all fields
        f.write("Molecule,Symbols,Calculator,d_eq_calc(Å),d_eq_exp(Å),d_eq_error(%),"
                "freq_calc(cm⁻¹),freq_exp(cm⁻¹),freq_error(%),"
                "Reference,Method,Time(s),Timestamp\n")
        
        for mol_name, mol_result in results.items():
            if mol_result:
                symbols = ''.join(mol_result.get('symbols', []))
                d_eq_exp = mol_result.get('exp_equilibrium_distance', 'N/A')
                d_eq_error = f"{mol_result.get('d_eq_error_percent', 0):.2f}" if mol_result.get('d_eq_error_percent') is not None else 'N/A'
                freq_exp = mol_result.get('exp_vibrational_frequency', 'N/A')
                freq_error = f"{mol_result.get('freq_error_percent', 0):.2f}" if mol_result.get('freq_error_percent') is not None else 'N/A'
                
                f.write(f"{mol_name},{symbols},Quantum ESPRESSO (ONCVPSP PBE),"
                       f"{mol_result['equilibrium_distance']:.4f},{d_eq_exp},{d_eq_error},"
                       f"{mol_result['vibrational_frequency_cm1']:.2f},{freq_exp},{freq_error},"
                       f"{mol_result.get('reference_source', 'N/A')},"
                       f"{mol_result.get('vibration_method', 'N/A')},"
                       f"{mol_result.get('calculation_time', 0):.1f},"
                       f"{mol_result.get('timestamp', 'N/A')}\n")
    
    print(f"✓ Results saved to {csv_file}")
    
    # Create a human-readable summary
    summary_file = os.path.join(output_dir, 'summary.txt')
    with open(summary_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("DIATOMIC MOLECULE ANALYSIS SUMMARY\n")
        f.write("="*80 + "\n\n")
        
        for mol_name, mol_result in results.items():
            if mol_result:
                f.write(f"Molecule: {mol_name}\n")
                f.write(f"  Symbols: {mol_result.get('symbols', [])}\n")
                f.write(f"  Equilibrium bond length: {mol_result['equilibrium_distance']:.4f} Å\n")
                
                exp_d_eq = mol_result.get('exp_equilibrium_distance')
                if exp_d_eq:
                    error = mol_result.get('d_eq_error_percent', 0)
                    f.write(f"  Experimental bond length: {exp_d_eq:.4f} Å (error: {error:.2f}%)\n")
                
                f.write(f"  Vibrational frequency: {mol_result['vibrational_frequency_cm1']:.2f} cm⁻¹\n")
                
                exp_freq = mol_result.get('exp_vibrational_frequency')
                if exp_freq:
                    error = mol_result.get('freq_error_percent', 0)
                    f.write(f"  Experimental frequency: {exp_freq:.2f} cm⁻¹ (error: {error:.2f}%)\n")
                
                f.write(f"  Reference source: {mol_result.get('reference_source', 'N/A')}\n")
                f.write(f"  Vibration method: {mol_result.get('vibration_method', 'N/A')}\n")
                f.write(f"  Calculation time: {mol_result.get('calculation_time', 0):.1f} seconds\n")
                f.write(f"  Timestamp: {mol_result.get('timestamp', 'N/A')}\n")
                f.write("-"*40 + "\n")
    
    print(f"✓ Human-readable summary saved to {summary_file}")

def compare_with_reference(results, config):
    """Compare with reference values from NIST."""
    print("\n" + "="*80)
    print("COMPARISON WITH EXPERIMENTAL VALUES")
    print("="*80)
    print(f"{'Molecule':<10} {'Property':<15} {'Calculated':<15} {'Experimental':<15} {'Error (%)':<12} {'Status'}")
    print("-"*80)
    
    comparisons = []
    
    for mol_name, res in results.items():
        if res is None:
            continue
        
        freq = res['vibrational_frequency_cm1']
        exp_d_eq = res.get('exp_equilibrium_distance')
        exp_freq = res.get('exp_vibrational_frequency')
        
        # Bond length comparison
        if exp_d_eq:
            dist_err = abs(res['equilibrium_distance'] - exp_d_eq) / exp_d_eq * 100
            d_eq_marker = "✓" if dist_err < 2 else "⚠" if dist_err < 5 else "✗"
            print(f"{mol_name:<10} {'d_eq (Å)':<15} {res['equilibrium_distance']:<15.4f} {exp_d_eq:<15.4f} {dist_err:<12.2f} {d_eq_marker}")
        
        # Frequency comparison
        if exp_freq and freq > 0:
            freq_err = abs(freq - exp_freq) / exp_freq * 100
            freq_marker = "✓" if freq_err < 10 else "⚠" if freq_err < 20 else "✗"
            print(f"{mol_name:<10} {'freq (cm⁻¹)':<15} {freq:<15.2f} {exp_freq:<15.2f} {freq_err:<12.2f} {freq_marker}")
        
        print("-"*80)
    
    # Summary statistics
    print("\n" + "="*80)
    print("SUMMARY STATISTICS")
    print("="*80)
    
    valid_results = [r for r in results.values() if r is not None]
    
    if valid_results:
        # Bond length errors
        d_eq_errors = [r.get('d_eq_error_percent') for r in valid_results if r.get('d_eq_error_percent') is not None]
        if d_eq_errors:
            avg_dist_err = np.mean(d_eq_errors)
            max_dist_err = np.max(d_eq_errors)
            min_dist_err = np.min(d_eq_errors)
            print(f"\n  Bond Length Errors:")
            print(f"    Average: {avg_dist_err:.2f}%")
            print(f"    Maximum: {max_dist_err:.2f}%")
            print(f"    Minimum: {min_dist_err:.2f}%")
        
        # Frequency errors
        freq_errors = [r.get('freq_error_percent') for r in valid_results if r.get('freq_error_percent') is not None and r.get('freq_error_percent') < 1000]
        if freq_errors:
            avg_freq_err = np.mean(freq_errors)
            max_freq_err = np.max(freq_errors)
            min_freq_err = np.min(freq_errors)
            print(f"\n  Frequency Errors:")
            print(f"    Average: {avg_freq_err:.2f}%")
            print(f"    Maximum: {max_freq_err:.2f}%")
            print(f"    Minimum: {min_freq_err:.2f}%")
        
        # Overall assessment
        if d_eq_errors and freq_errors:
            if avg_dist_err < 2 and avg_freq_err < 10:
                print("\n  ✓ Excellent agreement with experimental values")
            elif avg_dist_err < 5 and avg_freq_err < 20:
                print("\n  ✓ Good agreement with experimental values")
            else:
                print("\n  ⚠ Moderate agreement - consider improving convergence parameters")

def main():
    """Main execution function."""
    print("="*80)
    print("Diatomic Molecule Analysis with Quantum ESPRESSO")
    print("Using ASE Vibrations for Full Vibrational Analysis")
    print("="*80)
    
    config = load_config('config_qe.yaml')
    
    print("\n" + "="*60)
    print("CALCULATION SETTINGS")
    print("="*60)
    qe_config = config.get('qe', {})
    vib_method = qe_config.get('vibration_method', '1d')
    
    print(f"  Vibration method: {vib_method}")
    if vib_method == 'full':
        print(f"    nfree: {qe_config.get('nfree', 2)}")
    else:
        print(f"    n_points: {qe_config.get('n_points', 7)}")
    print(f"  delta: {qe_config.get('delta', 0.005)} Å")
    
    # Show which molecules will be calculated
    molecules_to_calc = config.get('molecules_to_calculate', {})
    selected_molecules = [m for m, enabled in molecules_to_calc.items() if enabled]
    print(f"\n  Molecules to calculate: {', '.join(selected_molecules) if selected_molecules else 'None'}")
    print("="*60)
    
    analyzer = QEDiatomicAnalyzer(config)
    
    molecules = config.get('molecules', {})
    results = {}
    
    for mol_name, properties in molecules.items():
        # Check if this molecule should be calculated
        if not molecules_to_calc.get(mol_name, False):
            print(f"\n⏭ Skipping {mol_name} (disabled in config)")
            continue
        
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
    print("\n  Files generated:")
    print(f"    - {output_dir}/summary.csv: All calculated properties with experimental comparison")
    print(f"    - {output_dir}/summary.txt: Human-readable summary")
    print(f"    - {output_dir}/*_qe_opt.xyz: Optimized structures")
    print("    - *_opt.traj: Per-molecule optimization trajectories")
    print("    - *_opt.log: Per-molecule optimization logs")
    if vib_method == 'full':
        print("    - vib/*.json: Vibration displacement files")
        print("    - vib/*.traj: Vibrational mode trajectories")
    print("="*80)

if __name__ == "__main__":
    main()
