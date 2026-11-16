#!/usr/bin/env python
"""
orb_env_verify.py
Verification script for orb-models v0.7.0 in orb_env.
Tests on H2O molecule using orbmol_v2.

Fixes for 0.7.0:
  - ORBCalculator imported from orb_models.forcefield.inference.calculator
  - atomic_system import removed (no longer exported at top level)
  - Section 5 resolves cached_path hash-named blobs via the "resource"
    metadata key (cached_path stores the original URL there, not "url").
    orbmol_v2 weights are served from AWS S3, so on-disk names are hashes.
"""

import os
import sys
import time
import json
import glob
import warnings

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

# 0.7.0: calculator lives under inference.calculator
from orb_models.forcefield.inference.calculator import ORBCalculator
print("✓ orb_models.forcefield.inference.calculator.ORBCalculator")

# Note: atomic_system is no longer re-exported from orb_models.forcefield in 0.7.0.
# The atoms_adapter returned by pretrained factories replaces its role.

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
print("4. Load Model & Run on H2O")
print("=" * 60)

from ase.build import molecule

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

orbff = None
atoms_adapter = None
model_loaded = False
model_name = None

# --- Priority 1: orbmol_v2 (v0.7.0 model for molecular systems) ---
if hasattr(pretrained, "orbmol_v2"):
    print("Loading pretrained.orbmol_v2(...)")
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

# --- Priority 2: orb_v2 fallback ---
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

if not model_loaded:
    print("⚠ Could not load any pretrained model.")
    sys.exit(1)

print(f"✓ Loaded model: {model_name}")

# ------------------------------------------------------------------
# Build H2O and set charge/spin (required by orbmol_v2)
atoms = molecule("H2O")
atoms.info["charge"] = 0   # neutral
atoms.info["spin"] = 1     # singlet (2S+1)
print(f"Test system: H2O ({len(atoms)} atoms), charge=0, spin=1")

# ------------------------------------------------------------------
# Build calculator (0.7.0: pass atoms_adapter)
calc = ORBCalculator(orbff, atoms_adapter=atoms_adapter, device=device)
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

cached_path_root = os.path.expanduser(
    os.environ.get("CACHED_PATH_CACHE_ROOT")
    or os.path.join(os.environ.get("XDG_CACHE_HOME", "~/.cache"),
                    "cached_path")
)
hf_hub_cache = os.path.expanduser("~/.cache/huggingface/hub")

roots = [r for r in (cached_path_root, hf_hub_cache) if os.path.isdir(r)]
print("\nScanned cache roots:")
for d in roots:
    print(f"  {d}")

# cached_path stores the original URL under "resource"; older versions
# used "url" or "source". Match any of them.
ORB_URL_MARKERS = ("orbmol", "orbitalmaterials", "/forcefields/orb",
                   "orb-v2", "orb-v3", "orb-d3", "/forcefields/")

def human_size(n):
    for unit in ("B", "K", "M", "G", "T"):
        if n < 1024:
            return f"{n:6.1f}{unit}"
        n /= 1024
    return f"{n:6.1f}P"

def url_is_orb(url: str) -> bool:
    low = (url or "").lower()
    return any(m in low for m in ORB_URL_MARKERS)

def extract_url(meta: dict) -> str:
    for key in ("resource", "url", "source", "requested_url", "path"):
        v = meta.get(key)
        if isinstance(v, str) and v.startswith(("http", "s3", "gs", "hf")):
            return v
    return ""

# ---- 5a. cached_path: resolve hash-named blobs via metadata JSON ----
print("\norb-models checkpoints in cached_path (via metadata 'resource' URL):")
hits = []
for jpath in glob.glob(os.path.join(cached_path_root, "*.json")):
    try:
        meta = json.load(open(jpath))
    except Exception:
        continue
    url = extract_url(meta)
    if not url_is_orb(url):
        continue
    # Blob is sibling without ".json"
    blob = jpath[:-5]
    if not os.path.exists(blob):
        continue
    st = os.stat(blob)
    hits.append((st.st_mtime, blob, st.st_size, url))

if not hits:
    print("  (No cached_path entries with orb URLs.)")
else:
    hits.sort(key=lambda t: t[0], reverse=True)
    print(f"  {'mtime':<20} {'size':>10}  path")
    print(f"  {'-' * 110}")
    for mtime, blob, size, url in hits:
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime))
        print(f"  {ts:<20} {human_size(size):>10}  {blob}")
        print(f"  {'':<20} {'':>10}  ↳ {url}")
    print(f"\n  Total orb-models checkpoints: {len(hits)}")
    total = sum(s for _, _, s, _ in hits)
    print(f"  Total size on disk:           {human_size(total)}")

# ---- 5b. HuggingFace hub (fallback, filename-based) ----
print("\norb-models checkpoints in HuggingFace hub (by filename marker):")
hf_hits = []
for dirpath, dirnames, filenames in os.walk(hf_hub_cache):
    if "models--" in dirpath:
        dirnames[:] = [d for d in dirnames if "orb" in d.lower()]
    for fn in filenames:
        low = fn.lower()
        if not low.endswith((".ckpt", ".pt", ".pth", ".safetensors")):
            continue
        if not any(m in low for m in ("orbmol", "orb-v", "orb_d3", "orb-d3")):
            continue
        full = os.path.join(dirpath, fn)
        try:
            st = os.stat(full)
        except OSError:
            continue
        hf_hits.append((st.st_mtime, full, st.st_size))

if not hf_hits:
    print("  (No orb-models files under HF hub cache.)")
else:
    hf_hits.sort(key=lambda t: t[0], reverse=True)
    for mtime, full, size in hf_hits:
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime))
        print(f"  {ts:<20} {human_size(size):>10}  {full}")

print("\n" + "=" * 60)
print("Verification complete.")
print("=" * 60)
