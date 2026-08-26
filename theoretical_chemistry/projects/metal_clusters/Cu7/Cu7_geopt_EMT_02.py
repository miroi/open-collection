#!/usr/bin/env python3
"""
Enhanced analysis script for Cu7 cluster optimization results
Run this after the optimization is complete
"""

from ase.io import read
from ase.visualize import view
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the optimized structure
cu7 = read('cu7_optimized.xyz')

print("=" * 60)
print("Enhanced Cu7 Cluster Analysis")
print("=" * 60)

# 1. Structure symmetry analysis
print("\n1. STRUCTURE SYMMETRY:")
print("-" * 40)

# Find centroid
centroid = np.mean(cu7.positions, axis=0)
print(f"Centroid position: {centroid}")

# Distances from centroid
distances_from_center = np.linalg.norm(cu7.positions - centroid, axis=1)
print(f"Distances from center (Å):")
for i, d in enumerate(distances_from_center):
    print(f"  Atom {i+1}: {d:.4f} Å")

# Identify equatorial and axial atoms
# Axial atoms are those with largest z-component
z_coords = cu7.positions[:, 2]
axial_indices = np.argsort(np.abs(z_coords))[-2:]  # Two atoms with largest |z|
equatorial_indices = np.argsort(np.abs(z_coords))[:-2]  # Rest are equatorial

print(f"\nEquatorial atoms (5 atoms): {[i+1 for i in equatorial_indices]}")
print(f"  Average radius: {np.mean(distances_from_center[equatorial_indices]):.4f} Å")
print(f"  Average z-coordinate: {np.mean(z_coords[equatorial_indices]):.4f} Å")

print(f"\nAxial atoms (2 atoms): {[i+1 for i in axial_indices]}")
print(f"  Average radius: {np.mean(distances_from_center[axial_indices]):.4f} Å")
print(f"  Average z-coordinate: {np.mean(z_coords[axial_indices]):.4f} Å")

# 2. Bond analysis
print("\n2. BOND ANALYSIS:")
print("-" * 40)

# Get all distances
distances = cu7.get_all_distances()

# Find bonds (cutoff = 2.6 Å for Cu-Cu)
bond_cutoff = 2.6
bonds = []
for i in range(len(cu7)):
    for j in range(i+1, len(cu7)):
        if distances[i][j] < bond_cutoff and distances[i][j] > 0.1:
            bonds.append((i, j, distances[i][j]))

print(f"Total bonds found (cutoff {bond_cutoff} Å): {len(bonds)}")

# Classify bonds
equatorial_bonds = []
axial_equatorial_bonds = []
for i, j, d in bonds:
    if i in equatorial_indices and j in equatorial_indices:
        equatorial_bonds.append(d)
    elif (i in axial_indices and j in equatorial_indices) or \
         (j in axial_indices and i in equatorial_indices):
        axial_equatorial_bonds.append(d)

print(f"Equatorial-equatorial bonds: {len(equatorial_bonds)}")
print(f"  Average: {np.mean(equatorial_bonds):.4f} Å")
print(f"  Standard deviation: {np.std(equatorial_bonds):.4f} Å")

print(f"Axial-equatorial bonds: {len(axial_equatorial_bonds)}")
print(f"  Average: {np.mean(axial_equatorial_bonds):.4f} Å")
print(f"  Standard deviation: {np.std(axial_equatorial_bonds):.4f} Å")

# 3. Energy analysis
print("\n3. ENERGY ANALYSIS:")
print("-" * 40)
from ase.calculators.emt import EMT
cu7.calc = EMT()
energy = cu7.get_potential_energy()
forces = cu7.get_forces()

print(f"Final potential energy: {energy:.6f} eV")
print(f"Binding energy per atom: {energy/7:.6f} eV")
print(f"Maximum force: {np.max(np.abs(forces)):.6f} eV/Å")
print(f"RMS force: {np.sqrt(np.mean(forces**2)):.6f} eV/Å")

# 4. Geometry metrics
print("\n4. GEOMETRY METRICS:")
print("-" * 40)

# Calculate angles
print("\nEquatorial plane angles:")
# Project equatorial atoms onto xy-plane
equatorial_pos = cu7.positions[equatorial_indices][:, :2]
angles = []
for i in range(len(equatorial_pos)):
    for j in range(i+1, len(equatorial_pos)):
        # Calculate angle between vectors from center
        v1 = equatorial_pos[i]
        v2 = equatorial_pos[j]
        angle = np.arctan2(np.cross(v1, v2), np.dot(v1, v2))
        angles.append(np.degrees(np.abs(angle)))

# Theoretical angle for pentagon: 72°
print(f"Average angle between adjacent equatorial atoms: {np.mean(angles):.2f}°")
print(f"Theoretical angle for pentagon: 72.00°")
print(f"Deviation: {np.abs(np.mean(angles) - 72.0):.2f}°")

# 5. Create 3D visualization
print("\n5. VISUALIZATION:")
print("-" * 40)

try:
    # Create a more detailed visualization
    from ase.visualize import view
    print("Opening interactive 3D visualization...")
    print("Close the window to continue")
    view(cu7, viewer='ase')
except:
    print("ASE visualization not available. Using matplotlib instead...")
    
    # Create 3D plot with matplotlib
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot atoms
    positions = cu7.positions
    ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], 
              c='orange', s=200, edgecolors='black', linewidth=2, label='Cu')
    
    # Draw bonds
    for i, j, d in bonds:
        ax.plot([positions[i, 0], positions[j, 0]],
                [positions[i, 1], positions[j, 1]],
                [positions[i, 2], positions[j, 2]], 'k-', alpha=0.5)
    
    # Label atoms
    for i, pos in enumerate(positions):
        ax.text(pos[0], pos[1], pos[2], str(i+1), fontsize=12, fontweight='bold')
    
    ax.set_xlabel('X (Å)')
    ax.set_ylabel('Y (Å)')
    ax.set_zlabel('Z (Å)')
    ax.set_title('Cu7 Cluster - Optimized Structure')
    
    # Set equal aspect ratio
    max_range = np.max([np.max(positions[:, 0]) - np.min(positions[:, 0]),
                       np.max(positions[:, 1]) - np.min(positions[:, 1]),
                       np.max(positions[:, 2]) - np.min(positions[:, 2])]) / 2.0
    mid_x = (np.max(positions[:, 0]) + np.min(positions[:, 0])) * 0.5
    mid_y = (np.max(positions[:, 1]) + np.min(positions[:, 1])) * 0.5
    mid_z = (np.max(positions[:, 2]) + np.min(positions[:, 2])) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    plt.tight_layout()
    plt.savefig('cu7_structure.png', dpi=300, bbox_inches='tight')
    print("  ✓ Structure plot saved as 'cu7_structure.png'")
    plt.show()

# 6. Save coordinates for other software
print("\n6. EXPORTING:")
print("-" * 40)

# Save as extended XYZ with metadata
from ase.io import write
write('cu7_final.xyz', cu7, format='xyz')
print("  ✓ XYZ file saved: cu7_final.xyz")

# Save as Gaussian input (optional)
try:
    from ase.io.gaussian import write_gaussian_in
    write_gaussian_in('cu7.gjf', cu7, 
                     method='pbe1pbe', basis='def2tzvp', 
                     charge=0, mult=1)
    print("  ✓ Gaussian input saved: cu7.gjf")
except:
    pass

print("\n" + "=" * 60)
print("Analysis complete!")
print("=" * 60)
