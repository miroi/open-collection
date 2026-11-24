"""
ASE + ALIGNN-FF and ALIGNN-FF + DFT-D4: Adsorption of Hg atom on Au(111) slab.

Uses a 4x4 surface slab with 4 layers and the bottom layer frozen.
Runs both the plain ALIGNN-FF calculator and the mixed ALIGNN-FF + D4
calculator (via ASE SumCalculator), then writes comparison tables.

Requires: ase, alignn, torch, dftd4
"""
import os
import re
import warnings
import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.calculators.mixing import SumCalculator
from ase.io import write
from ase.io.trajectory import Trajectory

from alignn.ff.ff import AlignnAtomwiseCalculator, default_path
from dftd4.ase import DFTD4

warnings.filterwarnings("ignore")

OUTDIR = "results"
os.makedirs(OUTDIR, exist_ok=True)


def safe(name):
    """Turn an arbitrary label into a filesystem-safe stem."""
    name = re.sub(r'[^A-Za-z0-9_\-]+', '_', name).strip('_')
    return name or "struct"


# ----------------------------------------------------------------------
# Calculators
# ----------------------------------------------------------------------
def get_alignn_calculator(device: str = "cpu") -> AlignnAtomwiseCalculator:
    """Plain ALIGNN-FF calculator (no dispersion correction)."""
    return AlignnAtomwiseCalculator(path=default_path(), device=device)


def get_alignn_d4_calculator(device: str = "cpu") -> SumCalculator:
    """ALIGNN-FF wrapped with DFT-D4 via ASE SumCalculator."""
    alignn_calc = AlignnAtomwiseCalculator(path=default_path(), device=device)
    d4_calc = DFTD4(method="PBE")  # PBE-parameterized D4
    return SumCalculator([alignn_calc, d4_calc])


# ----------------------------------------------------------------------
# Slab construction
# ----------------------------------------------------------------------
def build_au111_slab(a: float = 4.08,
                     size=(4, 4, 4),
                     vacuum: float = 10.0) -> Atoms:
    """Construct a 4x4x4 Au(111) slab and fix the bottom layer."""
    slab = fcc111('Au', size=size, a=a, vacuum=vacuum)

    z_coords = slab.get_positions()[:, 2]
    z_sorted = np.sort(z_coords)

    # Bottom layer only: all atoms within ~0.1 A of the minimum z
    fix_mask = z_coords < (z_sorted[0] + 0.1)
    slab.set_constraint(FixAtoms(mask=fix_mask))

    fixed_z = sorted({round(z_coords[i], 2) for i in np.where(fix_mask)[0]})
    print(f"Slab: {len(slab)} atoms | "
          f"N fixed = {int(fix_mask.sum())} of {len(slab)} | "
          f"fixed z values: {fixed_z}")
    return slab


# ----------------------------------------------------------------------
# High-symmetry sites from surface geometry
# ----------------------------------------------------------------------
def _cross2d(u, v):
    """Scalar 2D cross product: u_x * v_y - u_y * v_x."""
    return u[0] * v[1] - u[1] * v[0]


def get_high_symmetry_sites(slab: Atoms):
    """Return Cartesian (x, y) positions of ontop, bridge, fcc, hcp sites."""
    positions = slab.get_positions()
    z = positions[:, 2]

    top_mask = z > (z.max() - 0.5)
    top_xy = positions[top_mask][:, :2]

    cell_xy = slab.cell[:2, :2]
    center = cell_xy.sum(axis=0) / 2.0
    dists = np.linalg.norm(top_xy - center, axis=1)
    ref = top_xy[np.argmin(dists)]

    vecs = top_xy - ref
    lengths = np.linalg.norm(vecs, axis=1)
    keep = lengths > 0.1
    vecs = vecs[keep]
    lengths = lengths[keep]
    order = np.argsort(lengths)
    vecs = vecs[order]

    a1 = vecs[0]
    a2 = None
    for v in vecs[1:]:
        if abs(_cross2d(a1, v)) > 0.1:
            a2 = v
            break
    if a2 is None:
        raise RuntimeError("Could not find a second non-collinear neighbour.")

    sites = {
        "ontop":  ref + np.array([0.0, 0.0]),
        "bridge": ref + 0.5 * a1,
        "fcc":    ref + (a1 + a2) / 3.0,
        "hcp":    ref + (2.0 * a1 + a2) / 3.0,
    }
    return {k: tuple(float(x) for x in v) for k, v in sites.items()}


# ----------------------------------------------------------------------
# Adsorption energy
# ----------------------------------------------------------------------
def adsorption_energy(slab: Atoms,
                      site: tuple,
                      site_name: str = "site",
                      height: float = 2.5,
                      calc=None,
                      prefix: str = "",
                      save: bool = True):
    """Compute E_ads = E(slab+Hg) - E(slab) - E(Hg) at a given (x, y) site.

    If save=True, writes:
        <OUTDIR>/<prefix>_<site_name>.traj   (relaxation trajectory)
        <OUTDIR>/<prefix>_<site_name>.vasp   (final relaxed structure)
    """
    stem = safe(f"{prefix}_{site_name}" if prefix else site_name)
    traj_path = os.path.join(OUTDIR, f"{stem}.traj")
    vasp_path = os.path.join(OUTDIR, f"{stem}.vasp")

    # 1. Clean slab reference
    clean = slab.copy()
    clean.calc = calc
    e_clean = clean.get_potential_energy()

    # 2. Isolated Hg reference (periodic box, large vacuum)
    hg_atom = Atoms('Hg', positions=[(0.0, 0.0, 0.0)],
                    cell=(10.0, 10.0, 10.0), pbc=True)
    hg_atom.calc = calc
    e_hg = hg_atom.get_potential_energy()

    # 3. Slab + adsorbate, relax (constraints inherited from slab.copy())
    ads = slab.copy()
    add_adsorbate(ads, 'Hg', height=height, position=site)
    ads.calc = calc

    traj = Trajectory(traj_path, 'w', ads) if save else None
    opt = BFGS(ads, logfile=None, trajectory=traj)
    try:
        opt.run(fmax=0.05, steps=200)
    except Exception as exc:
        print(f"  Optimization warning for {stem}: {exc}")
    finally:
        if traj is not None:
            traj.close()

    e_total = ads.get_potential_energy()
    e_ads = e_total - (e_clean + e_hg)

    if save:
        write(vasp_path, ads, format='vasp', direct=True, sort=True)
        print(f"  Saved: {traj_path}")
        print(f"  Saved: {vasp_path}")

    return e_ads, ads


# ----------------------------------------------------------------------
# Reporting helpers
# ----------------------------------------------------------------------
def write_comparison_tables(all_results: dict, all_geoms: dict):
    """Write summary and comparison tables to OUTDIR."""
    methods = list(all_results.keys())
    sites = list(next(iter(all_results.values()))["sites"].keys())

    # --- Per-method summary ---
    summary_path = os.path.join(OUTDIR, "summary.txt")
    with open(summary_path, "w") as f:
        f.write("=" * 60 + "\n")
        f.write("PER-METHOD SUMMARY\n")
        f.write("=" * 60 + "\n")
        for method, data in all_results.items():
            f.write(f"\n--- {method} ---\n")
            f.write(f"  E_slab = {data['e_slab']:12.6f} eV\n")
            f.write(f"  E_Hg   = {data['e_atom']:12.6f} eV\n")
            for site in sites:
                f.write(f"  E_ads[{site:7s}] = "
                        f"{data['sites'][site]:+10.4f} eV\n")
            best = min(data["sites"], key=data["sites"].get)
            f.write(f"  Most stable: {best} "
                    f"({data['sites'][best]:+.4f} eV)\n")

        # --- Side-by-side comparison ---
        f.write("\n" + "=" * 60 + "\n")
        f.write("SIDE-BY-SIDE: E_ads (eV)\n")
        f.write("=" * 60 + "\n")
        header = f"{'site':8s}" + "".join(f"{m:>16s}" for m in methods)
        header += f"{'Δ(D4−FF)':>14s}"
        f.write(header + "\n")
        f.write("-" * len(header) + "\n")
        for site in sites:
            row = f"{site:8s}"
            for m in methods:
                row += f"{all_results[m]['sites'][site]:>16.4f}"
            delta = (all_results["ALIGNN-FF+D4"]["sites"][site]
                     - all_results["ALIGNN-FF"]["sites"][site])
            row += f"{delta:>+14.4f}"
            f.write(row + "\n")

        # --- Final Hg geometry comparison ---
        f.write("\n" + "=" * 60 + "\n")
        f.write("FINAL Hg POSITION (x, y, z) IN Å\n")
        f.write("=" * 60 + "\n")
        header = f"{'site':8s}" + "".join(f"{m:>22s}" for m in methods)
        f.write(header + "\n")
        f.write("-" * len(header) + "\n")
        for site in sites:
            row = f"{site:8s}"
            for m in methods:
                hg = all_geoms[m][site].positions[-1]
                row += f"  ({hg[0]:5.2f},{hg[1]:5.2f},{hg[2]:5.2f})"
            f.write(row + "\n")

    print(f"\nComparison tables written to: {summary_path}")


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    DEVICE = "cpu"   # switch to "cuda" if a GPU is available

    slab = build_au111_slab()  # 4x4x4, bottom layer frozen

    # Both calculators: plain ALIGNN-FF and ALIGNN-FF + D4
    CALCS = {
        "ALIGNN-FF":    get_alignn_calculator(device=DEVICE),
        "ALIGNN-FF+D4": get_alignn_d4_calculator(device=DEVICE),
    }

    site_positions = get_high_symmetry_sites(slab)
    print("High-symmetry sites (Cartesian x, y in A):")
    for name, xy in site_positions.items():
        print(f"  {name:6s}: ({xy[0]:7.3f}, {xy[1]:7.3f})")

    all_results = {}   # method -> {e_slab, e_atom, sites: {site: E_ads}}
    all_geoms = {}     # method -> {site: final Atoms}

    for method, calc in CALCS.items():
        print("\n" + "#" * 60)
        print(f"# Method: {method}")
        print("#" * 60)

        # References
        clean = slab.copy()
        clean.calc = calc
        e_slab = clean.get_potential_energy()

        hg_atom = Atoms('Hg', positions=[(0.0, 0.0, 0.0)],
                        cell=(10.0, 10.0, 10.0), pbc=True)
        hg_atom.calc = calc
        e_atom = hg_atom.get_potential_energy()

        print(f"  E_slab = {e_slab:.6f} eV | E_Hg = {e_atom:.6f} eV")

        # Adsorption at each site
        results = {}
        geoms = {}
        for name, xy in site_positions.items():
            e_ads, ads_final = adsorption_energy(
                slab, site=xy, site_name=name, height=2.5,
                calc=calc, prefix=safe(method), save=True
            )
            results[name] = e_ads
            geoms[name] = ads_final

            hg_xy = ads_final.positions[-1][:2]
            hg_z = ads_final.positions[-1][2]
            print(f"  Site {name:6s}: E_ads = {e_ads:+.3f} eV | "
                  f"Hg final (x, y, z) = "
                  f"({hg_xy[0]:6.2f}, {hg_xy[1]:6.2f}, {hg_z:6.2f})")

        all_results[method] = {
            "e_slab": e_slab,
            "e_atom": e_atom,
            "sites":  results,
        }
        all_geoms[method] = geoms

        best = min(results, key=results.get)
        print(f"  Most stable: {best} ({results[best]:+.4f} eV)")

    # --- Final comparison tables ---
    write_comparison_tables(all_results, all_geoms)

    # --- Console comparison ---
    print("\n" + "=" * 60)
    print("SIDE-BY-SIDE: E_ads (eV)")
    print("=" * 60)
    header = f"{'site':8s}" + "".join(f"{m:>16s}" for m in CALCS)
    header += f"{'Δ(D4−FF)':>14s}"
    print(header)
    print("-" * len(header))
    for site in site_positions:
        row = f"{site:8s}"
        for m in CALCS:
            row += f"{all_results[m]['sites'][site]:>16.4f}"
        delta = (all_results["ALIGNN-FF+D4"]["sites"][site]
                 - all_results["ALIGNN-FF"]["sites"][site])
        row += f"{delta:>+14.4f}"
        print(row)

    print("=" * 60)
    print(f"\nAll outputs written to: {os.path.abspath(OUTDIR)}/")
