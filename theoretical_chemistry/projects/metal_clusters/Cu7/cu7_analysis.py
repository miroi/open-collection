#!/usr/bin/env python3
"""
Enhanced analysis script for Cu7 cluster optimization results
"""

from ase.io import read
from ase.calculators.emt import EMT
import numpy as np

print("=" * 60)
print("Enhanced Cu7 Cluster Analysis")
print("=" * 60)

# Read the optimized structure
try:
    cu7 = read('cu7_optimized.xyz')
except:
    try:
        cu7 = read('cu7_optimization.traj')[-1]
    except:
        print("Error: Could not find structure file!")
        exit(1)

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

# Calculate angles in the equatorial plane
print("\nEquatorial plane angles:")
# Get equatorial atom positions in 2D (xy-plane only)
equatorial_pos_2d = cu7.positions[equatorial_indices][:, :2]

# Sort atoms by angle around center to get correct order
center_2d = np.mean(equatorial_pos_2d, axis=0)
angles_from_center = []
for pos in equatorial_pos_2d:
    angle = np.arctan2(pos[1] - center_2d[1], pos[0] - center_2d[0])
    angles_from_center.append(angle)

# Sort by angle
sorted_indices = np.argsort(angles_from_center)
equatorial_pos_sorted = equatorial_pos_2d[sorted_indices]

# Calculate angles between adjacent atoms (in 2D)
angles_between = []
for i in range(len(equatorial_pos_sorted)):
    j = (i + 1) % len(equatorial_pos_sorted)
    v1 = equatorial_pos_sorted[i] - center_2d
    v2 = equatorial_pos_sorted[j] - center_2d
    # Calculate angle in 2D
    cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    angle = np.arccos(np.clip(cos_angle, -1.0, 1.0))
    angles_between.append(np.degrees(angle))

print(f"Angles between adjacent equatorial atoms:")
for i, angle in enumerate(angles_between):
    print(f"  Atoms {i+1}-{i+2 if i+2 <= len(equatorial_pos_sorted) else 1}: {angle:.2f}°")
print(f"Average angle: {np.mean(angles_between):.2f}°")
print(f"Theoretical angle for pentagon: 72.00°")
print(f"Deviation: {np.abs(np.mean(angles_between) - 72.0):.2f}°")

# 5. Calculate distances between equatorial atoms
print("\nEquatorial atom distances (in xy-plane):")
for i in range(len(equatorial_pos_sorted)):
    j = (i + 1) % len(equatorial_pos_sorted)
    dist = np.linalg.norm(equatorial_pos_sorted[i] - equatorial_pos_sorted[j])
    print(f"  Atoms {i+1}-{j+1}: {dist:.4f} Å")

# 6. Coordination numbers
print("\n5. COORDINATION NUMBERS:")
print("-" * 40)
coord_numbers = []
for i in range(len(cu7)):
    coord = sum(1 for j in range(len(cu7)) if i != j and distances[i][j] < bond_cutoff)
    coord_numbers.append(coord)

for i, coord in enumerate(coord_numbers):
    print(f"  Atom {i+1}: {coord}")

# 7. Detailed bond list
print("\n6. DETAILED BOND LIST:")
print("-" * 40)
for i, j, d in sorted(bonds, key=lambda x: x[2]):
    bond_type = ""
    if i in equatorial_indices and j in equatorial_indices:
        bond_type = "(eq-eq)"
    elif (i in axial_indices and j in equatorial_indices) or \
         (j in axial_indices and i in equatorial_indices):
        bond_type = "(ax-eq)"
    print(f"  Cu{i+1} - Cu{j+1}: {d:.4f} Å {bond_type}")

# 8. Save analysis results
print("\n7. SAVING RESULTS:")
print("-" * 40)

# Save detailed analysis to file
with open('cu7_analysis_results.txt', 'w') as f:
    f.write("Cu7 Cluster Analysis Results\n")
    f.write("=" * 60 + "\n\n")
    
    f.write("STRUCTURE INFORMATION:\n")
    f.write(f"  Structure type: Pentagonal bipyramid\n")
    f.write(f"  Number of atoms: 7\n")
    f.write(f"  Equatorial atoms: {[i+1 for i in equatorial_indices]}\n")
    f.write(f"  Axial atoms: {[i+1 for i in axial_indices]}\n\n")
    
    f.write("ENERGY:\n")
    f.write(f"  Final energy: {energy:.6f} eV\n")
    f.write(f"  Binding energy per atom: {energy/7:.6f} eV\n")
    f.write(f"  Maximum force: {np.max(np.abs(forces)):.6f} eV/Å\n\n")
    
    f.write("BOND LENGTHS:\n")
    f.write(f"  Equatorial-equatorial: {np.mean(equatorial_bonds):.4f} ± {np.std(equatorial_bonds):.4f} Å\n")
    f.write(f"  Axial-equatorial: {np.mean(axial_equatorial_bonds):.4f} ± {np.std(axial_equatorial_bonds):.4f} Å\n\n")
    
    f.write("ANGLES (equatorial plane):\n")
    for i, angle in enumerate(angles_between):
        f.write(f"  Angle {i+1}: {angle:.2f}°\n")
    f.write(f"  Average: {np.mean(angles_between):.2f}°\n")
    f.write(f"  Theoretical (pentagon): 72.00°\n\n")
    
    f.write("COORDINATION NUMBERS:\n")
    for i, coord in enumerate(coord_numbers):
        f.write(f"  Atom {i+1}: {coord}\n")
    
    f.write("\nALL BONDS:\n")
    for i, j, d in sorted(bonds, key=lambda x: x[2]):
        bond_type = "eq-eq" if (i in equatorial_indices and j in equatorial_indices) else "ax-eq"
        f.write(f"  Cu{i+1} - Cu{j+1}: {d:.4f} Å ({bond_type})\n")

print("  ✓ Results saved to: cu7_analysis_results.txt")

# 9. Optional: Visualization
print("\n8. VISUALIZATION:")
print("-" * 40)

try:
    from ase.visualize import view
    print("Opening interactive 3D visualization...")
    print("Close the window to continue")
    view(cu7, viewer='ase')
except ImportError:
    print("ASE visualization not available.")
    print("You can view the structure with:")
    print("  - Avogadro: avogadro cu7_optimized.xyz")
    print("  - VMD: vmd cu7_optimized.xyz")
except Exception as e:
    print(f"Visualization failed: {e}")

print("\n" + "=" * 60)
print("✅ Analysis Complete!")
print("=" * 60)
