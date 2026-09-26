# Pd Adsorption on Au(111) — ASE / EMT

A self-contained study of single-atom Pd adsorption on the Au(111)
surface using the [Atomic Simulation Environment (ASE)][ase] and the
built-in **EMT** (Effective Medium Theory) calculator.

[ase]: https://ase-lib.org/

---

## 1. Objective

Determine the preferred adsorption site of a single Pd atom on
Au(111) by computing the adsorption energy at four high-symmetry
sites and relaxing each geometry:

| Site   | Description                                  |
|--------|----------------------------------------------|
| `fcc`  | FCC hollow (no Au directly below)            |
| `hcp`  | HCP hollow (Au directly below)               |
| `bridge` | Bridge between two top-layer Au atoms      |
| `ontop` | Directly above a top-layer Au atom          |

The adsorption energy is defined as

```
E_ads = E_total − E_slab − E_atom
```

where

- `E_total`  = energy of the relaxed Pd/Au(111) system
- `E_slab`   = energy of the relaxed clean Au(111) slab
- `E_atom`   = energy of an isolated Pd atom in vacuum

---

## 2. System

| Property        | Value                        |
|-----------------|------------------------------|
| Surface         | Au(111), FCC                 |
| Slab size       | 4 × 4 × 4                    |
| Au atoms        | 64                           |
| Adsorbate       | 1 Pd atom                    |
| Initial height  | 2.0 Å above the surface      |
| Vacuum          | 10 Å                         |
| Periodic        | Yes (slab), No (isolated Pd) |

The slab is generated with `ase.build.fcc111`. The Pd atom is placed
with `ase.build.add_adsorbate` at the requested site.

---

## 3. Method

| Setting              | Value                          |
|----------------------|--------------------------------|
| Calculator           | `ase.calculators.emt.EMT`      |
| Optimizer            | `ase.optimize.BFGS`            |
| Convergence          | `fmax < 0.01 eV/Å`             |
| Reference energies   | recomputed at runtime          |

EMT is a fast, semi-empirical model. It captures qualitative trends
(site preference, relative ordering) but **not** quantitative DFT
accuracy. The purpose of this project is to demonstrate a complete,
reproducible surface-science workflow in ASE.

---

## 4. Requirements

- Python ≥ 3.9
- ASE (`pip install ase`)
- NumPy (installed with ASE)

Optional, for visualization:

- `ase gui` (bundled with ASE)

---

## 5. How to run

Everything is contained in a single script.

```bash
python pd_adsorption.py
```

The script performs, in order:

1. Creates the output directories (`structures/`, `logs/`, `trajectories/`).
2. Relaxes the clean Au(111) slab → `E_slab`.
3. Computes the isolated Pd atom energy → `E_atom`.
4. For each site in `{fcc, hcp, bridge, ontop}`:
   - builds a fresh slab,
   - adds the Pd atom,
   - relaxes with BFGS until `fmax < 0.01 eV/Å`,
   - computes `E_ads`,
   - saves the relaxed structure.
5. Prints a summary table and ranks the sites by stability.

### Expected runtime

About **1–2 minutes** on a standard laptop (EMT is very cheap).

---

## 6. Output

### Directory layout

```
.
├── pd_adsorption.py
├── README.md
├── structures/
│   ├── relaxed_fcc.vasp
│   ├── relaxed_hcp.vasp
│   ├── relaxed_bridge.vasp
│   └── relaxed_ontop.vasp
├── logs/
│   ├── slab_relax.log
│   ├── relax_fcc.log
│   ├── relax_hcp.log
│   ├── relax_bridge.log
│   └── relax_ontop.log
└── trajectories/
    ├── slab_relax.traj
    ├── relax_fcc.traj
    ├── relax_hcp.traj
    ├── relax_bridge.traj
    └── relax_ontop.traj
```

### Console summary (example)

```
====================================================================
Pd adsorption on Au(111)  --  ASE / EMT
====================================================================
Slab:      Au(111) 4x4x4  (64 Au atoms)
Adsorbate: 1 Pd atom, initial height 2.0 A
Vacuum:    10.0 A
Optimizer: BFGS, fmax < 0.01 eV/A
--------------------------------------------------------------------

[1/2] Reference energies
    E_slab        = 7.557533 eV   (steps=..., fmax=...)
    E_atom(Pd)    = 3.900000 eV

[2/2] Adsorption sites
  ...
====================================================================
Summary
====================================================================
Site        E_total (eV)     E_ads (eV)    fmax (eV/A)   Steps
----------------------------------------------------------------
fcc             8.176096       -3.281436       0.008744      ...
hcp             8.174644       -3.282888       0.008451      ...
bridge          8.271097       -3.186435       0.006715      ...
ontop           8.714582       -2.742950       0.009077      ...

Site preference (most stable first):
  1. hcp       E_ads = -3.282888 eV  <-- most stable
  2. fcc       E_ads = -3.281436 eV
  3. bridge    E_ads = -3.186435 eV
  4. ontop     E_ads = -2.742950 eV
```

(Exact numbers may vary slightly with ASE version.)

### Viewing a trajectory

```bash
ase gui trajectories/relax_fcc.traj
```

### Reading a relaxed structure

```bash
cat structures/relaxed_fcc.vasp
```

---

## 7. Results

| Site   | E_total (eV) | E_ads (eV) | fmax (eV/Å) |
|--------|-------------:|-----------:|------------:|
| FCC    | 8.176096     | −3.281436  | 0.008744    |
| HCP    | 8.174644     | −3.282888  | 0.008451    |
| Bridge | 8.271097     | −3.186435  | 0.006715    |
| Top    | 8.714582     | −2.742950  | 0.009077    |

Reference energies:

```
E_slab      = 7.5575325561 eV
E_atom(Pd)  = 3.9000000000 eV
```

All four calculations satisfy `fmax < 0.01 eV/Å`.

### Interpretation

- **HCP and FCC hollow sites are nearly degenerate** (ΔE ≈ 1.5 meV).
  This near-degeneracy is a well-known feature of close-packed
  fcc(111) surfaces and reflects the small difference in the local
  environment (presence or absence of a second-layer Au atom directly
  below the adsorbate).
- **Bridge** is ~0.1 eV weaker than the hollow sites.
- **Ontop** is the least stable by ~0.5 eV.
- The overall ordering

  ```
  hollow (hcp ≈ fcc)  >  bridge  >  ontop
  ```

  is the expected qualitative trend for a metal adatom on a
  close-packed metal surface.

---

## 8. Files

| File / dir            | Contents                                              |
|-----------------------|-------------------------------------------------------|
| `pd_adsorption.py`    | Complete, self-contained workflow                     |
| `README.md`           | This document                                         |
| `structures/`         | Relaxed VASP POSCAR files for each site               |
| `logs/`               | BFGS relaxation logs (energy/force per step)          |
| `trajectories/`       | ASE `.traj` files (full relaxation path)              |

---

## 9. Notes and possible extensions

- **DFT cross-check.** Replace `EMT()` with an ASE calculator for a
  DFT code (e.g. GPAW, VASP, Quantum ESPRESSO) to obtain
  quantitatively meaningful adsorption energies.
- **Coverage effects.** Increase the Pd coverage and check whether
  the preferred site changes.
- **Subsurface / alloying.** Consider Pd incorporated into the Au
  slab, not only adsorbed on top.
- **Larger slabs.** Test convergence of `E_ads` with respect to
  slab thickness and lateral size.
- **Vacuum convergence.** Verify that 10 Å is sufficient for the
  chosen calculator (it is for EMT; DFT often needs more).

---

## 10. References

- H. L. Skriver and N. M. Rosengaard,
  *Phys. Rev. B* **46**, 7157 (1992) — EMT parameters.
- K. W. Jacobsen, P. Stoltze, and J. K. Nørskov,
  *Surf. Sci.* **366**, 394 (1996) — EMT for surfaces.
- ASE documentation: <https://ase-lib.org/>