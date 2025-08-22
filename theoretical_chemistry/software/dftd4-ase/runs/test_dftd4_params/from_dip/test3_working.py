#!/usr/bin/env python3

import sys
import os
from ase import Atoms
import numpy as np

# Remove dftd4 from Python path to force external command usage
original_sys_path = sys.path.copy()
sys.path = [p for p in sys.path if 'dftd4' not in p and 'site-packages' not in p]

try:
    # Now try to import DFTD4 - it should fail and we can handle it
    from dftd4.ase import DFTD4
    print("WARNING: dftd4 library still available - may still use Python API")
except ImportError:
    print("dftd4 Python library not available - good!")
    # We'll handle this case below

# Restore original path
sys.path = original_sys_path

# Create NaCl crystal structure
atoms = Atoms(
    symbols=['Na']*4 + ['Cl']*4,
    positions=[ # positions in Angstrom
        [0.000000000000000, 0.000000000000000, 0.000000000000000],
        [2.810000000000000, 0.000000000000000, 2.810000000000000],
        [2.810000000000000, 2.810000000000000, 2.810000000000000],
        [0.000000000000000, 2.810000000000000, 0.000000000000000],
        [2.810000000000000, 2.810000000000000, 0.000000000000000],
        [0.000000000000000, 2.810000000000000, 2.810000000000000],
        [0.000000000000000, 0.000000000000000, 2.810000000000000],
        [2.810000000000000, 0.000000000000000, 0.000000000000000]
    ],
    cell=[ # cell in Angstrom
        [5.620000000000000, 0.000000000000000, 0.000000000000000],
        [0.000000000000000, 5.620000000000000, 0.000000000000000],
        [0.000000000000000, 0.000000000000000, 5.620000000000000]
    ],
    pbc=[True, True, True]
)

# Simple function to calculate DFT-D4 energy using external executable
def calculate_dftd4_energy(atoms, s8_factor=1.0):
    """Calculate DFT-D4 energy using external executable"""
    import subprocess
    import tempfile
    
    # Create temporary XYZ file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xyz', delete=False) as f:
        f.write(f"{len(atoms)}\n")
        f.write("DFTD4 calculation\n")
        for symbol, pos in zip(atoms.get_chemical_symbols(), atoms.positions):
            f.write(f"{symbol} {pos[0]:.10f} {pos[1]:.10f} {pos[2]:.10f}\n")
        input_file = f.name
    
    try:
        # Run DFT-D4 with custom parameters
        cmd = [
            '/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4/bin/dftd4',
            input_file,
            '--param', '1.0', str(s8_factor), '0.4', '5.0'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Parse energy from output
        for line in result.stdout.split('\n'):
            if 'Dispersion energy:' in line:
                energy_str = line.split(':')[1].strip().split()[0]
                energy = float(energy_str) * 27.211386245988  # Hartree to eV
                return energy
        
        print("DFT-D4 output for debugging:")
        print(result.stdout)
        raise ValueError("Could not parse energy from DFTD4 output")
            
    finally:
        os.unlink(input_file)

# Test the external command approach
print("Testing DFT-D4 with different s8 factors on NaCl crystal:")
print("=" * 60)

for s8_factor in [1.0, 0.8, 0.6, 0.4, 0.2, 0.0]:
    energy = calculate_dftd4_energy(atoms, s8_factor)
    print(f"s8 = {s8_factor:4.1f}: Energy = {energy:12.6f} eV")

print("=" * 60)
print("Note: Lower s8 values result in weaker dispersion interaction")