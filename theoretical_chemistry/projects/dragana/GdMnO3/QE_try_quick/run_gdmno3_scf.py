#!/usr/bin/env python3
"""
Direct interactive Quantum ESPRESSO SCF for GdMnO3
- Geometry from GdMnO3.cif
- DFT+U (Hubbard) for Mn 3d and Gd 4f
- High-spin configuration enforced via tot_magnetization
    Mn3+ (3d4, S=2) ~ 4 muB
    Gd3+ (4f7, S=7/2) ~ 7 muB
    -> 11 muB / f.u.  x  Z=4  =>  tot_magnetization = 44 muB
- Launches pw.x directly from Python (interactive run)
"""

import os
import sys
import numpy as np
from ase.io import read, write
from ase.calculators.espresso import Espresso, EspressoProfile

# ======================================================================
# 0. User-configurable paths
# ======================================================================
CIF_FILE   = "GdMnO3.cif"          # geometry file
PSEUDO_DIR = "./"                  # pseudopotentials in the current dir
OUTDIR     = "./tmp"               # scratch directory
PREFIX     = "GdMnO3"

PW_COMMAND = "mpirun -np 4 pw.x"   # adjust to your machine

os.makedirs(OUTDIR, exist_ok=True)

# ======================================================================
# 1. Read the CIF
# ======================================================================
if not os.path.isfile(CIF_FILE):
    sys.exit(f"ERROR: CIF file '{CIF_FILE}' not found.")

atoms = read(CIF_FILE, format="cif")

print("=" * 72)
print("GdMnO3 structure read from CIF")
print("=" * 72)
print(f"Formula         : {atoms.get_chemical_formula()}")
print(f"Number of atoms : {len(atoms)}")
print(f"Cell (a,b,c)    : {atoms.cell.cellpar()[:3]}  Å")
print(f"Cell angles     : {atoms.cell.cellpar()[3:]}  deg")
print("=" * 72)

# ======================================================================
# 2. High-spin total magnetization
# ----------------------------------------------------------------------
# Per formula unit GdMnO3:
#   Gd3+ : 4f7  -> S = 7/2  -> 7 muB
#   Mn3+ : 3d4  -> S = 2    -> 4 muB   (high spin, t2g^3 eg^1)
#   O2-  : closed shell    -> 0
#   ----------------------------------------
#   Total per f.u.         -> 11 muB
#
# The CIF cell has Z = 4 formula units:
#   tot_magnetization (per cell) = 11 * 4 = 44 muB
# ======================================================================
Z_FORMULA_UNITS = 4
MU_GD_HIGHSPIN  = 7.0
MU_MN_HIGHSPIN  = 4.0
TOT_MAG = (MU_GD_HIGHSPIN + MU_MN_HIGHSPIN) * Z_FORMULA_UNITS   # = 44

print(f"[i] Target tot_magnetization = {TOT_MAG:.1f} muB  "
      f"(Gd {MU_GD_HIGHSPIN} + Mn {MU_MN_HIGHSPIN}) x Z={Z_FORMULA_UNITS}")

# ======================================================================
# 3. Pseudopotentials (filenames must match files in PSEUDO_DIR)
# ======================================================================
pseudopotentials = {
    "Gd": "Gd.pbe-spdn-kjpaw_psl.1.0.0.UPF",
    "Mn": "Mn.pbe-spn-kjpaw_psl.0.3.1.UPF",
    "O" : "O.pbe-n-kjpaw_psl.1.0.0.UPF",
}

# ======================================================================
# 4. DFT+U setup
# ======================================================================
HUBBARD_U = {"Mn": 4.5, "Gd": 6.5}      # eV, effective U (U - J)

# ======================================================================
# 5. QE input parameters
# ======================================================================
input_data = {
    "control": {
        "calculation"  : "scf",
        "restart_mode" : "from_scratch",
        "prefix"       : PREFIX,
        "outdir"       : OUTDIR,
        "pseudo_dir"   : PSEUDO_DIR,
        "tstress"      : True,
        "tprnfor"      : True,
        "disk_io"      : "low",
        "verbosity"    : "high",
    },
    "system": {
        "ibrav"        : 0,
        "nat"          : len(atoms),
        "ntyp"         : 3,
        "ecutwfc"      : 60.0,         # Ry
        "ecutrho"      : 480.0,        # Ry (8x ecutwfc for PAW)
        "occupations"  : "smearing",
        "smearing"     : "gaussian",
        "degauss"      : 0.01,         # Ry
        "nspin"        : 2,            # spin-polarized

        # ---- Fixed total magnetization (in muB per cell) ----
        # This ENFORCES the high-spin configuration globally.
        "tot_magnetization": TOT_MAG,

        # ---- Initial guess for per-species moments ----
        # tot_magnetization fixes the SUM; starting_magnetization
        # only sets the initial sign pattern / guess.
        "starting_magnetization": {
            "Gd": 1.0,     # f7 -> maximum positive
            "Mn": 0.8,     # high-spin d4
            "O" : 0.0,
        },

        # ---- DFT+U ----
        "lda_plus_u"        : True,
        "Hubbard_U"         : HUBBARD_U,
        "U_projection_type" : "ortho-atomic",
    },
    "electrons": {
        "conv_thr"         : 1.0e-8,
        "mixing_beta"      : 0.2,      # smaller for DFT+U stability
        "mixing_type"      : "plain",
        "electron_maxstep" : 300,
        "diagonalization"  : "david",
    },
    "ions": {
        "ion_dynamics": "bfgs",
    },
}

KPOINTS  = (4, 4, 3)
KOFFSET  = (0, 0, 0)

# ======================================================================
# 6. Espresso profile + calculator
# ======================================================================
profile = EspressoProfile(
    command=PW_COMMAND,
    pseudo_dir=PSEUDO_DIR,
)

calc = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials,
    input_data=input_data,
    kpts=KPOINTS,
    koffset=KOFFSET,
)

atoms.calc = calc

# ======================================================================
# 7. Write the QE input file explicitly (for inspection / reproducibility)
# ----------------------------------------------------------------------
# Use ase.io.write with format="espresso-in" – this is independent of the
# calculator and works in all recent ASE versions.
# ======================================================================
write(
    f"{PREFIX}.scf.in",
    atoms,
    format="espresso-in",
    input_data=input_data,
    pseudopotentials=pseudopotentials,
    kpts=KPOINTS,
    koffset=KOFFSET,
)
print(f"[i] QE input written to {PREFIX}.scf.in\n")

# ======================================================================
# 8. Run SCF directly (interactive)
# ======================================================================
print("=" * 72)
print("Launching Quantum ESPRESSO SCF (DFT+U, high-spin via tot_magnetization)")
print("=" * 72)

energy  = atoms.get_potential_energy()     # <-- runs pw.x
forces  = atoms.get_forces()
magmoms = atoms.get_magnetic_moments()

print("\n" + "=" * 72)
print("SCF RESULTS")
print("=" * 72)
print(f"Total energy         : {energy:.6f} eV")
print(f"Total energy / atom  : {energy / len(atoms):.6f} eV/atom")
print(f"Max |F|              : {np.max(np.linalg.norm(forces, axis=1)):.6f} eV/Å")
print(f"Total magnetization  : {magmoms.sum():.4f} μB  "
      f"(target {TOT_MAG:.1f} μB)")
print("-" * 72)
print("Per-atom magnetic moments (μB):")
for atom, m in zip(atoms, magmoms):
    print(f"  {atom.symbol:>2s}  idx={atom.index:<3d}  m = {m:+.4f}")
print("=" * 72)

# ======================================================================
# 9. Save results
# ======================================================================
np.savetxt(
    f"{PREFIX}_forces.dat",
    np.column_stack([np.arange(len(atoms)), forces]),
    header="index  Fx(eV/A)  Fy(eV/A)  Fz(eV/A)",
    fmt="%4d  %14.8f  %14.8f  %14.8f",
)
print(f"[i] Forces written to {PREFIX}_forces.dat")

write(f"{PREFIX}_final.xyz", atoms)
print(f"[i] Final structure written to {PREFIX}_final.xyz")
