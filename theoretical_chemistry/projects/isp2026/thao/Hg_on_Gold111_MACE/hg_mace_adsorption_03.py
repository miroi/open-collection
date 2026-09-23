#!/usr/bin/env python
"""
Hg adsorption on Au(111) using MACE + ASE (float64, tight convergence).

MACE-MP-0 is used in float64 to make geometry optimization reliable.
float32 introduces ~1 meV numerical noise in the energy, which is
comparable to the fcc/hcp energy difference and would make the site
ranking unreliable.

Reference energies are recomputed at runtime so the script is fully
self-contained and reproducible.
"""

import os
import warnings
import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.io import write

# Silence the harmless torch.load(weights_only=False) FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning,
                        message=".*weights_only.*")

from mace.calculators import mace_mp


# ============================================================
# Configuration
# ============================================================
SLAB_SIZE   = (4, 4, 4)      # 4x4x4 Au(111) slab  -> 64 Au atoms
VACUUM      = 10.0           # Angstrom
ADSORBATE   = 'Hg'           # adsorbate element
HEIGHT      = 2.0            # initial adsorbate height (Angstrom)

# Convergence: 0.01 eV/A is the standard "tight" target. In float64
# MACE forces are accurate enough to actually reach this.
FMAX        = 0.01           # force convergence (eV/Angstrom)
MAXSTEPS    = 500            # BFGS safety limit

SITES       = ['fcc', 'hcp', 'bridge', 'ontop']

# MACE model configuration
#MACE_MODEL  = "small"        # "small" | "medium" | "large"
MACE_MODEL  = "medium"        # "small" | "medium" | "large"
MACE_DEVICE = "cuda"         # "cuda" | "cpu"
MACE_DTYPE  = "float64"      # REQUIRED for geometry optimization

OUT_STRUCT  = 'structures'
OUT_LOGS    = 'logs'
OUT_TRAJ    = 'trajectories'

# Threshold below which two adsorption energies are considered
# numerically indistinguishable (in eV). With float64 + fmax=0.01,
# differences below ~1 meV should not be interpreted as physical.
DEGENERACY_THRESHOLD = 1e-3   # 1 meV


# ============================================================
# Helpers
# ============================================================
def ensure_dirs():
    for d in (OUT_STRUCT, OUT_LOGS, OUT_TRAJ):
        os.makedirs(d, exist_ok=True)


def max_force(atoms):
    """Return the maximum per-atom force magnitude (eV/Angstrom)."""
    return float(np.sqrt((atoms.get_forces() ** 2).sum(axis=1)).max())


def get_mace_calculator():
    """Initialize and return the MACE calculator (float64)."""
    print(f"    Initializing MACE "
          f"(model={MACE_MODEL}, device={MACE_DEVICE}, "
          f"dtype={MACE_DTYPE})...")
    calc = mace_mp(
        model=MACE_MODEL,
        dispersion=True,
        default_dtype=MACE_DTYPE,
        device=MACE_DEVICE,
    )
    print("    MACE calculator ready.")
    return calc


def relax(atoms, calc, traj_path, log_path, label=""):
    """Attach calculator, run BFGS to FMAX, return (energy, fmax, nsteps)."""
    atoms.calc = calc
    opt = BFGS(atoms,
               trajectory=traj_path,
               logfile=log_path,
               maxstep=0.2)          # smaller max step -> stable near minimum
    opt.run(fmax=FMAX, steps=MAXSTEPS)

    E    = atoms.get_potential_energy()
    fmax = max_force(atoms)
    return E, fmax, opt.nsteps


# ============================================================
# Reference calculations
# ============================================================
def compute_E_slab(calc):
    """Relaxed energy of the clean Au(111) slab."""
    slab = fcc111('Au', size=SLAB_SIZE, vacuum=VACUUM)
    E, fmax, nsteps = relax(
        slab, calc,
        traj_path=os.path.join(OUT_TRAJ, 'slab_relax.traj'),
        log_path=os.path.join(OUT_LOGS, 'slab_relax.log'),
        label='slab',
    )
    return E, fmax, nsteps


def compute_E_atom(calc):
    """Energy of an isolated Hg atom in a large box (no relaxation)."""
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

    E_total, fmax, nsteps = relax(
        slab, calc,
        traj_path=os.path.join(OUT_TRAJ, f'relax_{site}.traj'),
        log_path=os.path.join(OUT_LOGS,  f'relax_{site}.log'),
        label=site,
    )

    E_ads = E_total - E_slab - E_atom

    # Save relaxed geometry
    write(os.path.join(OUT_STRUCT, f'relaxed_{site}.vasp'),
          slab, format='vasp')

    return {
        'site':      site,
        'E_total':   E_total,
        'E_ads':     E_ads,
        'fmax':      fmax,
        'nsteps':    nsteps,
        'converged': fmax < FMAX,
    }


# ============================================================
# Main
# ============================================================
def main():
    ensure_dirs()

    print("=" * 72)
    print("Hg adsorption on Au(111)  --  MACE (float64, tight convergence)")
    print("=" * 72)
    print(f"Slab:       Au(111) {SLAB_SIZE[0]}x{SLAB_SIZE[1]}x{SLAB_SIZE[2]}"
          f"  ({SLAB_SIZE[0]*SLAB_SIZE[1]*SLAB_SIZE[2]} Au atoms)")
    print(f"Adsorbate:  1 {ADSORBATE} atom, initial height {HEIGHT} A")
    print(f"Vacuum:     {VACUUM} A")
    print(f"Optimizer:  BFGS, fmax < {FMAX} eV/A (maxsteps={MAXSTEPS})")
    print(f"Calculator: MACE ({MACE_MODEL}, {MACE_DTYPE}, {MACE_DEVICE})")
    print(f"Degeneracy threshold: {DEGENERACY_THRESHOLD*1000:.2f} meV")
    print("-" * 72)

    # --- Initialize calculator once, share across all calculations ---
    calc = get_mace_calculator()

    # --- Reference energies ---------------------------------
    print("\n[1/2] Reference energies")
    E_slab, fmax_slab, nsteps_slab = compute_E_slab(calc)
    E_atom = compute_E_atom(calc)
    slab_ok = fmax_slab < FMAX
    print(f"    E_slab           = {E_slab:.6f} eV"
          f"   (steps={nsteps_slab}, fmax={fmax_slab:.6f}"
          f"  [{'OK' if slab_ok else 'NOT CONVERGED'}])")
    print(f"    E_atom({ADSORBATE:<2s})     = {E_atom:.6f} eV")

    if not slab_ok:
        print("\n    WARNING: slab did not reach FMAX. "
              "E_slab (and thus every E_ads) is unreliable.")

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
        print(f"     fmax    = {r['fmax']:.6f} eV/A   "
              f"[{status}, {r['nsteps']} steps]")

    # --- Summary table --------------------------------------
    print("\n" + "=" * 72)
    print("Summary")
    print("=" * 72)
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

    # --- Numerical-resolution diagnostic --------------------
    print("\nNumerical resolution check "
          f"(threshold = {DEGENERACY_THRESHOLD*1000:.2f} meV):")
    if len(ranked) >= 2:
        gap = ranked[1]['E_ads'] - ranked[0]['E_ads']
        if gap < DEGENERACY_THRESHOLD:
            print(f"  {ranked[0]['site']} vs {ranked[1]['site']}: "
                  f"gap = {gap*1000:.2f} meV  "
                  f"-> NOT RESOLVABLE, treat as degenerate")
        else:
            print(f"  {ranked[0]['site']} vs {ranked[1]['site']}: "
                  f"gap = {gap*1000:.2f} meV  -> resolved")
    for i in range(1, len(ranked) - 1):
        gap = ranked[i+1]['E_ads'] - ranked[i]['E_ads']
        tag = "resolved" if gap >= DEGENERACY_THRESHOLD else "NOT RESOLVABLE"
        print(f"  {ranked[i]['site']} vs {ranked[i+1]['site']}: "
              f"gap = {gap*1000:.2f} meV  -> {tag}")

    # --- Convergence summary --------------------------------
    if all(r['converged'] for r in results) and slab_ok:
        print("\nAll calculations converged.\n")
    else:
        print("\nWARNING: not all calculations converged!\n")


if __name__ == "__main__":
    main()
