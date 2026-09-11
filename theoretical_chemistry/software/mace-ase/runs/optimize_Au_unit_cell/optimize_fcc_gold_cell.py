from ase import units
from ase.build import bulk
from ase.optimize import BFGS
from ase.filters import UnitCellFilter
from mace.calculators import mace_mp
from mace.calculators.foundations import MACECalculator
from ase.io import write
import configparser
import os

# --- 1. Load Configuration ---
def load_config(config_file='mace_config.ini'):
    """
    Load MACE model path from configuration file.
    Expected format:
        [mace-model]
        path = /path/to/mace-mp-0b3-medium.model
    """
    config = configparser.ConfigParser()
    
    # Check if config file exists
    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found. Please create it with [mace-model] section.")
    
    config.read(config_file)
    
    # Check if required section and key exist
    if 'mace-model' not in config:
        raise ValueError(f"Section '[mace-model]' not found in '{config_file}'.")
    
    if 'path' not in config['mace-model']:
        raise ValueError(f"Key 'path' not found in [mace-model] section of '{config_file}'.")
    
    model_path = config['mace-model']['path'].strip()
    
    # Validate the path exists
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"MACE model file not found at: {model_path}")
    
    return model_path

# --- 2. Load Configuration File ---
CONFIG_FILE = 'mace_config.ini'  # Change this to your config file path
try:
    model_path = load_config(CONFIG_FILE)
    print(f"Loading MACE model from: {model_path}")
except Exception as e:
    print(f"Error loading configuration: {e}")
    print("Falling back to default MACE-MP-0 model...")
    model_path = None  # Will use default model

# --- 3. Set up the MACE Calculator ---
try:
    if model_path is not None:
        # Load from local model file
        # For older MACE versions, you might need to use MACECalculator directly
        try:
            # Try the newer mace_mp with local path
            calc = mace_mp(model=model_path, device='cuda', default_dtype='float64')
        except (TypeError, ValueError):
            # Fallback for older versions or when local file loading fails
            print("Using MACECalculator directly for local model...")
            calc = MACECalculator(
                model_paths=model_path,
                device='cuda',
                default_dtype='float64'
            )
        print("MACE calculator initialized from local model file.")
    else:
        # Use default Hugging Face model
        calc = mace_mp(model="medium", device='cuda', default_dtype='float64')
        print("MACE calculator initialized with default medium model from Hugging Face.")
        
except RuntimeError as e:
    print(f"CUDA not available or insufficient memory. Falling back to CPU. Error: {e}")
    if model_path is not None:
        try:
            calc = mace_mp(model=model_path, device='cpu', default_dtype='float64')
        except (TypeError, ValueError):
            calc = MACECalculator(
                model_paths=model_path,
                device='cpu',
                default_dtype='float64'
            )
        print("MACE calculator initialized on CPU from local model file.")
    else:
        calc = mace_mp(model="medium", device='cpu', default_dtype='float64')
        print("MACE calculator initialized on CPU with default medium model.")

# --- 4. Create the Gold Crystal Structure ---
print("\nCreating initial gold crystal structure...")
# Create a conventional cubic cell for gold (FCC structure)
# Experimental lattice constant for gold is ~4.08 Å. Starting slightly off to test optimization.
initial_lattice_constant = 4.10
atoms = bulk('Au', crystalstructure='fcc', a=initial_lattice_constant, cubic=True)

# --- 5. Attach the Calculator ---
atoms.calc = calc

# Print initial energy and cell parameters
initial_energy = atoms.get_potential_energy()
print(f"Initial energy: {initial_energy:.4f} eV")
print(f"Initial lattice constant: {initial_lattice_constant:.4f} Å")
print("Initial cell vectors:\n", atoms.cell)

# --- 6. Set up and run the Lattice Optimization ---
print("\nStarting lattice optimization...")
# Use the UnitCellFilter to optimize both atomic positions and the unit cell.
# This filter allows the BFGS optimizer to adjust the cell shape and volume.
ucf = UnitCellFilter(atoms, mask=[True, True, True, True, True, True])  # All degrees of freedom are free

optimizer = BFGS(ucf, trajectory='gold_opt.traj', logfile='opt.log')
# Run the optimizer. 'fmax' is the maximum force tolerance in eV/Å.
optimizer.run(fmax=0.01)

# --- 7. Results ---
final_energy = atoms.get_potential_energy()
final_lattice_constant = atoms.cell[0, 0]  # For a cubic cell, a is the length of the first cell vector

print("\n--- Optimization Finished ---")
print(f"Final energy: {final_energy:.4f} eV")
print(f"Final optimized lattice constant: {final_lattice_constant:.4f} Å")
print("Final cell vectors:\n", atoms.cell)

# Save the optimized structure
write('gold_optimized.xyz', atoms)
write('gold_optimized.cif', atoms)
print("\nOptimized structure saved to 'gold_optimized.xyz' and 'gold_optimized.cif'.")


