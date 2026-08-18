#!/usr/bin/env python
"""
Test QUIPPY/ASE integration using the Stillinger-Weber potential
for a silicon dimer.
"""

import numpy as np
from ase import Atoms
from quippy.potential import Potential

def test_si_dimer():
    """Test QUIPPY with a silicon dimer."""
    
    # 1. Create a simple Silicon dimer structure
    distance = 2.4  # Å (typical Si-Si bond length)
    atoms = Atoms(
        symbols="SiSi", 
        positions=[[0.0, 0.0, 0.0], [0.0, 0.0, distance]], 
        pbc=False
    )
    
    print(f"System: {len(atoms)} silicon atoms")
    print(f"Bond distance: {distance:.3f} Å")
    print("-" * 50)
    
    try:
        # 2. Create the QUIPPY calculator with Stillinger-Weber potential
        # Use the correct initialization format - args_str for IP
        calc = Potential(args_str="IP SW", param_str="")
        atoms.calc = calc
        
        # 3. Calculate properties
        energy = atoms.get_potential_energy()
        forces = atoms.get_forces()
        
        # 4. Print results
        print("\n✓ QUIPPY / ASE Integration Successful")
        print("="*60)
        print(f"Total Potential Energy: {energy:.6f} eV")
        print(f"Energy per atom: {energy/len(atoms):.6f} eV/atom")
        print("\nForces on each atom (eV/Å):")
        print("-" * 60)
        for i, force in enumerate(forces):
            fx, fy, fz = force
            f_mag = np.linalg.norm(force)
            print(f"  Atom {i} (Si): ({fx:10.6f}, {fy:10.6f}, {fz:10.6f})  |F| = {f_mag:.6f}")
        
        # 5. Check force balance
        total_force = np.sum(forces, axis=0)
        print("-" * 60)
        print(f"Total force on system: ({total_force[0]:.6f}, {total_force[1]:.6f}, {total_force[2]:.6f}) eV/Å")
        print("(Should be near zero for isolated system)")
        
        return energy, forces
        
    except Exception as e:
        print("\n✗ QUIPPY Test Failed")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return None, None

def test_with_params():
    """Alternative approach with explicit parameters."""
    print("\n" + "="*60)
    print("Testing alternative initialization:")
    print("="*60)
    
    # Create atoms
    atoms = Atoms("SiSi", positions=[[0,0,0], [0,0,2.4]], pbc=False)
    
    try:
        # Method 1: Using args_str and param_str
        calc = Potential(args_str="IP SW", param_str="")
        atoms.calc = calc
        energy = atoms.get_potential_energy()
        print(f"✓ Method 1 (args_str='IP SW', param_str=''): Energy = {energy:.6f} eV")
    except Exception as e:
        print(f"✗ Method 1 failed: {e}")
    
    try:
        # Method 2: Try with different format
        calc = Potential(args_str="ip=SW", param_str="")
        atoms.calc = calc
        energy = atoms.get_potential_energy()
        print(f"✓ Method 2 (args_str='ip=SW', param_str=''): Energy = {energy:.6f} eV")
    except Exception as e:
        print(f"✗ Method 2 failed: {e}")
    
    try:
        # Method 3: Try with full potential string
        calc = Potential(args_str="Potential=IP SW", param_str="")
        atoms.calc = calc
        energy = atoms.get_potential_energy()
        print(f"✓ Method 3 (args_str='Potential=IP SW', param_str=''): Energy = {energy:.6f} eV")
    except Exception as e:
        print(f"✗ Method 3 failed: {e}")

def test_with_different_potential():
    """Test with a different potential that might work."""
    print("\n" + "="*60)
    print("Testing different potential formats:")
    print("="*60)
    
    atoms = Atoms("SiSi", positions=[[0,0,0], [0,0,2.4]], pbc=False)
    
    # Try different potential specifications
    test_cases = [
        ("IP SW", ""),
        ("IP=SW", ""),
        ("StillingerWeber Si", ""),
        ("SW", ""),
        ("", "Si Si Si Si"),
    ]
    
    for args_str, param_str in test_cases:
        try:
            calc = Potential(args_str=args_str, param_str=param_str)
            atoms.calc = calc
            energy = atoms.get_potential_energy()
            print(f"✓ args='{args_str}', param='{param_str}': Energy = {energy:.6f} eV")
        except Exception as e:
            print(f"✗ args='{args_str}', param='{param_str}': {str(e)[:60]}...")

if __name__ == "__main__":
    print("="*60)
    print("QUIPPY-ASE Integration Test")
    print("="*60)
    
    # Run main test with explicit args_str
    energy, forces = test_si_dimer()
    
    # Try alternative methods
    test_with_params()
    test_with_different_potential()
    
    print("\n" + "="*60)
    print("Test completed!")
