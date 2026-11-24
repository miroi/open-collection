#!/usr/bin/env python
"""
Atom adsorption (default: Hg) on Au(111) with a NequIP/Allegro potential via ASE.

All arguments are optional. Just run:

    python hg_on_gold_nequip.py

Edit the DEFAULTS block below to change the model path and other settings,
or override on the command line, e.g.:

    python hg_on_gold_nequip.py --model other.nequip.pt2 --adsorbate Pd
"""
import argparse
import os

import numpy as np
import torch
from ase import Atoms
from ase.build import add_adsorbate, bulk, fcc111
from ase.constraints import FixAtoms
from ase.io import write
from ase.optimize import BFGS

try:  # ASE >= 3.23
    from ase.filters import FrechetCellFilter as CellFilter
except ImportError:
    from ase.constraints import ExpCellFilter as CellFilter

# --------------------------------------------------------------------------
# DEFAULTS  (edit here)
# --------------------------------------------------------------------------
DEFAULT_MODEL = os.environ.get("NEQUIP_MODEL", "model.nequip.pt2")
DEFAULT_DEVICE = "cuda"
DEFAULT_ADSORBATE = "Hg"
DEFAULT_SIZE = (4, 4)
DEFAULT_LAYERS = 4
DEFAULT_VACUUM = 10.0
DEFAULT_N_FIXED = 2
DEFAULT_HEIGHT = 2.8  # initial adsorbate height (A); Hg sits higher than Pd
DEFAULT_FMAX = 0.03
DEFAULT_E_ATOM = None  # isolated-atom reference energy (eV); auto-computed if None

# Starting lattice constants (A) for fcc bulk references.
# Hg is not fcc (liquid at RT), so no bulk reference is computed for it.
FCC_A0 = {"Au": 4.08, "Pd": 3.89, "Pt": 3.92, "Ag": 4.09, "Cu": 3.61}


# --------------------------------------------------------------------------
# Calculator & Diagnostics
# --------------------------------------------------------------------------
def load_calculator(model_path, device, type_names):
    """NequIP ASE calculator for either old (<=0.6) or new (>=0.7) API."""
    if device.startswith("cuda") and torch.cuda.is_available():
        torch.set_float32_matmul_precision("high")

    try:
        from nequip.integrations.ase import NequIPCalculator
    except ImportError:
        from nequip.ase import NequIPCalculator

    if hasattr(NequIPCalculator, "from_compiled_model"):  # NequIP 0.7+
        return NequIPCalculator.from_compiled_model(
            compile_path=model_path,
            device=device,
            chemical_species_to_atom_type_map=True,
        )
    return NequIPCalculator.from_deployed_model(  # NequIP <= 0.6
        model_path=model_path,
        device=device,
        species_to_type_name={s: s for s in type_names},
    )


def print_model_info(model_path, calc, device):
    """Inspect and print metadata from the loaded NequIP calculator and hardware."""
    import nequip

    file_size_mb = os.path.getsize(model_path) / (1024 ** 2)
    r_max = getattr(calc, "r_max", None)
    type_names = getattr(calc, "type_names", None)
    species_map = getattr(calc, "chemical_species_to_atom_type_map", None)

    gpu_info = "CPU"
    if device.startswith("cuda") and torch.cuda.is_available():
        idx = torch.cuda.current_device()
        props = torch.cuda.get_device_properties(idx)
        vram_gb = props.total_memory / (1024 ** 3)
        gpu_info = f"{props.name} ({vram_gb:.1f} GB VRAM, CUDA {torch.version.cuda})"

    print("=" * 68)
    print("NEQUIP MODEL & RUNTIME INFORMATION")
    print("=" * 68)
    print(f"  Model file      : {os.path.abspath(model_path)} ({file_size_mb:.1f} MB)")
    print(f"  NequIP / Torch  : nequip {nequip.__version__} | torch {torch.__version__}")
    print(f"  Compute device  : {device} -> {gpu_info}")
    if r_max is not None:
        print(f"  Cutoff (r_max)  : {float(r_max):.3f} A")
    if type_names is not None:
        n_types = len(type_names)
        preview = ", ".join(type_names[:12]) + (" ..." if n_types > 12 else "")
        print(f"  Model species   : {n_types} types [{preview}]")
    elif isinstance(species_map, dict):
        n_types = len(species_map)
        preview = ", ".join(list(species_map.keys())[:12]) + (" ..." if n_types > 12 else "")
        print(f"  Mapped species  : {n_types} types [{preview}]")
    print("=" * 68)


def print_slab_info(slab, args, a_au):
    """Print detailed geometry and simulation parameters for the Au(111) slab."""
    cell = slab.get_cell()
    a_len, b_len, c_len = cell.lengths()
    area = np.linalg.norm(np.cross(cell[0], cell[1]))

    n_total = len(slab)
    n_fixed = len(slab.constraints[0].index) if slab.constraints else 0
    n_free = n_total - n_fixed

    z_coords = slab.positions[:, 2]
    slab_thickness = z_coords.max() - z_coords.min()

    print("\n" + "=" * 68)
    print("SLAB & ADSORPTION SIMULATION PARAMETERS")
    print("=" * 68)
    print(f"  Surface         : Au(111) fcc | bulk a = {a_au:.4f} A")
    print(f"  Supercell       : {args.size[0]} x {args.size[1]} x {args.layers} layers")
    print(f"  Cell vectors    : a = {a_len:.3f} A, b = {b_len:.3f} A, c = {c_len:.3f} A")
    print(f"  Surface area    : {area:.2f} A^2 (coverage = 1/{args.size[0]*args.size[1]} ML)")
    print(f"  Slab thickness  : {slab_thickness:.3f} A (vacuum = {args.vacuum:.1f} A total)")
    print(f"  Atom counts     : {n_total} total ({n_free} relaxed, {n_fixed} fixed in bottom {args.n_fixed} layers)")
    print(f"  Adsorbate       : {args.adsorbate} (initial height = {args.height:.2f} A)")
    print(f"  Optimizer       : BFGS (fmax = {args.fmax:.4f} eV/A)")
    print("=" * 68 + "\n")


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def relax_bulk_lattice(symbol, a0, calc, fmax=0.01):
    atoms = bulk(symbol, "fcc", a=a0)
    atoms.calc = calc
    BFGS(CellFilter(atoms), logfile=None).run(fmax=fmax, steps=200)
    a = (4 * atoms.get_volume()) ** (1 / 3)
    return a, atoms.get_potential_energy() / len(atoms)


def get_isolated_atom_energy(symbol, calc):
    """Compute the potential energy of an isolated gas-phase atom."""
    atom = Atoms(symbol, positions=[[0.0, 0.0, 0.0]], cell=[20.0, 20.0, 20.0], pbc=False)
    atom.calc = calc
    return float(atom.get_potential_energy())


def make_slab(a, size, layers, vacuum, n_fixed):
    slab = fcc111("Au", size=(*size, layers), a=a, vacuum=vacuum, orthogonal=False)
    slab.pbc = (True, True, False)
    z = slab.positions[:, 2]
    layer_z = np.unique(np.round(z, 3))
    fixed = [i for i, zi in enumerate(z) if round(zi, 3) in layer_z[:n_fixed]]
    slab.set_constraint(FixAtoms(indices=fixed))
    return slab


def relax(atoms, calc, fmax, steps=300, traj=None):
    atoms.calc = calc
    BFGS(atoms, trajectory=traj, logfile=None).run(fmax=fmax, steps=steps)
    return atoms.get_potential_energy()


def write_clean_xyz(filename, atoms):
    """Write structure to extended XYZ without unhashable ASE metadata warnings."""
    atoms_copy = atoms.copy()
    atoms_copy.info.pop("adsorbate_info", None)
    write(filename, atoms_copy)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--model", default=DEFAULT_MODEL, help="Path to compiled/deployed NequIP model")
    p.add_argument("--device", default=DEFAULT_DEVICE)
    p.add_argument("--adsorbate", default=DEFAULT_ADSORBATE, help="Adsorbate element symbol")
    p.add_argument("--size", type=int, nargs=2, default=list(DEFAULT_SIZE), help="Surface supercell (nx ny)")
    p.add_argument("--layers", type=int, default=DEFAULT_LAYERS)
    p.add_argument("--vacuum", type=float, default=DEFAULT_VACUUM)
    p.add_argument("--n-fixed", type=int, default=DEFAULT_N_FIXED, help="Number of frozen bottom layers")
    p.add_argument("--height", type=float, default=DEFAULT_HEIGHT, help="Initial adsorbate height (A)")
    p.add_argument("--fmax", type=float, default=DEFAULT_FMAX)
    p.add_argument("--e-atom", "--e-pd-atom", dest="e_atom", type=float, default=DEFAULT_E_ATOM,
                   help="Isolated adsorbate-atom energy in the model's energy zero (eV)")
    args = p.parse_args()

    if not os.path.isfile(args.model):
        raise SystemExit(
            f"Model file not found: {args.model}\n"
            f"Set DEFAULT_MODEL in the script, export NEQUIP_MODEL=/path/to/model, or pass --model."
        )

    ads_sym = args.adsorbate
    calc = load_calculator(args.model, args.device, type_names=("Au", ads_sym))
    print_model_info(args.model, calc, args.device)

    # 1. Bulk and isolated-atom references
    a_au, e_au_bulk = relax_bulk_lattice("Au", FCC_A0["Au"], calc)
    print(f"Model Au lattice constant : {a_au:.4f} A  (E = {e_au_bulk:.4f} eV/atom)")

    e_ads_bulk = None
    if ads_sym in FCC_A0:
        a_x, e_ads_bulk = relax_bulk_lattice(ads_sym, FCC_A0[ads_sym], calc)
        print(f"Model {ads_sym} fcc lattice constant: {a_x:.4f} A  (E = {e_ads_bulk:.4f} eV/atom)")
    else:
        print(f"No fcc bulk reference for {ads_sym}.")

    if args.e_atom is None:
        e_atom = get_isolated_atom_energy(ads_sym, calc)
        print(f"Isolated {ads_sym} gas-atom energy (computed): {e_atom:.4f} eV")
    else:
        e_atom = args.e_atom
        print(f"Isolated {ads_sym} gas-atom energy (user-supplied): {e_atom:.4f} eV")

    # 2. Clean slab
    slab = make_slab(a_au, tuple(args.size), args.layers, args.vacuum, args.n_fixed)
    print_slab_info(slab, args, a_au)

    e_slab = relax(slab, calc, args.fmax, traj="slab_clean.traj")
    write_clean_xyz("slab_clean.xyz", slab)
    print(f"Clean slab energy: {e_slab:.4f} eV ({len(slab)} atoms)")

    # 3. Adsorption sites
    results = {}
    for site in ["ontop", "bridge", "fcc", "hcp"]:
        ads = slab.copy()
        ads.set_constraint(slab.constraints[0])
        add_adsorbate(ads, ads_sym, height=args.height, position=site)
        e_tot = relax(ads, calc, args.fmax, traj=f"{ads_sym.lower()}_{site}.traj")
        write_clean_xyz(f"{ads_sym.lower()}_{site}.xyz", ads)
        dz = ads.positions[-1, 2] - ads.positions[: len(slab), 2].max()
        results[site] = (e_tot, dz)

    # 4. Report
    header = f"{'Site':<8} {'E_total (eV)':>13} {'dz (A)':>8}"
    if e_ads_bulk is not None:
        header += f" {'E_ads vs bulk (eV)':>20}"
    header += f" {'E_ads vs gas atom (eV)':>24}"
    print("\n" + header)
    for site, (e_tot, dz) in results.items():
        line = f"{site:<8} {e_tot:13.4f} {dz:8.3f}"
        if e_ads_bulk is not None:
            line += f" {e_tot - e_slab - e_ads_bulk:20.4f}"
        line += f" {e_tot - e_slab - e_atom:24.4f}"
        print(line)

    best = min(results, key=lambda s: results[s][0])
    print(f"\nMost stable site: {best}")


if __name__ == "__main__":
    main()

