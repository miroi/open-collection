#!/usr/bin/env python3
"""
Direct interactive Quantum ESPRESSO SCF for GdMnO3
------------------------------------------------------------------
- Geometry from GdMnO3.cif (read with ASE)
- DFT+U (Hubbard) on Mn 3d only (Gd 4f is frozen in the UPF core;
  the pseudopotential Gd.pbe-spdn-kjpaw_psl.1.0.0.UPF does not expose
  a 4F manifold, so U(Gd) cannot be applied with this UPF)
- High-spin configuration enforced via tot_magnetization = 44 muB
    Gd3+ 4f7  -> S = 7/2 -> 7 muB
    Mn3+ 3d4  -> S = 2   -> 4 muB   (high-spin, t2g^3 eg^1)
    per formula unit: 11 muB;  Z = 4  =>  44 muB per cell
- Writes a VALID pw.x input manually.
- Uses the NEW DFT+U syntax (QE >= 7.1): the HUBBARD card.
- mixing parameters in &MIXING namelist (not &ELECTRONS).
- Launches pw.x directly with subprocess (interactive run).
------------------------------------------------------------------
"""

import os
import re
import sys
import subprocess
import numpy as np
from ase.io import read

# ======================================================================
# 0. User-configurable paths
# ======================================================================
CIF_FILE   = "GdMnO3.cif"
PSEUDO_DIR = "./"
OUTDIR     = "./tmp"
PREFIX     = "GdMnO3"

PW_COMMAND = "mpirun -np 4 pw.x"       # or just "pw.x" for a serial run

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
# 2. High-spin total magnetization (muB per cell)
# ======================================================================
Z_FORMULA_UNITS = 4
MU_GD_HIGHSPIN  = 7.0
MU_MN_HIGHSPIN  = 4.0
TOT_MAG = (MU_GD_HIGHSPIN + MU_MN_HIGHSPIN) * Z_FORMULA_UNITS   # = 44.0
print(f"[i] Target tot_magnetization = {TOT_MAG:.1f} muB  "
      f"(Gd {MU_GD_HIGHSPIN} + Mn {MU_MN_HIGHSPIN}) x Z={Z_FORMULA_UNITS}")

# ======================================================================
# 3. Species table
# ======================================================================
species_order = ["Gd", "Mn", "O"]
species_mass  = {"Gd": 157.25, "Mn": 54.938044, "O": 15.999}

pseudopotentials = {
    "Gd": "Gd.pbe-spdn-kjpaw_psl.1.0.0.UPF",
    "Mn": "Mn.pbe-spn-kjpaw_psl.0.3.1.UPF",
    "O" : "O.pbe-n-kjpaw_psl.1.0.0.UPF",
}

start_mag = {"Gd": 1.0, "Mn": 0.8, "O": 0.0}

# ----------------------------------------------------------------
# Hubbard U: only Mn 3d is available in the chosen UPFs.
# Gd 4f is frozen in the core of Gd.pbe-spdn-...UPF, so U(Gd)=0.
# ----------------------------------------------------------------
hubbard_u        = {"Gd": 0.0, "Mn": 4.5, "O": 0.0}
hubbard_manifold = {"Gd": "4f", "Mn": "3d", "O": "2p"}

KPOINTS = (4, 4, 3)
KOFFSET = (0, 0, 0)

# ======================================================================
# 4. Build the pw.x input
# ======================================================================
lines = []

# ---- &CONTROL ----
lines.append("&CONTROL")
lines.append("   calculation       = 'scf'")
lines.append(f"   prefix            = '{PREFIX}'")
lines.append(f"   outdir            = '{OUTDIR}'")
lines.append(f"   pseudo_dir        = '{PSEUDO_DIR}'")
lines.append("   restart_mode      = 'from_scratch'")
lines.append("   tstress           = .true.")
lines.append("   tprnfor           = .true.")
lines.append("   disk_io           = 'low'")
lines.append("   verbosity         = 'high'")
lines.append("/")

# ---- &SYSTEM ----
lines.append("&SYSTEM")
lines.append("   ibrav             = 0")
lines.append(f"   nat               = {len(atoms)}")
lines.append(f"   ntyp              = {len(species_order)}")
lines.append("   ecutwfc           = 60.0")
lines.append("   ecutrho           = 480.0")
lines.append("   occupations       = 'smearing'")
lines.append("   smearing          = 'gaussian'")
lines.append("   degauss           = 0.01")
lines.append("   nspin             = 2")
lines.append(f"   tot_magnetization = {TOT_MAG:.1f}")
for i, sp in enumerate(species_order, start=1):
    lines.append(f"   starting_magnetization({i}) = {start_mag[sp]:.4f}")
lines.append("/")

# ---- &ELECTRONS ----
lines.append("&ELECTRONS")
lines.append("   conv_thr          = 1.0d-8")
lines.append("   electron_maxstep  = 300")
lines.append("   diagonalization   = 'david'")
lines.append("/")

# ---- &MIXING ----
lines.append("&MIXING")
lines.append("   mixing_beta       = 0.2")
lines.append("   mixing_mode       = 'plain'")
lines.append("   mixing_type       = 'plain'")
lines.append("/")

# ---- &IONS ----
lines.append("&IONS")
lines.append("   ion_dynamics      = 'bfgs'")
lines.append("/")

# ---- ATOMIC_SPECIES ----
lines.append("ATOMIC_SPECIES")
for sp in species_order:
    lines.append(f"{sp}  {species_mass[sp]}  {pseudopotentials[sp]}")
lines.append("")

# ---- K_POINTS ----
lines.append("K_POINTS automatic")
lines.append(f"{KPOINTS[0]} {KPOINTS[1]} {KPOINTS[2]}  "
             f"{KOFFSET[0]} {KOFFSET[1]} {KOFFSET[2]}")
lines.append("")

# ---- HUBBARD card (QE >= 7.1): only species with U > 0 ----
if any(hubbard_u[sp] > 0.0 for sp in species_order):
    lines.append("HUBBARD (ortho-atomic)")
    for sp in species_order:
        if hubbard_u[sp] > 0.0:
            lines.append(f"U {sp}-{hubbard_manifold[sp]} {hubbard_u[sp]:.4f}")
    lines.append("")

# ---- CELL_PARAMETERS ----
lines.append("CELL_PARAMETERS angstrom")
for vec in atoms.cell:
    lines.append(f"  {vec[0]:.10f}  {vec[1]:.10f}  {vec[2]:.10f}")
lines.append("")

# ---- ATOMIC_POSITIONS ----
lines.append("ATOMIC_POSITIONS crystal")
for atom in atoms:
    x, y, z = atom.scaled_position
    lines.append(f"{atom.symbol:2s}  {x:.10f}  {y:.10f}  {z:.10f}")

qe_input_text = "\n".join(lines) + "\n"

INPUT_FILE  = f"{PREFIX}.scf.in"
OUTPUT_FILE = f"{PREFIX}.scf.out"

with open(INPUT_FILE, "w") as fh:
    fh.write(qe_input_text)

print(f"[i] Wrote valid pw.x input to {INPUT_FILE}")
print(f"[i] DFT+U applied to Mn-3d only (Gd 4f frozen in UPF core)\n")

# ======================================================================
# 5. Launch pw.x directly
# ======================================================================
print("=" * 72)
print(f"Launching: {PW_COMMAND} -in {INPUT_FILE}")
print("=" * 72)

with open(OUTPUT_FILE, "w") as out_fh:
    result = subprocess.run(
        PW_COMMAND.split() + ["-in", INPUT_FILE],
        stdout=out_fh,
        stderr=subprocess.STDOUT,
    )

# ======================================================================
# 6. Error handling
# ======================================================================
if result.returncode != 0:
    print(f"\n[!] pw.x failed with exit code {result.returncode}.")
    print(f"    Last 60 lines of {OUTPUT_FILE}:\n")
    with open(OUTPUT_FILE) as fh:
        for line in fh.readlines()[-60:]:
            print(line.rstrip())
    sys.exit(1)

print(f"[i] pw.x finished successfully. Output: {OUTPUT_FILE}\n")

# ======================================================================
# 7. Parse key results
# ======================================================================
with open(OUTPUT_FILE) as fh:
    out = fh.read()

RY_TO_EV = 13.605693122994

m = re.findall(r"!\s+total energy\s+=\s+([-\d.]+)\s+Ry", out)
if m:
    e_ry = float(m[-1])
    e_ev = e_ry * RY_TO_EV
    print(f"[i] Total energy           : {e_ry:.6f} Ry  =  {e_ev:.6f} eV")

m = re.findall(r"total magnetization\s+=\s+([-\d.]+)", out)
if m:
    print(f"[i] Total magnetization    : {m[-1]} muB  "
          f"(target {TOT_MAG:.1f} muB)")

m = re.findall(r"absolute magnetization\s+=\s+([-\d.]+)", out)
if m:
    print(f"[i] Absolute magnetization : {m[-1]} muB")

m = re.findall(r"the Fermi energy is\s+([-\d.]+)", out)
if m:
    print(f"[i] Fermi energy           : {m[-1]} eV")

m = re.findall(r"number of Kohn-Sham states=\s+(\d+)", out)
if m:
    print(f"[i] Number of KS states    : {m[-1]}")

m = re.findall(r"convergence has been achieved in\s+(\d+)\s+iterations", out)
if m:
    print(f"[i] SCF converged in       : {m[-1]} iterations")

# Print any Hubbard summary lines QE printed
for line in out.splitlines():
    low = line.lower()
    if "hubbard" in low and ("u =" in low or "manifold" in low or "atom" in low):
        print(f"[i] {line.strip()}")

print("\nDone.")
