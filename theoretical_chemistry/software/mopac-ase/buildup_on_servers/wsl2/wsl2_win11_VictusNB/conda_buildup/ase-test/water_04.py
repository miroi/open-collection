#!/usr/bin/env python3
"""
MOPAC parser for water molecule with additional properties
"""

from ase.build import molecule
from ase.io import write
import subprocess
import os
import re
import numpy as np

# Get water from ASE database
water = molecule('H2O')
water.set_cell([10.0, 10.0, 10.0])
water.center()

print("Initial water geometry (from ASE):")
for i, (symbol, pos) in enumerate(zip(water.symbols, water.positions)):
    print(f"  {symbol}{i+1}: {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f}")

# Write input file
with open('water.mop', 'w') as f:
    f.write("PM7 XYZ\nWater optimization\n\n")
    for atom, pos in zip(water.symbols, water.positions):
        f.write(f"{atom}    {pos[0]:.6f}    {pos[1]:.6f}    {pos[2]:.6f}\n")
    f.write("\n")

# Run MOPAC
print("\nRunning MOPAC optimization...")
subprocess.run('mopac water.mop', shell=True, capture_output=True)

# Parse output
if os.path.exists('water.out'):
    with open('water.out', 'r') as f:
        content = f.read()
        lines = content.split('\n')
    
    print("=" * 60)
    print("MOPAC RESULTS FOR WATER")
    print("=" * 60)
    
    # 1. Energy
    match = re.search(r'FINAL HEAT OF FORMATION\s*=\s*([-\d.]+)', content)
    if match:
        kcal = float(match.group(1))
        ev = kcal / 23.061
        print(f"\nEnergy: {ev:.6f} eV")
        print(f"       {kcal:.4f} kcal/mol")
    
    # 2. Dipole
    dipole_found = False
    for i, line in enumerate(lines):
        if 'DIPOLE' in line and 'X' in line and 'Y' in line and 'Z' in line:
            for j in range(i+1, min(i+5, len(lines))):
                if 'POINT-CHG' in lines[j] or 'SUM' in lines[j]:
                    parts = lines[j].strip().split()
                    if len(parts) >= 5:
                        try:
                            dipole = float(parts[-1])
                            print(f"\nDipole: {dipole:.4f} Debye")
                            dipole_found = True
                            break
                        except ValueError:
                            pass
            if dipole_found:
                break
    
    if not dipole_found:
        match = re.search(r'DIPOLE\s+.*?TOTAL\s+([\d.]+)', content, re.DOTALL)
        if match:
            print(f"\nDipole: {float(match.group(1)):.4f} Debye")
    
    # 3. Optimized coordinates
    print("\nOptimized geometry:")
    
    coord_pattern = r'CARTESIAN COORDINATES\s*\n\s*\n([\s\S]*?)(?:\n\s*\n|\Z)'
    coord_sections = re.findall(coord_pattern, content)
    
    if coord_sections:
        coord_text = coord_sections[-1]
        coord_lines = [line.strip() for line in coord_text.split('\n') if line.strip()]
        
        coords = []
        symbols = []
        for line in coord_lines:
            parts = line.split()
            if len(parts) >= 5 and parts[0].isdigit():
                atom_num = int(parts[0])
                if atom_num <= 3:
                    symbols.append(parts[1])
                    coords.append([float(parts[2]), float(parts[3]), float(parts[4])])
        
        if coords and len(coords) >= 3:
            o_idx = -1
            h_indices = []
            for i, s in enumerate(symbols):
                if s == 'O':
                    o_idx = i
                elif s == 'H':
                    h_indices.append(i)
            
            if o_idx >= 0 and len(h_indices) >= 2:
                print(f"  O1: {coords[o_idx][0]:.6f} {coords[o_idx][1]:.6f} {coords[o_idx][2]:.6f}")
                water.positions[0] = coords[o_idx]
                
                for j, idx in enumerate(h_indices[:2]):
                    print(f"  H{j+2}: {coords[idx][0]:.6f} {coords[idx][1]:.6f} {coords[idx][2]:.6f}")
                    water.positions[j+1] = coords[idx]
    
    # 4. Mulliken charges
    print("\nMulliken charges:")
    
    charge_pattern = r'NET ATOMIC CHARGES\s*\n\s*\n([\s\S]*?)(?:\n\s*\n|\Z)'
    charge_sections = re.findall(charge_pattern, content)
    
    if charge_sections:
        charge_text = charge_sections[-1]
        charge_lines = [line.strip() for line in charge_text.split('\n') if line.strip()]
        
        charges = []
        symbols_charges = []
        for line in charge_lines:
            parts = line.split()
            if len(parts) >= 3 and parts[0].isdigit():
                atom_num = int(parts[0])
                if atom_num <= 3:
                    symbols_charges.append(parts[1])
                    charges.append(float(parts[2]))
        
        if charges and len(charges) >= 3:
            o_idx = -1
            h_indices = []
            for i, s in enumerate(symbols_charges):
                if s == 'O':
                    o_idx = i
                elif s == 'H':
                    h_indices.append(i)
            
            if o_idx >= 0 and len(h_indices) >= 2:
                print(f"  O1: {charges[o_idx]:.4f} e")
                for j, idx in enumerate(h_indices[:2]):
                    print(f"  H{j+2}: {charges[idx]:.4f} e")
    
    # 5. HOMO-LUMO
    match = re.search(r'HOMO LUMO ENERGIES \(EV\)\s*=\s*([-\d.]+)\s+([-\d.]+)', content)
    if match:
        homo = float(match.group(1))
        lumo = float(match.group(2))
        print(f"\nHOMO: {homo:.4f} eV")
        print(f"LUMO: {lumo:.4f} eV")
        print(f"Gap: {lumo - homo:.4f} eV")
    
    # 6. Gradient
    match = re.search(r'GRADIENT NORM\s*=\s*([-\d.]+)', content)
    if match:
        print(f"\nGradient norm: {float(match.group(1)):.4f}")

# Calculate additional properties from optimized geometry
print("\n" + "=" * 60)
print("GEOMETRIC PROPERTIES")
print("=" * 60)

# Bond lengths
if len(water.positions) >= 3:
    # O-H bond lengths
    o_pos = water.positions[0]
    h1_pos = water.positions[1]
    h2_pos = water.positions[2]
    
    bond_oh1 = np.linalg.norm(o_pos - h1_pos)
    bond_oh2 = np.linalg.norm(o_pos - h2_pos)
    
    print(f"\nO-H1 bond length: {bond_oh1:.4f} Å")
    print(f"O-H2 bond length: {bond_oh2:.4f} Å")
    print(f"Average O-H: {(bond_oh1 + bond_oh2) / 2:.4f} Å")
    
    # H-O-H angle
    v1 = h1_pos - o_pos
    v2 = h2_pos - o_pos
    cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    angle = np.arccos(cos_angle) * 180 / np.pi
    print(f"H-O-H angle: {angle:.2f}°")
    
    # H-H distance
    hh_dist = np.linalg.norm(h1_pos - h2_pos)
    print(f"H-H distance: {hh_dist:.4f} Å")

# Save optimized structure
write('water_optimized.xyz', water)
print(f"\n✅ Optimized structure saved to water_optimized.xyz")

print("\nFinal optimized coordinates (from ASE):")
for i, (symbol, pos) in enumerate(zip(water.symbols, water.positions)):
    print(f"  {symbol}{i+1}: {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f}")
