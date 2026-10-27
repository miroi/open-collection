from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import write
from ase.io.trajectory import Trajectory
from mace.calculators import mace_mp
import numpy as np
import re
import os

calc = mace_mp(model="medium", device='cpu', default_dtype="float64")

OUTDIR = "results"
os.makedirs(OUTDIR, exist_ok=True)

def safe(name):
    """Turn an arbitrary label into a filesystem-safe stem."""
    name = re.sub(r'[^A-Za-z0-9_\-]+', '_', name).strip('_')
    return name or "struct"

def get_optimized_energy(atoms, label="", save=True):
    """
    Relax `atoms` with BFGS.
    - If save=True, writes:
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
slab = fcc111('Au', size=(4,4,4), vacuum=12.0)

# Freeze bottom layer by z-coordinate (robust to tag convention)
zmin = min(a.position[2] for a in slab)
slab.set_constraint(FixAtoms(mask=[a.position[2] < zmin + 0.1 for a in slab]))

fa = slab.constraints[0]
fixed_z = sorted({round(slab[i].position[2], 2) for i in fa.get_indices()})
print("fixed z values:", fixed_z, "| N fixed =", len(fa.get_indices()),
      "of", len(slab))

# --- References ---
e_slab = get_optimized_energy(slab, "clean_slab")

from ase import Atoms
hg = Atoms('Hg', pbc=True); hg.set_cell([15,15,15]); hg.center()
e_atom = get_optimized_energy(hg, "Hg_atom")

# --- Adsorption, all sites, on a fresh copy each time ---
results = {}
#for site in ('ontop', 'bridge', 'fcc', 'hcp'):
for site in ('hcp'):
    s = slab.copy()
    add_adsorbate(s, 'Hg', height=2.5, position=site)
    e_tot = get_optimized_energy(s, f"HgAu_{site}")
    results[site] = e_tot - e_slab - e_atom

print("\n" + "="*40)
print(f"Slab Energy:  {e_slab:10.4f} eV")
print(f"Hg Atom:      {e_atom:10.4f} eV")
for site, e in results.items():
    print(f"E_ads[{site:7s}] = {e:+.4f} eV")
best = min(results, key=results.get)
print(f"Most stable: {best}  ({results[best]:+.4f} eV)")
print("="*40)
print(f"\nAll outputs written to: {os.path.abspath(OUTDIR)}/")
