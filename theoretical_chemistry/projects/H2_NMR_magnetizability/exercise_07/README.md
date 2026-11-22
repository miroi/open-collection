# Exercise 07

*Ab initio* Gauge-Including Atomic Orbital (**GIAO**) NMR magnetic shielding and $^1\text{H}$ chemical shift calculation of molecular hydrogen ($\text{H}_2$, the simplest neutral molecule) driven by **ASE** and **NWChem**.

## Methodology

- **Geometry Optimization:** ASE `BFGS` ($f_{\max} = 0.001\text{ eV/\AA}$) using MPI-parallel `NWChem` at the `B3LYP/6-311++G**` level of theory (`grid fine`).
- **Magnetic Shielding Tensor:** Computed on the relaxed equilibrium geometry via NWChem's GIAO `property` / `shielding` module.
- **Chemical Shift Reference:** Evaluated relative to the precalculated `B3LYP/6-311++G**` isotropic $^1\text{H}$ shielding of tetramethylsilane ($\text{TMS}$, $\text{Si(CH}_3)_4$, $\sigma_{\text{iso}}(\text{TMS}) = 31.820\text{ ppm}$):

$$\delta(^1\text{H}) = \sigma_{\text{iso}}(\text{TMS}) - \sigma_{\text{iso}}(\text{sample})$$

*(Note: Using the precalculated $31.820\text{ ppm}$ `B3LYP/6-311++G**` reference avoids running a computationally expensive 29-atom, 462-basis-function $C_1$ optimization of $\text{TMS}$ during classroom exercises.)*

## Results vs. Experimental & High-Level Benchmarks

| Method / Reference | $r(\text{H–H})$ ($\text{\AA}$) | $\sigma_{\text{iso}}(\text{H}_2)$ ($\text{ppm}$) | $\sigma_{\text{iso}}(\text{TMS})$ ($\text{ppm}$) | Chemical Shift $\delta(^1\text{H})$ ($\text{ppm}$) |
| :--- | :---: | :---: | :---: | :---: |
| **NWChem (`B3LYP/6-311++G**`, static $0\text{ K}$)** | **$0.7442$** | **$26.802$** | $31.820$ *(precalc.)* | **$+5.018$** |
| **CCSD(T)/CBS + Rovibrational ZPVE** | $0.7414$ | $26.29$ | $30.84$ | $+4.55$ |
| **Gas-Phase Experiment ($300\text{ K}$)** | $0.7414$ | **$26.26$** | $30.58$ *(extrap.)* | **$+4.32$** |
| **Solution NMR ($\text{CDCl}_3$ / $\text{C}_6\text{D}_6$, $298\text{ K}$)** | — | — | $0.00$ *(defined)* | **$+4.47\text{ to }+4.62$** |

## Physical Takeaways

1. **Rovibrational Zero-Point Deshielding ($+0.54\text{ ppm}$ in $\sigma_{\text{iso}}$):**
   - Static $0\text{ K}$ `B3LYP/6-311++G**` predicts $\sigma_{\text{iso}}(\text{H}_2) = 26.802\text{ ppm}$ at the equilibrium bond length $r_e = 0.7442\text{ \AA}$.
   - At $300\text{ K}$, zero-point and thermal vibrational stretching elongates the average bond length to $r_0 \approx 0.767\text{ \AA}$, reducing electron density around the protons and deshielding $\sigma_{\text{iso}}$ to the experimental gas-phase value of $26.26\text{ ppm}$.
2. **Systematic DFT Reference Offset:**
   - Static `B3LYP/6-311++G**` also slightly overestimates $\sigma_{\text{iso}}(\text{TMS})$ ($31.820\text{ ppm}$ vs. $30.58\text{ ppm}$ gas-phase experimental reference), shifting the unscaled chemical shift to $+5.018\text{ ppm}$ ($\sim 0.4\text{–}0.7\text{ ppm}$ downfield of experiment—typical for unscaled hybrid-DFT $^1\text{H}$ shifts).

## Usage

```bash
python nmr_h2_nwchem.py
```

## Challenge

With the help of AI agents:

1. **Hybridization & Magnetic Anisotropy Series ($sp^3 \rightarrow sp^2 \rightarrow sp$):** Extend `nmr_h2_nwchem.py` to optimize and compute GIAO $^1\text{H}$ chemical shifts (using the same $\sigma_{\text{TMS}} = 31.820\text{ ppm}$ reference) for **methane ($\text{CH}_4$)**, **ethene ($\text{C}_2\text{H}_4$)**, and **ethyne ($\text{C}_2\text{H}_2$)**, and compare against experimental gas-phase/solution $^1\text{H}$ shifts:
   - **Methane ($\text{CH}_4$, $sp^3$):** $\delta_{\text{expt}}(^1\text{H}) \approx +0.13\text{ to }+0.23\text{ ppm}$
   - **Ethene ($\text{C}_2\text{H}_4$, $sp^2$):** $\delta_{\text{expt}}(^1\text{H}) \approx +5.25\text{ to }+5.31\text{ ppm}$ *(deshielded by $\pi$-bond ring/diamagnetic anisotropy)*
   - **Ethyne ($\text{C}_2\text{H}_2$, $sp$):** $\delta_{\text{expt}}(^1\text{H}) \approx +1.48\text{ to }+1.91\text{ ppm}$ *(shielded inside the cylindrical $\text{C}\equiv\text{C}$ triple-bond cone)*
2. **NMR-Specialized Functional (`KT2`):** Re-run $\text{H}_2$ with `xc_func = "kt2"` (Keal–Tozer functional parameterized for magnetic shielding) and compare its raw $\sigma_{\text{iso}}(\text{H}_2)$ against `B3LYP` and the $26.26\text{ ppm}$ experimental value.

