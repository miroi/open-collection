"""
ASE + ALIGNN-FF: Adsorption of Hg atom on Au(111) slab.

Requires: ase, alignn, torch
"""
import warnings
import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms

from alignn.ff.ff import AlignnAtomwiseCalculator, default_path

warnings.filterwarnings("ignore")


# ----------------------------------------------------------------------
# Calculator
# ----------------------------------------------------------------------
def get_alignn_calculator(device: str = "cpu") -> AlignnAtomwiseCalculator:
    """Initialize the pre-trained ALIGNN-FF calculator."""
    model_path = default_path()
    calc = AlignnAtomwiseCalculator(path=model_path, device=device)
    return calc


# ----------------------------------------------------------------------
# Slab construction
# ----------------------------------------------------------------------
def build_au111_slab(a: float = 4.08,
                     size=(3, 3, 3),
                     vacuum: float = 10.0) -> Atoms:
    """Construct an Au(111) slab and fix the bottom two layers."""
    slab = fcc111('Au', size=size, a=a, vacuum=vacuum)

    z_coords = slab.get_positions()[:, 2]
    z_sorted = np.sort(z_coords)
    layer_thickness = (z_sorted[-1] - z_sorted[0]) / 3.0
    fix_mask = z_coords < (z_sorted[0] + 2 * layer_thickness + 0.1)
    slab.set_constraint(FixAtoms(mask=fix_mask))
    return slab


# ----------------------------------------------------------------------
# High-symmetry sites from surface geometry
# ----------------------------------------------------------------------
def _cross2d(u, v):
    """Scalar 2D cross product: u_x * v_y - u_y * v_x."""
    return u[0] * v[1] - u[1] * v[0]


def get_high_symmetry_sites(slab: Atoms):
    """Return Cartesian (x, y) positions of ontop, bridge, fcc, hcp sites.

    Sites are built from the actual top-layer atom positions so that
    they are geometrically distinct in the ASE fcc111 convention.
    """
    positions = slab.get_positions()
    z = positions[:, 2]

    # Top layer atoms (within 0.5 A of the maximum z)
    top_mask = z > (z.max() - 0.5)
    top_xy = positions[top_mask][:, :2]

    # Reference atom: top-layer atom closest to the in-plane cell center
    cell_xy = slab.cell[:2, :2]
    center = cell_xy.sum(axis=0) / 2.0
    dists = np.linalg.norm(top_xy - center, axis=1)
    ref = top_xy[np.argmin(dists)]

    # In-plane neighbour vectors from the reference atom
    vecs = top_xy - ref
    lengths = np.linalg.norm(vecs, axis=1)
    keep = lengths > 0.1
    vecs = vecs[keep]
    lengths = lengths[keep]
    order = np.argsort(lengths)
    vecs = vecs[order]

    # Nearest neighbour (a1) and a second, non-collinear neighbour (a2)
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
                      height: float = 2.5,
                      calc=None):
    """Compute E_ads = E(slab+Hg) - E(slab) - E(Hg) at a given (x, y) site."""
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

    opt = BFGS(ads, logfile=None)
    try:
        opt.run(fmax=0.05, steps=200)
    except Exception as exc:
        print(f"  Optimization warning for site {site}: {exc}")

    e_total = ads.get_potential_energy()
    e_ads = e_total - (e_clean + e_hg)
    return e_ads, ads


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    DEVICE = "cpu"   # switch to "cuda" if a GPU is available in WSL2

    slab = build_au111_slab()
    print(f"Slab: {len(slab)} atoms, constraints: {len(slab.constraints)}")

    calc = get_alignn_calculator(device=DEVICE)

    site_positions = get_high_symmetry_sites(slab)
    print("High-symmetry sites (Cartesian x, y in A):")
    for name, xy in site_positions.items():
        print(f"  {name:6s}: ({xy[0]:7.3f}, {xy[1]:7.3f})")

    results = {}
    final_geometries = {}
    for name, xy in site_positions.items():
        e_ads, ads_final = adsorption_energy(slab, site=xy, height=2.5, calc=calc)
        results[name] = e_ads
        final_geometries[name] = ads_final

        hg_xy = ads_final.positions[-1][:2]
        hg_z = ads_final.positions[-1][2]
        print(f"Site {name:6s}: E_ads = {e_ads:+.3f} eV | "
              f"Hg final (x, y, z) = ({hg_xy[0]:6.2f}, {hg_xy[1]:6.2f}, {hg_z:6.2f})")

    best = min(results, key=results.get)
    print(f"\nMost stable site: {best} ({results[best]:+.3f} eV)")
