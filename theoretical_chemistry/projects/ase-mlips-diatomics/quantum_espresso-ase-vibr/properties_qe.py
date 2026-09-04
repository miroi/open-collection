#!/usr/bin/env python3
"""
Diatomic molecule analysis with Quantum ESPRESSO
Full vibrational analysis using ASE Vibrations class
Supports 1D scan, X-Only Hessian, and Full Hessian methods
"""

import os
import sys
import yaml
import numpy as np
import pandas as pd
import time
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.optimize import BFGS
from ase.vibrations import Vibrations, VibrationsData
from ase.constraints import FixAtoms, FixInternals
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
        
        # Vibration method
        self.vibration_method = self.qe_config.get('vibration_method', 'xonly')
        
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
    
    # ========================================================================
    # VIBRATION METHODS
    # ========================================================================
    
    def calculate_vibrational_frequency_1d(self, atoms, mol_name, delta=0.005, n_points=7):
        """
        Method 1: 1D Scan along bond (fastest)
        Fits a quadratic to the PES along the bond direction.
        """
        try:
            print(f"    Using 1D scan with n_points={n_points}, delta={delta}")
            
            symbols = atoms.get_chemical_symbols()
            r_eq = atoms.get_distance(0, 1)
            
            r_values = np.linspace(r_eq - delta, r_eq + delta, n_points)
            energies = []
            
            print(f"    Scanning bond length from {r_values[0]:.4f} to {r_values[-1]:.4f} Å")
            
            cell = atoms.get_cell()
            
            for i, r in enumerate(r_values):
                temp_atoms = Atoms(symbols, positions=[(0, 0, 0), (r, 0, 0)])
                temp_atoms.set_cell(cell)
                temp_atoms.set_pbc(True)
                temp_atoms.set_calculator(self.vib_calc)
                
                energy = temp_atoms.get_potential_energy()
                energies.append(energy)
                
                print(f"      Point {i+1}/{n_points}: r = {r:.4f} Å, E = {energy:.6f} eV")
            
            r_shifted = r_values - r_eq
            coeffs = np.polyfit(r_shifted, energies, 2)
            
            second_deriv = 2 * coeffs[0]
            
            if second_deriv <= 0:
                print(f"    Warning: Negative second derivative ({second_deriv:.6f} eV/A^2)")
                if n_points < 11:
                    print(f"    Retrying with more points...")
                    return self.calculate_vibrational_frequency_1d(atoms, mol_name, delta, n_points + 2)
                return 0.0
            
            masses = self._get_masses(symbols)
            reduced_mass_amu = (masses[0] * masses[1]) / (masses[0] + masses[1])
            reduced_mass_kg = reduced_mass_amu * 1.66054e-27
            
            k_Nm = second_deriv * 160.2177
            c_cm_s = 2.99792458e10
            freq_cm1 = 1/(2 * np.pi * c_cm_s) * np.sqrt(k_Nm / reduced_mass_kg)
            
            print(f"    Force constant: {k_Nm:.2f} N/m")
            print(f"    Reduced mass: {reduced_mass_amu:.4f} amu")
            print(f"    1D scan frequency: {abs(freq_cm1):.2f} cm⁻¹")
            
            return abs(freq_cm1)
            
        except Exception as e:
            print(f"  Error in 1D frequency calculation: {e}")
            return 0.0
    
    def calculate_vibrational_frequency_xonly(self, atoms, mol_name, delta=0.005, nfree=2):
        """
        Method 2: X-Only Hessian using ASE Vibrations class.
        Uses FixAtoms to freeze all atoms, then manually displaces along x.
        This is the correct ASE way to do X-Only Hessian.
        """
        print(f"    Using X-Only Hessian with delta={delta}, nfree={nfree}")
        print(f"    Only displacing along x-axis (bond direction)")
        
        # Save original constraints
        original_constraints = atoms.constraints.copy()
        
        # Method: Use FixAtoms to freeze all atoms, then manually displace along x
        # This is the correct ASE approach since FixCartesian is deprecated
        
        try:
            # Freeze all atoms first
            from ase.constraints import FixAtoms
            constraint = FixAtoms(indices=[0, 1])
            atoms.set_constraint([constraint])
            
            # Now we manually displace atoms along x and calculate forces
            print(f"    Using manual displacement along x with FixAtoms")
            
            # We'll create a custom calculation by manually displacing atoms
            symbols = atoms.get_chemical_symbols()
            r_eq = atoms.get_distance(0, 1)
            cell = atoms.get_cell()
            
            # Store energies for each displacement
            displacements = []
            energies = []
            
            # Displace atom 0 and atom 1 along x
            for atom_idx in [0, 1]:
                for sign in [-1, 1]:
                    for step in range(1, nfree + 1):
                        displacement = sign * step * delta / nfree
                        
                        # Create a copy and displace along x only
                        temp_atoms = Atoms(symbols, positions=[(0, 0, 0), (r_eq, 0, 0)])
                        temp_atoms.set_cell(cell)
                        temp_atoms.set_pbc(True)
                        
                        # Displace the specific atom
                        pos = temp_atoms.get_positions()
                        pos[atom_idx][0] += displacement
                        temp_atoms.set_positions(pos)
                        
                        temp_atoms.set_calculator(self.vib_calc)
                        energy = temp_atoms.get_potential_energy()
                        
                        displacements.append((atom_idx, displacement))
                        energies.append(energy)
                        
                        print(f"      Atom {atom_idx}, dx = {displacement:.4f} Å, E = {energy:.6f} eV")
            
            # Get equilibrium energy
            temp_atoms = Atoms(symbols, positions=[(0, 0, 0), (r_eq, 0, 0)])
            temp_atoms.set_cell(cell)
            temp_atoms.set_pbc(True)
            temp_atoms.set_calculator(self.vib_calc)
            energy_eq = temp_atoms.get_potential_energy()
            print(f"      Equilibrium: r = {r_eq:.4f} Å, E = {energy_eq:.6f} eV")
            
            # Calculate Hessian from displacements
            # For each atom, compute second derivative from +/- displacements
            hessian_diag = []
            
            for atom_idx in [0, 1]:
                # Get energies for this atom at +/- displacements
                d_plus = None
                e_plus = None
                d_minus = None
                e_minus = None
                
                for disp, energy in zip(displacements, energies):
                    if disp[0] == atom_idx:
                        if disp[1] > 0:
                            d_plus = disp[1]
                            e_plus = energy
                        else:
                            d_minus = abs(disp[1])
                            e_minus = energy
                
                if d_plus is not None and d_minus is not None:
                    # Use the average displacement magnitude
                    d_avg = (d_plus + d_minus) / 2
                    second_deriv = (e_plus + e_minus - 2 * energy_eq) / (d_avg**2)
                    hessian_diag.append(second_deriv)
                    print(f"      Atom {atom_idx}: d_avg = {d_avg:.4f} Å, second_deriv = {second_deriv:.6f} eV/A²")
            
            if len(hessian_diag) == 0:
                print(f"    Warning: No valid Hessian diagonal elements")
                atoms.set_constraint(original_constraints)
                return 0.0
            
            # Take average of the diagonal Hessian elements
            avg_second_deriv = np.mean(hessian_diag)
            
            if avg_second_deriv <= 0:
                print(f"    Warning: Negative second derivative ({avg_second_deriv:.6f} eV/A^2)")
                atoms.set_constraint(original_constraints)
                return 0.0
            
            # Convert to frequency
            masses = self._get_masses(symbols)
            reduced_mass_amu = (masses[0] * masses[1]) / (masses[0] + masses[1])
            reduced_mass_kg = reduced_mass_amu * 1.66054e-27
            
            # Convert eV/A^2 to N/m
            k_Nm = avg_second_deriv * 160.2177
            
            # Frequency in cm^-1
            c_cm_s = 2.99792458e10
            freq_cm1 = 1/(2 * np.pi * c_cm_s) * np.sqrt(k_Nm / reduced_mass_kg)
            
            print(f"\n    {'='*50}")
            print(f"    X-ONLY HESSIAN RESULTS FOR {mol_name}")
            print(f"    {'='*50}")
            print(f"    Force constant: {k_Nm:.2f} N/m")
            print(f"    Reduced mass: {reduced_mass_amu:.4f} amu")
            print(f"    ✓ Stretching mode: {abs(freq_cm1):.2f} cm⁻¹")
            print(f"    {'='*50}")
            
            # Restore original constraints
            atoms.set_constraint(original_constraints)
            
            return abs(freq_cm1)
            
        except Exception as e:
            print(f"  Error in X-Only vibration calculation: {e}")
            print(f"  Falling back to 1D scan method...")
            
            # Restore original constraints
            atoms.set_constraint(original_constraints)
            
            # Fall back to 1D scan
            return self.calculate_vibrational_frequency_1d(atoms, mol_name, delta, 7)
    
    def calculate_vibrational_frequency_full(self, atoms, mol_name, delta=0.005, nfree=2):
        """
        Method 3: Full 3D Hessian using ASE Vibrations class.
        Most accurate but slowest for diatomics.
        """
        try:
            print(f"    Using ASE Vibrations (full Hessian) with delta={delta}, nfree={nfree}")
            
            atoms.set_calculator(self.vib_calc)
            
            vib_name = f'vib/{mol_name}_full'
            vib = Vibrations(
                atoms, 
                indices=[0, 1],
                name=vib_name,
                delta=delta,
                nfree=nfree
            )
            
            total_calcs = 2 * nfree * 3 * 2
            print(f"    Running {total_calcs} displacement calculations (all directions)...")
            vib.run()
            
            frequencies = vib.get_frequencies()
            energies = vib.get_energies()
            
            print(f"\n    {'='*50}")
            print(f"    FULL HESSIAN RESULTS FOR {mol_name}")
            print(f"    {'='*50}")
            print(f"    {'Mode':<6} {'Energy (eV)':<15} {'Frequency (cm⁻¹)':<15} {'Type'}")
            print(f"    {'-'*50}")
            
            stretching_mode = None
            stretching_freq = 0.0
            
            for i, (freq, energy) in enumerate(zip(frequencies, energies)):
                freq_abs = abs(freq)
                energy_abs = abs(energy)
                
                if freq_abs < 1.0:
                    mode_type = "Translation"
                elif freq_abs < 100.0:
                    mode_type = "Rotation"
                else:
                    mode_type = "STRETCHING ✓"
                    if freq_abs > stretching_freq:
                        stretching_freq = freq_abs
                        stretching_mode = i
                
                freq_str = f"{freq:.2f}" if freq_abs > 0.01 else "0.00"
                print(f"    {i:<6} {energy_abs:<15.4f} {freq_str:<15} {mode_type}")
            
            print(f"    {'='*50}")
            
            if stretching_mode is not None:
                print(f"    ✓ Stretching mode: Mode {stretching_mode}, {stretching_freq:.2f} cm⁻¹")
                try:
                    vib.write_mode(stretching_mode)
                    print(f"    Mode written to {vib_name}.{stretching_mode}.traj")
                except:
                    pass
                
                try:
                    vib_data = vib.get_vibrations()
                    zero_point = vib_data.get_zero_point_energy()
                    print(f"    Total zero-point energy: {zero_point:.4f} eV")
                except:
                    pass
            else:
                stretching_freq = 0.0
                print(f"    ⚠ No stretching mode found!")
            
            try:
                vib.clean()
            except:
                pass
            
            return stretching_freq
            
        except Exception as e:
            print(f"  Error in full vibration calculation: {e}")
            return 0.0
    
    def _parse_vibration_methods(self, vib_method):
        """
        Parse the vibration method string and return a list of methods to run.
        """
        method_map = {
            '1d': ['1d'],
            'xonly': ['xonly'],
            'full': ['full'],
            '1d+xonly': ['1d', 'xonly'],
            '1d+full': ['1d', 'full'],
            'xonly+full': ['xonly', 'full'],
            'all': ['1d', 'xonly', 'full']
        }
        
        return method_map.get(vib_method, ['1d'])
    
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
        methods_to_run = self._parse_vibration_methods(vib_method)
        
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
            freq_1d = self.calculate_vibrational_frequency_1d(opt_atoms, molecule_name, delta, n_points)
            elapsed_1d = time.time() - start_time
            
            if freq_1d > 0:
                print(f"    ✓ 1D Scan: {freq_1d:.2f} cm⁻¹ (took {elapsed_1d:.1f}s, {n_points} SCF)")
            freq_results['1d'] = {'freq': freq_1d, 'time': elapsed_1d, 'scf': n_points}
        
        if 'xonly' in methods_to_run:
            print(f"\n  Method 2: X-Only Hessian (ASE Vibrations, only along bond)")
            delta = self.qe_config.get('xonly_settings', {}).get('delta', 0.005)
            nfree = self.qe_config.get('xonly_settings', {}).get('nfree', 2)
            scf_count = 2 * nfree
            
            start_time = time.time()
            freq_xonly = self.calculate_vibrational_frequency_xonly(opt_atoms, molecule_name, delta, nfree)
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
            freq_full = self.calculate_vibrational_frequency_full(opt_atoms, molecule_name, delta, nfree)
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
        
        # Select primary method: prefer xonly, then full, then 1d
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
                
                has_results = False
                if mol_result.get('freq_1d', 0) > 0 or mol_result.get('freq_xonly', 0) > 0 or mol_result.get('freq_full', 0) > 0:
                    f.write(f"  All methods:\n")
                    has_results = True
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
    
    analyzer = QEDiatomicAnalyzer(config)
    
    molecules = config.get('molecules', {})
    results = {}
    
    for mol_name, properties in molecules.items():
        if not molecules_to_calc.get(mol_name, False):
            print(f"\n⏭ Skipping {mol_name} (disabled in config)")
            continue
        
        result, atoms = analyzer.analyze_molecule(mol_name, properties)
        if result:
            results[mol_name] = result
            
            output_config = config.get('output'{})
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
