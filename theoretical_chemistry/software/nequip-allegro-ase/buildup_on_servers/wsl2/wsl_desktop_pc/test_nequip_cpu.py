# test_nequip_cpu.py

import torch
import numpy as np
from ase.build import bulk
from nequip.integrations.ase import NequIPCalculator

def main():
    print("=" * 60)
    print("Testing NequIP CPU-compiled model")
    print("=" * 60)
    
    # Load the CPU-compiled model
    print("\nLoading model...")
    calculator = NequIPCalculator.from_compiled_model(
        compile_path="allegro_oam_l.nequip.pt2",
        device="cpu",
        chemical_species_to_atom_type_map=True,
    )
    print("✓ Model loaded successfully!")
    
    # Create a silicon diamond structure
    print("\nCreating silicon structure...")
    atoms = bulk("Si", crystalstructure="diamond", a=5.43, cubic=True)
    print(f"✓ Created {len(atoms)} atoms")
    
    # Attach calculator and run calculation
    print("\nRunning calculation...")
    atoms.calc = calculator
    
    # Get energy and forces
    energy = atoms.get_potential_energy()
    forces = atoms.get_forces()
    
    # Print results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Potential Energy: {energy:.8f} eV")
    print(f"Max force component: {np.max(np.abs(forces)):.8f} eV/Å")
    print(f"Force array shape: {forces.shape}")
    
    # Show first few forces
    print("\nFirst 3 force vectors (eV/Å):")
    for i in range(min(3, len(atoms))):
        print(f"  Atom {i}: ({forces[i][0]:.6f}, {forces[i][1]:.6f}, {forces[i][2]:.6f})")
    
    print("\n✓ Calculation completed successfully!")
    return atoms, energy, forces

if __name__ == "__main__":
    main()
