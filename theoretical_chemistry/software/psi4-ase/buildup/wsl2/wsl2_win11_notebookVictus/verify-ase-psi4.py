import numpy as np
from ase.build import molecule
from ase.calculators.psi4 import Psi4

def verify_psi4_setup():
    print("--- Initializing ASE-Psi4 Verification Script ---")
    
    try:
        # 1. Build a simple water molecule test case
        atoms = molecule('H2O')
        print(f"Successfully generated molecule: {atoms.get_chemical_formula()}")
        
        # 2. Configure the Psi4 calculator 
        # Using a fast Hartree-Fock method and small basis set for validation
        calc = Psi4(
            atoms=atoms, 
            method='hf', 
            basis='3-21g',
            memory='500MB',
            num_threads=1
        )
        atoms.calc = calc
        
        # 3. Trigger electronic structure computations
        print("Running potential energy calculation...")
        energy = atoms.get_potential_energy()
        print(f"Success! Potential Energy: {energy:.6f} eV")
        
        print("Running atomic force calculation...")
        forces = atoms.get_forces()
        print("Success! Forces matrix successfully computed:")
        print(forces)
        
        print("\n[PASSED]: Psi4 is integrated and running well with ASE.")
        
    except ImportError as e:
        print(f"\n[FAILED]: Missing dependency module. Details: {e}")
        print("Ensure you have activated your environment: 'conda activate p4env'")
        
    except Exception as e:
        print(f"\n[FAILED]: Calculation runtime error. Details: {e}")

if __name__ == "__main__":
    verify_psi4_setup()

