#!/usr/bin/env python
"""
Hg adsorption on Au(111) using MACE + ASE.

MACE (Machine Learning Interatomic Potential) replaces the EMT
calculator. This provides a much more accurate description of
the Hg/Au system.

NOTE: MACE is computationally expensive compared to EMT. 
Expect minutes to hours per relaxation, not seconds.
"""

import os
import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.io import write

# MACE imports
from mace.calculators import mace_mp


# ============================================================
# Configuration
# ============================================================
SLAB_SIZE   = (4, 4, 4)      # 4x4x4 Au(111) slab  -> 64 Au atoms
VACUUM      = 10.0           # Angstrom
ADSORBATE   = 'Hg'           # Changed from 'Pd' to 'Hg'
HEIGHT      = 2.0            # initial adsorbate height (Angstrom)
FMAX        = 0.05           # relaxed convergence for MACE (more realistic)
SITES       = ['fcc', 'hcp', 'bridge', 'ontop']

# MACE model configuration
MACE_MODEL  = "small"        # Options: "small", "medium", "large"
MACE_DEVICE = "cuda"         # Use "cuda" for GPU, "cpu" otherwise
MACE_DTYPE  = "float32"      # float32 for speed, float64 for precision

OUT_STRUCT  = 'structures'
OUT_LOGS    = 'logs'
OUT_TRAJ    = 'trajectories'


# ============================================================
# Helpers
# ============================================================
def ensure_dirs():
    for d in (OUT_STRUCT, OUT_LOGS, OUT_TRAJ):
        os.makedirs(d, exist_ok=True)


def max_force(atoms):
    """Return the maximum per-atom force magnitude (eV/Angstrom)."""
    return np.sqrt((atoms.get_forces() ** 2).sum(axis=1)).max()


def get_mace_calculator():
    """Initialize and return the MACE calculator."""
    print(f"    Initializing MACE (model={MACE_MODEL}, device={MACE_DEVICE})...")
    calc = mace_mp(
        model=MACE_MODEL,
        dispersion=False,        # MACE-MP doesn't include dispersion by default
        default_dtype=MACE_DTYPE,
        device=MACE_DEVICE
    )
    print("    MACE calculator ready.")
    return calc


# ============================================================
# Reference calculations
# ============================================================
def compute_E_slab(calc):
    """Relaxed energy of the clean Au(111) slab."""
    slab = fcc111('Au', size=SLAB_SIZE, vacuum=VACUUM)
    slab.calc = calc
    opt = BFGS(slab,
               trajectory=os.path.join(OUT_TRAJ, 'slab_relax.traj'),
               logfile=os.path.join(OUT_LOGS, 'slab_relax.log'))
    opt.run(fmax=FMAX)
    return slab.get_potential_energy(), opt.nsteps, max_force(slab)


def compute_E_atom(calc):
    """Energy of an isolated Hg atom in a large box."""
    atom = Atoms(ADSORBATE,
                 positions=[[0, 0, 0]],
                 cell=[10, 10, 10],
                 pbc=False)
    atom.calc = calc
    return atom.get_potential_energy()


# ============================================================
# Site calculation
# ============================================================
def run_site(site, calc, E_slab, E_atom):
    """Relax Hg/Au(111) at a given site; return a result dict."""
    slab = fcc111('Au', size=SLAB_SIZE, vacuum=VACUUM)
    add_adsorbate(slab, ADSORBATE, height=HEIGHT, position=site)
    slab.calc = calc

    opt = BFGS(slab,
               trajectory=os.path.join(OUT_TRAJ, f'relax_{site}.traj'),
               logfile=os.path.join(OUT_LOGS,  f'relax_{site}.log'))
    opt.run(fmax=FMAX)

    E_total = slab.get_potential_energy()
    fmax    = max_force(slab)
    E_ads   = E_total - E_slab - E_atom

    # Save relaxed geometry
    write(os.path.join(OUT_STRUCT, f'relaxed_{site}.vasp'),
          slab, format='vasp')

    return {
        'site':      site,
        'E_total':   E_total,
        'E_ads':     E_ads,
        'fmax':      fmax,
        'nsteps':    opt.nsteps,
        'converged': fmax < FMAX,
    }


# ============================================================
# Main
# ============================================================
def main():
    ensure_dirs()

    print("=" * 68)
    print("Hg adsorption on Au(111)  --  MACE (Machine Learning Potential)")
    print("=" * 68)
    print(f"Slab:      Au(111) {SLAB_SIZE[0]}x{SLAB_SIZE[1]}x{SLAB_SIZE[2]}"
          f"  ({SLAB_SIZE[0]*SLAB_SIZE[1]*SLAB_SIZE[2]} Au atoms)")
    print(f"Adsorbate: 1 {ADSORBATE} atom, initial height {HEIGHT} A")
    print(f"Vacuum:    {VACUUM} A")
    print(f"Optimizer: BFGS, fmax < {FMAX} eV/A")
    print(f"Calculator: MACE ({MACE_MODEL} model, device={MACE_DEVICE})")
    print("-" * 68)

    # --- Initialize calculator (shared across all calculations) ---
    calc = get_mace_calculator()

    # --- Reference energies ---------------------------------
    print("\n[1/2] Reference energies")
    E_slab, nsteps_slab, fmax_slab = compute_E_slab(calc)
    E_atom = compute_E_atom(calc)
    print(f"    E_slab        = {E_slab:.6f} eV"
          f"   (steps={nsteps_slab}, fmax={fmax_slab:.4f})")
    print(f"    E_atom({ADSORBATE}) = {E_atom:.6f} eV")

    # --- Site sweep -----------------------------------------
    print("\n[2/2] Adsorption sites")
    results = []
    for site in SITES:
        print(f"\n  -> {site}")
        r = run_site(site, calc, E_slab, E_atom)
        results.append(r)
        status = "OK" if r['converged'] else "NOT CONVERGED"
        print(f"     E_total = {r['E_total']:.6f} eV")
        print(f"     E_ads   = {r['E_ads']:.6f} eV")
        print(f"     fmax    = {r['fmax']:.6f} eV/A   [{status},"
              f" {r['nsteps']} steps]")

    # --- Summary table --------------------------------------
    print("\n" + "=" * 68)
    print("Summary")
    print("=" * 68)
    header = (f"{'Site':<8s}{'E_total (eV)':>16s}"
              f"{'E_ads (eV)':>16s}{'fmax (eV/A)':>16s}{'Steps':>8s}")
    print(header)
    print("-" * len(header))
    for r in results:
        print(f"{r['site']:<8s}"
              f"{r['E_total']:>16.6f}"
              f"{r['E_ads']:>16.6f}"
              f"{r['fmax']:>16.6f}"
              f"{r['nsteps']:>8d}")

    # --- Ranking --------------------------------------------
    ranked = sorted(results, key=lambda r: r['E_ads'])
    print("\nSite preference (most stable first):")
    for i, r in enumerate(ranked, 1):
        marker = "  <-- most stable" if i == 1 else ""
        print(f"  {i}. {r['site']:<8s}  E_ads = {r['E_ads']:.6f} eV{marker}")

    if all(r['converged'] for r in results):
        print("\nAll calculations converged.\n")
    else:
        print("\nWARNING: not all calculations converged!\n")


if __name__ == "__main__":
    main()
