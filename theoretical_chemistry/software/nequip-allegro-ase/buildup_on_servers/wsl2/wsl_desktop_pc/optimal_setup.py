# optimal_setup.py
import torch
from ase.build import bulk
from nequip.integrations.ase import NequIPCalculator

class OptimalNequIPCalculator:
    """Optimized calculator for GTX 1650 (4GB VRAM)."""
    
    def __init__(self):
        self.cpu_path = "allegro_oam_l.nequip.pt2"
        self.gpu_path = "allegro_oam_l_gpu.nequip.pt2"  # Use original (more accurate)
        self._cpu_calc = None
        self._gpu_calc = None
        self.gpu_memory_limit = 3.5  # GB, leave room for CUDA overhead
        
    @property
    def cpu_calc(self):
        if self._cpu_calc is None:
            self._cpu_calc = NequIPCalculator.from_compiled_model(
                compile_path=self.cpu_path,
                device="cpu",
                chemical_species_to_atom_type_map=True,
            )
        return self._cpu_calc
    
    @property
    def gpu_calc(self):
        if self._gpu_calc is None:
            self._gpu_calc = NequIPCalculator.from_compiled_model(
                compile_path=self.gpu_path,
                device="cuda",
                chemical_species_to_atom_type_map=True,
            )
        return self._gpu_calc
    
    def estimate_memory(self, n_atoms):
        """Rough estimate of GPU memory needed."""
        # Rough estimate: ~7 MB per atom for this model
        return n_atoms * 7 / 1024  # GB
    
    def get_calculator(self, atoms):
        """Choose the best device for the system."""
        n_atoms = len(atoms)
        estimated_memory = self.estimate_memory(n_atoms)
        
        if torch.cuda.is_available() and estimated_memory < self.gpu_memory_limit:
            try:
                # Quick test if GPU can handle it
                test_atoms = atoms.copy()
                test_atoms.calc = self.gpu_calc
                test_atoms.get_potential_energy()
                return self.gpu_calc
            except:
                torch.cuda.empty_cache()
                return self.cpu_calc
        else:
            if n_atoms > 0:
                print(f"Using CPU for {n_atoms} atoms (estimated {estimated_memory:.2f} GB)")
            return self.cpu_calc

# Example usage
calc = OptimalNequIPCalculator()

# Small system: GPU
atoms_small = bulk("Si", "diamond", a=5.43) * (2, 2, 2)
calc.get_calculator(atoms_small)  # GPU

# Large system: CPU
atoms_large = bulk("Si", "diamond", a=5.43) * (6, 6, 6)
calc.get_calculator(atoms_large)  # CPU (auto-fallback)
