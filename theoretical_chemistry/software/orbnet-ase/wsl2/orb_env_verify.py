#!/usr/bin/env python
"""
orb_env_verify_latest.py
Verification script for orb-models v0.7.0 (latest) in orb_env.
Tests on H2O molecule, prioritizing the new orbmol_v2 model.
"""

import os
import sys
import time
import warnings
import subprocess

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

public_names = [n for n in dir(pretrained) if not n.startswith("_")]
print("Public symbols in pretrained module:")
for name in public_names:
    print(f"  - {name}")

if hasattr(pretrained, "ORB_PRETRAINED_MODELS"):
    print("\nORB_PRETRAINED_MODELS registry keys:")
    for key in pretrained.ORB_PRETRAINED_MODELS:
        print(f"  - {key}")

# ------------------------------------------------------------------
print("\n" + "=" * 60)
print("4. Load Latest Model & Run on H2O")
print("=" * 60)

from ase.build import molecule

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

orbff = None
atoms_adapter = None
model_loaded = False
model_name = None

# --- Priority 1: orbmol_v2 (new in v0.7.0, molecular systems) ---
if hasattr(pretrained, "orbmol_v2"):
    print("Loading pretrained.orbmol_v2(...) [new in v0.7.0]")
    try:
        result = pretrained.orbmol_v2(device=device)
        if isinstance(result, tuple):
            orbff, atoms_adapter = result
        else:
            orbff = result
        model_loaded = True
        model_name = "orbmol_v2"
    except Exception as e:
        print(f"  orbmol_v2 failed: {e}")

# --- Priority 2: orb_v2 (stable fallback) ---
if not model_loaded and hasattr(pretrained, "orb_v2"):
    print("Loading pretrained.orb_v2(...) [fallback]")
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

# --- Priority 3: first registry entry ---
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
    except Exception as e:
        print(f"  Fallback failed: {e}")

if not model_loaded:
    print("⚠ Could not load any pretrained model.")
    sys.exit(1)

print(f"✓ Loaded model: {model_name}")

# ------------------------------------------------------------------
# Build H2O and set charge/spin (required by orbmol_v2, safe for all)
atoms = molecule("H2O")
atoms.info["charge"] = 0   # neutral
atoms.info["spin"] = 1     # singlet (2S+1)
print(f"Test system: H2O ({len(atoms)} atoms), charge=0, spin=1")

# ------------------------------------------------------------------
# Build calculator (v0.7.0 may require atoms_adapter)
try:
    calc = ORBCalculator(orbff, atoms_adapter=atoms_adapter, device=device)
except TypeError:
    try:
        calc = ORBCalculator(orbff, device=device)
    except TypeError:
        # v0.7.0 new API: ORBCalculator(model, device=...)
        calc = ORBCalculator(orbff, device=device)

atoms.calc = calc

energy = atoms.get_potential_energy()
forces = atoms.get_forces()

print(f"Energy (eV): {energy:.6f}")
print(f"Forces shape: {forces.shape}")
print(f"Max force component: {abs(forces).max():.6f} eV/Å")

if abs(forces).max() < 1e-8:
    print("⚠ Warning: forces are essentially zero.")
else:
    print("✓ Forces are non-zero; model inference looks healthy.")

# ------------------------------------------------------------------
print("\n" + "=" * 60)
print("5. Locate orb-models Checkpoints on Disk")
print("=" * 60)

print("Cache-related environment variables:")
for var in ("ORB_MODELS_CACHE", "CACHED_PATH_CACHE_ROOT",
            "XDG_CACHE_HOME", "HF_HOME", "TRANSFORMERS_CACHE"):
    val = os.environ.get(var)
    print(f"  {var} = {val}" if val else f"  {var} = (unset)")

orb_cache_roots = []
for candidate in (
    os.path.expanduser(os.environ.get("ORB_MODELS_CACHE", "")),
    os.path.expanduser("~/.cache/orb_models"),
    os.path.expanduser("~/.cache/cached_path"),
    os.path.join(os.path.expanduser(os.environ.get("XDG_CACHE_HOME", "~/.cache")),
                 "orb_models"),
):
    if candidate and os.path.isdir(candidate) and candidate not in orb_cache_roots:
        orb_cache_roots.append(candidate)

if not orb_cache_roots:
    print("\nNo orb-models-specific cache directory found.")
    hf_orb = os.path.expanduser("~/.cache/huggingface/hub")
    if os.path.isdir(hf_orb):
        for entry in os.listdir(hf_orb):
            if "orb" in entry.lower():
                orb_cache_roots.append(os.path.join(hf_orb, entry))
else:
    print("\norb-models cache directory:")
    for d in orb_cache_roots:
        print(f"  {d}")

checkpoint_exts = (".ckpt", ".pt", ".pth", ".bin", ".safetensors")
ORB_MARKERS = ("orb_models", "orb-models", "orb-v", "orb_d3",
               "orb-mptraj", "forcefields/orb", "orbital-materials",
               "orbmol")

def human_size(n):
    for unit in ("B", "K", "M", "G", "T"):
        if n < 1024:
            return f"{n:6.1f}{unit}"
        n /= 1024
    return f"{n:6.1f}P"

def is_orb_checkpoint(path):
    low = path.lower()
    return (low.endswith(checkpoint_exts)
            and any(m in low for m in ORB_MARKERS))

print("\norb-models checkpoint files (newest first, ls -lt style):")

hits = []
for root in orb_cache_roots:
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            if not is_orb_checkpoint(full):
                continue
            try:
                st = os.stat(full)
            except OSError:
                continue
            hits.append((st.st_mtime, full, st.st_size))

if not hits:
    print("  (No orb-models checkpoint files found.)")
else:
    hits.sort(key=lambda t: t[0], reverse=True)
    print(f"  {'mtime':<20} {'size':>10}  path")
    print(f"  {'-' * 100}")
    for mtime, full, size in hits:
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime))
        print(f"  {ts:<20} {human_size(size):>10}  {full}")

    print(f"\n  Total orb-models checkpoints: {len(hits)}")
    total = sum(s for _, _, s in hits)
    print(f"  Total size on disk:           {human_size(total)}")

# literal ls -lt on primary
primary = os.path.expanduser("~/.cache/orb_models")
if os.path.isdir(primary):
    print(f"\nLiteral `ls -lt {primary}`:")
    try:
        out = subprocess.check_output(["ls", "-lt", primary],
                                      text=True, stderr=subprocess.STDOUT)
        for line in out.splitlines():
            print(f"  {line}")
    except Exception as e:
        print(f"  ls failed: {e}")

print("\n" + "=" * 60)
print("Verification complete.")
print("=" * 60)
