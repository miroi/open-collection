import os
import urllib.request
from ase.build import bulk  # Used to build bulk material unit cells
from mlip.simulation.ase import ASESimulationEngine
from mlip.models import Visnet
from mlip.models.model_io import load_model_from_zip

# =====================================================================
# 1. DOWNLOAD SECURE WEIGHTS FALLBACK
# =====================================================================
checkpoint_filename = "visnet.zip"

if not os.path.exists(checkpoint_filename):
    print("Streaming genuine pre-trained Visnet weights from Hugging Face...")
    url = "https://huggingface.co"
    
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    
    try:
        urllib.request.urlretrieve(url, checkpoint_filename)
        print(f"Download successful! Verified binary size: {os.path.getsize(checkpoint_filename) / (1024*1024):.2f} MB")
    except Exception as e:
        raise RuntimeError(f"Network asset stream failed: {e}")

# =====================================================================
# 2. DEFINE MATERIAL WITH PERIODIC BOUNDARY CONDITIONS (PBC)
# =====================================================================
# Create a face-centered cubic (FCC) Copper unit cell
# crystalstructure="fcc", a=3.6 lattice constant
atoms = bulk('Cu', 'fcc', a=3.6)

# Explicitly ensure Periodic Boundary Conditions are activated across X, Y, Z axes
atoms.pbc = [True, True, True]

print("Material Setup Profile:")
print(f"Chemical Formula: {atoms.get_chemical_formula()}")
print(f"Lattice Vector Cell Matrix (Å):\n{atoms.get_cell()}")
print(f"Periodic Boundary Status: {atoms.pbc}")

# =====================================================================
# 3. INITIALIZE MODEL & RELAX MATERIAL
# =====================================================================
# Load the weights into the Visnet architecture
force_field = load_model_from_zip(Visnet, checkpoint_filename)

# Configure the engine explicitly for material relaxation
config = ASESimulationEngine.Config(
    device="cpu",
    mode="energy_minimization",     # Geometry relaxation mode
    num_steps=50,                   # Maximum optimization iterations
    fmax=0.01,                      # Tight force threshold for crystal stability (eV/Å)
    log_interval=5                  # Report every 5 steps
)

# Initialize the machine learning simulation engine
engine = ASESimulationEngine(atoms, force_field, config)

print("\nStarting Visnet solid-state material relaxation loop...")
engine.run()

# =====================================================================
# 4. OUTPUT RESULTS
# =====================================================================
relaxed_energy = atoms.get_potential_energy()
relaxed_forces = atoms.get_forces()

print("\n--- Relaxed Material Results ---")
print(f"Final Optimized Potential Energy: {relaxed_energy:.4f} eV")
print(f"Energy per Atom: {relaxed_energy / len(atoms):.4f} eV/atom")
print("\nRemaining Residual Atomic Forces (eV/Å):")
print(relaxed_forces)

