# visualize_vibrations_working.py
"""
Working Vibrational Mode Visualization of Hg on Au(111)
Properly positions Hg atom and calculates vibrations
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
print("WORKING VIBRATIONAL MODE VISUALIZATION")
print("Hg ADSORPTION ON Au(111)")
print("=" * 70)

# ============================================================================
# 1. SETUP SYSTEM WITH PROPER Hg POSITIONING
# ============================================================================

print("\nLoading M3GNet potential...")
pot = matgl.load_model("M3GNet-PES-MatPES-PBE-2025.2")
calc = M3GNetCalculator(potential=pot, stress_unit="eV/A3")

# Build slab
print("Building Au(111) slab...")
slab = fcc111('Au', size=(3, 3, 3), a=4.08, vacuum=15.0)
slab.pbc = True

# Fix bottom layers
z_pos = slab.get_positions()[:, 2]
mask = z_pos < np.percentile(z_pos, 40)
constraint = FixAtoms(mask=mask)
slab.set_constraint(constraint)

# Add Hg adsorbate at a reasonable height
from ase import Atoms
hg = Atoms("Hg", positions=[[0, 0, 0]])
adslab = slab.copy()

# The add_adsorbate function places Hg at the fcc site
# with the specified height above the surface
add_adsorbate(adslab, hg, height=2.0, position='fcc')
adslab.set_constraint(constraint)

print(f"System: {len(adslab)} atoms (including Hg)")

# ============================================================================
# 2. RELAX STRUCTURE
# ============================================================================

print("\nRelaxing structure...")
adslab.set_calculator(calc)
opt = BFGS(adslab, trajectory='relaxation.traj')
opt.run(fmax=0.02, steps=100)

write('relaxed_structure.xyz', adslab)
print("✓ Relaxed structure saved to relaxed_structure.xyz")

# Get Hg position and height
index_hg = len(adslab) - 1
hg_pos = adslab.positions[index_hg]
print(f"Hg position: ({hg_pos[0]:.3f}, {hg_pos[1]:.3f}, {hg_pos[2]:.3f}) Å")

# Calculate height above surface (top layer of Au)
top_layer_z = np.max([pos[2] for pos in adslab.positions[:-1] 
                      if pos[2] < hg_pos[2] - 1.0])
height = hg_pos[2] - top_layer_z
print(f"Hg height above surface: {height:.3f} Å")

if height > 4.0:
    print("⚠ Warning: Hg appears to be floating. Trying constrained relaxation...")
    # Force Hg to be closer to surface by constraining it
    adslab_cons = adslab.copy()
    # Constrain all Au atoms, relax only Hg
    from ase.constraints import FixAtoms
    all_indices = list(range(len(adslab_cons)))
    au_indices = [i for i in all_indices if i != index_hg]
    constraint_cons = FixAtoms(indices=au_indices)
    adslab_cons.set_constraint(constraint_cons)
    adslab_cons.set_calculator(calc)
    opt_cons = BFGS(adslab_cons)
    opt_cons.run(fmax=0.02, steps=50)
    
    # Update positions
    adslab.positions[index_hg] = adslab_cons.positions[index_hg]
    write('relaxed_structure_fixed.xyz', adslab)
    print("✓ Fixed structure saved to relaxed_structure_fixed.xyz")
    
    # Recalculate height
    hg_pos = adslab.positions[index_hg]
    height = hg_pos[2] - top_layer_z
    print(f"Hg height after fixing: {height:.3f} Å")

# ============================================================================
# 3. CALCULATE VIBRATIONS
# ============================================================================

print("\nCalculating vibrational modes...")
print(f"Hg atom index: {index_hg}")

# Calculate vibrations for Hg atom only
vib = Vibrations(adslab, indices=[index_hg], name='vibrations_hg')
vib.run()

# Get frequencies and modes
frequencies_raw = vib.get_frequencies()
frequencies = np.real(frequencies_raw)

print(f"\nVibrational modes of Hg on Au(111):")
print("-" * 80)
print(f"{'Mode':<8s} | {'Frequency (cm⁻¹)':>18s} | {'Frequency (THz)':>18s} | {'Type':>15s} | {'Direction':>15s}")
print("-" * 80)

# Get modes and classify them
mode_types = []
mode_directions = []
modes = []

for i in range(len(frequencies)):
    mode = vib.get_mode(i)
    modes.append(mode)
    
    hg_disp = np.real(mode[0])
    
    # Normalize
    norm = np.linalg.norm(hg_disp)
    if norm > 1e-6:
        hg_disp_norm = hg_disp / norm
    else:
        hg_disp_norm = hg_disp
    
    freq = float(frequencies[i])
    
    # Classify based on dominant displacement
    abs_x = abs(hg_disp_norm[0])
    abs_y = abs(hg_disp_norm[1])
    abs_z = abs(hg_disp_norm[2])
    
    # Better classification with thresholds
    if abs_z > 0.7:
        if abs_x > 0.3 or abs_y > 0.3:
            mode_type = "Mixed (vertical)"
        else:
            mode_type = "Vertical"
        mode_direction = "Z"
    elif abs_x > 0.7:
        if abs_y > 0.3:
            mode_type = "Mixed (horizontal)"
            mode_direction = "XY"
        else:
            mode_type = "Horizontal"
            mode_direction = "X"
    elif abs_y > 0.7:
        if abs_x > 0.3:
            mode_type = "Mixed (horizontal)"
            mode_direction = "XY"
        else:
            mode_type = "Horizontal"
            mode_direction = "Y"
    else:
        # Mixed mode - determine dominant
        if abs_z > abs_x and abs_z > abs_y:
            mode_type = "Mixed (vertical dominant)"
            mode_direction = "Z"
        elif abs_x > abs_y:
            mode_type = "Mixed (X dominant)"
            mode_direction = "X"
        else:
            mode_type = "Mixed (Y dominant)"
            mode_direction = "Y"
    
    mode_types.append(mode_type)
    mode_directions.append(mode_direction)
    
    freq_real = float(freq)
    freq_thz = freq_real * 0.029979
    print(f"{i+1:<8d} | {freq_real:18.1f} | {freq_thz:18.3f} | {mode_type:>15s} | {mode_direction:>15s}")

# ============================================================================
# 4. VISUALIZE MODES
# ============================================================================

print("\n" + "=" * 70)
print("3D VIBRATIONAL MODE VISUALIZATION")
print("=" * 70)

fig = plt.figure(figsize=(16, 12))
n_modes = min(3, len(frequencies))

for mode_idx in range(n_modes):
    ax = fig.add_subplot(2, 3, mode_idx + 1, projection='3d')
    
    hg_pos = adslab.positions[index_hg]
    disp = np.real(modes[mode_idx][0])
    
    disp_norm = np.linalg.norm(disp)
    if disp_norm > 1e-6:
        disp_scaled = disp / disp_norm * 0.3
    else:
        disp_scaled = disp * 0.3
    
    # Plot Au atoms
    au_positions = adslab.positions[:-1]
    ax.scatter(au_positions[:, 0], au_positions[:, 1], au_positions[:, 2], 
               c='gold', s=20, alpha=0.4, label='Au')
    
    # Highlight nearest Au atoms
    all_positions = adslab.positions
    distances = np.linalg.norm(all_positions - hg_pos, axis=1)
    nearest_indices = np.argsort(distances)[1:4]
    nearest_positions = all_positions[nearest_indices]
    ax.scatter(nearest_positions[:, 0], nearest_positions[:, 1], nearest_positions[:, 2],
               c='orange', s=60, alpha=0.8, label='Nearest Au')
    
    # Plot Hg
    ax.scatter([hg_pos[0]], [hg_pos[1]], [hg_pos[2]], 
               c='red', s=100, marker='o', label='Hg (eq.)')
    
    # Displaced position
    displaced_pos = hg_pos + disp_scaled
    ax.scatter([displaced_pos[0]], [displaced_pos[1]], [displaced_pos[2]], 
               c='blue', s=100, marker='^', label='Hg (disp.)')
    
    # Arrow
    ax.quiver(hg_pos[0], hg_pos[1], hg_pos[2],
              disp_scaled[0], disp_scaled[1], disp_scaled[2],
              color='red', linewidth=2, arrow_length_ratio=0.2)
    
    freq = float(frequencies[mode_idx])
    mode_type = mode_types[mode_idx]
    direction = mode_directions[mode_idx]
    ax.set_title(f'Mode {mode_idx+1}: {freq:.1f} cm⁻¹\n{mode_type} ({direction})', fontsize=11)
    ax.set_xlabel('X (Å)')
    ax.set_ylabel('Y (Å)')
    ax.set_zlabel('Z (Å)')
    ax.legend(loc='upper right', fontsize=7)
    ax.set_box_aspect([1, 1, 0.8])

# Top view
for mode_idx in range(n_modes):
    ax = fig.add_subplot(2, 3, mode_idx + 4)
    
    hg_pos = adslab.positions[index_hg]
    disp = np.real(modes[mode_idx][0])
    
    disp_norm = np.linalg.norm(disp)
    if disp_norm > 1e-6:
        disp_scaled = disp / disp_norm * 0.3
    else:
        disp_scaled = disp * 0.3
    
    # Top view of surface
    au_positions = adslab.positions[:-1]
    ax.scatter(au_positions[:, 0], au_positions[:, 1], 
               c='gold', s=20, alpha=0.4)
    
    # Nearest Au
    all_positions = adslab.positions
    distances = np.linalg.norm(all_positions - hg_pos, axis=1)
    nearest_indices = np.argsort(distances)[1:4]
    nearest_positions = all_positions[nearest_indices]
    ax.scatter(nearest_positions[:, 0], nearest_positions[:, 1],
               c='orange', s=60, alpha=0.8)
    
    # Hg equilibrium
    ax.scatter([hg_pos[0]], [hg_pos[1]], 
               c='red', s=80, marker='o', label='Equilibrium')
    
    # Arrow
    ax.arrow(hg_pos[0], hg_pos[1],
             disp_scaled[0], disp_scaled[1],
             head_width=0.08, head_length=0.08, fc='red', ec='red', linewidth=2)
    
    # Displaced
    displaced_pos = hg_pos + disp_scaled
    ax.scatter([displaced_pos[0]], [displaced_pos[1]], 
               c='blue', s=60, marker='^', label='Displaced')
    
    freq = float(frequencies[mode_idx])
    direction = mode_directions[mode_idx]
    ax.set_title(f'Mode {mode_idx+1}: {freq:.1f} cm⁻¹\nDirection: {direction}', fontsize=11)
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
# 5. SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"""
FINAL RESULTS:

1. Hg Adsorption Geometry:
   • Height above surface: {height:.3f} Å
   • Hg position: ({hg_pos[0]:.3f}, {hg_pos[1]:.3f}, {hg_pos[2]:.3f}) Å

2. Vibrational Modes:
""")

for i, (freq, mode_type, direction) in enumerate(zip(frequencies, mode_types, mode_directions)):
    freq_real = float(freq)
    print(f"   Mode {i+1}: {freq_real:6.1f} cm⁻¹ ({freq_real*0.029979:6.3f} THz)")
    print(f"             Type: {mode_type}, Direction: {direction}")

# ZPE
ZPE = 0.5 * 4.135667696e-15 * 1e12 * sum(float(freq) * 0.029979 for freq in frequencies if float(freq) > 0)
print(f"""
3. Zero-Point Energy: {ZPE:.4f} eV

4. Files Created:
   • relaxed_structure.xyz - Relaxed structure
   • vibrational_modes_3d.png - 3D mode visualization
   • vibrational_modes.txt - Data file
""")

print("\n" + "=" * 70)
print("✓ COMPLETE!")
print("=" * 70)
