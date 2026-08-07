#!/usr/bin/env python3
"""
MOPAC calculations for water molecule
Works with MOPAC v23.2.5
"""

from ase import Atoms
from ase.io import write
import numpy as np
import subprocess
import os
import re

def parse_mopac_output(output_file, n_atoms):
    """Parse MOPAC output file"""
    results = {}
    
    with open(output_file, 'r') as f:
        lines = f.readlines()
    
    # 1. Energy
    for line in lines:
        if 'FINAL HEAT OF FORMATION' in line:
            parts = line.split()
            for i, part in enumerate(parts):
                if part == '=':
                    kcal = float(parts[i + 1])
                    results['energy_ev'] = kcal / 23.061
                    results['energy_kcal'] = kcal
                    break
            break
    
    # 2. Dipole
    for line in lines:
        if 'DIPOLE' in line and 'TOTAL' in line:
            parts = line.split()
            for i, part in enumerate(parts):
                if part == 'TOTAL' and i + 1 < len(parts):
                    results['dipole'] = float(parts[i + 1])
                    break
            break
    
    # 3. HOMO-LUMO
    for line in lines:
        if 'HOMO LUMO ENERGIES' in line:
            parts = line.split()
            results['homo'] = float(parts[-2])
            results['lumo'] = float(parts[-1])
            results['gap'] = results['lumo'] - results['homo']
            break
    
    # 4. Optimized coordinates - look for final coordinates section
    coords = []
    in_coords = False
    coord_count = 0
    
    for line in lines:
        if 'CARTESIAN COORDINATES' in line and 'OPTIMIZED' not in line:
            in_coords = True
            coord_count = 0
            continue
        if in_coords:
            parts = line.strip().split()
            if len(parts) >= 5 and parts[0].isdigit():
                coords.append([float(parts[2]), float(parts[3]), float(parts[4])])
                coord_count += 1
            elif coord_count >= n_atoms and len(parts) < 5:
                break
    
    if coords:
        results['coordinates'] = np.array(coords[:n_atoms])
    
    # 5. Charges
    charges = []
    in_charges = False
    charge_count = 0
    
    for line in lines:
        if 'NET ATOMIC CHARGES' in line:
            in_charges = True
            charge_count = 0
            continue
        if in_charges:
            parts = line.strip().split()
            if len(parts) >= 3 and parts[0].isdigit():
                charges.append(float(parts[2]))
                charge_count += 1
            elif charge_count >= n_atoms:
                break
    
    if charges:
        results['charges'] = np.array(charges[:n_atoms])
    
    # 6. Gradient - fixed parsing
    for line in lines:
        if 'GRADIENT NORM' in line:
            parts = line.split()
            # Find the number before the equals sign or after
            for i, part in enumerate(parts):
                if part == '=' and i + 1 < len(parts):
                    try:
                        results['gradient'] = float(parts[i + 1])
                    except ValueError:
                        # Try the next part if this fails
                        if i + 2 < len(parts):
                            try:
                                results['gradient'] = float(parts[i + 2])
                            except ValueError:
                                pass
                    break
            break
    
    # 7. Also try to get coordinates from the final summary section
    if 'coordinates' not in results:
        # Look for coordinates in the summary section
        coord_pattern = r'\n\s*(\d+)\s+([A-Z][a-z]?)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s*\n'
        matches = re.findall(coord_pattern, ''.join(lines))
        if matches:
            # Take the last N atoms (optimized geometry)
            matches = matches[-n_atoms:] if len(matches) >= n_atoms else matches
            if len(matches) == n_atoms:
                coords = []
                for match in matches:
                    coords.append([float(match[2]), float(match[3]), float(match[4])])
                results['coordinates'] = np.array(coords)
    
    return results

def run_mopac(method='PM7', task='singlepoint', atoms=None):
    """Run MOPAC calculation"""
    if atoms is None:
        raise ValueError("Atoms object required")
    
    n_atoms = len(atoms)
    
    # Build input
    coord_lines = []
    for symbol, pos in zip(atoms.symbols, atoms.positions):
        coord_lines.append(f"{symbol}    {pos[0]:.6f}    {pos[1]:.6f}    {pos[2]:.6f}")
    
    keywords = '1SCF' if task == 'singlepoint' else ''
    
    # Write input file
    with open('mopac.mop', 'w') as f:
        f.write(f"{method} XYZ {keywords}\n")
        f.write("MOPAC calculation\n\n")
        f.write("\n".join(coord_lines))
        f.write("\n")
    
    # Run MOPAC
    subprocess.run('mopac mopac.mop', shell=True, capture_output=True)
    
    # Parse output
    results = {}
    if os.path.exists('mopac.out'):
        results = parse_mopac_output('mopac.out', n_atoms)
    
    # Clean up
    for f in ['mopac.mop', 'mopac.out', 'mopac.arc']:
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
print("MOPAC WATER MOLECULE CALCULATION")
print("=" * 60)

# 1. Single point
print("\n1. Single point calculation...")
results = run_mopac(method='PM7', task='singlepoint', atoms=water)

if 'energy_ev' in results:
    print(f"   Energy: {results['energy_ev']:.6f} eV")
    print(f"   Heat of formation: {results['energy_kcal']:.4f} kcal/mol")
else:
    print("   Warning: Energy not found in output")

# 2. Geometry optimization
print("\n2. Geometry optimization...")
results = run_mopac(method='PM7', task='optimize', atoms=water)

if 'energy_ev' in results:
    print(f"\n   Optimized energy: {results['energy_ev']:.6f} eV")
    print(f"   Heat of formation: {results['energy_kcal']:.4f} kcal/mol")

if 'coordinates' in results:
    print("\n   Optimized coordinates (Å):")
    symbols = ['O', 'H', 'H']
    for i, (symbol, pos) in enumerate(zip(symbols, results['coordinates'])):
        print(f"     {symbol}{i+1}: {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f}")
    water.positions = results['coordinates']
else:
    print("\n   Warning: Could not parse optimized coordinates")

if 'dipole' in results:
    print(f"\n   Dipole moment: {results['dipole']:.4f} Debye")

if 'charges' in results:
    print("\n   Mulliken charges:")
    for i, (symbol, charge) in enumerate(zip(['O', 'H', 'H'], results['charges'])):
        print(f"     {symbol}{i+1}: {charge:.4f} e")

if 'homo' in results:
    print(f"\n   HOMO: {results['homo']:.4f} eV")
    print(f"   LUMO: {results['lumo']:.4f} eV")
    print(f"   Gap: {results['gap']:.4f} eV")

if 'gradient' in results:
    print(f"   Gradient norm: {results['gradient']:.4f}")

# Save
write('water_mopac_opt.xyz', water)
print(f"\n✅ Results saved to water_mopac_opt.xyz")
