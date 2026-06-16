import os
from ase.build import molecule
from huggingface_hub import hf_hub_download
from mlip.simulation.ase import ASESimulationEngine
from mlip.models import Visnet
from mlip.models.model_io import load_model_from_zip

# 1. Download the up-to-date model weights from Hugging Face
checkpoint_filename = "visnet_spice2.zip"
if not os.path.exists(checkpoint_filename):
    print("Fetching up-to-date Visnet weights from Hugging Face...")
    local_checkpoint_path = hf_hub_download(
        repo_id="instadeepai/mlip",       # Modern official repository 
        filename=checkpoint_filename,
        local_dir="."
    )
else:
    local_checkpoint_path = checkpoint_filename

# 2. Define the starting molecular structure (Ethanol)
atoms = molecule('CH3CH2OH')

# 3. Load the ForceField model from the zip file
print(f"Loading pre-trained force field from {checkpoint_filename}...")
force_field = load_model_from_zip(Visnet, local_checkpoint_path)

# 4. Configure the simulation runtime explicitly for structural optimization
config = ASESimulationEngine.Config(
    device="cpu",
    mode="energy_minimization",     # High-level geometry relaxation mode
    num_steps=100,                  # Maximum relaxation iterations
    fmax=0.05,                      # Max residual force convergence tolerance (eV/Å)
    log_interval=5                  # Interval tracking print frequency
)

# 5. Initialize the engine with the required positional parameters
# Signature format: (atoms, force_field, config)
engine = ASESimulationEngine(atoms, force_field, config)

# 6. Run the geometry optimization loop
print("Starting Visnet structural relaxation loop...")
engine.run()

# 7. Extract the fully minimized properties directly from the updated atoms object
relaxed_energy = atoms.get_potential_energy()
relaxed_forces = atoms.get_forces()

print("\n--- Relaxed Structural Results ---")
print(f"Final Optimized Potential Energy: {relaxed_energy:.4f} eV")
print("\nRemaining Residual Atomic Forces (eV/Å):")
print(relaxed_forces)

