#!/usr/bin/env python
import os
import numpy as np
import subprocess
import glob
import matplotlib.pyplot as plt
import re

# ====================================================
# PDOS Plotter - non-spinpolarized without Spin-orbit
# ====================================================

def sum_pdos_files(files_to_sum, output_file):
    """Sum multiple PDOS files using sumpdos.x"""
    print(f"  Summing {len(files_to_sum)} components -> {os.path.basename(output_file)}")
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        #update sum_pdos executable here
        cmd = ["/lustre/home/user/m/milias/work/software/quantum-espresso/qe-develop/q-e/build_intelmpi_mkl_elpa/bin/sumpdos.x", *files_to_sum]
        
        with open(output_file, 'w') as fout:
            result = subprocess.run(
                cmd,
                stdout=fout,
                stderr=subprocess.PIPE,
                check=False
            )
        
        if result.returncode != 0:
            print(f"  !!! Sum failed (code {result.returncode})")
            if result.stderr:
                print(f"  Error: {result.stderr.decode().strip()}")
            return False

        if not os.path.exists(output_file):
            print("  !!! No output file created")
            return False

        print(f"  Created summed file: {os.path.basename(output_file)}")
        return True

    except Exception as e:
        print(f"  !!! Summing error: {str(e)}")
        return False

def get_fermi_level():
    """Extract Fermi level from espresso.pwo file"""
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

def analyze_available_pdos():
    """Analyze available PDOS files with proper orbital parsing"""
    pdos_files = glob.glob('pdos_results/pdos.pdos_atm#*')
    atoms_info = {}
    
    for fname in pdos_files:
        try:
            # Extract atom number, symbol and orbital using regex
            match = re.match(r'pdos.pdos_atm#(\d+)\(([A-Za-z]+)\)_wfc#\d+\(([spdf])\)', os.path.basename(fname))
            if not match:
                continue
                
            atom_num = int(match.group(1))
            symbol = match.group(2)
            orbital = match.group(3).lower()
            
            if atom_num not in atoms_info:
                atoms_info[atom_num] = {
                    'symbol': symbol,
                    'orbitals': {},
                    'total_files': 0
                }
            
            atoms_info[atom_num]['total_files'] += 1
            
            if orbital not in atoms_info[atom_num]['orbitals']:
                atoms_info[atom_num]['orbitals'][orbital] = {
                    'count': 0,
                    'sum_exists': False
                }
            
            atoms_info[atom_num]['orbitals'][orbital]['count'] += 1
            
            # Check if summed file exists
            summed_file = f'pdos_results/summed/pdos.sum_atm#{atom_num}({symbol})_{orbital}.dat'
            atoms_info[atom_num]['orbitals'][orbital]['sum_exists'] = os.path.exists(summed_file)
            
        except Exception as e:
            print(f"Warning: Could not parse {os.path.basename(fname)}: {str(e)}")
            continue
    
    return atoms_info

def get_energy_range():
    """Get energy range from user input"""
    while True:
        energy_range = input("\nEnter energy range [min,max] (default: -10,5): ").strip()
        if not energy_range:
            return (-10, 5)
        try:
            emin, emax = map(float, energy_range.split(','))
            return (emin, emax)
        except:
            print(" !!! Invalid format. Please use 'min,max' (e.g., -8,4) or press Enter for default")

def get_y_range(dos_data, energy_range, fermi_level):
    """Calculate and get y-range from user input"""
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
            return (y_min, y_max)
        try:
            ymin, ymax = map(float, y_range.split(','))
            return (ymin, ymax)
        except:
            print(" !!! Invalid format. Please use 'min,max' (e.g., 0,10) or press Enter to accept suggestion")

def plot_pdos():
    """Main function to plot PDOS with proper orbital display"""
    print("\n=== Quantum ESPRESSO PDOS Plotter ===")
     
    # Get Fermi level
    fermi_level = get_fermi_level()
    print(f"\nFermi energy: {fermi_level:.4f} eV (Will be set to 0 in plots)\n")
    
    # Get energy range (asked only once)
    energy_range = get_energy_range()
    
    # Analyze available PDOS files
    atoms_info = analyze_available_pdos()
    if not atoms_info:
        print("Error: No PDOS files found in pdos_results/")
        return
    
    # Display available atoms with orbital info
    print("Available atoms and projected dos file:")
    for atom_num, info in sorted(atoms_info.items()):
        symbol = info['symbol']
        orbital_info = []
        summed_info = []
        
        for orbital, data in sorted(info['orbitals'].items()):
            orbital_info.append(f"{orbital}({data['count']})")
            if data['count'] > 1 and data['sum_exists']:
                summed_info.append(f"{orbital}({data['count']})")
        
        # Build the output line
        output_line = f"Atom {atom_num} ({symbol}): {info['total_files']} PDOS files, " + " ".join(orbital_info)
        if summed_info:
            output_line += f" - sum of {' '.join(summed_info)} already exists"
        print(output_line)
    
    # Interactive selection
    selected_atoms = input("\nEnter atom numbers (comma-separated or 'all'): ").strip()
    if selected_atoms.lower() == 'all':
        selected_atoms = list(atoms_info.keys())
    else:
        try:
            selected_atoms = [int(x.strip()) for x in selected_atoms.split(',')]
            invalid_atoms = [x for x in selected_atoms if x not in atoms_info]
            if invalid_atoms:
                print(f"Error: Invalid atoms: {invalid_atoms}")
                return
        except ValueError:
            print("Error: Invalid input format")
            return
    
    available_orbitals = sorted({orb for info in atoms_info.values() for orb in info['orbitals']})
    print(f"\nAvailable orbitals: {', '.join(available_orbitals)}")
    orbitals = input("Enter orbitals (comma-separated or 'all'): ").strip().lower()
    if orbitals == 'all':
        orbitals = None  # Will use all available orbitals
    else:
        orbitals = [x.strip() for x in orbitals.split(',')]
        invalid_orbitals = [x for x in orbitals if x not in available_orbitals]
        if invalid_orbitals:
            print(f"Error: Invalid orbitals: {invalid_orbitals}")
            return
    
    # Color scheme for orbitals
    colors = {'s': 'red', 'p': 'green', 'd': 'blue', 'f': 'purple'}
    
    # Create summed directory if needed
    os.makedirs('pdos_results/summed', exist_ok=True)
    
    # First pass to collect all data for y-range calculation
    all_visible_dos = []
    for atom_num in selected_atoms:
        symbol = atoms_info[atom_num]['symbol']
        atom_orbitals = orbitals if orbitals else atoms_info[atom_num]['orbitals'].keys()
        
        for orbital in sorted(atom_orbitals):
            if orbital not in atoms_info[atom_num]['orbitals']:
                continue
            
            orbital_data = atoms_info[atom_num]['orbitals'][orbital]
            summed_file = f'pdos_results/summed/pdos.sum_atm#{atom_num}({symbol})_{orbital}.dat'
            
            if orbital_data['count'] > 1:
                if orbital_data['sum_exists']:
                    data_file = summed_file
                else:
                    components = glob.glob(f'pdos_results/pdos.pdos_atm#{atom_num}({symbol})_wfc#*({orbital})')
                    if not sum_pdos_files(components, summed_file):
                        continue
                    data_file = summed_file
            else:
                data_file = glob.glob(f'pdos_results/pdos.pdos_atm#{atom_num}({symbol})_wfc#*({orbital})')[0]
            
            try:
                data = np.loadtxt(data_file)
                if data.size == 0:
                    continue
                
                energies = data[:,0] - fermi_level
                dos_values = data[:,1]
                mask = (energies >= energy_range[0]) & (energies <= energy_range[1])
                all_visible_dos.extend(dos_values[mask])
            except:
                continue
    
    # Get y-range based on all visible data
    if all_visible_dos:
        y_range = get_y_range(np.column_stack(([0]*len(all_visible_dos), all_visible_dos)), energy_range, 0)
    else:
        print("Warning: No data points in selected energy range, using default y-range")
        y_range = (0, 10)  # Default fallback
    
    # Second pass to actually plot
    for atom_num in selected_atoms:
        symbol = atoms_info[atom_num]['symbol']
        print(f"\nProcessing Atom {atom_num} ({symbol}):")
        
        plt.figure(figsize=(10, 6))
        has_data = False
        
        # Determine which orbitals to plot for this atom
        atom_orbitals = orbitals if orbitals else atoms_info[atom_num]['orbitals'].keys()
        
        for orbital in sorted(atom_orbitals):
            if orbital not in atoms_info[atom_num]['orbitals']:
                print(f"  {orbital}-orbital not available")
                continue
            
            orbital_data = atoms_info[atom_num]['orbitals'][orbital]
            summed_file = f'pdos_results/summed/pdos.sum_atm#{atom_num}({symbol})_{orbital}.dat'
            
            if orbital_data['count'] > 1:
                if orbital_data['sum_exists']:
                    print(f"  Using existing sum: {orbital}({orbital_data['count']})")
                    data_file = summed_file
                else:
                    components = glob.glob(f'pdos_results/pdos.pdos_atm#{atom_num}({symbol})_wfc#*({orbital})')
                    print(f"  Summing {orbital}({len(components)}): {os.path.basename(summed_file)}")
                    if sum_pdos_files(components, summed_file):
                        data_file = summed_file
                    else:
                        continue
            else:
                print(f"  Using single: {orbital}(1)")
                data_file = glob.glob(f'pdos_results/pdos.pdos_atm#{atom_num}({symbol})_wfc#*({orbital})')[0]
            
            # Plot the data
            try:
                data = np.loadtxt(data_file)
                if data.size == 0:
                    print(f"  !!! Empty file: {os.path.basename(data_file)}")
                    continue
                
                plt.plot(data[:,0] - fermi_level, data[:,1], 
                        color=colors.get(orbital, 'black'),
                        lw=1.5,
                        label=f'{orbital}-orbital')
                has_data = True
            except Exception as e:
                print(f"  !!! Plot error: {str(e)}")
        
        # Finalize and save plot if we have data
        if has_data:
            plt.axvline(x=0, color='r', linestyle='--', linewidth=1, label='Fermi level')
            plt.xlabel('Energy (eV)', fontsize=12)
            plt.ylabel('PDOS (states/eV)', fontsize=12)
            
            # Apply the ranges
            plt.xlim(*energy_range)
            plt.ylim(*y_range)
            
            plt.title(f'Projected DOS for Atom {atom_num} ({symbol})', fontsize=14)
            plt.legend(fontsize=10)
            plt.grid(alpha=0.3)
            plot_file = f'pdos_atom_{atom_num}.png'
            plt.savefig(plot_file, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"  PDOS plot saved to {plot_file}")
        else:
            plt.close()
            print("  No PDOS data available for plotting")
    
    print("\n=== PDOS Plotting Complete ===")

if __name__ == "__main__":
    plot_pdos()