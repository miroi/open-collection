# benchmark_speed.py
import time
import torch
from ase.build import bulk
from nequip.integrations.ase import NequIPCalculator

print("=" * 60)
print("NequIP Performance Benchmark")
print("=" * 60)

# Load both models
print("\nLoading models...")
cpu_calc = NequIPCalculator.from_compiled_model(
    compile_path="allegro_oam_l.nequip.pt2",
    device="cpu",
    chemical_species_to_atom_type_map=True,
)

gpu_calc = NequIPCalculator.from_compiled_model(
    compile_path="allegro_oam_l_gpu.nequip.pt2",
    device="cuda",
    chemical_species_to_atom_type_map=True,
)

# Test different system sizes
for size in [1, 2, 3]:
    n_atoms = (size * 2)**3 * 8
    print(f"\n{'='*60}")
    print(f"System: {n_atoms} atoms ({(size*2)}x{(size*2)}x{(size*2)} supercell)")
    print(f"{'='*60}")
    
    atoms = bulk("Si", crystalstructure="diamond", a=5.43, cubic=True) * (size*2, size*2, size*2)
    
    # CPU timing
    print("\n[CPU]")
    atoms.calc = cpu_calc
    start = time.time()
    energy_cpu = atoms.get_potential_energy()
    cpu_time = time.time() - start
    print(f"  Energy: {energy_cpu:.6f} eV")
    print(f"  Time: {cpu_time:.4f} seconds")
    
    # GPU timing
    if torch.cuda.is_available():
        print("\n[GPU]")
        # Warm-up
        atoms.calc = gpu_calc
        atoms.get_potential_energy()
        torch.cuda.synchronize()
        
        # Actual timing
        start = time.time()
        energy_gpu = atoms.get_potential_energy()
        torch.cuda.synchronize()
        gpu_time = time.time() - start
        
        print(f"  Energy: {energy_gpu:.6f} eV")
        print(f"  Time: {gpu_time:.4f} seconds")
        print(f"  Speedup: {cpu_time/gpu_time:.2f}x")
        
        # Verify energies match
        energy_diff = abs(energy_cpu - energy_gpu)
        print(f"  Energy difference: {energy_diff:.8f} eV")
        print(f"  ✓ Energies match!" if energy_diff < 1e-4 else "  ⚠ Energy mismatch!")
