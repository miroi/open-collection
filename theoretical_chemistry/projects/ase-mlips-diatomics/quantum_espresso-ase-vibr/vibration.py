# =============================================================================
# FILE: vibration.py
# Vibration calculation methods for diatomic molecules.
# =============================================================================

import time
import numpy as np
from ase import Atoms
from ase.vibrations import Vibrations
from ase.constraints import FixAtoms
from utils import get_atomic_masses

class VibrationCalculator:
    """Calculate vibrational frequencies using different methods."""
    
    def __init__(self, vib_calc, qe_config):
        """Initialize with vibration calculator and configuration."""
        self.vib_calc = vib_calc
        self.qe_config = qe_config
    
    def calculate_1d_scan(self, atoms, mol_name, delta=0.001, n_points=9):
        """
        Method 1: 1D Scan along bond (fastest)
        Fits a quadratic to the PES along the bond direction.
        Uses a smaller displacement range for better accuracy.
        """
        try:
            print(f"    Using 1D scan with n_points={n_points}, delta={delta}")
            
            symbols = atoms.get_chemical_symbols()
            r_eq = atoms.get_distance(0, 1)
            
            # Generate symmetric points around equilibrium
            # Points go from r_eq - delta to r_eq + delta
            r_values = np.linspace(r_eq - delta, r_eq + delta, n_points)
            energies = []
            
            print(f"    Scanning bond length from {r_values[0]:.6f} to {r_values[-1]:.6f} Å")
            print(f"    Center: {r_eq:.6f} Å, Range: ±{delta:.6f} Å")
            
            cell = atoms.get_cell()
            
            for i, r in enumerate(r_values):
                temp_atoms = Atoms(symbols, positions=[(0, 0, 0), (r, 0, 0)])
                temp_atoms.set_cell(cell)
                temp_atoms.set_pbc(True)
                temp_atoms.calc = self.vib_calc
                
                energy = temp_atoms.get_potential_energy()
                energies.append(energy)
                
                print(f"      Point {i+1}/{n_points}: r = {r:.6f} Å, E = {energy:.6f} eV")
            
            # Fit to a quadratic polynomial
            r_shifted = r_values - r_eq
            coeffs = np.polyfit(r_shifted, energies, 2)
            
            second_deriv = 2 * coeffs[0]
            
            if second_deriv <= 0:
                print(f"    Warning: Negative second derivative ({second_deriv:.6f} eV/A^2)")
                return 0.0
            
            # Calculate frequency
            masses = get_atomic_masses(symbols)
            reduced_mass_amu = (masses[0] * masses[1]) / (masses[0] + masses[1])
            reduced_mass_kg = reduced_mass_amu * 1.66054e-27
            
            # Convert eV/A^2 to N/m
            k_Nm = second_deriv * 160.2177
            
            # Frequency in cm^-1
            c_cm_s = 2.99792458e10
            freq_cm1 = 1/(2 * np.pi * c_cm_s) * np.sqrt(k_Nm / reduced_mass_kg)
            
            print(f"    Force constant: {k_Nm:.2f} N/m")
            print(f"    Reduced mass: {reduced_mass_amu:.4f} amu")
            print(f"    1D scan frequency: {abs(freq_cm1):.2f} cm⁻¹")
            
            return abs(freq_cm1)
            
        except Exception as e:
            print(f"  Error in 1D frequency calculation: {e}")
            return 0.0
    
    def calculate_1d_scan_refined(self, atoms, mol_name, delta=0.0005, n_points=11):
        """
        Method 1b: Refined 1D Scan with more points and smaller displacement.
        More accurate but slightly slower.
        """
        try:
            print(f"    Using refined 1D scan with n_points={n_points}, delta={delta}")
            
            symbols = atoms.get_chemical_symbols()
            r_eq = atoms.get_distance(0, 1)
            
            # Generate symmetric points around equilibrium
            # Points go from r_eq - delta to r_eq + delta
            r_values = np.linspace(r_eq - delta, r_eq + delta, n_points)
            energies = []
            
            print(f"    Scanning bond length from {r_values[0]:.6f} to {r_values[-1]:.6f} Å")
            print(f"    Center: {r_eq:.6f} Å, Range: ±{delta:.6f} Å")
            
            cell = atoms.get_cell()
            
            for i, r in enumerate(r_values):
                temp_atoms = Atoms(symbols, positions=[(0, 0, 0), (r, 0, 0)])
                temp_atoms.set_cell(cell)
                temp_atoms.set_pbc(True)
                temp_atoms.calc = self.vib_calc
                
                energy = temp_atoms.get_potential_energy()
                energies.append(energy)
                
                print(f"      Point {i+1}/{n_points}: r = {r:.6f} Å, E = {energy:.6f} eV")
            
            # Fit to a quartic polynomial for better accuracy
            r_shifted = r_values - r_eq
            coeffs = np.polyfit(r_shifted, energies, 4)
            
            # Second derivative at r_eq: 2 * coeffs[2] (for quadratic term)
            # For quartic: E = a0 + a1*r + a2*r^2 + a3*r^3 + a4*r^4
            # Second derivative = 2*a2 + 6*a3*r + 12*a4*r^2
            # At r_eq (r=0 in shifted coordinates): second_deriv = 2*a2
            second_deriv = 2 * coeffs[2]
            
            if second_deriv <= 0:
                print(f"    Warning: Negative second derivative ({second_deriv:.6f} eV/A^2)")
                # Fall back to quadratic fit
                coeffs2 = np.polyfit(r_shifted, energies, 2)
                second_deriv = 2 * coeffs2[0]
                if second_deriv <= 0:
                    return 0.0
            
            # Calculate frequency
            masses = get_atomic_masses(symbols)
            reduced_mass_amu = (masses[0] * masses[1]) / (masses[0] + masses[1])
            reduced_mass_kg = reduced_mass_amu * 1.66054e-27
            
            k_Nm = second_deriv * 160.2177
            c_cm_s = 2.99792458e10
            freq_cm1 = 1/(2 * np.pi * c_cm_s) * np.sqrt(k_Nm / reduced_mass_kg)
            
            print(f"    Force constant: {k_Nm:.2f} N/m")
            print(f"    Reduced mass: {reduced_mass_amu:.4f} amu")
            print(f"    Refined 1D scan frequency: {abs(freq_cm1):.2f} cm⁻¹")
            
            return abs(freq_cm1)
            
        except Exception as e:
            print(f"  Error in refined 1D frequency calculation: {e}")
            return 0.0
    
    def calculate_xonly_hessian(self, atoms, mol_name, delta=0.001, nfree=2):
        """
        Method 2: X-Only Hessian using manual displacement along x.
        Uses FixAtoms to freeze atoms, then manually displaces along x.
        """
        print(f"    Using X-Only Hessian with delta={delta}, nfree={nfree}")
        print(f"    Only displacing along x-axis (bond direction)")
        
        # Save original constraints
        original_constraints = atoms.constraints.copy()
        
        try:
            # Freeze all atoms
            constraint = FixAtoms(indices=[0, 1])
            atoms.set_constraint([constraint])
            
            print(f"    Using manual displacement along x with FixAtoms")
            
            # Get molecule info
            symbols = atoms.get_chemical_symbols()
            r_eq = atoms.get_distance(0, 1)
            cell = atoms.get_cell()
            
            # Store energies for each displacement
            displacements = []
            energies = []
            
            # Use smaller displacement steps for better accuracy
            step_size = delta / (nfree * 2)
            
            # Displace atom 0 and atom 1 along x
            for atom_idx in [0, 1]:
                for sign in [-1, 1]:
                    for step in range(1, nfree + 1):
                        displacement = sign * step * step_size
                        
                        # Create a copy and displace along x only
                        temp_atoms = Atoms(symbols, positions=[(0, 0, 0), (r_eq, 0, 0)])
                        temp_atoms.set_cell(cell)
                        temp_atoms.set_pbc(True)
                        
                        # Displace the specific atom
                        pos = temp_atoms.get_positions()
                        pos[atom_idx][0] += displacement
                        temp_atoms.set_positions(pos)
                        
                        temp_atoms.calc = self.vib_calc
                        energy = temp_atoms.get_potential_energy()
                        
                        displacements.append((atom_idx, displacement))
                        energies.append(energy)
                        
                        print(f"      Atom {atom_idx}, dx = {displacement:.6f} Å, E = {energy:.6f} eV")
            
            # Get equilibrium energy
            temp_atoms = Atoms(symbols, positions=[(0, 0, 0), (r_eq, 0, 0)])
            temp_atoms.set_cell(cell)
            temp_atoms.set_pbc(True)
            temp_atoms.calc = self.vib_calc
            energy_eq = temp_atoms.get_potential_energy()
            print(f"      Equilibrium: r = {r_eq:.6f} Å, E = {energy_eq:.6f} eV")
            
            # Calculate Hessian from displacements
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
                    d_avg = (d_plus + d_minus) / 2
                    second_deriv = (e_plus + e_minus - 2 * energy_eq) / (d_avg**2)
                    hessian_diag.append(second_deriv)
                    print(f"      Atom {atom_idx}: d_avg = {d_avg:.6f} Å, second_deriv = {second_deriv:.6f} eV/A²")
            
            if len(hessian_diag) == 0:
                print(f"    Warning: No valid Hessian diagonal elements")
                atoms.set_constraint(original_constraints)
                return 0.0
            
            avg_second_deriv = np.mean(hessian_diag)
            
            if avg_second_deriv <= 0:
                print(f"    Warning: Negative second derivative ({avg_second_deriv:.6f} eV/A^2)")
                atoms.set_constraint(original_constraints)
                return 0.0
            
            # Convert to frequency
            masses = get_atomic_masses(symbols)
            reduced_mass_amu = (masses[0] * masses[1]) / (masses[0] + masses[1])
            reduced_mass_kg = reduced_mass_amu * 1.66054e-27
            
            k_Nm = avg_second_deriv * 160.2177
            c_cm_s = 2.99792458e10
            freq_cm1 = 1/(2 * np.pi * c_cm_s) * np.sqrt(k_Nm / reduced_mass_kg)
            
            print(f"\n    {'='*50}")
            print(f"    X-ONLY HESSIAN RESULTS FOR {mol_name}")
            print(f"    {'='*50}")
            print(f"    Force constant: {k_Nm:.2f} N/m")
            print(f"    Reduced mass: {reduced_mass_amu:.4f} amu")
            print(f"    ✓ Stretching mode: {abs(freq_cm1):.2f} cm⁻¹")
            print(f"    {'='*50}")
            
            atoms.set_constraint(original_constraints)
            return abs(freq_cm1)
            
        except Exception as e:
            print(f"  Error in X-Only vibration calculation: {e}")
            print(f"  Falling back to refined 1D scan method...")
            atoms.set_constraint(original_constraints)
            # Get refined parameters from config
            refined_delta = self.qe_config.get('1d_settings', {}).get('refined_delta', 0.0005)
            refined_n_points = self.qe_config.get('1d_settings', {}).get('refined_n_points', 11)
            return self.calculate_1d_scan_refined(atoms, mol_name, refined_delta, refined_n_points)
    
    def calculate_full_hessian(self, atoms, mol_name, delta=0.001, nfree=2):
        """
        Method 3: Full 3D Hessian using ASE Vibrations class.
        Most accurate but slowest for diatomics.
        """
        try:
            print(f"    Using ASE Vibrations (full Hessian) with delta={delta}, nfree={nfree}")
            
            atoms.calc = self.vib_calc
            
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
