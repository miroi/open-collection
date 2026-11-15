import os
import platform
import torch
import ase
from ase.build import molecule
from ase.units import kcal, mol
from torchmdnet.calculators import TMDNETCalculator
from huggingface_hub import hf_hub_download


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ---------------------------------------------------------------------------
# 1. Environment / device diagnostics
# ---------------------------------------------------------------------------
section("ENVIRONMENT & DEVICE")

print(f"Python           : {platform.python_version()} ({platform.system()} {platform.machine()})")
print(f"PyTorch          : {torch.__version__}")
print(f"PyTorch CUDA     : {torch.version.cuda}")
print(f"CUDA available   : {torch.cuda.is_available()}")

if torch.cuda.is_available():
    n = torch.cuda.device_count()
    print(f"CUDA device count: {n}")
    for i in range(n):
        props = torch.cuda.get_device_properties(i)
        print(f"  [{i}] {props.name} | "
              f"{props.total_memory / 1024**3:.2f} GiB | "
              f"sm_{props.major}{props.minor} | "
              f"multi_processor_count={props.multi_processor_count}")
    device = "cuda"
else:
    print("No CUDA device found -> falling back to CPU")
    device = "cpu"

print(f"ASE              : {ase.__version__}")

# ---------------------------------------------------------------------------
# 2. Download / locate the AceFF model
# ---------------------------------------------------------------------------
section("ACEFF MODEL")

REPO_ID = "Acellera/AceFF-2.0"
FILENAME = "aceff_v2.0.ckpt"

model_file_path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
size_mb = os.path.getsize(model_file_path) / 1024**2
print(f"Repo ID          : {REPO_ID}")
print(f"File name        : {FILENAME}")
print(f"Local path       : {model_file_path}")
print(f"File size        : {size_mb:.2f} MiB")

# ---------------------------------------------------------------------------
# 3. Build calculator
# ---------------------------------------------------------------------------
section("CALCULATOR")

calc = TMDNETCalculator(model_file_path, device=device)

print(f"Calculator class : {type(calc).__name__}")
print(f"Requested device : {device}")

# Some versions expose .device; print defensively
calc_device = getattr(calc, "device", None)
if calc_device is None and hasattr(calc, "model"):
    try:
        p = next(calc.model.parameters())
        calc_device = p.device
    except StopIteration:
        calc_device = "unknown"
print(f"Resolved device  : {calc_device}")

# Try to report model hyper-parameters if available
model = getattr(calc, "model", None)
if model is not None:
    n_params = sum(p.numel() for p in model.parameters())
    n_trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Model class      : {type(model).__name__}")
    print(f"Parameters       : {n_params:,} (trainable {n_trainable:,})")
    hp = getattr(model, "hparams", None)
    if hp is not None:
        print("Hyper-parameters :")
        for k, v in sorted(dict(hp).items()):
            print(f"    {k:<28}: {v}")

# ---------------------------------------------------------------------------
# 4. Build molecule
# ---------------------------------------------------------------------------
section("MOLECULE")

atoms = molecule("C2H6")
atoms.calc = calc
atoms.info["charge"] = 0

symbols = atoms.get_chemical_symbols()
formula = atoms.get_chemical_formula()
print(f"Formula          : {formula}")
print(f"Number of atoms  : {len(atoms)}")
print(f"Symbols          : {symbols}")
print(f"Charge           : {atoms.info['charge']}")
print(f"Cell             : {'periodic' if atoms.pbc.any() else 'non-periodic (molecule)'}")

# ---------------------------------------------------------------------------
# 5. Run single-point calculation
# ---------------------------------------------------------------------------
section("SINGLE-POINT CALCULATION")

energy = atoms.get_potential_energy()      # eV
forces = atoms.get_forces()                # eV / Å
fmax = (forces ** 2).sum(axis=1).max() ** 0.5

print(f"Energy           : {energy:.6f} eV")
print(f"Energy           : {energy / mol:.6f} kcal/mol")
print(f"Energy / atom    : {energy / len(atoms):.6f} eV/atom")
print(f"Forces shape     : {forces.shape}")
print(f"Max force (fmax) : {fmax:.6f} eV/Å")
print(f"RMS force        : {(forces**2).sum()/forces.size)**0.5:.6f} eV/Å")
print("Forces (eV/Å):")
for i, (sym, f) in enumerate(zip(symbols, forces)):
    print(f"  {i:>2} {sym:<3} {f[0]: .6f} {f[1]: .6f} {f[2]: .6f}")

# Sanity checks
if not torch.isfinite(torch.as_tensor(energy)):
    print("WARNING: energy is not finite!")
if not torch.isfinite(torch.as_tensor(forces)).all():
    print("WARNING: forces contain non-finite values!")

section("DONE")
