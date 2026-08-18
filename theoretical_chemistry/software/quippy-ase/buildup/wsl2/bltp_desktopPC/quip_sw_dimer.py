#!/usr/bin/env python
"""
Test QUIP with a simple Lennard-Jones potential for silicon.
Uses the simpler XML format that might work with your QUIP build.
"""

import numpy as np
import subprocess
import tempfile
import os
import re

# Path to QUIP executable
QUIP_EXE = "/home/milias/miniconda3/envs/materials_sim/lib/python3.10/site-packages/quippy/quip"

def create_lj_potential_file():
    """Create a Lennard-Jones potential parameter file."""
    
    # Simple LJ potential for Si (approximate parameters)
    lj_params = """<?xml version="1.0"?>
<potential>
  <version>1.0</version>
  <name>Lennard-Jones Silicon</name>
  <species>
    <species name="Si" mass="28.0855" charge="0.0"/>
  </species>
  <potentials>
    <potential type="LJ">
      <args>
        <arg name="epsilon">0.01745</arg>
        <arg name="sigma">2.392</arg>
        <arg name="cutoff">10.0</arg>
      </args>
      <species>
        <species>Si</species>
      </species>
    </potential>
  </potentials>
</potential>
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        f.write(lj_params)
        return f.name

def create_sw_potential_simple():
    """Create Stillinger-Weber potential using simple format."""
    
    sw_simple = """<?xml version="1.0"?>
<potential>
  <version>1.0</version>
  <name>SW Silicon Simple</name>
  <species>
    <species name="Si"/>
  </species>
  <potentials>
    <potential type="SW">
      <args>
        <arg name="A">7.049556277</arg>
        <arg name="B">0.6022245584</arg>
        <arg name="p">4</arg>
        <arg name="q">0</arg>
        <arg name="sigma">2.0951</arg>
        <arg name="epsilon">2.1683</arg>
        <arg name="lambda">21.0</arg>
        <arg name="gamma">1.2</arg>
        <arg name="cos0">-0.3333333333</arg>
        <arg name="cutoff">3.771</arg>
      </args>
      <species>
        <species>Si</species>
      </species>
    </potential>
  </potentials>
</potential>
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        f.write(sw_simple)
        return f.name

def test_potential_file_format(param_file):
    """Test if a potential file is valid."""
    
    cmd = [QUIP_EXE, f'param_filename={param_file}', '--help']
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Check if it loads successfully
    if "ERROR" in result.stderr or "ABORT" in result.stderr:
        return False, result.stderr
    return True, "OK"

def calculate_energy(atoms, param_file, calc_type="energy"):
    """Calculate energy using QUIP with potential file."""
    
    # Write atoms to XYZ file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xyz', delete=False) as f:
        f.write(f"{len(atoms)}\n")
        f.write("QUIP calculation\n")
        for atom, pos in zip(atoms.symbols, atoms.positions):
            f.write(f"{atom} {pos[0]:.10f} {pos[1]:.10f} {pos[2]:.10f}\n")
        xyz_file = f.name
    
    # Build command
    cmd = [
        QUIP_EXE,
        f'atoms_filename={xyz_file}',
        f'param_filename={param_file}',
        'energy'
    ]
    
    if calc_type in ["forces", "energy_forces"]:
        cmd.append('forces')
    
    result_dict = {'success': False}
    
    try:
        # Run QUIP
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            result_dict['success'] = True
            result_dict['output'] = result.stdout
            
            # Parse energy
            energy_match = re.search(r'energy\s*=\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)', result.stdout)
            if energy_match:
                result_dict['energy'] = float(energy_match.group(1))
            
            # Parse forces
            if calc_type in ["forces", "energy_forces"]:
                forces = []
                force_lines = re.findall(
                    r'force\s+\d+\s+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)',
                    result.stdout
                )
                for line in force_lines:
                    forces.append([float(line[0]), float(line[1]), float(line[2])])
                if forces:
                    result_dict['forces'] = np.array(forces)
        else:
            result_dict['error'] = result.stderr
            
    except subprocess.TimeoutExpired:
        result_dict['error'] = "Timeout"
    except Exception as e:
        result_dict['error'] = str(e)
    finally:
        # Clean up
        if os.path.exists(xyz_file):
            os.unlink(xyz_file)
    
    return result_dict

def test_different_potential_formats():
    """Test different potential format styles."""
    
    print("="*60)
    print("Testing Different Potential Formats")
    print("="*60)
    
    # Create atoms
    atoms = Atoms("SiSi", positions=[[0,0,0], [0,0,2.35]], pbc=False)
    
    # Test 1: LJ potential
    print("\n1. Testing Lennard-Jones potential...")
    param_file = create_lj_potential_file()
    print(f"   Created: {param_file}")
    
    # Check if file is valid
    valid, msg = test_potential_file_format(param_file)
    if valid:
        print("   ✓ Potential file format is valid")
        
        # Calculate energy
        result = calculate_energy(atoms, param_file)
        if result['success']:
            print(f"   ✓ Energy: {result['energy']:.6f} eV")
        else:
            print(f"   ✗ Calculation failed: {result.get('error', 'Unknown')[:80]}")
    else:
        print(f"   ✗ Invalid format: {msg[:100]}")
    
    os.unlink(param_file)
    
    # Test 2: SW potential
    print("\n2. Testing Stillinger-Weber potential...")
    param_file = create_sw_potential_simple()
    print(f"   Created: {param_file}")
    
    # Check if file is valid
    valid, msg = test_potential_file_format(param_file)
    if valid:
        print("   ✓ Potential file format is valid")
        
        # Calculate energy
        result = calculate_energy(atoms, param_file)
        if result['success']:
            print(f"   ✓ Energy: {result['energy']:.6f} eV")
        else:
            print(f"   ✗ Calculation failed: {result.get('error', 'Unknown')[:80]}")
    else:
        print(f"   ✗ Invalid format: {msg[:100]}")
    
    os.unlink(param_file)

def test_alternative_approach():
    """Try a completely different approach using QUIP's built-in simple potential."""
    
    print("\n" + "="*60)
    print("Testing Alternative Approach")
    print("="*60)
    
    # Some QUIP builds support a simple LJ by just specifying the potential type
    # without needing a separate XML file
    
    atoms = Atoms("SiSi", positions=[[0,0,0], [0,0,2.35]], pbc=False)
    
    # Write XYZ file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xyz', delete=False) as f:
        f.write(f"{len(atoms)}\n")
        f.write("QUIP calculation\n")
        for atom, pos in zip(atoms.symbols, atoms.positions):
            f.write(f"{atom} {pos[0]:.10f} {pos[1]:.10f} {pos[2]:.10f}\n")
        xyz_file = f.name
    
    try:
        # Try to use LJ potential directly (without param file)
        # This only works if the potential is compiled into QUIP
        cmd = [QUIP_EXE, f'atoms_filename={xyz_file}', 'potential=LJ', 'energy']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print("✓ QUIP built-in LJ potential works!")
            energy_match = re.search(r'energy\s*=\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)', result.stdout)
            if energy_match:
                print(f"  Energy: {float(energy_match.group(1)):.6f} eV")
        else:
            print("✗ Built-in LJ potential not available")
            print(f"  Error: {result.stderr[:200]}")
            
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        if os.path.exists(xyz_file):
            os.unlink(xyz_file)

def create_simple_tabulated_potential():
    """Create a simple tabulated potential as a last resort."""
    
    print("\n" + "="*60)
    print("Creating Tabulated Potential")
    print("="*60)
    
    # Create a simple Morse potential for Si dimer
    # Parameters: D_e = 3.28 eV, r_e = 2.35 Å, a = 1.5 Å^-1
    
    distances = np.linspace(1.5, 6.0, 50)
    energies = []
    
    D_e = 3.28  # eV
    r_e = 2.35  # Å
    a = 1.5     # Å^-1
    
    for r in distances:
        # Morse potential: V(r) = D_e * (1 - exp(-a*(r-r_e)))^2 - D_e
        energy = D_e * (1 - np.exp(-a * (r - r_e)))**2 - D_e
        energies.append(energy)
    
    # Write to file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.pot', delete=False) as f:
        f.write("# Morse potential for Si dimer\n")
        f.write("# r (Å)  V (eV)\n")
        for r, e in zip(distances, energies):
            f.write(f"{r:.6f} {e:.6f}\n")
        pot_file = f.name
    
    print(f"Created tabulated potential: {pot_file}")
    print(f"  D_e = {D_e:.3f} eV, r_e = {r_e:.3f} Å, a = {a:.3f} Å^-1")
    
    # This potential file can be used with other codes (LAMMPS, etc.)
    # but QUIP may not support tabulated potentials directly
    
    return pot_file

if __name__ == "__main__":
    # Import ASE here for testing
    from ase import Atoms
    
    print(f"Using QUIP executable: {QUIP_EXE}")
    print()
    
    # Test different approaches
    test_different_potential_formats()
    test_alternative_approach()
    
    # Create a tabulated potential for reference
    pot_file = create_simple_tabulated_potential()
    print(f"\nTabulated potential saved to: {pot_file}")
    print("You can use this with other codes (LAMMPS, etc.)")
    
    print("\n" + "="*60)
    print("Test completed!")
