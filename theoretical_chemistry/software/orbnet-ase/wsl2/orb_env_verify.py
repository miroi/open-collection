#!/usr/bin/env python
"""
orb_env_verify.py
Comprehensive verification script for orb-models in a conda environment.
Tailored for orb-models 0.5.5 / Python 3.10 / CUDA-enabled WSL2.

Fixes applied:
  - Handles orb_v2 returning a single model object (not a tuple).
  - Sets atoms.info["charge"] / ["spin"] required by omol models.
  - Falls back to orb-v3-conservative-omol with charge/spin set.
"""

import sys
import warnings

# Suppress known non-blocking warnings during verification
warnings.filterwarnings("ignore", category=FutureWarning, module="google.api_core")
warnings.filterwarnings("ignore", category=FutureWarning, module="torch.jit")

print("=" * 60)
print("1. Python & Package Versions")
print("=" * 60)

print(f"Python: {sys.version}")

import orb_models
print(f"orb_models version: {orb_models.__version__}")

import torch
print(f"torch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA device: {torch.cuda.get_device_name(0)}")

# ------------------------------------------------------------------
print("\n" + "=" * 60)
print("2. Import Core Modules")
print("=" * 60)

from orb_models.forcefield import pretrained
print("✓ orb_models.forcefield.pretrained")

from orb_models.forcefield.calculator import ORBCalculator
print("✓ orb_models.forcefield.calculator.ORBCalculator")

from orb_models.forcefield import atomic_system
print("✓ orb_models.forcefield.atomic_system")

# ------------------------------------------------------------------
print("\n" + "=" * 60)
print("3. Discover Available Pretrained Models")
print("=" * 60)

# Public names in the pretrained module
public_names = [n for n in dir(pretrained) if not n.startswith("_")]
print("Public symbols in pretrained module:")
for name in public_names:
    print(f"  - {name}")

# Registry dict (if present) gives the canonical factory names
if hasattr(pretrained, "ORB_PRETRAINED_MODELS"):
    print("\nORB_PRETRAINED_MODELS registry keys:")
    for key in pretrained.ORB_PRETRAINED_MODELS:
        print(f"  - {key}")
else:
    print("\n(No ORB_PRETRAINED_MODELS registry found in this version.)")

# ------------------------------------------------------------------
print("\n" + "=" * 60)
print("4. Load a Pretrained Model & Run ASE Calculator")
print("=" * 60)

from ase.build import molecule

# Choose device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

orbff = None
atoms_adapter = None
model_loaded = False
model_name = None
needs_charge_spin = False  # omol models require charge/spin

# --- Preferred: orb_v2 (returns a single model object in 0.5.5) ---
if hasattr(pretrained, "orb_v2"):
    print("Loading pretrained.orb_v2(...)")
    try:
        result = pretrained.orb_v2(device=device)
        if isinstance(result, tuple):
            orbff, atoms_adapter = result
        else:
            orbff = result
        model_loaded = True
        model_name = "orb_v2"
    except Exception as e:
        print(f"  orb_v2 failed: {e}")

# --- Fallback: orb-v3-conservative-omol (needs charge/spin) ---
if not model_loaded:
    print("Falling back to orb-v3-conservative-omol (requires charge/spin)")
    try:
        result = pretrained.orb_v3_conservative_omol(device=device)
        if isinstance(result, tuple):
            orbff, atoms_adapter = result
        else:
            orbff = result
        model_loaded = True
        model_name = "orb-v3-conservative-omol"
        needs_charge_spin = True
    except Exception as e:
        print(f"  orb-v3-conservative-omol failed: {e}")

# --- Last resort: first registry entry ---
if not model_loaded and hasattr(pretrained, "ORB_PRETRAINED_MODELS"):
    first_key = next(iter(pretrained.ORB_PRETRAINED_MODELS))
    print(f"Falling back to ORB_PRETRAINED_MODELS['{first_key}']()")
    try:
        factory = pretrained.ORB_PRETRAINED_MODELS[first_key]
        result = factory(device=device)
        if isinstance(result, tuple):
            orbff, atoms_adapter = result
        else:
            orbff = result
        model_loaded = True
        model_name = first_key
        needs_charge_spin = "omol" in first_key
    except Exception as e:
        print(f"  Fallback failed: {e}")

if not model_loaded:
    print("⚠ Could not load any pretrained model. Skipping calculator test.")
    sys.exit(1)

print(f"✓ Loaded model: {model_name}")

# ------------------------------------------------------------------
# Build test system: water molecule
atoms = molecule("H2O")
print(f"Test system: {atoms.get_chemical_formula()} ({len(atoms)} atoms)")

# omol models require explicit charge/spin in atoms.info
if needs_charge_spin:
    atoms.info["charge"] = 0   # neutral water
    atoms.info["spin"] = 1     # singlet (2S+1)
    print(f"Set atoms.info charge={atoms.info['charge']}, spin={atoms.info['spin']}")
else:
    # Safe to set even for models that don't require it
    atoms.info["charge"] = 0
    atoms.info["spin"] = 1

# ------------------------------------------------------------------
# Initialize ORBCalculator (handle API differences across versions)
try:
    calc = ORBCalculator(orbff, atoms_adapter=atoms_adapter, device=device)
except TypeError:
    # Older API signature without atoms_adapter keyword
    calc = ORBCalculator(orbff, device=device)

atoms.calc = calc

energy = atoms.get_potential_energy()
forces = atoms.get_forces()

print(f"Energy (eV): {energy:.6f}")
print(f"Forces shape: {forces.shape}")
print(f"Max force component: {abs(forces).max():.6f} eV/Å")

# Basic sanity: forces should not be all zero for a non-equilibrium geometry
if abs(forces).max() < 1e-8:
    print("⚠ Warning: forces are essentially zero — verify model/geometry.")
else:
    print("✓ Forces are non-zero; model inference looks healthy.")

# ------------------------------------------------------------------
print("\n" + "=" * 60)
print("Verification complete.")
print("=" * 60)
