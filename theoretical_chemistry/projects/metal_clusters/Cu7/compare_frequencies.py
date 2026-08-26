#!/usr/bin/env python3
"""
Compare vibrational frequencies between EMT and MACE for Cu7 cluster
Load frequencies from saved text files
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import re

def load_frequencies_from_file(filename):
    """Load frequencies from the saved text file"""
    frequencies = []
    
    if not os.path.exists(filename):
        print(f"  File not found: {filename}")
        return None
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        # Find the frequency table
        in_table = False
        for line in lines:
            # Skip header lines
            if 'Mode' in line and 'Frequency' in line:
                in_table = True
                continue
            if '--------' in line and in_table:
                continue
            
            if in_table:
                # Try to parse frequency from line
                # Format: "   1    0.00+1.95j     0.00+0.24j     Rotation"
                # or: "   1    0.00         0.00     Translation"
                parts = line.strip().split()
                if len(parts) >= 4:
                    # Check if it's a frequency line (starts with a number)
                    if parts[0].isdigit():
                        # Get the frequency (second column)
                        freq_str = parts[1]
                        # Handle complex numbers like "0.00+1.95j"
                        if '+' in freq_str or '-' in freq_str:
                            # Extract real part
                            real_part = freq_str.split('+')[0] if '+' in freq_str else freq_str.split('-')[0]
                            try:
                                freq = float(real_part)
                                frequencies.append(freq)
                            except:
                                pass
                        else:
                            try:
                                freq = float(freq_str)
                                frequencies.append(freq)
                            except:
                                pass
    except Exception as e:
        print(f"  Error reading {filename}: {e}")
        return None
    
    return np.array(frequencies)

def load_frequencies_from_vibrations(label):
    """Try to load frequencies from Vibrations object"""
    try:
        from ase.vibrations import Vibrations
        from ase.io import read
        
        # Try to read the optimized structure
        struct_file = f'cu7_optimized_{label.lower()}.xyz'
        if os.path.exists(struct_file):
            atoms = read(struct_file)
            # Try to load vibrations
            vib_name = f'cu7_vibrations_{label.lower()}'
            vib = Vibrations(atoms, name=vib_name)
            
            # Try to get frequencies
            try:
                frequencies = vib.get_frequencies()
                return np.real(frequencies)
            except:
                pass
    except:
        pass
    
    return None

def load_frequencies(label):
    """Load frequencies from available sources"""
    
    print(f"\nLoading {label} frequencies...")
    
    # Method 1: Try text file first
    freq_file = f'cu7_frequencies_{label.lower()}.txt'
    freqs = load_frequencies_from_file(freq_file)
    
    if freqs is not None:
        print(f"  ✓ Loaded {len(freqs)} frequencies from {freq_file}")
        return freqs
    
    # Method 2: Try Vibrations object
    freqs = load_frequencies_from_vibrations(label)
    if freqs is not None:
        print(f"  ✓ Loaded {len(freqs)} frequencies from Vibrations object")
        return freqs
    
    print(f"  ✗ Could not load {label} frequencies")
    return None

def plot_frequency_comparison(emt_freqs, mace_freqs):
    """Plot comparison of vibrational frequencies"""
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Filter out translations/rotations (freq < 10 cm⁻¹)
    emt_vib = emt_freqs[emt_freqs > 10]
    mace_vib = mace_freqs[mace_freqs > 10]
    
    # Make sure we have the same number of modes
    n_modes = min(len(emt_vib), len(mace_vib))
    emt_vib = emt_vib[:n_modes]
    mace_vib = mace_vib[:n_modes]
    
    # Plot 1: Stick spectra comparison
    ax1 = axes[0, 0]
    x_pos = np.arange(n_modes)
    width = 0.35
    
    ax1.bar(x_pos - width/2, emt_vib, width, label='EMT', color='blue', alpha=0.7)
    ax1.bar(x_pos + width/2, mace_vib, width, label='MACE', color='red', alpha=0.7)
    ax1.set_xlabel('Mode Number')
    ax1.set_ylabel('Frequency (cm⁻¹)')
    ax1.set_title('Vibrational Frequencies Comparison')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Add value labels
    for i, (e, m) in enumerate(zip(emt_vib, mace_vib)):
        ax1.text(i - width/2, e + 2, f'{e:.0f}', ha='center', va='bottom', fontsize=8)
        ax1.text(i + width/2, m + 2, f'{m:.0f}', ha='center', va='bottom', fontsize=8)
    
    # Plot 2: Frequency differences
    ax2 = axes[0, 1]
    diff = mace_vib - emt_vib
    ax2.bar(range(len(diff)), diff, color='green', alpha=0.7)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax2.set_xlabel('Mode Number')
    ax2.set_ylabel('Frequency Difference (cm⁻¹)')
    ax2.set_title('MACE - EMT Frequency Difference')
    ax2.grid(True, alpha=0.3)
    
    # Add value labels
    for i, d in enumerate(diff):
        ax2.text(i, d + (5 if d > 0 else -15), f'{d:.1f}', 
                ha='center', va='bottom' if d > 0 else 'top', fontsize=8)
    
    # Plot 3: Scatter plot
    ax3 = axes[1, 0]
    ax3.scatter(emt_vib, mace_vib, s=100, c='purple', alpha=0.7)
    
    # Add identity line
    max_freq = max(max(emt_vib), max(mace_vib)) + 10
    ax3.plot([0, max_freq], [0, max_freq], 'k--', alpha=0.5, label='y=x')
    
    # Add best fit line
    z = np.polyfit(emt_vib, mace_vib, 1)
    p = np.poly1d(z)
    ax3.plot(emt_vib, p(emt_vib), 'r-', alpha=0.5, 
             label=f'y = {z[0]:.2f}x + {z[1]:.1f}')
    
    ax3.set_xlabel('EMT Frequency (cm⁻¹)')
    ax3.set_ylabel('MACE Frequency (cm⁻¹)')
    ax3.set_title('EMT vs MACE Frequencies')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Histogram of differences
    ax4 = axes[1, 1]
    ax4.hist(diff, bins=10, color='orange', alpha=0.7, edgecolor='black')
    ax4.axvline(x=np.mean(diff), color='red', linestyle='--', 
                label=f'Mean: {np.mean(diff):.1f} cm⁻¹')
    ax4.axvline(x=np.median(diff), color='blue', linestyle='--', 
                label=f'Median: {np.median(diff):.1f} cm⁻¹')
    ax4.set_xlabel('Frequency Difference (cm⁻¹)')
    ax4.set_ylabel('Number of Modes')
    ax4.set_title('Distribution of Frequency Differences')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('cu7_frequency_comparison.png', dpi=300, bbox_inches='tight')
    print("\n✓ Frequency comparison plot saved to: cu7_frequency_comparison.png")
    plt.show()

def print_frequency_table(emt_freqs, mace_freqs):
    """Print a comparison table of frequencies"""
    
    # Filter out translations/rotations
    emt_vib = emt_freqs[emt_freqs > 10]
    mace_vib = mace_freqs[mace_freqs > 10]
    
    # Make sure we have the same number of modes
    n_modes = min(len(emt_vib), len(mace_vib))
    emt_vib = emt_vib[:n_modes]
    mace_vib = mace_vib[:n_modes]
    
    print("\n" + "=" * 70)
    print("Vibrational Frequencies Comparison Table")
    print("=" * 70)
    print(f"{'Mode':>6} {'EMT (cm⁻¹)':>14} {'MACE (cm⁻¹)':>14} {'Difference':>14} {'% Diff':>10}")
    print("-" * 70)
    
    for i in range(n_modes):
        diff = mace_vib[i] - emt_vib[i]
        pct_diff = (diff / emt_vib[i]) * 100 if emt_vib[i] != 0 else 0
        print(f"{i+1:6d} {emt_vib[i]:14.2f} {mace_vib[i]:14.2f} {diff:14.2f} {pct_diff:9.1f}%")
    
    print("-" * 70)
    print(f"{'Average:':>6} {np.mean(emt_vib):14.2f} {np.mean(mace_vib):14.2f} {np.mean(mace_vib - emt_vib):14.2f}")
    print(f"{'Std Dev:':>6} {np.std(emt_vib):14.2f} {np.std(mace_vib):14.2f}")
    print("=" * 70)
    
    # Statistics
    print("\n📊 Statistics:")
    print(f"  Number of vibrational modes: {n_modes}")
    print(f"  Average EMT frequency:  {np.mean(emt_vib):.1f} cm⁻¹")
    print(f"  Average MACE frequency: {np.mean(mace_vib):.1f} cm⁻¹")
    print(f"  Mean difference:        {np.mean(mace_vib - emt_vib):.1f} cm⁻¹")
    print(f"  RMS difference:         {np.sqrt(np.mean((mace_vib - emt_vib)**2)):.1f} cm⁻¹")
    print(f"  Correlation coefficient: {np.corrcoef(emt_vib, mace_vib)[0,1]:.4f}")

def display_frequency_summary(emt_freqs, mace_freqs):
    """Display the frequency content summary"""
    
    emt_vib = emt_freqs[emt_freqs > 10]
    mace_vib = mace_freqs[mace_freqs > 10]
    
    n_modes = min(len(emt_vib), len(mace_vib))
    emt_vib = emt_vib[:n_modes]
    mace_vib = mace_vib[:n_modes]
    
    print("\n" + "=" * 70)
    print("Frequency Distribution Summary")
    print("=" * 70)
    
    # Classify modes by frequency range
    ranges = [(0, 100, "Low (<100)"),
              (100, 200, "Medium (100-200)"),
              (200, 300, "High (200-300)"),
              (300, 400, "Very High (>300)")]
    
    print("\nEMT Frequency Distribution:")
    for low, high, label in ranges:
        count = np.sum((emt_vib >= low) & (emt_vib < high))
        print(f"  {label}: {count:2d} modes ({count/n_modes*100:5.1f}%)")
    
    print("\nMACE Frequency Distribution:")
    for low, high, label in ranges:
        count = np.sum((mace_vib >= low) & (mace_vib < high))
        print(f"  {label}: {count:2d} modes ({count/n_modes*100:5.1f}%)")

def main():
    """Main function to compare frequencies"""
    
    print("=" * 60)
    print("Cu7 Vibrational Frequencies: EMT vs MACE Comparison")
    print("=" * 60)
    
    # Check for frequency files
    print("\nChecking for frequency files...")
    emt_file = 'cu7_frequencies_emt.txt'
    mace_file = 'cu7_frequencies_mace.txt'
    
    if not os.path.exists(emt_file):
        print(f"  ⚠️  {emt_file} not found")
    else:
        print(f"  ✓ {emt_file} found")
    
    if not os.path.exists(mace_file):
        print(f"  ⚠️  {mace_file} not found")
    else:
        print(f"  ✓ {mace_file} found")
    
    # Load frequencies
    emt_freqs = load_frequencies('EMT')
    mace_freqs = load_frequencies('MACE')
    
    if emt_freqs is None:
        print("\n❌ Could not load EMT frequencies!")
        print("Please run the optimization script first.")
        return
    
    if mace_freqs is None:
        print("\n❌ Could not load MACE frequencies!")
        print("Please run the optimization script first.")
        return
    
    print(f"\n✓ Loaded {len(emt_freqs)} EMT frequencies")
    print(f"✓ Loaded {len(mace_freqs)} MACE frequencies")
    
    # Display the full frequency table
    print_frequency_table(emt_freqs, mace_freqs)
    
    # Display distribution summary
    display_frequency_summary(emt_freqs, mace_freqs)
    
    # Create comparison plots
    plot_frequency_comparison(emt_freqs, mace_freqs)
    
    # Save comparison data to file
    with open('cu7_frequency_comparison.txt', 'w') as f:
        f.write("Cu7 Vibrational Frequencies: EMT vs MACE\n")
        f.write("=" * 70 + "\n\n")
        
        emt_vib = emt_freqs[emt_freqs > 10]
        mace_vib = mace_freqs[mace_freqs > 10]
        n_modes = min(len(emt_vib), len(mace_vib))
        emt_vib = emt_vib[:n_modes]
        mace_vib = mace_vib[:n_modes]
        
        f.write(f"{'Mode':>6} {'EMT (cm⁻¹)':>14} {'MACE (cm⁻¹)':>14} {'Difference':>14}\n")
        f.write("-" * 70 + "\n")
        
        for i in range(n_modes):
            diff = mace_vib[i] - emt_vib[i]
            f.write(f"{i+1:6d} {emt_vib[i]:14.2f} {mace_vib[i]:14.2f} {diff:14.2f}\n")
        
        f.write("-" * 70 + "\n")
        f.write(f"{'Average:':>6} {np.mean(emt_vib):14.2f} {np.mean(mace_vib):14.2f} {np.mean(mace_vib - emt_vib):14.2f}\n")
        f.write("=" * 70 + "\n")
    
    print("\n✓ Comparison data saved to: cu7_frequency_comparison.txt")
    print("\n" + "=" * 60)
    print("✅ Comparison complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
