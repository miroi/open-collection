#!/usr/bin/env python
import os
import numpy as np
import matplotlib.pyplot as plt
import subprocess

# ==============================================
# TDOS Plotter for Quantum ESPRESSO
# ==============================================

def get_fermi_level():
    """Extract Fermi level from scf output"""
    try:
        with open('espresso.pwo', 'r') as f:
            for line in f:
                if 'the Fermi energy is' in line:
                    return float(line.split()[-2])
        print("Warning: Fermi level not found, using 0")
        return 0.0
    except Exception as e:
        print(f"Error reading Fermi level: {str(e)}, using 0")
        return 0.0

def plot_tdos():
    """Main function to plot total DOS with interactive controls"""
    print("\n=== Quantum ESPRESSO TDOS Plotter ===")
    
    # Check for DOS file
    dos_file = 'total_dos.dat'
    if not os.path.exists(dos_file):
        print(f"Error: {dos_file} not found")
        return
    
    # Get Fermi level
    fermi_level = get_fermi_level()
    print(f"\nFermi energy: {fermi_level:.4f} eV (Will be set to 0 in plots)\n")
    
    # Load DOS data
    try:
        dos_data = np.loadtxt(dos_file)
        if dos_data.size == 0:
            print("Error: Empty DOS file")
            return
    except Exception as e:
        print(f"Error loading DOS data: {str(e)}")
        return
    
    # Interactive energy range selection
    while True:
        energy_range = input("Enter energy range [min,max] (default: -10,5): ").strip()
        if not energy_range:
            energy_range = (-10, 5)
            break
        try:
            emin, emax = map(float, energy_range.split(','))
            energy_range = (emin, emax)
            break
        except:
            print(" !!! Invalid format. Please use 'min,max' (e.g., -8,4) or press Enter for default")
    
    # Calculate y-range based on visible data
    energies = dos_data[:,0] - fermi_level
    dos_values = dos_data[:,1]
    
    # Find indices within the selected energy range
    mask = (energies >= energy_range[0]) & (energies <= energy_range[1])
    visible_dos = dos_values[mask]
    
    if len(visible_dos) == 0:
        print("Warning: No data points in selected energy range, using full y-range")
        y_min, y_max = 0, np.max(dos_values) * 1.1
    else:
        y_min = 0
        y_max = np.max(visible_dos) * 1.1  # Add 10% padding
    
    # Interactive y-range adjustment
    print(f"\nSuggested y-range: [0, {y_max:.2f}]")
    while True:
        y_range = input(f"Enter y-range [min,max] (press Enter to accept suggestion): ").strip()
        if not y_range:
            y_range = (y_min, y_max)
            break
        try:
            ymin, ymax = map(float, y_range.split(','))
            y_range = (ymin, ymax)
            break
        except:
            print(" !!! Invalid format. Please use 'min,max' (e.g., 0,10) or press Enter to accept suggestion")
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(energies, dos_values, 'k-', lw=1.5, label='Total DOS')
    plt.axvline(x=0, color='r', linestyle='--', linewidth=1, label='Fermi level')
    
    # Apply ranges
    plt.xlim(*energy_range)
    plt.ylim(*y_range)
    
    # Labels and formatting
    plt.xlabel('Energy (eV)', fontsize=12)
    plt.ylabel('DOS (states/eV)', fontsize=12)
    plt.title('Total Density of States', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(alpha=0.3)
    
    # Save plot
    plot_file = 'total_dos.png'
    plt.savefig(plot_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nTDOS plot saved to {plot_file}")
    print("\n=== TDOS Plotting Complete ===")

if __name__ == "__main__":
    plot_tdos()