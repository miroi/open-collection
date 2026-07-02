# visualize_vibrations_improved.py
"""
Improved Vibrational Mode Visualization of Hg on Au(111)
Better mode classification and handling
"""

import matgl
from matgl.ext.ase import M3GNetCalculator
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.io import write
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("IMPROVED VIBRATIONAL MODE VISUALIZATION")
print("Hg ADSORPTION ON Au(111)")
print("=" * 70)

# ============================================================================
# 1. SETUP SYSTEM
# ============================================================================

print("\nLoading M3GNet potential...")
pot = matgl.load_model("M3GNet-PES-MatPES-PBE-2025.2")
calc = M3GNetCalculator(potential=pot, stress_unit="eV/A3")

# Build slab
print("Building Au(111) slab...")
slab = fcc111('Au', size=(3, 3, 4), a=4.08, vacuum=15.0)
slab.pbc = True

# Fix bottom layers
z_pos = slab.get_positions()[:, 2]
mask = z_pos < np.percentile(z_pos, 40)
constraint = FixAtoms(mask=mask)
slab.set_constraint(constraint)

# Add Hg adsorbate
from ase import Atoms
hg = Atoms("Hg", positions=[[0, 0, 0]])
adslab = slab.copy()
add_adsorbate(adslab, hg, height=2.0, position='fcc')
adslab.set_constraint(constraint)

print(f"System: {len(adslab)} atoms (including Hg)")

# ============================================================================
# 2. RELAX STRUCTURE
# ============================================================================

print("\nRelaxing structure...")
adslab.set_calculator(calc)
opt = BFGS(adslab)
opt.run(fmax=0.01, steps=100)

write('relaxed_structure.xyz', adslab)
print("✓ Relaxed structure saved to relaxed_structure.xyz")

# ============================================================================
# 3. CALCULATE VIBRATIONS
# ============================================================================

print("\nCalculating vibrational modes...")
index_hg = len(adslab) - 1
print(f"Hg atom index: {index_hg}")

# Calculate vibrations for Hg atom only
vib = Vibrations(adslab, indices=[index_hg], name='vibrations_hg')
vib.run()

# Get frequencies and modes
frequencies_raw = vib.get_frequencies()  # in cm^-1

# Convert to real numbers (take real part)
frequencies = np.real(frequencies_raw)

print(f"\nVibrational modes of Hg on Au(111):")
print("-" * 70)
print(f"{'Mode':<8s} | {'Frequency (cm⁻¹)':>18s} | {'Frequency (THz)':>18s} | {'Type':>15s}")
print("-" * 70)

# Get modes and classify them
mode_types = []
modes = []

for i in range(len(frequencies)):
    # Get mode for this frequency
    mode = vib.get_mode(i)
    modes.append(mode)
    
    # Get displacement for Hg atom (first atom in the indices list)
    hg_displacement = mode[0]  # First atom in the mode
    
    # Take real part
    hg_disp_real = np.real(hg_displacement)
    
    # Normalize for classification
    norm = np.linalg.norm(hg_disp_real)
    if norm > 0:
        hg_disp_real = hg_disp_real / norm
    
    # Determine mode type based on dominant displacement
    abs_x = abs(hg_disp_real[0])
    abs_y = abs(hg_disp_real[1])
    abs_z = abs(hg_disp_real[2])
    
    # Get actual frequency
    freq = frequencies[i]
    
    # Special handling for modes with same frequency
    if freq < 10:  # Very low frequency (could be numerical artifact)
        mode_type = "Low frequency"
    elif abs_z > 0.7:  # Mostly vertical
        if abs(hg_disp_real[0]) > 0.1 or abs(hg_disp_real[1]) > 0.1:
            mode_type = "Vertical + Horizontal"
        else:
            mode_type = "Vertical (stretch)"
    elif abs_x > 0.7:  # Mostly x-direction
        if abs_y > 0.3:
            mode_type = "Horizontal (xy)"
        else:
            mode_type = "Horizontal (x)"
    elif abs_y > 0.7:  # Mostly y-direction
        if abs_x > 0.3:
            mode_type = "Horizontal (xy)"
        else:
            mode_type = "Horizontal (y)"
    else:
        mode_type = "Mixed"
    
    mode_types.append(mode_type)
    
    # Print with proper formatting
    freq_real = float(freq)
    freq_thz = freq_real * 0.029979
    print(f"{i+1:<8d} | {freq_real:18.1f} | {freq_thz:18.3f} | {mode_type:>15s}")

# ============================================================================
# 4. VISUALIZE MODES IN 3D
# ============================================================================

print("\n" + "=" * 70)
print("3D VIBRATIONAL MODE VISUALIZATION")
print("=" * 70)

# Create figure for 3D visualization
fig = plt.figure(figsize=(16, 12))

n_modes = min(3, len(frequencies))

for mode_idx in range(n_modes):
    ax = fig.add_subplot(2, 3, mode_idx + 1, projection='3d')
    
    # Get Hg position and displacement
    hg_pos = adslab.positions[index_hg]
    disp = np.real(modes[mode_idx][0])
    
    # Scale for visualization (normalize to 0.3 Å)
    disp_norm = np.linalg.norm(disp)
    if disp_norm > 0:
        disp_scaled = disp / disp_norm * 0.3
    else:
        disp_scaled = disp * 0.3
    
    # Get surface atoms (nearest neighbors)
    all_positions = adslab.positions
    distances = np.linalg.norm(all_positions - hg_pos, axis=1)
    nearest_indices = np.argsort(distances)[1:4]  # 3 nearest Au atoms
    
    # Plot Au surface atoms
    au_positions = adslab.positions[:-1]  # All except Hg
    ax.scatter(au_positions[:, 0], au_positions[:, 1], au_positions[:, 2], 
               c='gold', s=30, alpha=0.5, label='Au')
    
    # Highlight nearest Au atoms
    nearest_positions = all_positions[nearest_indices]
    ax.scatter(nearest_positions[:, 0], nearest_positions[:, 1], nearest_positions[:, 2],
               c='orange', s=80, alpha=0.8, label='Nearest Au')
    
    # Plot Hg atom (equilibrium position)
    ax.scatter([hg_pos[0]], [hg_pos[1]], [hg_pos[2]], 
               c='red', s=120, marker='o', label='Hg (eq.)')
    
    # Plot displaced Hg position
    displaced_pos = hg_pos + disp_scaled
    ax.scatter([displaced_pos[0]], [displaced_pos[1]], [displaced_pos[2]], 
               c='blue', s=120, marker='^', label='Hg (disp.)')
    
    # Draw arrow for displacement
    ax.quiver(hg_pos[0], hg_pos[1], hg_pos[2],
              disp_scaled[0], disp_scaled[1], disp_scaled[2],
              color='red', linewidth=2, arrow_length_ratio=0.2)
    
    # Set labels and title
    freq = float(frequencies[mode_idx])
    mode_type = mode_types[mode_idx]
    ax.set_title(f'Mode {mode_idx+1}: {freq:.1f} cm⁻¹\n({mode_type})', fontsize=12)
    ax.set_xlabel('X (Å)')
    ax.set_ylabel('Y (Å)')
    ax.set_zlabel('Z (Å)')
    ax.legend(loc='upper right', fontsize=8)
    ax.set_box_aspect([1, 1, 0.8])

# ============================================================================
# 5. PLOT DISPLACEMENT VECTORS (2D Top View)
# ============================================================================

for mode_idx in range(n_modes):
    ax = fig.add_subplot(2, 3, mode_idx + 4)
    
    # Get Hg position and displacement
    hg_pos = adslab.positions[index_hg]
    disp = np.real(modes[mode_idx][0])
    
    # Scale for visualization
    disp_norm = np.linalg.norm(disp)
    if disp_norm > 0:
        disp_scaled = disp / disp_norm * 0.3
    else:
        disp_scaled = disp * 0.3
    
    # Plot surface atoms (top view)
    au_positions = adslab.positions[:-1]
    ax.scatter(au_positions[:, 0], au_positions[:, 1], 
               c='gold', s=30, alpha=0.5)
    
    # Highlight nearest Au atoms
    all_positions = adslab.positions
    distances = np.linalg.norm(all_positions - hg_pos, axis=1)
    nearest_indices = np.argsort(distances)[1:4]
    nearest_positions = all_positions[nearest_indices]
    ax.scatter(nearest_positions[:, 0], nearest_positions[:, 1],
               c='orange', s=60, alpha=0.8)
    
    # Plot Hg equilibrium position
    ax.scatter([hg_pos[0]], [hg_pos[1]], 
               c='red', s=80, marker='o', label='Equilibrium')
    
    # Plot displacement arrow
    ax.arrow(hg_pos[0], hg_pos[1],
             disp_scaled[0], disp_scaled[1],
             head_width=0.08, head_length=0.08, fc='red', ec='red', linewidth=2)
    
    # Plot displaced position
    displaced_pos = hg_pos + disp_scaled
    ax.scatter([displaced_pos[0]], [displaced_pos[1]], 
               c='blue', s=60, marker='^', label='Displaced')
    
    freq = float(frequencies[mode_idx])
    mode_type = mode_types[mode_idx]
    ax.set_title(f'Mode {mode_idx+1}: {freq:.1f} cm⁻¹\nTop View', fontsize=11)
    ax.set_xlabel('X (Å)')
    ax.set_ylabel('Y (Å)')
    ax.legend(loc='upper right', fontsize=7)
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)

plt.tight_layout()
plt.savefig('vibrational_modes_3d.png', dpi=150)
print("✓ 3D visualization saved to vibrational_modes_3d.png")

# ============================================================================
# 6. PRINT SUMMARY TABLE
# ============================================================================

print("\n" + "=" * 70)
print("VIBRATIONAL ANALYSIS SUMMARY")
print("=" * 70)

# Get Hg position relative to surface
hg_z = adslab.positions[index_hg][2]
surface_atoms = [pos[2] for pos in adslab.positions[:-1] if pos[2] < hg_z - 1.0]
surface_z = np.mean(surface_atoms) if surface_atoms else hg_z - 2.0
height = hg_z - surface_z

print(f"""
Hg Adsorption Geometry:
  • Height above surface: {height:.3f} Å
  • Number of Au atoms: {len(slab)}
  • Number of Hg atoms: 1

Vibrational Modes:
""")

for i, (freq, mode_type) in enumerate(zip(frequencies, mode_types)):
    freq_real = float(freq)
    print(f"  Mode {i+1}: {freq_real:6.1f} cm⁻¹ ({freq_real*0.029979:6.3f} THz) - {mode_type}")

# Calculate ZPE from frequencies (real part only)
ZPE = 0.5 * 4.135667696e-15 * 1e12 * sum(float(freq) * 0.029979 for freq in frequencies if float(freq) > 0)
print(f"""
ZPE Corrections:
  • Zero-Point Energy: {ZPE:.4f} eV (from calculated frequencies)

Visualization Files Created:
  • relaxed_structure.xyz - Relaxed structure
  • vibrational_modes_3d.png - 3D mode visualization
""")

# ============================================================================
# 7. SAVE VIBRATIONAL DATA
# ============================================================================

with open('vibrational_modes.txt', 'w') as f:
    f.write("Vibrational Modes of Hg on Au(111)\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"{'Mode':<8s} | {'Frequency (cm⁻¹)':>18s} | {'Frequency (THz)':>18s} | {'Type':>15s}\n")
    f.write("-" * 70 + "\n")
    for i, (freq, mode_type) in enumerate(zip(frequencies, mode_types)):
        freq_real = float(freq)
        f.write(f"{i+1:<8d} | {freq_real:18.1f} | {freq_real*0.029979:18.3f} | {mode_type:>15s}\n")
    
    f.write("\n" + "=" * 60 + "\n")
    f.write(f"Hg height: {height:.3f} Å\n")
    f.write(f"Number of Au atoms: {len(slab)}\n")
    f.write(f"Zero-Point Energy: {ZPE:.4f} eV\n")

print("✓ Vibrational data saved to vibrational_modes.txt")

# ============================================================================
# 8. DISPLAY SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("✓ VIBRATIONAL ANALYSIS COMPLETE!")
print("=" * 70)
print("\nTo view the 3D visualization:")
print("  • Open vibrational_modes_3d.png")
print("\nTo view the structure in ASE GUI:")
print("  ase gui relaxed_structure.xyz")

print("\n" + "=" * 70)
print("✓ COMPLETE!")
print("=" * 70)
