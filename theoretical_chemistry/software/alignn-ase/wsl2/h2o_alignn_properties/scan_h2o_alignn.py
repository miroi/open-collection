#!/usr/bin/env python
"""
Water geometry scans with pretrained ALIGNN QM9 models (no PySCF needed).

 * r(OH) scan at fixed HOH angle, and HOH angle scan at fixed r(OH)
 * ALIGNN checkpoints are loaded once (cached), not once per prediction
 * Reference: equilibrium values only (REF_EQ below, edit them), drawn as
   dashed lines and compared in the equilibrium table. There is no
   per-geometry reference, so the plots show how ALIGNN behaves, not how wrong
   it is at each point.
 * results go to h2o_scan_out/: scan.csv, equilibrium.txt, scan.png

Requires: alignn, jarvis-tools, ase, numpy; matplotlib for the plot.
"""
import argparse
import contextlib
import csv
import io
import os
import tempfile
from functools import lru_cache
from pathlib import Path

import numpy as np
from ase import Atoms

HA2EV = 27.211386

# ---------------------------------------------------------------- settings
CUTOFF, BOX = 5.0, 60.0
TARGETS = ["gap", "ZPVE", "alpha", "U0"]
# (mean, std) used to de-standardise the raw model output. Units: gap/ZPVE eV,
# alpha bohr^3, U0 Ha. The U0 numbers are from memory and UNVERIFIED -- check
# them against the equilibrium table this script prints.
CONV = {"gap": (6.8587, 1.2843), "ZPVE": (4.0568, 0.9017),
        "alpha": (75.19, 8.19), "U0": (-411.54, 40.06)}

# Reference values for water at equilibrium (B3LYP/6-31G(2df,p) QM9 entry).
# Values are from memory / rough: look up the real QM9 H2O entry and edit.
# Set a value to None to leave it out.  gap, ZPVE in eV; alpha in bohr^3;
# U0 in Ha.
REF_EQ = {"gap": None, "ZPVE": 0.580, "alpha": 9.01, "U0": -76.4}

R0, A0 = 0.962, 103.7                      # fixed values for the scans
R_SCAN = np.round(np.arange(0.80, 1.4001, 0.02), 4)
A_SCAN = np.round(np.arange(80.0, 140.01, 4.0), 2)

OUT = Path.cwd() / "h2o_scan_out"


# ---------------------------------------------------------------- geometry
def water(r, angle, periodic=True):
    t = np.radians(angle / 2)
    a = Atoms("OHH", positions=[[0, 0, 0],
                                [r * np.sin(t), r * np.cos(t), 0],
                                [-r * np.sin(t), r * np.cos(t), 0]])
    if periodic:
        a.set_cell([BOX] * 3)
        a.pbc = True
        a.center()
    return a


# ---------------------------------------------------------------- ALIGNN
def run_alignn(geoms):
    """geoms: list of (label, r, angle). Returns array (n, len(TARGETS))."""
    import alignn.pretrained as ap
    from jarvis.core.atoms import ase_to_atoms

    # get_prediction() reloads the checkpoint on every call; patching the
    # module-level loader with a cached version makes each model load once.
    ap.get_figshare_model = lru_cache(maxsize=None)(ap.get_figshare_model)

    res = np.zeros((len(geoms), len(TARGETS)))
    cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as td:   # alignn drops files in the cwd
        os.chdir(td)
        try:
            for i, (_, r, ang) in enumerate(geoms):
                ja = ase_to_atoms(water(r, ang))
                for j, t in enumerate(TARGETS):
                    with contextlib.redirect_stdout(io.StringIO()):
                        z = float(np.ravel(ap.get_prediction(
                            model_name=f"qm9_{t}_alignn", atoms=ja,
                            cutoff=CUTOFF))[0])
                    mu, sd = CONV[t]
                    res[i, j] = z * sd + mu
                if i % 10 == 0:
                    print(f"  ALIGNN {i + 1}/{len(geoms)}", flush=True)
        finally:
            os.chdir(cwd)
    return res


# ---------------------------------------------------------------- output
def plot(rows):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 4, figsize=(16, 7))
    for row, (scan, xlab) in enumerate([("r", "r(OH) / Å"),
                                        ("angle", "HOH angle / deg")]):
        sel = [x for x in rows if x["scan"] == scan]
        x = np.array([s["r"] if scan == "r" else s["angle"] for s in sel])
        for col, (t, ylab) in enumerate([("gap", "gap / eV"),
                                         ("ZPVE", "ZPVE / eV"),
                                         ("alpha", "alpha / bohr³")]):
            ax = axes[row, col]
            ax.plot(x, [s[f"alignn_{t}"] for s in sel], "o-", ms=3, label="ALIGNN")
            if REF_EQ.get(t) is not None:
                ax.axhline(REF_EQ[t], color="C1", ls="--", label="reference @ eq.")
            ax.set_xlabel(xlab)
            ax.set_ylabel(ylab)
            ax.legend(fontsize=7)
        ax = axes[row, 3]
        u = np.array([s["alignn_U0"] for s in sel]) * HA2EV
        ax.plot(x, u - u.min(), "o-", ms=3, label="ALIGNN")
        ax.set_xlabel(xlab)
        ax.set_ylabel("U0 relative to scan minimum / eV")
        ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(OUT / "scan.png", dpi=150)


def main():
    ap_ = argparse.ArgumentParser()
    ap_.add_argument("--no-plot", action="store_true")
    args = ap_.parse_args()
    OUT.mkdir(exist_ok=True)

    geoms = [("r", r, A0) for r in R_SCAN] + [("angle", R0, a) for a in A_SCAN]

    print("ALIGNN ...")
    al = run_alignn(geoms + [("eq", R0, A0)])
    al_eq, al = al[-1], al[:-1]

    rows = []
    for (scan, r, ang), a in zip(geoms, al):
        d = dict(scan=scan, r=r, angle=ang)
        d.update({f"alignn_{t}": v for t, v in zip(TARGETS, a)})
        rows.append(d)
    with open(OUT / "scan.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    lines = [f"Equilibrium-like geometry: r = {R0} A, angle = {A0} deg",
             f"{'':8s}{'ALIGNN':>12s}{'reference':>12s}"]
    for t, v in zip(TARGETS, al_eq):
        rv = REF_EQ.get(t)
        lines.append(f"{t:8s}{v:12.4f}" + (f"{rv:12.4f}" if rv is not None else ""))
    lines.append("(units: gap, ZPVE eV; alpha bohr^3; U0 Ha; REF_EQ values are "
                 "rough, check them against the QM9 water entry)")
    txt = "\n".join(lines)
    (OUT / "equilibrium.txt").write_text(txt)
    print(txt)

    if not args.no_plot:
        try:
            plot(rows)
        except ImportError:
            print("matplotlib not available, skipping plot")
    print(f"Wrote results to {OUT}")


if __name__ == "__main__":
    main()
