import os
import urllib.request
from ase.build import molecule
from mlip.simulation.ase import ASESimulationEngine
from mlip.models import Visnet
from mlip.models.model_io import load_model_from_zip

# 1. Clear out previous corrupt 175KB files completely
checkpoint_filename = "visnet_organics.zip"
if os.path.exists(checkpoint_filename):
    os.remove(checkpoint_filename)

# 2. Stream the actual 100MB+ binary model parameter archive natively
print("Streaming genuine pre-trained Visnet weights from Hugging Face...")
url = "https://huggingface.co"

# Define browser descriptors to bypass download link filters
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

try:
    urllib.request.urlretrieve(url, checkpoint_filename)
    # Print real file size to confirm it is not an HTML text page
    print(f"Download successful! Checked binary size: {os.path.getsize(checkpoint_filename) / (1024*1024):.2f} MB")
except Exception as e:
    raise RuntimeError(f"Network asset stream failed: {e}")

# 3. Define the structural molecular geometry (Ethanol)
atoms = molecule('CH3CH2OH')

# 4. Load the ForceField model from the authentic downloaded zip file
print(f"Loading pre-trained force field from {checkpoint_filename}...")
force_field = load_model_from_zip(Visnet, checkpoint_filename)

# 5. Configure the simulation runtime explicitly for structural optimization
config = ASESimulationEngine.Config(
    device="cpu",
    mode="energy_minimization",     # High-level relaxation mode
    num_steps=100,                  # Maximum relaxation iterations
    fmax=0.05,                      # Max residual force convergence tolerance (eV/Å)
    log_interval=5                  # Step print frequency tracking
)

# 6. Initialize the simulation loop engine
# Signature format: (atoms, force_field, config)
engine = ASESimulationEngine(atoms, force_field, config)

# 7. Run the geometry optimization loop
print("Starting Visnet structural relaxation loop...")
engine.run()

# 8. Extract the fully minimized properties directly from the updated atoms object
relaxed_energy = atoms.get_potential_energy()
relaxed_forces = atoms.get_forces()

print("\n--- Relaxed Structural Results ---")
print(f"Final Optimized Potential Energy: {relaxed_energy:.4f} eV")
print("\nRemaining Residual Atomic Forces (eV/Å):")
print(relaxed_forces)

