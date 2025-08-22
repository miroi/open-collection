#!/usr/bin/env python3

import subprocess
import tempfile
import os

def calculate_dftd4_energy(xyz_content, s8_factor=1.0):
    """
    Calculate DFT-D4 energy with weakened interaction by reducing s8 parameter
    
    Args:
        xyz_content: XYZ file content as string
        s8_factor: Factor to scale s8 parameter (0.0 to 1.0), lower = weaker dispersion
    
    Returns:
        D4 dispersion energy in Hartree
    """
    
    # Default damping parameters (from the output we saw)
    s6 = 1.0
    s8 = s8_factor  # Scale the s8 parameter to weaken interaction
    a1 = 0.4
    a2 = 5.0
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xyz', delete=False) as f:
        f.write(xyz_content)
        xyz_file = f.name
    
    try:
        cmd = [
            '/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/installed_dftd4/bin/dftd4',
            xyz_file,
            '--param', str(s6), str(s8), str(a1), str(a2)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Parse energy from output
        for line in result.stdout.split('\n'):
            if 'Dispersion energy:' in line:
                energy_line = line.strip()
                energy_str = energy_line.split(':')[1].strip().split()[0]
                energy = float(energy_str)
                return energy
        
        print("Full output for debugging:")
        print(result.stdout)
        raise ValueError("Could not find energy in DFT-D4 output")
        
    finally:
        os.unlink(xyz_file)

# Example usage
if __name__ == "__main__":
    # Example XYZ content (water molecule)
    xyz_content = """3
water molecule
O    0.000000    0.000000    0.119262
H    0.000000    0.763239   -0.477047
H    0.000000   -0.763239   -0.477047
"""
    
    print("Weakening DFT-D4 interaction by reducing s8 parameter:")
    print("=" * 60)
    
    # Test different weakening factors
    for s8_factor in [1.0, 0.8, 0.6, 0.4, 0.2, 0.0]:
        energy = calculate_dftd4_energy(xyz_content, s8_factor=s8_factor)
        print(f"s8 = {s8_factor:4.1f}: D4 energy = {energy:12.6e} Hartree")
    
    print("\n" + "=" * 60)
    print("Note: Lower s8 values result in weaker dispersion interaction")
    print("s8 = 1.0: Full strength D4 dispersion")
    print("s8 = 0.0: No D4 dispersion (only s6 term)")