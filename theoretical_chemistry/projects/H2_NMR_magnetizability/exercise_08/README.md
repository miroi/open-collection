# Exercise 08

*Ab initio* Gauge-Including Atomic Orbital (**GIAO**) molecular magnetizability (magnetic susceptibility) tensor calculation of molecular hydrogen (H₂) driven by **ASE** and **PySCF** (`B3LYP/aug-cc-pVTZ`).

## Methodology

- **Geometry Optimization:** ASE `BFGS` ($f_{\max} = 0.001\ \text{eV/\AA}$) via a custom ASE `Calculator` wrapping `pyscf.dft.RKS` at the `B3LYP/aug-cc-pVTZ` level (`grid_level = 4`).
- **GIAO Magnetizability Tensor ($\boldsymbol{\chi}$):** Computed analytically on the relaxed equilibrium geometry using `pyscf.prop.magnetizability.rks.Magnetizability`, evaluating both the diamagnetic ($\boldsymbol{\chi}^d$) and paramagnetic ($\boldsymbol{\chi}^p$) second-order magnetic response tensors:

$$
\chi_{\alpha\beta} = -\left.\frac{\partial^{2} E(\mathbf{B})}{\partial B_{\alpha}\,\partial B_{\beta}}\right|_{\mathbf{B}=\mathbf{0}},
\qquad
\chi_{\mathrm{iso}} = \tfrac{1}{3}\,\mathrm{Tr}(\chi),
\qquad
\Delta\chi = \chi_{\parallel} - \chi_{\perp}
$$

## Results vs. Experimental & High-Level Benchmarks

| Property | `PySCF` (`B3LYP/aug-cc-pVTZ`) | Experimental Reference (300 K) | Agreement / Physical Meaning |
| :--- | :---: | :---: | :--- |
| **Equilibrium Bond Length** $r(\text{H–H})$ | **$0.7429\ \text{\AA}$** | $0.7414\ \text{\AA}$ | Within $0.0015\ \text{\AA}$ of gas-phase experiment |
| **Isotropic Magnetizability** $\chi_{\text{iso}}$ (a.u.) | **$-0.8582\ \text{a.u.}$** | **$-0.847\ \text{a.u.}$** | Within $1.3\%$ of experiment ($1\ \text{a.u.} = e^2 a_0^2 / m_e$) |
| **Isotropic Magnetizability** $\chi_{\text{iso}}$ (SI) | **$-6.77 \times 10^{-29}\ \text{J/T}^2$** | **$-6.68 \times 10^{-29}\ \text{J/T}^2$** | Closed-shell diamagnetic Lenz response ($\chi_{\text{iso}} < 0$) |
| **Molar Magnetic Susceptibility** $\chi_M$ (cgs) | **$-4.08 \times 10^{-6}\ \text{cm}^3/\text{mol}$** | **$-4.02 \times 10^{-6}\ \text{cm}^3/\text{mol}$** | Direct molar cgs-emu susceptibility ($\chi_M = N_A \chi_{\text{iso}}$) |
| **Magnetizability Anisotropy** $\Delta\chi$ (a.u.) | **$+0.1085\ \text{a.u.}$** | **$+0.114\ \text{a.u.}$** | Weak paramagnetic circulation perpendicular to the H–H bond axis |

## Usage

```bash
conda install -c conda-forge pyscf
pip install pyscf-properties
python magnetizability_h2_pyscf.py
```

## Challenge

With the help of AI agents:

1. **Isotropic Spherical Top** ($\mathrm{CH_4}$): Adapt `magnetizability_h2_pyscf.py` to compute the GIAO magnetizability tensor of **methane** ($\mathrm{CH_4}$, $T_{d}$ symmetry) at `B3LYP/aug-cc-pVTZ` and verify that:
   - The anisotropy vanishes identically ($\Delta\chi = 0.000\ \mathrm{a.u.}$) by tetrahedral symmetry.
   - The molar magnetic susceptibility matches the experimental gas-phase value ($\chi_{M}(\mathrm{CH_4}) \approx -17.4 \times 10^{-6}\ \mathrm{cm^{3}/mol}$, or $\chi_{\mathrm{iso}} \approx -3.66\ \mathrm{a.u.}$).

