#!/usr/bin/env python
"""
Atom adsorption (default: Pd) on Au(111) with a NequIP/Allegro potential via ASE.
Adsorption energies are reported against two references, for comparison:

    E_ads(gas)  = E(slab + atom) - E(slab) - E(isolated atom)
    E_ads(bulk) = E(slab + atom) - E(slab) - E(bulk per atom)

All arguments are optional. Just run:

    python pd_on_gold_nequip.py

Edit the DEFAULTS block below to change the model path and other settings,
or override on the command line, e.g.:

    python pd_on_gold_nequip.py --model other.nequip.pth --e-atom -1.23
"""
import argparse
import os

import numpy as np
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
DEFAULT_MODEL = os.environ.get("NEQUIP_MODEL", "model.nequip.pt2")  # <-- set your model path
DEFAULT_DEVICE = "cpu"
DEFAULT_ADSORBATE = "Pd"
DEFAULT_SIZE = (4, 4)
DEFAULT_LAYERS = 4
DEFAULT_VACUUM = 10.0
DEFAULT_N_FIXED = 1
DEFAULT_HEIGHT = 2.4  # initial adsorbate height (A); use ~2.8 for Hg
DEFAULT_FMAX = 0.03
DEFAULT_E_ATOM = None  # isolated-atom energy (eV); None -> computed with the model
ATOM_BOX = 30.0  # box size (A) for the isolated-atom calculation

# Starting lattice constants (A) for fcc bulk references.
# Hg is not fcc (liquid at RT), so no bulk reference is computed for it.
FCC_A0 = {"Au": 4.08, "Pd": 3.89, "Pt": 3.92, "Ag": 4.09, "Cu": 3.61}


# --------------------------------------------------------------------------
# Calculator
# --------------------------------------------------------------------------
def load_calculator(model_path, device, type_names):
    """NequIP ASE calculator for either old (<=0.6) or new (>=0.7) API."""
    from nequip.ase import NequIPCalculator

    if hasattr(NequIPCalculator, "from_compiled_model"):  # NequIP 0.7+
        return NequIPCalculator.from_compiled_model(
            compile_path=model_path,
            device=device,
            chemical_species_to_atom_type_map=True,  # type names == chemical symbols
        )
    return NequIPCalculator.from_deployed_model(  # NequIP <= 0.6
        model_path=model_path,
        device=device,
        species_to_type_name={s: s for s in type_names},
    )


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def relax_bulk_lattice(symbol, a0, calc, fmax=0.01):
    """Relax a primitive fcc cell (positions + cell); return cubic a and E/atom."""
    atoms = bulk(symbol, "fcc", a=a0)
    atoms.calc = calc
    BFGS(CellFilter(atoms), logfile=None).run(fmax=fmax, steps=200)
    a = (4 * atoms.get_volume()) ** (1 / 3)
    return a, atoms.get_potential_energy() / len(atoms)


def isolated_atom_energy(symbol, calc, box=ATOM_BOX):
    """Energy of a single atom alone in a large box (no neighbours within cutoff)."""
    atom = Atoms(symbol, positions=[[box / 2] * 3], cell=[box] * 3, pbc=False)
    atom.calc = calc
    return atom.get_potential_energy()


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
                   help="Isolated adsorbate-atom energy (eV). If omitted, computed with the model.")
    args = p.parse_args()

    if not os.path.isfile(args.model):
        raise SystemExit(
            f"Model file not found: {args.model}\n"
            f"Set DEFAULT_MODEL in the script, export NEQUIP_MODEL=/path/to/model, or pass --model."
        )

    ads_sym = args.adsorbate
    calc = load_calculator(args.model, args.device, type_names=("Au", ads_sym))

    # 1. Au lattice constant (model-consistent)
    a_au, _ = relax_bulk_lattice("Au", FCC_A0["Au"], calc)
    print(f"Model Au lattice constant: {a_au:.4f} A")

    # 2. References for the adsorbate: bulk (if fcc) and gas-phase atom
    e_bulk = None
    if ads_sym in FCC_A0:
        a_x, e_bulk = relax_bulk_lattice(ads_sym, FCC_A0[ads_sym], calc)
        print(f"Model {ads_sym} fcc lattice constant: {a_x:.4f} A  (E_bulk = {e_bulk:.4f} eV/atom)")
    else:
        print(f"No fcc bulk reference for {ads_sym}; bulk column will be skipped.")

    if args.e_atom is not None:
        e_atom = args.e_atom
        print(f"{ads_sym} gas-atom energy (user-supplied): {e_atom:.4f} eV")
    else:
        e_atom = isolated_atom_energy(ads_sym, calc)
        print(f"{ads_sym} gas-atom energy (model, isolated atom in {ATOM_BOX:.0f} A box): {e_atom:.4f} eV")

    if e_bulk is not None:
        print(f"E_coh-like (E_atom - E_bulk): {e_atom - e_bulk:.4f} eV")

    # 3. Clean slab
    slab = make_slab(a_au, tuple(args.size), args.layers, args.vacuum, args.n_fixed)
    e_slab = relax(slab, calc, args.fmax, traj="slab_clean.traj")
    write("slab_clean.xyz", slab)
    print(f"Clean slab energy: {e_slab:.4f} eV ({len(slab)} atoms)")

    # 4. Adsorption sites
    results = {}
    for site in ["ontop", "bridge", "fcc", "hcp"]:
        ads = slab.copy()
        ads.set_constraint(slab.constraints[0])
        add_adsorbate(ads, ads_sym, height=args.height, position=site)
        e_tot = relax(ads, calc, args.fmax, traj=f"{ads_sym.lower()}_{site}.traj")
        write(f"{ads_sym.lower()}_{site}.xyz", ads)
        dz = ads.positions[-1, 2] - ads.positions[: len(slab), 2].max()
        results[site] = (e_tot, dz)

    # 5. Report
    header = f"{'Site':<8} {'E_total (eV)':>13} {'dz (A)':>8} {'E_ads gas (eV)':>15}"
    if e_bulk is not None:
        header += f" {'E_ads bulk (eV)':>16}"
    print("\n" + header)
    for site, (e_tot, dz) in results.items():
        line = f"{site:<8} {e_tot:13.4f} {dz:8.3f} {e_tot - e_slab - e_atom:15.4f}"
        if e_bulk is not None:
            line += f" {e_tot - e_slab - e_bulk:16.4f}"
        print(line)

    best = min(results, key=lambda s: results[s][0])
    print(f"\nMost stable site: {best}")


if __name__ == "__main__":
    main()
