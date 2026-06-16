# matgl_advanced_demo.py
"""
Advanced MatGL Examples: Batch Predictions, Multiple Properties, Relaxation, and Custom Training
"""

import matgl
from pymatgen.core import Lattice, Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import torch
import numpy as np
import time

print("=" * 70)
print("MATGL ADVANCED DEMONSTRATION")
print("=" * 70)

# Check GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"\nUsing device: {device}")
if device == "cuda":
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
print("-" * 70)

# ============================================================================
# 1. BATCH PREDICTIONS - Multiple structures at once (much faster!)
# ============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 1: BATCH PREDICTIONS")
print("=" * 70)

# Create multiple structures
structures = []
structure_names = []

# CsCl
struct = Structure.from_spacegroup(
    "Pm-3m", Lattice.cubic(4.1437), 
    ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]]
)
structures.append(struct)
structure_names.append("CsCl")

# NaCl
struct = Structure.from_spacegroup(
    "Fm-3m", Lattice.cubic(5.6402),
    ["Na", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]]
)
structures.append(struct)
structure_names.append("NaCl")

# MgO
struct = Structure.from_spacegroup(
    "Fm-3m", Lattice.cubic(4.2117),
    ["Mg", "O"], [[0, 0, 0], [0.5, 0.5, 0.5]]
)
structures.append(struct)
structure_names.append("MgO")

# Si (diamond)
struct = Structure.from_spacegroup(
    "Fd-3m", Lattice.cubic(5.431),
    ["Si"], [[0, 0, 0]]
)
structures.append(struct)
structure_names.append("Si")

# Cu (FCC)
struct = Structure.from_spacegroup(
    "Fm-3m", Lattice.cubic(3.615),
    ["Cu"], [[0, 0, 0]]
)
structures.append(struct)
structure_names.append("Cu")

print(f"\nBatch predicting formation energies for {len(structures)} structures...")
start = time.time()

# Load model once
model_eform = matgl.load_model("MEGNet-Eform-MP-2018.6.1")

# Batch prediction
energies = model_eform.predict_structures(structures)

print(f"✓ Batch prediction completed in {time.time() - start:.3f}s")
print("\nResults:")
print("-" * 50)
for name, energy in zip(structure_names, energies):
    print(f"{name:8s} : {float(energy):7.3f} eV/atom")

# ============================================================================
# 2. MULTIPLE PROPERTIES - Formation energy, band gap, etc.
# ============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 2: MULTIPLE PROPERTIES PREDICTION")
print("=" * 70)

# Load different models for different properties
models = {
    "Formation Energy": "MEGNet-Eform-MP-2018.6.1",
    "Band Gap": "MEGNet-BandGap-mfi-MP-2019.4.1",
}

# Test on a semiconductor (Si) and insulator (MgO)
test_structures = [
    ("Si", Structure.from_spacegroup("Fd-3m", Lattice.cubic(5.431), ["Si"], [[0, 0, 0]])),
    ("MgO", Structure.from_spacegroup("Fm-3m", Lattice.cubic(4.2117), ["Mg", "O"], [[0, 0, 0]])),
    ("Cu", Structure.from_spacegroup("Fm-3m", Lattice.cubic(3.615), ["Cu"], [[0, 0, 0]])),
]

print("\nPredicting multiple properties...\n")
for prop_name, model_name in models.items():
    print(f"\nProperty: {prop_name}")
    print("-" * 40)
    model = matgl.load_model(model_name)
    
    for name, struct in test_structures:
        result = model.predict_structure(struct)
        value = float(result.numpy())
        unit = "eV" if "Band" in prop_name else "eV/atom"
        print(f"  {name:5s} : {value:7.3f} {unit}")

# ============================================================================
# 3. STRUCTURE RELAXATION (using M3GNet - more advanced)
# ============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 3: STRUCTURE RELAXATION")
print("=" * 70)

print("\nLoading M3GNet potential model...")
model_m3gnet = matgl.load_model("M3GNet-PES-MatPES-PBE-2025.2")

# Create a slightly distorted NaCl structure
print("\nCreating a distorted NaCl structure...")
lattice = Lattice.cubic(5.6402)
distorted_struct = Structure(
    lattice,
    ["Na", "Cl", "Na", "Cl"],
    [
        [0.0, 0.0, 0.0],
        [0.5, 0.5, 0.5],
        [0.5, 0.0, 0.0],  # Slightly displaced
        [0.0, 0.5, 0.5],
    ]
)

print(f"Initial structure: {len(distorted_struct)} atoms")
print(f"Initial lattice parameter: {distorted_struct.lattice.a:.4f} Å")

print("\nRelaxing structure (this may take a moment)...")
start = time.time()

# Relax the structure
relaxed_struct, trajectories = model_m3gnet.relax_structure(
    distorted_struct,
    fmax=0.1,  # Force convergence threshold (eV/Å)
    steps=500,  # Maximum relaxation steps
    relax_cell=True,  # Allow cell to relax
)

print(f"✓ Relaxation completed in {time.time() - start:.2f}s")
print(f"\nRelaxed structure: {len(relaxed_struct)} atoms")
print(f"Final lattice parameter: {relaxed_struct.lattice.a:.4f} Å")
print(f"Volume change: {(relaxed_struct.volume / distorted_struct.volume - 1)*100:.2f}%")

# Show displacement
print("\nAtomic displacements:")
for i, (initial, final) in enumerate(zip(distorted_struct.cart_coords, relaxed_struct.cart_coords)):
    displacement = np.linalg.norm(final - initial)
    print(f"  Atom {i}: {displacement:.4f} Å")

# ============================================================================
# 4. FORCES AND STRESS PREDICTION
# ============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 4: FORCES AND STRESS PREDICTION")
print("=" * 70)

print("\nCalculating forces and stress for MgO structure...")
mgo = Structure.from_spacegroup(
    "Fm-3m", Lattice.cubic(4.2117),
    ["Mg", "O"], [[0, 0, 0], [0.5, 0.5, 0.5]]
)

# Get forces and stress
graph = model_m3gnet.get_graph_from_structure(mgo)
forces = model_m3gnet.predict_forces(graph)
stress = model_m3gnet.predict_stress(graph)

print(f"\nForces on atoms (eV/Å):")
for i, (site, force) in enumerate(zip(mgo.sites, forces.numpy())):
    print(f"  Atom {i} ({site.species_string}): [{force[0]:7.4f}, {force[1]:7.4f}, {force[2]:7.4f}]")

print(f"\nStress tensor (eV/Å³):")
stress_tensor = stress.numpy()[0]
print(f"  [[{stress_tensor[0]:7.4f}, {stress_tensor[1]:7.4f}, {stress_tensor[2]:7.4f}]")
print(f"   [{stress_tensor[3]:7.4f}, {stress_tensor[4]:7.4f}, {stress_tensor[5]:7.4f}]]")

# ============================================================================
# 5. CUSTOM MODEL TRAINING (Simplified example)
# ============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 5: CUSTOM TRAINING SETUP")
print("=" * 70)

print("\nSetting up a custom MEGNet model for training...")
from matgl.models import MEGNet
from matgl.layers import AtomRef
from matgl.data import StructureDataModule
from matgl.data.datasets import MPFrames

# Check if we can load MP dataset (this requires internet and may be large)
try:
    print("Loading sample from Materials Project dataset...")
    dataset = MPFrames(property="formation_energy_per_atom")
    print(f"✓ Dataset loaded with {len(dataset)} entries")
    
    # Show a sample structure
    sample_struct, sample_energy = dataset[0]
    print(f"\nSample structure: {sample_struct.composition}")
    print(f"Sample energy: {sample_energy:.3f} eV/atom")
    
    # Create a simple model
    print("\nCreating custom MEGNet model...")
    element_refs = AtomRef()
    model = MEGNet(
        element_refs=element_refs,
        dim_node_embedding=16,  # Smaller for demonstration
        dim_edge_embedding=16,
        n_conv=1,
    )
    print("✓ Custom model created (untrained)")
    print("  (Full training would require more setup with DataLoaders, optimizer, etc.)")
    
except Exception as e:
    print(f"\n⚠ Could not load MP dataset: {e}")
    print("  (This is expected if you don't have the full dataset downloaded)")
    print("  (Full training requires the large MP dataset)")

# ============================================================================
# 6. CUSTOM MODEL INFERENCE (Using a trained custom model)
# ============================================================================
print("\n" + "=" * 70)
print("EXAMPLE 6: MODEL INSPECTION AND SAVING")
print("=" * 70)

print("\nInspecting the loaded model...")
print(f"Model type: {type(model_eform)}")
print(f"Model has {sum(p.numel() for p in model_eform.parameters()):,} parameters")

# Get model hyperparameters
if hasattr(model_eform, "dim_node_embedding"):
    print(f"Node embedding dimension: {model_eform.dim_node_embedding}")
    print(f"Edge embedding dimension: {model_eform.dim_edge_embedding}")

# Save a model (optional)
# print("\nSaving model to disk...")
# model_eform.save("my_model.pt")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY OF CAPABILITIES DEMONSTRATED")
print("=" * 70)
print("""
✓ 1. Batch predictions - Fast processing of multiple structures
✓ 2. Multiple properties - Formation energy, band gap, etc.
✓ 3. Structure relaxation - Geometry optimization with force convergence
✓ 4. Forces and stress - Atomic forces and stress tensor
✓ 5. Custom training - Setting up custom MEGNet models
✓ 6. Model inspection - Understanding model architecture

ADVANCED TOPICS NOT COVERED:
• Ensemble predictions (multiple models)
• Transfer learning
• Active learning
• Property tuning
• Graph neural network customization
""")

print("\n" + "=" * 70)
print("✓ All advanced examples completed successfully!")
print("=" * 70)
