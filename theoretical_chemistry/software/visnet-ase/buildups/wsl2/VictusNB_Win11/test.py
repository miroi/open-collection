import os
from ase.build import molecule
from huggingface_hub import hf_hub_download
from mlip.simulation.ase import ASESimulationEngine  # Re-added missing import
from mlip.models import Visnet
from mlip.models.model_io import load_model_from_zip

# 1. Map out local file parameters
checkpoint_filename = "visnet_organics_01.zip"
if not os.path.exists(checkpoint_filename):
    print("Fetching official Visnet weights from Hugging Face...")
    local_checkpoint_path = hf_hub_download(
        repo_id="InstaDeepAI/visnet-organics",
        filename=checkpoint_filename,
        local_dir="."
    )
else:
    local_checkpoint_path = checkpoint_filename

# 2. Define structural molecular input (Ethanol)
atoms = molecule('CH3CH2OH')

# 3. Load the pre-compiled ForceField natively using positional class inputs
print("Unpacking model structures into the execution layer...")
force_field = load_model_from_zip(Visnet, local_checkpoint_path)

# 4. Define runtime environments
config = ASESimulationEngine.Config(
    device="cpu",                   # Enforces CPU execution to bypass driver flags
    num_steps=1,                    # Satisfies Pydantic baseline parameters (>0)
    log_interval=1
)

# 5. Initialize the simulation loop engine
engine = ASESimulationEngine(atoms, force_field, config)

# 6. Execute forward computation pass
print("Running simulation step via Visnet...")
engine.run()

# 7. Extract structural metrics directly from the updated atoms instance object
potential_energy = atoms.get_potential_energy()
forces = atoms.get_forces()

# 8. Output results
print("\n--- Structural Simulation Results ---")
print(f"Total Potential Energy: {potential_energy:.4f} eV")
print("\nAtomic Forces (eV/Å):")
print(forces)

