# test_precise_gpu.py
import torch
import numpy as np
import time
from ase.build import bulk
from nequip.integrations.ase import NequIPCalculator

print("=" * 70)
print("Testing Precise GPU Model vs CPU")
print("=" * 70)

# Load all three models
print("\nLoading models...")
cpu_calc = NequIPCalculator.from_compiled_model(
    compile_path="allegro_oam_l.nequip.pt2",
    device="cpu",
    chemical_species_to_atom_type_map=True,
)

gpu_original = NequIPCalculator.from_compiled_model(
    compile_path="allegro_oam_l_gpu.nequip.pt2",
    device="cuda",
    chemical_species_to_atom_type_map=True,
)

gpu_precise = NequIPCalculator.from_compiled_model(
    compile_path="allegro_oam_l_gpu_precise.nequip.pt2",
    device="cuda",
    chemical_species_to_atom_type_map=True,
)

# Test different system sizes
for size in [1, 2, 3]:
    n_atoms = (size * 2)**3 * 8
    print(f"\n{'='*70}")
    print(f"System: {n_atoms} atoms ({(size*2)}x{(size*2)}x{(size*2)} supercell)")
    print(f"{'='*70}")
    
    atoms = bulk("Si", crystalstructure="diamond", a=5.43, cubic=True) * (size*2, size*2, size*2)
    
    # CPU (reference)
    atoms.calc = cpu_calc
    energy_cpu = atoms.get_potential_energy()
    print(f"\n[CPU Reference]")
    print(f"  Energy: {energy_cpu:.10f} eV")
    
    # GPU Original
    atoms.calc = gpu_original
    energy_gpu_orig = atoms.get_potential_energy()
    diff_orig = abs(energy_cpu - energy_gpu_orig)
    print(f"\n[GPU Original]")
    print(f"  Energy: {energy_gpu_orig:.10f} eV")
    print(f"  Diff from CPU: {diff_orig:.8f} eV ({diff_orig*1000:.4f} meV)")
    
    # GPU Precise
    atoms.calc = gpu_precise
    energy_gpu_precise = atoms.get_potential_energy()
    diff_precise = abs(energy_cpu - energy_gpu_precise)
    print(f"\n[GPU Precise]")
    print(f"  Energy: {energy_gpu_precise:.10f} eV")
    print(f"  Diff from CPU: {diff_precise:.8f} eV ({diff_precise*1000:.4f} meV)")
    
    # Compare
    print(f"\n[Comparison]")
    if diff_precise < diff_orig:
        improvement = (diff_orig - diff_precise) / diff_orig * 100
        print(f"  ✓ Precise model is better by {improvement:.1f}%")
    else:
        print(f"  ℹ Original model is better")
    
    # Check if improvement is meaningful
    if diff_precise < 1e-6:
        print(f"  ✓ Excellent accuracy (< 1e-6 eV)")
    elif diff_precise < 1e-4:
        print(f"  ✓ Good accuracy (< 1e-4 eV)")
    else:
        print(f"  ⚠ Moderate accuracy")

# Force comparison
print("\n" + "="*70)
print("Force Comparison")
print("="*70)

for size in [2, 3]:
    n_atoms = (size * 2)**3 * 8
    atoms = bulk("Si", crystalstructure="diamond", a=5.43, cubic=True) * (size*2, size*2, size*2)
    
    print(f"\nSystem: {n_atoms} atoms")
    
    # CPU
    atoms.calc = cpu_calc
    forces_cpu = atoms.get_forces()
    
    # GPU Original
    atoms.calc = gpu_original
    forces_gpu_orig = atoms.get_forces()
    
    # GPU Precise
    atoms.calc = gpu_precise
    forces_gpu_precise = atoms.get_forces()
    
    # Compare
    max_diff_orig = np.max(np.abs(forces_cpu - forces_gpu_orig))
    max_diff_precise = np.max(np.abs(forces_cpu - forces_gpu_precise))
    
    print(f"\nMax force differences (eV/Å):")
    print(f"  Original GPU: {max_diff_orig:.8f}")
    print(f"  Precise GPU:  {max_diff_precise:.8f}")
    
    if max_diff_precise < max_diff_orig:
        improvement = (max_diff_orig - max_diff_precise) / max_diff_orig * 100
        print(f"  ✓ Precise model improves forces by {improvement:.1f}%")
