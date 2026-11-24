from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import write
from ase.io.trajectory import Trajectory
from ase.calculators.mixing import SumCalculator
from mace.calculators import mace_mp
from dftd4.ase import DFTD4
import numpy as np
import re
import os

# --- Two calculators: plain MACE and MACE + D4 (via ASE SumCalculator) ---
mace_calc = mace_mp(model="medium", device='cpu', default_dtype="float64")

mace_d4_calc = SumCalculator([
    mace_mp(model="medium", device='cpu', default_dtype="float64"),
    DFTD4(method="PBE"),
])

CALCS = {
    "MACE":    mace_calc,
    "MACE-D4": mace_d4_calc,
}

OUTDIR = "results"
os.makedirs(OUTDIR, exist_ok=True)


def safe(name):
    """Turn an arbitrary label into a filesystem-safe stem."""
    name = re.sub(r'[^A-Za-z0-9_\-]+', '_', name).strip('_')
    return name or "struct"


def get_optimized_energy(atoms, calc, label="", save=True):
    """
    Relax `atoms` with BFGS using the supplied calculator.

    If save=True, writes:
        <OUTDIR>/<safe(label)>.traj   (full trajectory)
        <OUTDIR>/<safe(label)>.vasp   (final relaxed structure, POSCAR format)

    Returns the final potential energy (eV).
    """
    stem = safe(label)
    traj_path = os.path.join(OUTDIR, f"{stem}.traj")
    vasp_path = os.path.join(OUTDIR, f"{stem}.vasp")

    atoms.calc = calc
    r0 = atoms.get_positions().copy()

    traj = Trajectory(traj_path, 'w', atoms) if save else None
    dyn = BFGS(atoms, logfile=None, trajectory=traj)
    dyn.run(fmax=0.005)
    if traj is not None:
        traj.close()

    dr = np.linalg.norm(atoms.get_positions() - r0, axis=1).max()
    e = atoms.get_potential_energy()
    print(f"[{label}] steps={dyn.nsteps:3d}  max|Δr|={dr:.4f} Å  "
          f"E={e:.6f} eV  -> {traj_path if save else '(not saved)'}")

    if save:
        write(vasp_path, atoms, format='vasp', direct=True, sort=True)
        print(f"    final structure -> {vasp_path}")

    return e


# --- Slab ---
slab = fcc111('Au', size=(4, 4, 4), vacuum=12.0)

# Freeze the bottom layer by z-coordinate (robust to tag convention)
zmin = min(a.position[2] for a in slab)
slab.set_constraint(FixAtoms(mask=[a.position[2] < zmin + 0.1 for a in slab]))

fa = slab.constraints[0]
fixed_z = sorted({round(slab[i].position[2], 2) for i in fa.get_indices()})
print("fixed z values:", fixed_z,
      "| N fixed =", len(fa.get_indices()), "of", len(slab))

# --- Run both methods ---
from ase import Atoms

all_results = {}  # method -> {site: E_ads}

for method, calc in CALCS.items():
    print("\n" + "#" * 60)
    print(f"# Method: {method}")
    print("#" * 60)

    # References (fresh copy for each method)
    e_slab = get_optimized_energy(slab.copy(), calc, f"{method}_clean_slab")

    pd = Atoms('Pd', pbc=True)
    pd.set_cell([15, 15, 15])
    pd.center()
    e_atom = get_optimized_energy(pd, calc, f"{method}_Pd_atom")

    # Adsorption: all sites, on a fresh copy each time
    results = {}
    for site in ('ontop', 'bridge', 'fcc', 'hcp'):
        s = slab.copy()
        add_adsorbate(s, 'Pd', height=2.5, position=site)
        e_tot = get_optimized_energy(s, calc, f"{method}_PdAu_{site}")
        results[site] = e_tot - e_slab - e_atom

    all_results[method] = {
        "e_slab": e_slab,
        "e_atom": e_atom,
        "sites":  results,
    }

# --- Comparison summary ---
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

for method, data in all_results.items():
    print(f"\n--- {method} ---")
    print(f"  Slab Energy: {data['e_slab']:10.4f} eV")
    print(f"  Pd Atom:     {data['e_atom']:10.4f} eV")
    for site, e in data["sites"].items():
        print(f"  E_ads[{site:7s}] = {e:+.4f} eV")
    best = min(data["sites"], key=data["sites"].get)
    print(f"  Most stable: {best}  ({data['sites'][best]:+.4f} eV)")

# Side-by-side comparison
print("\n" + "=" * 60)
print("SIDE-BY-SIDE: E_ads (eV)")
print("=" * 60)
header = f"{'site':8s}" + "".join(f"{m:>14s}" for m in CALCS) + f"{'Δ(D4−MACE)':>16s}"
print(header)
print("-" * len(header))
for site in ('ontop', 'bridge', 'fcc', 'hcp'):
    row = f"{site:8s}"
    e_mace = all_results["MACE"]["sites"][site]
    for m in CALCS:
        row += f"{all_results[m]['sites'][site]:>14.4f}"
    delta = all_results["MACE-D4"]["sites"][site] - e_mace
    row += f"{delta:>+16.4f}"
    print(row)

print("=" * 60)
print(f"\nAll outputs written to: {os.path.abspath(OUTDIR)}/")
