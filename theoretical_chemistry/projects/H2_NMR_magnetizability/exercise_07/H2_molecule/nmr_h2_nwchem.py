import re
import subprocess
from pathlib import Path
import numpy as np
from ase.build import molecule
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem

# 1. Configure DFT functional, triple-zeta basis set, and MPI ranks
xc_func = "b3lyp"
basis_set = "6-311++G**"
nprocs = 6
nwchem_cmd = f"mpirun -np {nprocs} nwchem PREFIX.nwi > PREFIX.nwo"

# Precalculated GIAO B3LYP/6-311++G** isotropic 1H shielding for TMS (Si(CH3)4, Td)
SIGMA_TMS_REF_PPM = 31.82

print("=== NWChem GIAO NMR Chemical Shift Calculation ===")
print(f"Functional / Basis : {xc_func.upper()} / {basis_set}")
print(f"MPI Launch Command : {nwchem_cmd}")
print("Target Molecule    : H2 (simplest molecule, 2 atoms)")
print(f"NMR Reference      : Precalculated TMS sigma_iso(1H) = {SIGMA_TMS_REF_PPM:.2f} ppm")

def make_nwchem_calc(label, run_nmr=False):
    params = {
        "label": label,
        "theory": "dft",
        "basis": basis_set,
        "dft": {
            "xc": xc_func,
            "mult": 1,
            "grid": "fine",
            "convergence": {
                "energy": 1e-8,
                "density": 1e-6,
                "gradient": 5e-6,
            },
        },
        "command": nwchem_cmd,
    }
    if run_nmr:
        params["property"] = {"shielding": None}
        params["task"] = "property"
    return NWChem(**params)

# 2. Optimize H2 geometry with ASE BFGS
h2_atoms = molecule("H2")
h2_atoms.pbc = False
h2_atoms.calc = make_nwchem_calc("nwchem_opt_H2", run_nmr=False)
opt = BFGS(h2_atoms, logfile=None)
opt.run(fmax=0.001)
e_opt = h2_atoms.get_potential_energy()
d_hh = h2_atoms.get_distance(0, 1)

# 3. Run GIAO NMR shielding calculation on relaxed H2
nmr_label = "nwchem_nmr_H2"
nmr_calc = make_nwchem_calc(nmr_label, run_nmr=True)
nmr_calc.write_input(h2_atoms)
subprocess.run(nwchem_cmd.replace("PREFIX", nmr_label), shell=True, check=True)

nwo_text = Path(f"{nmr_label}.nwo").read_text(errors="ignore")
iso_values = [float(val) for val in re.findall(r"isotropic\s*=\s*([+-]?\d+\.\d+)", nwo_text)]
sigma_h2 = float(np.mean(iso_values))
delta_h2_ppm = SIGMA_TMS_REF_PPM - sigma_h2

print(f"\n[H2] BFGS steps={opt.nsteps} | E_opt={e_opt:.6f} eV | r(H-H)={d_hh:.4f} A")
print("\n=== 1H NMR Chemical Shift Summary for H2 (vs. TMS) ===")
print(f"sigma_iso(1H) in TMS (ref) : {SIGMA_TMS_REF_PPM:7.3f} ppm  (B3LYP/6-311++G** reference)")
print(f"sigma_iso(1H) in H2        : {sigma_h2:7.3f} ppm  (Expt gas-phase: 26.26 ppm)")
print(f"Chemical Shift delta(1H)   : {delta_h2_ppm:+7.3f} ppm")
print("Reference Values           : +4.32 ppm (gas phase, 300 K) | +4.47 to +4.62 ppm (solution)")

# Clean up NWChem scratch files
for pattern in ("nwchem_opt_*", "nwchem_nmr_*"):
    for f in Path(".").glob(pattern):
        if f.is_file():
            f.unlink()

