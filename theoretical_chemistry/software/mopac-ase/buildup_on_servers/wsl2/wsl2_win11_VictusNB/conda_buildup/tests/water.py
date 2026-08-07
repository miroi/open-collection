#!/usr/bin/env python3
"""
MOPAC calculations using direct subprocess calls
Works with any MOPAC version including v23.2.5
"""

from ase import Atoms
from ase.io import write
import numpy as np
import subprocess
import os
import re

def run_mopac(method='PM7', task='singlepoint', atoms=None):
    """
    Run MOPAC calculation directly
    """
    if atoms is None:
        raise ValueError("Atoms object required")
    
    # Build coordinates string
    coord_lines = []
    for i, (symbol, pos) in enumerate(zip(atoms.symbols, atoms.positions)):
        coord_lines.append(f"{symbol}    {pos[0]:.6f}    {pos[1]:.6f}    {pos[2]:.6f}")
    coord_string = "\n".join(coord_lines)
    
    # Set keywords
    keywords = '1SCF' if task == 'singlepoint' else ''
    
    # Write input file
    input_file = 'mopac_input.mop'
    with open(input_file, 'w') as f:
        f.write(f"{method} XYZ {keywords}\n")
        f.write("MOPAC calculation\n\n")
        f.write(coord_string)
        f.write("\n")
    
    # Run MOPAC
    subprocess.run(f"mopac {input_file}", shell=True, capture_output=True)
    
    # Parse output
    output_file = 'mopac_input.out'
    results = {}
    
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            content = f.read()
        
        # Parse energy
        energy_match = re.search(r'FINAL HEAT OF FORMATION\s*=\s*([-\d.]+)', content)
        if energy_match:
            energy_kcal = float(energy_match.group(1))
            results['energy'] = energy_kcal / 23.061
            results['energy_kcal'] = energy_kcal
        
        # Parse dipole
        dipole_match = re.search(r'DIPOLE\s+.*TOTAL\s+([\d.]+)', content, re.DOTALL)
        if dipole_match:
            results['dipole'] = float(dipole_match.group(1))
        
        # Parse optimized coordinates - find "CARTESIAN COORDINATES" section
        # Look for the section with optimized coordinates (after optimization)
        coord_pattern = r'CARTESIAN COORDINATES\s*\n\s*\n(?:\s*\d+\s+[A-Z][a-z]?\s+[-\d.]+\s+[-\d.]+\s+[-\d.]+\s*\n)+'
        coord_section = re.search(coord_pattern, content)
        
        if coord_section:
            # Extract individual coordinates
            atom_pattern = r'(\d+)\s+([A-Z][a-z]?)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)'
            matches = re.findall(atom_pattern, coord_section.group(0))
            
            if matches:
                coords = []
                symbols = []
                for match in matches:
                    symbols.append(match[1])
                    coords.append([float(match[2]), float(match[3]), float(match[4])])
                results['symbols'] = symbols
                results['coordinates'] = np.array(coords)
        
        # If the above fails, try alternative parsing
        if 'coordinates' not in results:
            atom_pattern = r'\n\s*(\d+)\s+([A-Z][a-z]?)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s*\n'
            matches = re.findall(atom_pattern, content)
            if matches:
                # Skip the first few lines which might be input coordinates
                # Take the last N atoms matching input size
                n_atoms = len(atoms)
                matches = matches[-n_atoms:] if len(matches) >= n_atoms else matches
                coords = []
                symbols = []
                for match in matches:
                    symbols.append(match[1])
                    coords.append([float(match[2]), float(match[3]), float(match[4])])
                if len(coords) == n_atoms:
                    results['symbols'] = symbols
                    results['coordinates'] = np.array(coords)
        
        # Parse charges
        charges = []
        charge_pattern = r'(\d+)\s+([A-Z][a-z]?)\s+([-\d.]+)\s+([\d.]+)'
        charge_matches = re.findall(charge_pattern, content)
        if charge_matches:
            n_atoms = len(atoms)
            charges = [float(match[2]) for match in charge_matches[:n_atoms]]
            results['charges'] = np.array(charges)
        
        # Parse HOMO-LUMO
        homo_match = re.search(r'HOMO LUMO ENERGIES \(EV\)\s*=\s*([-\d.]+)\s+([-\d.]+)', content)
        if homo_match:
            results['homo'] = float(homo_match.group(1))
            results['lumo'] = float(homo_match.group(2))
            results['gap'] = results['lumo'] - results['homo']
        
        # Parse gradient
        grad_match = re.search(r'GRADIENT NORM\s*=\s*([-\d.]+)', content)
        if grad_match:
            results['gradient'] = float(grad_match.group(1))
    
    # Clean up
    for f in ['mopac_input.mop', 'mopac_input.out', 'mopac_input.arc']:
        if os.path.exists(f):
            os.remove(f)
    
    return results

# Create water molecule
water = Atoms('H2O',
              positions=[[0.000, 0.000, 0.000],
                        [0.757, 0.586, 0.000],
                        [-0.757, 0.586, 0.000]],
              cell=[10.0, 10.0, 10.0])

print("=" * 60)
print("MOPAC CALCULATIONS FOR WATER MOLECULE")
print("=" * 60)

# 1. Single point energy
print("\n1. Single point energy calculation...")
results = run_mopac(method='PM7', task='singlepoint', atoms=water)

if 'energy' in results:
    print(f"   Total energy: {results['energy']:.6f} eV")
    print(f"   Heat of formation: {results['energy_kcal']:.4f} kcal/mol")
if 'dipole' in results:
    print(f"   Dipole moment: {results['dipole']:.4f} Debye")
if 'charges' in results:
    print("   Mulliken charges:")
    for i, (symbol, charge) in enumerate(zip(water.symbols, results['charges'])):
        print(f"     {symbol}{i+1}: {charge:.4f} e")

# 2. Geometry optimization
print("\n2. Geometry optimization...")
results = run_mopac(method='PM7', task='optimize', atoms=water)

if 'energy' in results:
    print(f"   Optimized energy: {results['energy']:.6f} eV")
    print(f"   Heat of formation: {results['energy_kcal']:.4f} kcal/mol")

if 'coordinates' in results:
    print("\n   Optimized geometry:")
    for i, (symbol, pos) in enumerate(zip(results['symbols'], results['coordinates'])):
        print(f"     {symbol}{i+1}: {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f}")
    # Update atoms
    water.positions = results['coordinates']
else:
    print("\n   Warning: Could not parse optimized coordinates")

if 'dipole' in results:
    print(f"\n   Optimized dipole: {results['dipole']:.4f} Debye")

if 'charges' in results:
    print("\n   Optimized Mulliken charges:")
    for i, (symbol, charge) in enumerate(zip(water.symbols, results['charges'])):
        print(f"     {symbol}{i+1}: {charge:.4f} e")

if 'homo' in results:
    print(f"\n   HOMO energy: {results['homo']:.4f} eV")
    print(f"   LUMO energy: {results['lumo']:.4f} eV")
    print(f"   HOMO-LUMO gap: {results['gap']:.4f} eV")

if 'gradient' in results:
    print(f"   Gradient norm: {results['gradient']:.4f}")

# Save results
write('water_mopac_opt.xyz', water)
print(f"\n✅ Results saved to water_mopac_opt.xyz")
