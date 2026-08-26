#!/usr/bin/env python3
"""
ASE script for geometry optimization of Cu7 cluster comparing EMT and MACE calculators
with harmonic vibrational frequency analysis for both
"""

from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write
from ase.vibrations import Vibrations
import numpy as np
import os
import time
import warnings
from pathlib import Path

# Try to import MACE
try:
    from mace.calculators import MACECalculator
    MACE_AVAILABLE = True
except ImportError:
    try:
        from mace.calculators import mace_mp
        MACE_AVAILABLE = True
    except ImportError:
        MACE_AVAILABLE = False
        print("MACE not installed. Install with: pip install mace-torch")

# Create Cu7 cluster
def create_pentagonal_bipyramid():
    """Create a pentagonal bipyramid Cu7 cluster (5 equatorial + 2 axial)"""
    positions = []
    
    # Pentagon in xy-plane (5 atoms)
    radius = 2.5  # Å
    for i in range(5):
        angle = 2 * np.pi * i / 5
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        positions.append([x, y, 0.0])
    
    # Two axial atoms (top and bottom)
    positions.append([0.0, 0.0, 2.5])
    positions.append([0.0, 0.0, -2.5])
    
    return positions

def setup_calculator(calc_type='EMT', device='cpu', model='medium'):
    """
    Setup the calculator based on user choice
    """
    if calc_type.upper() == 'EMT':
        return EMT()
    
    elif calc_type.upper() == 'MACE':
        if not MACE_AVAILABLE:
            raise ImportError("MACE is not available")
        
        # Try different MACE import methods
        try:
            # Try MACECalculator first
            from mace.calculators import MACECalculator
            
            # Check for model in common locations
            model_paths = [
                Path.home() / '.cache' / 'mace' / 'mace_mp_medium.model',
                Path.home() / '.cache' / 'mace' / 'macempa0mediummodel',
                Path.home() / '.cache' / 'mace' / 'mace_mp_small.model',
                Path.home() / '.cache' / 'mace' / 'mace_mp_large.model'
            ]
            
            model_path = None
            for path in model_paths:
                if path.exists():
                    model_path = str(path)
                    break
            
            if model_path is None:
                # Try to download model if not found
                print("  Model not found locally. Trying to download...")
                try:
                    from mace.calculators import mace_mp
                    return mace_mp(model='medium', device=device)
                except:
                    raise FileNotFoundError("No MACE model found. Please download first.")
            
            print(f"  Using MACE model: {model_path}")
            return MACECalculator(model_path=model_path, device=device)
            
        except (ImportError, AttributeError):
            # Fallback to mace_mp
            try:
                from mace.calculators import mace_mp
                return mace_mp(model='medium', device=device)
            except:
                raise ImportError("Could not initialize MACE calculator")
    
    else:
        raise ValueError(f"Unknown calculator type: {calc_type}")

def optimize_cluster(atoms, calculator, label, max_steps=100, fmax=0.05):
    """Optimize cluster with given calculator"""
    
    print(f"\n{'='*60}")
    print(f"Optimizing Cu7 with {label} calculator")
    print(f"{'='*60}")
    
    # Create a copy of atoms with the calculator
    atoms_copy = atoms.copy()
    atoms_copy.calc = calculator
    
    # Get initial energy
    try:
        initial_energy = atoms_copy.get_potential_energy()
        print(f"Initial energy: {initial_energy:.6f} eV")
    except Exception as e:
        print(f"Could not calculate initial energy: {e}")
        initial_energy = None
    
    # Setup optimizer
    traj_file = f'cu7_optimization_{label.lower()}.traj'
    log_file = f'cu7_optimization_{label.lower()}.log'
    optimizer = BFGS(atoms_copy, trajectory=traj_file, logfile=log_file)
    
    # Run optimization
    start_time = time.time()
    optimizer.run(fmax=fmax, steps=max_steps)
    optimization_time = time.time() - start_time
    
    # Get final properties
    final_energy = atoms_copy.get_potential_energy()
    final_forces = atoms_copy.get_forces()
    
    print(f"\nOptimization complete!")
    print(f"  Final energy: {final_energy:.6f} eV")
    print(f"  Energy change: {(initial_energy - final_energy) if initial_energy is not None else 'N/A':.6f} eV")
    print(f"  Maximum force: {np.max(np.abs(final_forces)):.6f} eV/Å")
    print(f"  Optimization steps: {optimizer.get_number_of_steps()}")
    print(f"  Converged: {optimizer.converged()}")
    print(f"  Time: {optimization_time:.2f} seconds")
    
    return atoms_copy, initial_energy, final_energy, final_forces, optimization_time

def calculate_vibrations(atoms, label, delta=0.01):
    """Calculate vibrational frequencies"""
    
    print(f"\nCalculating vibrational frequencies for {label}...")
    
    # Create vibrations object
    vib_name = f'cu7_vibrations_{label.lower()}'
    vib = Vibrations(atoms, name=vib_name, delta=delta)
    
    try:
        # Run vibrational calculation
        start_time = time.time()
        vib.run()
        vib_time = time.time() - start_time
        
        # Get frequencies
        frequencies = vib.get_frequencies()
        freqs_real = np.real(frequencies)
        freqs_imag = np.imag(frequencies)
        
        # Get meaningful vibrations (excluding translations/rotations)
        meaningful_freqs = freqs_real[freqs_real > 10]
        
        # Calculate zero-point energy
        zero_point_energy = 0.0
        if len(meaningful_freqs) > 0:
            zero_point_energy = 0.5 * np.sum(meaningful_freqs) * 0.123984  # meV
        
        # Write modes for visualization
        vib.write_mode(-1)
        
        # Save frequencies to file
        freq_file = f'cu7_frequencies_{label.lower()}.txt'
        with open(freq_file, 'w') as f:
            f.write(f"Cu7 Vibrational Frequencies ({label} calculator)\n")
            f.write("=" * 60 + "\n\n")
            f.write("Mode    Frequency (cm⁻¹)    Energy (meV)    Type\n")
            f.write("-" * 55 + "\n")
            
            for i, freq in enumerate(freqs_real):
                freq_meV = freq * 0.123984
                if abs(freq) < 1.0:
                    mode_type = "Translation"
                elif abs(freq) < 10.0:
                    mode_type = "Rotation"
                elif abs(freq) < 50.0:
                    mode_type = "Low-frequency"
                elif abs(freq) < 100.0:
                    mode_type = "Bending/Breathing"
                elif abs(freq) < 200.0:
                    mode_type = "Deformation"
                else:
                    mode_type = "Stretching"
                
                f.write(f"{i+1:4d}    {freq:10.2f}        {freq_meV:8.2f}        {mode_type}\n")
            
            if len(meaningful_freqs) > 0:
                f.write("\n" + "-" * 55 + "\n")
                f.write(f"Zero-point energy: {zero_point_energy:.2f} meV ({zero_point_energy/1000:.6f} eV)\n")
            f.write(f"Number of modes: {len(frequencies)}\n")
        
        result = {
            'frequencies': frequencies,
            'freqs_real': freqs_real,
            'freqs_imag': freqs_imag,
            'meaningful_freqs': meaningful_freqs,
            'zero_point_energy': zero_point_energy,
            'vib_time': vib_time,
            'success': True
        }
        
        print(f"  ✓ Vibrational calculation complete")
        print(f"  ✓ Frequencies saved to: {freq_file}")
        print(f"  ✓ Modes saved to: {vib_name}.*.traj")
        print(f"  ✓ Time: {vib_time:.2f} seconds")
        
        return result
        
    except Exception as e:
        print(f"  ✗ Vibrational calculation failed: {e}")
        return {'success': False, 'error': str(e)}

def analyze_bonds(atoms, label):
    """Analyze bond lengths and structure"""
    
    positions = atoms.positions
    distances = atoms.get_all_distances()
    
    # Find bonds
    bonds = []
    for i in range(len(atoms)):
        for j in range(i+1, len(atoms)):
            if distances[i][j] < 3.5 and distances[i][j] > 0.1:
                bonds.append((i, j, distances[i][j]))
    
    bonds.sort(key=lambda x: x[2])
    
    # Calculate coordination numbers
    coord_numbers = []
    for i in range(len(atoms)):
        coord = sum(1 for j in range(len(atoms)) if i != j and distances[i][j] < 3.0)
        coord_numbers.append(coord)
    
    return {
        'bonds': bonds,
        'coord_numbers': coord_numbers,
        'avg_bond': np.mean([b[2] for b in bonds]) if bonds else 0,
        'min_bond': min([b[2] for b in bonds]) if bonds else 0,
        'max_bond': max([b[2] for b in bonds]) if bonds else 0,
        'num_bonds': len(bonds)
    }

def compare_results(emt_result, mace_result):
    """Compare EMT and MACE results"""
    
    print("\n" + "=" * 60)
    print("COMPARISON: EMT vs MACE")
    print("=" * 60)
    
    # Extract results
    emt_atoms, emt_initial, emt_final, emt_forces, emt_time = emt_result
    mace_atoms, mace_initial, mace_final, mace_forces, mace_time = mace_result
    
    # Energy comparison
    print("\n1. ENERGY COMPARISON:")
    print("-" * 40)
    print(f"  EMT initial:  {emt_initial:10.6f} eV")
    print(f"  MACE initial: {mace_initial:10.6f} eV")
    print(f"  Difference:   {abs(emt_initial - mace_initial):10.6f} eV")
    print()
    print(f"  EMT final:    {emt_final:10.6f} eV")
    print(f"  MACE final:   {mace_final:10.6f} eV")
    print(f"  Difference:   {abs(emt_final - mace_final):10.6f} eV")
    print()
    print(f"  EMT energy change:  {emt_initial - emt_final:10.6f} eV")
    print(f"  MACE energy change: {mace_initial - mace_final:10.6f} eV")
    print(f"  Difference:         {abs((emt_initial - emt_final) - (mace_initial - mace_final)):10.6f} eV")
    
    # Structure comparison
    print("\n2. STRUCTURE COMPARISON:")
    print("-" * 40)
    
    # Calculate RMSD between structures
    rmsd = np.sqrt(np.mean((emt_atoms.positions - mace_atoms.positions)**2))
    print(f"  RMSD between structures: {rmsd:.4f} Å")
    
    # Bond length comparison
    emt_bonds = analyze_bonds(emt_atoms, 'EMT')
    mace_bonds = analyze_bonds(mace_atoms, 'MACE')
    
    print(f"\n  EMT bond lengths:")
    print(f"    Average: {emt_bonds['avg_bond']:.4f} Å")
    print(f"    Min:     {emt_bonds['min_bond']:.4f} Å")
    print(f"    Max:     {emt_bonds['max_bond']:.4f} Å")
    
    print(f"\n  MACE bond lengths:")
    print(f"    Average: {mace_bonds['avg_bond']:.4f} Å")
    print(f"    Min:     {mace_bonds['min_bond']:.4f} Å")
    print(f"    Max:     {mace_bonds['max_bond']:.4f} Å")
    
    print(f"\n  Bond length differences:")
    print(f"    Average: {abs(emt_bonds['avg_bond'] - mace_bonds['avg_bond']):.4f} Å")
    print(f"    Min:     {abs(emt_bonds['min_bond'] - mace_bonds['min_bond']):.4f} Å")
    print(f"    Max:     {abs(emt_bonds['max_bond'] - mace_bonds['max_bond']):.4f} Å")
    
    # Coordination numbers
    print(f"\n  Coordination numbers:")
    print(f"    EMT:  {emt_bonds['coord_numbers']}")
    print(f"    MACE: {mace_bonds['coord_numbers']}")
    
    # Performance comparison
    print("\n3. PERFORMANCE COMPARISON:")
    print("-" * 40)
    print(f"  EMT optimization time:  {emt_time:.2f} seconds")
    print(f"  MACE optimization time: {mace_time:.2f} seconds")
    print(f"  Speedup (EMT vs MACE):  {mace_time/emt_time:.1f}x faster")
    
    # Forces
    print(f"\n  Maximum forces:")
    print(f"    EMT:  {np.max(np.abs(emt_forces)):.6f} eV/Å")
    print(f"    MACE: {np.max(np.abs(mace_forces)):.6f} eV/Å")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    if abs(emt_final - mace_final) > 1.0:
        print("⚠️  Large energy difference between EMT and MACE")
        print("   EMT is less accurate for this system")
        print("   MACE should provide more reliable results")
    else:
        print("✓  Good agreement between EMT and MACE")
        print("   Both methods give similar energies")
    
    if rmsd > 0.5:
        print("⚠️  Significant structural difference between methods")
        print("   MACE likely gives more accurate structure")
    else:
        print("✓  Good structural agreement between methods")

def main():
    """Main function to run both calculators and compare"""
    
    print("=" * 60)
    print("Cu7 Cluster: EMT vs MACE Comparison")
    print("=" * 60)
    
    # Check MACE availability
    if not MACE_AVAILABLE:
        print("\n❌ MACE is not available!")
        print("Please install with: pip install mace-torch")
        print("\nRunning EMT only...")
        # Continue with EMT only
        run_mace = False
    else:
        run_mace = True
        print("\n✓ MACE is available")
    
    # Create initial structure
    print("\nCreating initial Cu7 pentagonal bipyramid structure...")
    initial_positions = create_pentagonal_bipyramid()
    initial_atoms = Atoms('Cu7', positions=initial_positions)
    
    print(f"Number of atoms: {len(initial_atoms)}")
    
    # Results storage
    emt_result = None
    mace_result = None
    emt_vib = None
    mace_vib = None
    
    # ============================================================
    # RUN EMT CALCULATIONS
    # ============================================================
    print("\n" + "=" * 60)
    print("RUNNING EMT CALCULATIONS")
    print("=" * 60)
    
    # Setup EMT calculator
    emt_calc = EMT()
    
    # Optimize with EMT
    emt_atoms, emt_initial, emt_final, emt_forces, emt_time = optimize_cluster(
        initial_atoms, emt_calc, 'EMT'
    )
    emt_result = (emt_atoms, emt_initial, emt_final, emt_forces, emt_time)
    
    # Write EMT optimized structure
    write('cu7_optimized_emt.xyz', emt_atoms)
    write('cu7_optimized_emt.traj', emt_atoms)
    
    # Analyze EMT structure
    emt_bonds = analyze_bonds(emt_atoms, 'EMT')
    print(f"\nEMT Structure Analysis:")
    print(f"  Number of bonds: {emt_bonds['num_bonds']}")
    print(f"  Average bond:    {emt_bonds['avg_bond']:.4f} Å")
    print(f"  Coordination:    {emt_bonds['coord_numbers']}")
    
    # Calculate EMT vibrations
    print("\n" + "-" * 40)
    print("Calculating EMT Vibrations...")
    emt_vib = calculate_vibrations(emt_atoms, 'EMT', delta=0.01)
    
    # ============================================================
    # RUN MACE CALCULATIONS
    # ============================================================
    if run_mace:
        print("\n" + "=" * 60)
        print("RUNNING MACE CALCULATIONS")
        print("=" * 60)
        
        try:
            # Setup MACE calculator
            print("\nSetting up MACE calculator...")
            mace_calc = setup_calculator('MACE', device='cpu', model='medium')
            
            # Optimize with MACE
            mace_atoms, mace_initial, mace_final, mace_forces, mace_time = optimize_cluster(
                initial_atoms, mace_calc, 'MACE', max_steps=100, fmax=0.05
            )
            mace_result = (mace_atoms, mace_initial, mace_final, mace_forces, mace_time)
            
            # Write MACE optimized structure
            write('cu7_optimized_mace.xyz', mace_atoms)
            write('cu7_optimized_mace.traj', mace_atoms)
            
            # Analyze MACE structure
            mace_bonds = analyze_bonds(mace_atoms, 'MACE')
            print(f"\nMACE Structure Analysis:")
            print(f"  Number of bonds: {mace_bonds['num_bonds']}")
            print(f"  Average bond:    {mace_bonds['avg_bond']:.4f} Å")
            print(f"  Coordination:    {mace_bonds['coord_numbers']}")
            
            # Calculate MACE vibrations
            print("\n" + "-" * 40)
            print("Calculating MACE Vibrations...")
            mace_vib = calculate_vibrations(mace_atoms, 'MACE', delta=0.005)
            
        except Exception as e:
            print(f"\n❌ MACE calculation failed: {e}")
            print("Continuing with EMT results only...")
            run_mace = False
    
    # ============================================================
    # COMPARE RESULTS
    # ============================================================
    if run_mace and mace_result is not None:
        compare_results(emt_result, mace_result)
    else:
        print("\n" + "=" * 60)
        print("EMT Results Summary")
        print("=" * 60)
        print(f"Final energy: {emt_final:.6f} eV")
        print(f"Maximum force: {np.max(np.abs(emt_forces)):.6f} eV/Å")
        print(f"Optimization steps: {optimizer.get_number_of_steps()}")
        
        if emt_vib and emt_vib.get('success', False):
            print(f"Zero-point energy: {emt_vib['zero_point_energy']:.2f} meV")
            print(f"Number of vibrational modes: {len(emt_vib['meaningful_freqs'])}")
    
    print("\n" + "=" * 60)
    print("✅ Script completed successfully!")
    print("=" * 60)
    
    # Print instructions for viewing
    print("\nVisualization instructions:")
    print("  - EMT structure: ase gui cu7_optimized_emt.xyz")
    if run_mace and mace_result is not None:
        print("  - MACE structure: ase gui cu7_optimized_mace.xyz")
    print("  - EMT vibrations: ase gui cu7_vibrations_emt.*.traj")
    if run_mace and mace_result is not None:
        print("  - MACE vibrations: ase gui cu7_vibrations_mace.*.traj")
    print("  - Compare structures: ase gui cu7_optimized_emt.xyz cu7_optimized_mace.xyz")

if __name__ == "__main__":
    main()
