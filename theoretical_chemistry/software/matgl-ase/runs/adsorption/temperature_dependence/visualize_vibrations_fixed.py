# visualize_vibrations_fixed.py
"""
Visualize Vibrational Modes of Hg on Au(111)
Using ASE Vibrations module with MatGL calculator
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
print("VIBRATIONAL MODE VISUALIZATION")
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
# Index of Hg atom (last atom added)
index_hg = len(adslab) - 1
print(f"Hg atom index: {index_hg}")

# Calculate vibrations for Hg atom only
vib = Vibrations(adslab, indices=[index_hg], name='vibrations_hg')
vib.run()

# Get frequencies and modes
frequencies = vib.get_frequencies()  # in cm^-1

print(f"\nVibrational modes of Hg on Au(111):")
print("-" * 60)
print(f"{'Mode':<8s} | {'Frequency (cm⁻¹)':>15s} | {'Frequency (THz)':>15s} | {'Type':>15s}")
print("-" * 60)

# Get modes and classify them
mode_types = []
modes = []

for i in range(len(frequencies)):
    # Get mode for this frequency
    mode = vib.get_mode(i)  # This returns the eigenvector
    modes.append(mode)
    
    # Get displacement for Hg atom (first atom in the indices list)
    hg_displacement = mode[0]  # First atom in the mode
    
    # Determine mode type based on dominant displacement
    if abs(hg_displacement[2]) > abs(hg_displacement[0]) and abs(hg_displacement[2]) > abs(hg_displacement[1]):
        mode_type = "Vertical"
    elif abs(hg_displacement[0]) > abs(hg_displacement[1]):
        mode_type = "Horizontal (x)"
    else:
        mode_type = "Horizontal (y)"
    
    mode_types.append(mode_type)
    print(f"{i+1:<8d} | {frequencies[i]:15.1f} | {frequencies[i]*0.029979:15.3f} | {mode_type:>15s}")

# ============================================================================
# 4. VISUALIZE MODES IN 3D
# ============================================================================

print("\n" + "=" * 70)
print("3D VIBRATIONAL MODE VISUALIZATION")
print("=" * 70)

# Create figure for 3D visualization
fig = plt.figure(figsize=(16, 12))

# Plot each mode in 3D
n_modes = min(3, len(frequencies))

for mode_idx in range(n_modes):
    ax = fig.add_subplot(2, 3, mode_idx + 1, projection='3d')
    
    # Get Hg position and displacement
    hg_pos = adslab.positions[index_hg]
    displacement = modes[mode_idx][0] * 0.5  # Scale for visualization
    
    # Get surface atoms (nearest neighbors)
    all_positions = adslab.positions
    distances = np.linalg.norm(all_positions - hg_pos, axis=1)
    nearest_indices = np.argsort(distances)[1:4]  # 3 nearest Au atoms
    
    # Plot Au surface atoms
    au_positions = adslab.positions[:-1]  # All except Hg
    ax.scatter(au_positions[:, 0], au_positions[:, 1], au_positions[:, 2], 
               c='gold', s=50, alpha=0.6, label='Au')
    
    # Highlight nearest Au atoms
    nearest_positions = all_positions[nearest_indices]
    ax.scatter(nearest_positions[:, 0], nearest_positions[:, 1], nearest_positions[:, 2],
               c='orange', s=100, alpha=0.8, label='Nearest Au')
    
    # Plot Hg atom (equilibrium position)
    ax.scatter([hg_pos[0]], [hg_pos[1]], [hg_pos[2]], 
               c='red', s=150, marker='o', label='Hg (equilibrium)')
    
    # Plot displaced Hg position
    displaced_pos = hg_pos + displacement
    ax.scatter([displaced_pos[0]], [displaced_pos[1]], [displaced_pos[2]], 
               c='blue', s=150, marker='^', label='Hg (displaced)')
    
    # Draw arrow for displacement
    ax.quiver(hg_pos[0], hg_pos[1], hg_pos[2],
              displacement[0], displacement[1], displacement[2],
              color='red', linewidth=2, arrow_length_ratio=0.2, label='Displacement')
    
    # Set labels and title
    freq = frequencies[mode_idx]
    mode_type = mode_types[mode_idx]
    ax.set_title(f'Mode {mode_idx+1}: {freq:.1f} cm⁻¹ ({mode_type})', fontsize=12)
    ax.set_xlabel('X (Å)')
    ax.set_ylabel('Y (Å)')
    ax.set_zlabel('Z (Å)')
    ax.legend(loc='upper right', fontsize=8)
    
    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 0.8])

# ============================================================================
# 5. PLOT DISPLACEMENT VECTORS (2D Top View)
# ============================================================================

# Plot 2: Top view of displacements
for mode_idx in range(n_modes):
    ax = fig.add_subplot(2, 3, mode_idx + 4)
    
    # Get Hg position and displacement
    hg_pos = adslab.positions[index_hg]
    displacement = modes[mode_idx][0] * 0.5
    
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
               c='red', s=100, marker='o', label='Equilibrium')
    
    # Plot displacement arrow
    ax.arrow(hg_pos[0], hg_pos[1],
             displacement[0], displacement[1],
             head_width=0.1, head_length=0.1, fc='red', ec='red', linewidth=2)
    
    # Plot displaced position
    displaced_pos = hg_pos + displacement
    ax.scatter([displaced_pos[0]], [displaced_pos[1]], 
               c='blue', s=80, marker='^', label='Displaced')
    
    freq = frequencies[mode_idx]
    mode_type = mode_types[mode_idx]
    ax.set_title(f'Mode {mode_idx+1}: {freq:.1f} cm⁻¹ ({mode_type}) - Top View', fontsize=12)
    ax.set_xlabel('X (Å)')
    ax.set_ylabel('Y (Å)')
    ax.legend(loc='upper right', fontsize=8)
    ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('vibrational_modes_3d.png', dpi=150)
print("✓ 3D visualization saved to vibrational_modes_3d.png")

# ============================================================================
# 6. CREATE ANIMATION OF VIBRATIONAL MODES
# ============================================================================

print("\n" + "=" * 70)
print("VIBRATIONAL MODE ANIMATION")
print("=" * 70)

def create_mode_animation(mode_idx, steps=20):
    """Create an animation of a vibrational mode"""
    freq = frequencies[mode_idx]
    mode = modes[mode_idx][0]
    amplitude = 0.3  # Å
    
    # Get Hg position
    hg_pos = adslab.positions[index_hg]
    
    # Generate frames
    frames = []
    for step in range(steps):
        phase = 2 * np.pi * step / steps
        displacement = amplitude * mode * np.sin(phase)
        displaced_pos = hg_pos + displacement
        
        # Create a copy of the structure
        frame = adslab.copy()
        frame.positions[index_hg] = displaced_pos
        
        frames.append(frame)
    
    return frames

try:
    import imageio.v2 as imageio
    import glob
    import os
    
    for mode_idx in range(n_modes):
        print(f"\nCreating animation for Mode {mode_idx+1}...")
        frames = create_mode_animation(mode_idx, steps=30)
        
        # Save as GIF
        images = []
        filenames = []
        
        for step, frame in enumerate(frames):
            # Create 2D top view for each frame
            fig, ax = plt.subplots(figsize=(6, 6))
            
            # Plot surface atoms
            au_positions = frame.positions[:-1]
            ax.scatter(au_positions[:, 0], au_positions[:, 1], 
                      c='gold', s=30, alpha=0.5)
            
            # Plot Hg
            hg_pos = frame.positions[index_hg]
            ax.scatter([hg_pos[0]], [hg_pos[1]], 
                      c='red', s=100, marker='o')
            
            # Add text
            freq = frequencies[mode_idx]
            ax.set_title(f'Mode {mode_idx+1}: {freq:.1f} cm⁻¹', fontsize=14)
            ax.set_xlabel('X (Å)')
            ax.set_ylabel('Y (Å)')
            ax.set_aspect('equal')
            ax.set_xlim(-2, 2)
            ax.set_ylim(-2, 2)
            
            plt.tight_layout()
            filename = f'temp_frame_{mode_idx}_{step:03d}.png'
            plt.savefig(filename, dpi=80)
            plt.close()
            filenames.append(filename)
        
        # Create GIF
        with imageio.get_writer(f'vibration_mode_{mode_idx+1}.gif', mode='I', duration=0.1, loop=0) as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)
        
        # Clean up
        for filename in filenames:
            os.remove(filename)
        
        print(f"✓ Animation saved to vibration_mode_{mode_idx+1}.gif")
        
except ImportError:
    print("⚠ imageio not installed. Install with: pip install imageio")
    print("  Skipping GIF creation...")

# ============================================================================
# 7. PRINT SUMMARY TABLE
# ============================================================================

print("\n" + "=" * 70)
print("VIBRATIONAL ANALYSIS SUMMARY")
print("=" * 70)

# Get Hg position relative to surface
hg_z = adslab.positions[index_hg][2]
surface_atoms = [pos[2] for pos in adslab.positions[:-1] if pos[2] < hg_z]
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
    print(f"  Mode {i+1}: {freq:6.1f} cm⁻¹ ({freq*0.029979:6.3f} THz) - {mode_type}")

# Calculate ZPE from frequencies
ZPE = 0.5 * 4.135667696e-15 * 1e12 * sum(freq * 0.029979 for freq in frequencies)
print(f"""
ZPE Corrections:
  • Zero-Point Energy: {ZPE:.4f} eV (from calculated frequencies)

Visualization Files Created:
  • relaxed_structure.xyz - Relaxed structure
  • vibrational_modes_3d.png - 3D mode visualization
""")

if n_modes >= 1:
    print("  • vibration_mode_1.gif - Animation of Mode 1")
if n_modes >= 2:
    print("  • vibration_mode_2.gif - Animation of Mode 2")
if n_modes >= 3:
    print("  • vibration_mode_3.gif - Animation of Mode 3")

# ============================================================================
# 8. SAVE VIBRATIONAL DATA
# ============================================================================

# Save vibrational data to file
with open('vibrational_modes.txt', 'w') as f:
    f.write("Vibrational Modes of Hg on Au(111)\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"{'Mode':<8s} | {'Frequency (cm⁻¹)':>15s} | {'Frequency (THz)':>15s} | {'Type':>15s}\n")
    f.write("-" * 60 + "\n")
    for i, (freq, mode_type) in enumerate(zip(frequencies, mode_types)):
        f.write(f"{i+1:<8d} | {freq:15.1f} | {freq*0.029979:15.3f} | {mode_type:>15s}\n")
    
    f.write("\n" + "=" * 60 + "\n")
    f.write(f"Hg height: {height:.3f} Å\n")
    f.write(f"Number of Au atoms: {len(slab)}\n")
    f.write(f"Zero-Point Energy: {ZPE:.4f} eV\n")

print("✓ Vibrational data saved to vibrational_modes.txt")

# ============================================================================
# 9. DISPLAY SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("✓ VIBRATIONAL ANALYSIS COMPLETE!")
print("=" * 70)
print("\nTo view the 3D visualization:")
print("  • Open vibrational_modes_3d.png")
if n_modes >= 1:
    print("  • Open vibration_mode_1.gif for animation")
if n_modes >= 2:
    print("  • Open vibration_mode_2.gif for animation")
if n_modes >= 3:
    print("  • Open vibration_mode_3.gif for animation")
print("\nTo view the structure in ASE GUI:")
print("  ase gui relaxed_structure.xyz")
