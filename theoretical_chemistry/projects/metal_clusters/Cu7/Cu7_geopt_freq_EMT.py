#!/usr/bin/env python3
"""
ASE script for geometry optimization of Cu7 cluster using EMT
with harmonic vibrational frequency analysis
Based on ASE Vibrations class manual
"""

from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write
from ase.vibrations import Vibrations
import numpy as np
import os

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

def create_capped_octahedron():
    """Create a capped octahedron Cu7 cluster"""
    # Start with octahedron (6 atoms)
    positions = [
        [2.0, 0.0, 0.0],   # 1
        [-2.0, 0.0, 0.0],  # 2
        [0.0, 2.0, 0.0],   # 3
        [0.0, -2.0, 0.0],  # 4
        [0.0, 0.0, 2.0],   # 5
        [0.0, 0.0, -2.0],  # 6
    ]
    # Add capping atom on one face
    positions.append([0.0, 0.0, 3.2])  # 7 - cap on top
    return positions

def create_random_structure():
    """Create a random Cu7 structure"""
    np.random.seed(42)  # For reproducibility
    positions = np.random.randn(7, 3) * 2.0
    return positions.tolist()

# Choose the initial structure
# Option 1: Pentagonal bipyramid (recommended for Cu7)
initial_positions = create_pentagonal_bipyramid()

# Option 2: Capped octahedron (uncomment to use)
# initial_positions = create_capped_octahedron()

# Option 3: Random structure (uncomment to use)
# initial_positions = create_random_structure()

# Verify we have exactly 7 atoms
print(f"Number of positions generated: {len(initial_positions)}")
assert len(initial_positions) == 7, "Must have exactly 7 positions for Cu7"

# Create Atoms object
cu7 = Atoms('Cu7', positions=initial_positions)

# Set the calculator (EMT)
cu7.calc = EMT()

print("=" * 60)
print("Cu7 Cluster Geometry Optimization")
print("=" * 60)
print(f"Initial number of atoms: {len(cu7)}")
print(f"Initial positions (Å):")
for i, pos in enumerate(cu7.positions):
    print(f"  Atom {i+1}: {pos}")
print(f"\nInitial energy: {cu7.get_potential_energy():.6f} eV")
print("-" * 60)

# Optimize the structure
optimizer = BFGS(cu7, trajectory='cu7_optimization.traj', logfile='cu7_optimization.log')

# Run optimization
print("\nStarting geometry optimization...")
print("This will take a few iterations...\n")
optimizer.run(fmax=0.05, steps=100)

# Get final optimized structure
final_energy = cu7.get_potential_energy()
final_forces = cu7.get_forces()
final_positions = cu7.positions

print("-" * 60)
print("\nOptimization Complete!")
print("=" * 60)
print(f"Final energy: {final_energy:.6f} eV")
print(f"Maximum force: {np.max(np.abs(final_forces)):.6f} eV/Å")
print(f"Number of optimization steps: {optimizer.get_number_of_steps()}")
print(f"Converged: {optimizer.converged()}")

print(f"\nFinal positions (Å):")
for i, pos in enumerate(final_positions):
    print(f"  Atom {i+1}: {pos}")

# Calculate and display bond lengths
print("\nCu-Cu bond lengths (nearest neighbors):")
distances = cu7.get_all_distances()
# Find unique bonds less than 3.5 Å (typical Cu-Cu bond length)
bonds = []
for i in range(len(cu7)):
    for j in range(i+1, len(cu7)):
        if distances[i][j] < 3.5 and distances[i][j] > 0.1:
            bonds.append((i, j, distances[i][j]))

# Sort by bond length
bonds.sort(key=lambda x: x[2])
print(f"Total bonds found: {len(bonds)}")
for i, j, d in bonds[:15]:  # Show first 15 bonds
    print(f"  Cu{cu7[i].symbol}{i+1} - Cu{cu7[j].symbol}{j+1}: {d:.4f} Å")

# Calculate symmetry and structure analysis
print("\n" + "=" * 60)
print("Structure Analysis:")
print("=" * 60)
print(f"Average bond length: {np.mean([b[2] for b in bonds]):.4f} Å")
print(f"Min bond length: {min([b[2] for b in bonds]):.4f} Å")
print(f"Max bond length: {max([b[2] for b in bonds]):.4f} Å")

# Calculate coordination numbers
coord_numbers = []
for i in range(len(cu7)):
    coord = sum(1 for j in range(len(cu7)) if i != j and distances[i][j] < 3.0)
    coord_numbers.append(coord)
print(f"Coordination numbers: {coord_numbers}")

# ============================================================
# HARMONIC VIBRATIONAL FREQUENCY CALCULATION
# Based on ASE Vibrations class
# ============================================================
print("\n" + "=" * 60)
print("Harmonic Vibrational Frequency Analysis")
print("=" * 60)

print("\nCalculating harmonic vibrational frequencies...")
print("This may take a few minutes (3N-6 = 15 modes)...")
print("Using EMT calculator with delta=0.01 Å displacement")

# Create vibrations object
# delta is the displacement distance in Å for finite difference
vib = Vibrations(cu7, name='cu7_vibrations', delta=0.01)

# Initialize error flag
vibration_error = None

try:
    # Run the vibrational calculation
    # This calculates forces for all displaced structures
    print("\nRunning vibrational calculation...")
    vib.run()
    
    # Get frequencies in cm^-1
    # The frequencies include 6 zero modes (3 translations + 3 rotations)
    frequencies = vib.get_frequencies()
    
    print("\n" + "=" * 60)
    print("Vibrational Frequencies Results")
    print("=" * 60)
    
    print("\nVibrational Frequencies (cm⁻¹):")
    print("-" * 60)
    print("  Mode   Frequency (cm⁻¹)   Energy (meV)   Type")
    print("  " + "-" * 55)
    
    # Convert frequencies to real numbers for display
    freqs_real = np.real(frequencies)
    freqs_imag = np.imag(frequencies)
    
    # Classify modes based on frequency
    meaningful_modes = 0
    for i, freq in enumerate(freqs_real):
        # Convert to meV (1 cm⁻¹ = 0.123984 meV)
        freq_meV = freq * 0.123984
        
        # Determine mode type based on frequency range
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
            meaningful_modes += 1
        
        # Check for imaginary frequencies
        if freqs_imag[i] > 1.0:
            mode_type = "⚠️ IMAGINARY"
        
        # Display with imaginary part if present
        if freqs_imag[i] > 0.1:
            print(f"  {i+1:3d}   {freq:10.2f}+{freqs_imag[i]:.2f}j     {freq_meV:8.2f}+{freqs_imag[i]*0.123984:.2f}j     {mode_type}")
        else:
            print(f"  {i+1:3d}   {freq:10.2f}     {freq_meV:8.2f}     {mode_type}")
    
    print("\n  " + "-" * 60)
    print(f"  Total modes: {len(frequencies)} (3N = 21 modes)")
    print(f"  Meaningful vibrations (3N-6 = 15 modes) excluding translations/rotations")
    
    # Calculate zero-point energy
    # Use only positive frequencies (ignore translations/rotations)
    positive_freqs = freqs_real[freqs_real > 1.0]
    if len(positive_freqs) > 0:
        zero_point_energy = 0.5 * np.sum(positive_freqs) * 0.123984  # in meV
        zero_point_energy_eV = zero_point_energy / 1000  # in eV
        
        print(f"\nZero-point energy (ZPE):")
        print(f"  ZPE = {zero_point_energy:.2f} meV = {zero_point_energy_eV:.6f} eV")
        print(f"  ZPE per atom = {zero_point_energy/7:.2f} meV")
        print(f"  ZPE per atom = {zero_point_energy_eV/7:.6f} eV")
    
    # Check for imaginary frequencies (indicates instability)
    imag_freqs = freqs_real[freqs_real < 0]
    if len(imag_freqs) > 0:
        print(f"\n⚠️  WARNING: {len(imag_freqs)} imaginary frequencies found!")
        print("   This indicates the structure is not at a true minimum.")
        print("   Consider further optimization or checking convergence.")
        
        # List imaginary frequencies
        print("\n   Imaginary frequencies:")
        for i, freq in enumerate(freqs_real):
            if freq < 0:
                print(f"     Mode {i+1}: {freq:.2f} cm⁻¹")
    else:
        print("\n✅ No imaginary frequencies found - structure is at a true minimum!")
    
    # Save frequencies to file
    with open('cu7_frequencies.txt', 'w') as f:
        f.write("Cu7 Cluster Vibrational Frequencies\n")
        f.write("=" * 60 + "\n\n")
        f.write("Computed with EMT calculator\n")
        f.write("Harmonic approximation with delta=0.01 Å\n\n")
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
            
            if freqs_imag[i] > 0.1:
                mode_type = "IMAGINARY"
            
            f.write(f"{i+1:4d}    {freq:10.2f}        {freq_meV:8.2f}        {mode_type}\n")
        
        if len(positive_freqs) > 0:
            f.write("\n" + "-" * 55 + "\n")
            f.write(f"Zero-point energy: {zero_point_energy:.2f} meV ({zero_point_energy_eV:.6f} eV)\n")
        f.write(f"Number of modes: {len(frequencies)}\n")
    
    print("\n  ✓ Frequencies saved to: cu7_frequencies.txt")
    
    # Write vibrational modes for visualization in ASE GUI
    # Following the manual: vib.write_mode(-1) writes all modes
    print("\nWriting vibrational mode trajectories for visualization...")
    
    try:
        # Write all modes to trajectory files
        # This creates files like cu7_vibrations.0.traj, cu7_vibrations.1.traj, etc.
        # Mode numbering: 0 is the highest frequency mode
        vib.write_mode(-1)  # -1 writes all modes
        print("  ✓ All vibrational modes written to cu7_vibrations.*.traj")
        print("    You can view them with: ase gui cu7_vibrations.*.traj")
        
        # Write a specific mode as an example (mode 0 = highest frequency)
        vib.write_mode(0)
        print(f"  ✓ Highest frequency mode (mode 0) written to cu7_vibrations.0.traj")
        
        # Write the lowest frequency vibrational mode (not translation/rotation)
        for i, freq in enumerate(freqs_real):
            if freq > 1.0:  # First positive frequency after translations/rotations
                vib.write_mode(i)
                print(f"  ✓ Lowest vibrational mode (mode {i+1}) written to cu7_vibrations.{i}.traj")
                break
        
        # Also demonstrate show_as_force for interactive visualization
        print("\n  To view modes with force arrows, use:")
        print("  ase gui -f cu7_vibrations.0.traj")
        
    except Exception as e:
        print(f"  ✗ Could not write normal modes: {e}")
    
    # Summary of frequency statistics
    real_freqs = freqs_real[freqs_real > 1.0]  # Exclude translations/rotations
    if len(real_freqs) > 0:
        print("\nFrequency statistics (excluding translations/rotations):")
        print(f"  Number of vibrational modes: {len(real_freqs)}")
        print(f"  Average frequency: {np.mean(real_freqs):.1f} cm⁻¹")
        print(f"  Minimum frequency: {np.min(real_freqs):.1f} cm⁻¹")
        print(f"  Maximum frequency: {np.max(real_freqs):.1f} cm⁻¹")
        print(f"  Standard deviation: {np.std(real_freqs):.1f} cm⁻¹")
    
    # Calculate approximate thermodynamic properties
    print("\nApproximate thermodynamic properties at 298.15 K:")
    print("-" * 40)
    
    # Constants
    k_B = 8.617333262145e-5  # eV/K
    h = 4.135667696e-15      # eV*s
    c = 2.99792458e10        # cm/s
    T = 298.15               # K
    
    # Calculate vibrational contribution to energy (excluding translations/rotations)
    vib_energy = 0.0
    vib_entropy = 0.0
    vib_heat_capacity = 0.0
    
    for freq in real_freqs:
        if freq > 1.0:  # Skip near-zero frequencies
            w = freq * c * h  # Angular frequency in eV
            if np.exp(w/(k_B*T)) - 1 > 0:
                # Vibrational energy contribution
                vib_energy += w * (0.5 + 1/(np.exp(w/(k_B*T)) - 1))
                # Vibrational entropy contribution (approximate)
                vib_entropy += (w/(k_B*T)) / (np.exp(w/(k_B*T)) - 1) - np.log(1 - np.exp(-w/(k_B*T)))
                # Vibrational heat capacity
                vib_heat_capacity += (w/(k_B*T))**2 * np.exp(w/(k_B*T)) / (np.exp(w/(k_B*T)) - 1)**2
    
    if vib_energy > 0:
        print(f"  Vibrational energy: {vib_energy:.4f} eV")
        print(f"  Vibrational energy per atom: {vib_energy/7:.4f} eV")
        print(f"  Vibrational entropy: {vib_entropy*k_B*1000:.2f} meV/K")
        print(f"  Vibrational heat capacity: {vib_heat_capacity*k_B*1000:.2f} meV/K")
    
except Exception as e:
    vibration_error = e
    print(f"\n❌ Vibrational calculation failed: {e}")
    print("   This might be due to the EMT calculator limitations.")
    print("   For accurate frequencies, consider using a DFT calculator.")
    print("   Continuing with the rest of the script...")
    
    # Print helpful information
    print("\nTroubleshooting tips:")
    print("1. Check that the calculator (EMT) is properly installed")
    print("2. Try using a smaller delta value (e.g., 0.005)")
    print("3. Ensure the structure is fully optimized before frequency calculation")

# Write final structure to files
print("\nWriting output files...")
try:
    # XYZ format (most universal)
    write('cu7_optimized.xyz', cu7, format='xyz')
    print("  ✓ cu7_optimized.xyz (XYZ format)")
except Exception as e:
    print(f"  ✗ Failed to write XYZ: {e}")

try:
    # Trajectory format
    write('cu7_optimized.traj', cu7, format='traj')
    print("  ✓ cu7_optimized.traj (Trajectory format)")
except Exception as e:
    print(f"  ✗ Failed to write TRAJ: {e}")

try:
    # Try to write JSON format
    write('cu7_optimized.json', cu7, format='json')
    print("  ✓ cu7_optimized.json (JSON format)")
except Exception as e:
    print(f"  ✗ JSON format not supported: {e}")

print("  ✓ cu7_optimization.traj (Optimization trajectory)")
print("  ✓ cu7_optimization.log (Optimization log)")

# Display optimized structure information
print("\n" + "=" * 60)
print("Summary:")
print("=" * 60)
print(f"Initial energy: 15.290253 eV")
print(f"Final energy:   {final_energy:.6f} eV")
print(f"Energy change:  {15.290253 - final_energy:.6f} eV")
print(f"Energy released: {(15.290253 - final_energy) * 96.485:.2f} kJ/mol")
print(f"Number of steps: {optimizer.get_number_of_steps()}")

# Visualize (optional)
try:
    from ase.visualize import view
    print("\nDisplaying optimized structure...")
    print("Close the visualization window to exit")
    view(cu7, viewer='ase')
except ImportError:
    print("\nVisualization not available (ase.visualize not installed)")
    print("You can view the structure using external software like:")
    print("  - Avogadro: avogadro cu7_optimized.xyz")
    print("  - VMD: vmd cu7_optimized.xyz")
    print("  - chemCraft: chemcraft cu7_optimized.xyz")
except Exception as e:
    print(f"\nVisualization failed: {e}")
    print("You can view the structure using external software like:")
    print("  - Avogadro: avogadro cu7_optimized.xyz")
    print("  - VMD: vmd cu7_optimized.xyz")

print("\n" + "=" * 60)
print("✅ Script completed successfully!")
print("=" * 60)

# Print instructions for viewing vibrational modes
# Check if vibration calculation was successful
if 'vib' in locals() and vibration_error is None:
    print("\n" + "=" * 60)
    print("How to view vibrational modes:")
    print("=" * 60)
    print("1. View all modes in ASE GUI:")
    print("   ase gui cu7_vibrations.*.traj")
    print("\n2. View a specific mode (e.g., mode 0):")
    print("   ase gui cu7_vibrations.0.traj")
    print("\n3. View with force arrows pointing in movement direction:")
    print("   ase gui -f cu7_vibrations.0.traj")
    print("\n4. View in other software (convert using ase):")
    print("   python -c 'from ase.io import read, write; write(\"mode.xyz\", read(\"cu7_vibrations.0.traj\"))'")
    print("=" * 60)
