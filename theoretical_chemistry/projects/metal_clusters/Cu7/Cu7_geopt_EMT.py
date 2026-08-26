#!/usr/bin/env python3
"""
ASE script for geometry optimization of Cu7 cluster using EMT
"""

from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write
import numpy as np

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

# Write final structure to files (only formats that are supported)
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
    # Try to write PDB if available
    write('cu7_optimized.pdb', cu7, format='pdb')
    print("  ✓ cu7_optimized.pdb (PDB format)")
except Exception as e:
    print(f"  ✗ PDB format not supported: {e}")

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
