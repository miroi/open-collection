# test_nequip_working.py
import torch
import numpy as np
from ase.build import bulk
from nequip.integrations.ase import NequIPCalculator

def main():
    # Path to the cached model package
    model_path = "/home/milias/.nequip/model_cache/cd7794ba9456e3aef505c69a7db8985d06641057c976c58f272c1107f37aaf77.nequip.zip"
    
    print("Loading model from package...")
    
    # Load using the model from package (this is the correct method)
    calculator = NequIPCalculator.from_package(
        package_path=model_path,  # Note: parameter name is package_path
        device="cpu",
    )
    
    # Create a simple silicon structure
    atoms = bulk("Si", crystalstructure="diamond", a=5.43, cubic=True)
    print(f"Number of atoms: {len(atoms)}")
    
    # Run calculation
    atoms.calc = calculator
    energy = atoms.get_potential_energy()
    forces = atoms.get_forces()
    
    print(f"Potential Energy: {energy:.6f} eV")
    print(f"Max force component: {np.max(np.abs(forces)):.6f} eV/Å")
    print(f"Force array shape: {forces.shape}")
    
    return atoms, energy, forces

if __name__ == "__main__":
    main()
