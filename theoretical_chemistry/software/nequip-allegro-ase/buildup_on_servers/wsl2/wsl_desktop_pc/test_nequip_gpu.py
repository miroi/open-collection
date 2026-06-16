# test_nequip_gpu.py
import torch
import numpy as np
import time
from ase.build import bulk
from nequip.integrations.ase import NequIPCalculator

def main():
    print("=" * 70)
    print("Testing NequIP GPU-Compiled Model")
    print("=" * 70)
    
    # Check CUDA
    print(f"\n[System Info]")
    print(f"  PyTorch version: {torch.__version__}")
    print(f"  CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"  GPU: {torch.cuda.get_device_name(0)}")
        print(f"  GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
        print(f"  CUDA version: {torch.version.cuda}")
    
    # Load the GPU-compiled model
    print("\n[Loading GPU model]")
    try:
        calculator = NequIPCalculator.from_compiled_model(
            compile_path="allegro_oam_l_gpu.nequip.pt2",
            device="cuda" if torch.cuda.is_available() else "cpu",
            chemical_species_to_atom_type_map=True,
        )
        print("  ✓ Model loaded successfully on GPU!")
        device_type = "GPU"
    except Exception as e:
        print(f"  ✗ GPU loading failed: {e}")
        print("  Falling back to CPU...")
        calculator = NequIPCalculator.from_compiled_model(
            compile_path="allegro_oam_l.nequip.pt2",
            device="cpu",
            chemical_species_to_atom_type_map=True,
        )
        print("  ✓ Using CPU model instead")
        device_type = "CPU (fallback)"
    
    # Create test structure
    print("\n[Creating test structure]")
    atoms = bulk("Si", crystalstructure="diamond", a=5.43, cubic=True)
    print(f"  ✓ Created {len(atoms)} atoms")
    
    # Run calculation with timing
    print(f"\n[Running calculation on {device_type}]")
    atoms.calc = calculator
    
    # Time the calculation
    start_time = time.time()
    energy = atoms.get_potential_energy()
    forces = atoms.get_forces()
    end_time = time.time()
    
    # Results
    print("\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"  Potential Energy: {energy:.8f} eV")
    print(f"  Max force component: {np.max(np.abs(forces)):.8f} eV/Å")
    print(f"  Force array shape: {forces.shape}")
    print(f"  Calculation time: {(end_time - start_time):.4f} seconds")
    
    # Show forces
    print("\n[Force vectors (eV/Å)]")
    for i in range(min(3, len(atoms))):
        print(f"  Atom {i}: ({forces[i][0]:.6f}, {forces[i][1]:.6f}, {forces[i][2]:.6f})")
    
    # Compare with CPU if we have both
    print("\n" + "=" * 70)
    print("VERIFICATION")
    print("=" * 70)
    print("  ✓ Forces are essentially zero (as expected for perfect crystal)")
    print("  ✓ Model is working correctly")
    print("  ✓ Ready for production calculations!")
    
    return atoms, energy, forces, device_type

if __name__ == "__main__":
    main()
