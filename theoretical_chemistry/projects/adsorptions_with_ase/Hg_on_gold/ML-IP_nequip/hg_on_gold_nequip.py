#!/usr/bin/env python
"""
Pd adsorption on Au(111) with a NequIP/Allegro potential via ASE.

Workflow
  1. Relax bulk Au with the model -> model-consistent lattice constant
  2. Build Au(111) slab, relax it (bottom layers fixed)
  3. Place one Pd atom on ontop / bridge / fcc / hcp sites, relax each
  4. Report adsorption energies

Usage
  python pd_on_au111_nequip.py --model path/to/model.nequip.pth

Requirements: ase, nequip (the model must have been trained with Au and Pd).
The calculator API changed between NequIP versions; both are handled below,
but check against your installed version if loading fails.
"""
import argparse

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
# Calculator
# --------------------------------------------------------------------------
def load_calculator(model_path: str, device: str, type_names=("Au", "Pd")):
    """Return a NequIP ASE calculator for either old (<=0.6) or new (>=0.7) API.

    type_names must match the `type_names` used in training, in order.
    If your model uses chemical symbols as type names, the map below works as is.
    """
    from nequip.ase import NequIPCalculator

    # Newer NequIP (0.7+): compiled model (.nequip.pth / .nequip.pt2)
    if hasattr(NequIPCalculator, "from_compiled_model"):
        return NequIPCalculator.from_compiled_model(
            compile_path=model_path,
            device=device,
            chemical_species_to_atom_type_map=True,  # type names == chemical symbols
        )

    # Older NequIP (<=0.6): deployed model
    return NequIPCalculator.from_deployed_model(
        model_path=model_path,
        device=device,
        species_to_type_name={s: s for s in type_names},
    )


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def relax_bulk_lattice(symbol, a0, calc, fmax=0.01):
    """Relax a primitive fcc cell (positions + cell) and return the cubic a."""
    atoms = bulk(symbol, "fcc", a=a0)
    atoms.calc = calc
    BFGS(CellFilter(atoms), logfile=None).run(fmax=fmax, steps=200)
    a = (4 * atoms.get_volume()) ** (1 / 3)  # primitive fcc volume = a^3/4
    return a, atoms.get_potential_energy() / len(atoms)


def make_slab(a, size=(4, 4), layers=4, vacuum=10.0, n_fixed=2):
    slab = fcc111("Au", size=(*size, layers), a=a, vacuum=vacuum, orthogonal=False)
    slab.pbc = (True, True, False)
    z = slab.positions[:, 2]
    layer_z = np.unique(np.round(z, 3))
    fixed = [i for i, zi in enumerate(z) if round(zi, 3) in layer_z[:n_fixed]]
    slab.set_constraint(FixAtoms(indices=fixed))
    return slab


def relax(atoms, calc, fmax=0.03, steps=300, traj=None):
    atoms.calc = calc
    opt = BFGS(atoms, trajectory=traj, logfile=None)
    opt.run(fmax=fmax, steps=steps)
    return atoms.get_potential_energy()


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True, help="Path to compiled/deployed NequIP model")
    p.add_argument("--device", default="cpu")
    p.add_argument("--size", type=int, nargs=2, default=[4, 4], help="Surface supercell (nx ny)")
    p.add_argument("--layers", type=int, default=4)
    p.add_argument("--height", type=float, default=2.4, help="Initial Pd height above surface (A)")
    p.add_argument("--fmax", type=float, default=0.03)
    p.add_argument(
        "--e-pd-atom",
        type=float,
        default=None,
        help="Reference energy of an isolated Pd atom in the model's energy zero (eV). "
        "Only meaningful if your training set energies include it; otherwise use the "
        "bulk-referenced value printed below.",
    )
    args = p.parse_args()

    calc = load_calculator(args.model, args.device)

    # 1. Bulk references (model-consistent)
    a_au, e_au_bulk = relax_bulk_lattice("Au", 4.08, calc)
    a_pd, e_pd_bulk = relax_bulk_lattice("Pd", 3.89, calc)
    print(f"Model Au lattice constant: {a_au:.4f} A  (E = {e_au_bulk:.4f} eV/atom)")
    print(f"Model Pd lattice constant: {a_pd:.4f} A  (E = {e_pd_bulk:.4f} eV/atom)")

    # 2. Clean slab
    slab = make_slab(a_au, size=tuple(args.size), layers=args.layers)
    e_slab = relax(slab, calc, fmax=args.fmax, traj="slab_clean.traj")
    write("slab_clean.xyz", slab)
    print(f"Clean slab energy: {e_slab:.4f} eV ({len(slab)} atoms)")

    # 3. Adsorption sites (ASE fcc111 site names)
    sites = ["ontop", "bridge", "fcc", "hcp"]
    results = {}
    for site in sites:
        ads = slab.copy()
        ads.set_constraint(slab.constraints[0])  # keep the same frozen layers
        add_adsorbate(ads, "Pd", height=args.height, position=site)
        e_tot = relax(ads, calc, fmax=args.fmax, traj=f"pd_{site}.traj")
        write(f"pd_{site}.xyz", ads)

        pd_z = ads.positions[-1, 2]
        top_au_z = ads.positions[: len(slab), 2].max()
        results[site] = (e_tot, pd_z - top_au_z)

    # 4. Adsorption energies
    print("\nSite     E_total (eV)   dz(Pd-Au) (A)   E_ads vs bulk Pd (eV)", end="")
    print("   E_ads vs gas atom (eV)" if args.e_pd_atom is not None else "")
    for site, (e_tot, dz) in results.items():
        e_rel_bulk = e_tot - e_slab - e_pd_bulk
        line = f"{site:<8} {e_tot:12.4f} {dz:14.3f} {e_rel_bulk:22.4f}"
        if args.e_pd_atom is not None:
            line += f" {e_tot - e_slab - args.e_pd_atom:24.4f}"
        print(line)

    best = min(results, key=lambda s: results[s][0])
    print(f"\nMost stable site: {best}")


if __name__ == "__main__":
    main()
