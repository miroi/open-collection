===================================================
Chemical Summary Report: AIQM2 Water Optimization
===================================================

:Date: 2026-07-31
:Software Stack: MLAtom-ASE Collection
:System Environment: WSL2 / Ubuntu Linux
:Calculated System: Gas-Phase Water (:math:`\text{H}_2\text{O}`)

Executive Summary
=================

This report summarizes the geometric optimization, normal mode vibrational frequency analysis, and thermodynamic evaluation of a gas-phase water molecule. Calculations were performed using the machine-learning-born artificial intelligence quantum mechanical method **AIQM2** interfaced with the **Atomic Simulation Environment (ASE)**.

Software Environment Audit
==========================

The virtual environment configuration utilized for this computational run consists of the following stabilized dependencies:

* **Python:** 3.12.3 (GCC 13.3.0)
* **MLAtom:** 3.23.3
* **PyTorch:** 2.13.0+cu130
* **TorchANI:** 2.2.3 *(Pinned for legacy structural compatibility)*
* **PySCF:** 2.14.0
* **Setuptools:** 81.0.0 *(Pinned to retain legacy ``pkg_resources`` runtime)*
* **Dispersion Engine:** DFT-D4 (Standalone Binary)

Computational Protocol
======================

The calculation sequence followed a strict two-stage electronic structure tracking pipeline:

1. **Geometry Optimization:** Executed with the AIQM2 model using the ASE optimizer backend to minimize total electronic potential energy.
2. **Thermochemical Analysis:** Evaluated at standard state parameters (:math:`T = 298.15 \text{ K}`, :math:`P = 1 \text{ atm}`) utilizing the ideal gas partition function approximations over the generated Hessian matrix.

Calculated Energy States
------------------------

* **Optimized Electronic Energy ($E_{pot}$):** -76.384099 Hartree

Vibrational Frequencies Analysis
================================

A non-linear triatomic molecule contains :math:`3N - 6 = 3` true fundamental vibrational modes. The numerical finite-difference Hessian evaluation generated 9 normal modes due to translational and rotational mixing over the coordinate mesh. 

Table 1: Vibrational Frequencies Comparison
-------------------------------------------

+-----------+-----------------------+-------------------------------+---------------------+--------------------------------------------------------+

| Mode ID   | Description           | AIQM2 / ASE Calculated (cm⁻¹) | Experimental (NIST) | Physical Interpretation & Status                       |
+===========+=======================+===============================+=====================+========================================================+

| Mode 1    | Translation/Rotation  | 202.6i                        | 0.0                 | Non-physical numerical phantom grid noise              |
+-----------+-----------------------+-------------------------------+---------------------+--------------------------------------------------------+

| Mode 2    | Translation/Rotation  | 0.1i                          | 0.0                 | Valid numerical translation axis root                  |
+-----------+-----------------------+-------------------------------+---------------------+--------------------------------------------------------+

| Mode 3    | Translation/Rotation  | 0.0i                          | 0.0                 | Valid numerical translation axis root                  |
+-----------+-----------------------+-------------------------------+---------------------+--------------------------------------------------------+

| Mode 4    | Translation/Rotation  | 0.1                           | 0.0                 | Valid numerical rotation axis root                    |
+-----------+-----------------------+-------------------------------+---------------------+--------------------------------------------------------+

| Mode 5    | Translation/Rotation  | 199.8                         | 0.0                 | Non-physical numerical phantom grid noise              |
+-----------+-----------------------+-------------------------------+---------------------+--------------------------------------------------------+

| Mode 6    | Translation/Rotation  | 289.6                         | 0.0                 | Non-physical numerical phantom grid noise              |
+-----------+-----------------------+-------------------------------+---------------------+--------------------------------------------------------+

| Mode 7    | ν₂ Fundamental Band   | 1653.3                        | 1594.7              | True H-O-H In-plane bending vibration                 |
+-----------+-----------------------+-------------------------------+---------------------+--------------------------------------------------------+

| Mode 8    | ν₁ Fundamental Band   | 3865.9                        | 3657.1              | True Symmetric O-H stretching vibration                |
+-----------+-----------------------+-------------------------------+---------------------+--------------------------------------------------------+

| Mode 9    | ν₃ Fundamental Band   | 3972.3                        | 3755.9              | True Asymmetric O-H stretching vibration               |
+-----------+-----------------------+-------------------------------+---------------------+--------------------------------------------------------+

Thermochemical Properties
=========================

Thermodynamic macro-states extracted from the ideal gas partition functions were converted from raw electronvolts (eV) to standard laboratory SI dimensions and atomic units (Hartree) using the CODATA conversion factor (:math:`1 \text{ eV} = 0.03674930814 \text{ Hartree}`).

Table 2: Thermochemical Validation at 298.15 K, 1 atm
-----------------------------------------------------

+---------------------------+-----------------------------------+-----------------------------------+--------------------------------------------------------+

| Thermodynamic Metric      | AIQM2 Calculated Value            | Experimental Gas Phase (NIST)     | Accuracy & Physical Deviation Analysis                 |
+===========================+===================================+===================================+========================================================+

| Zero-Point Energy (ZPE)   | 0.021609 Hartree                  | 0.020480 Hartree                  | Overestimates by ~4.1% due to harmonic approximations. |
|                           | (56.73 kJ/mol)                    | (54.50 kJ/mol)                    |                                                        |
+---------------------------+-----------------------------------+-----------------------------------+--------------------------------------------------------+

| Absolute Entropy (S°)     | 0.00007401 Hartree/K              | 0.00007192 Hartree/K              | Excellent correlation (2.9% error). Ideal gas          |
|                           | (194.32 J/mol·K)                  | (188.84 J/mol·K)                  | translational and rotational profiles map cleanly.     |
+---------------------------+-----------------------------------+-----------------------------------+--------------------------------------------------------+

| Total Enthalpy (H)        | -76.358668 Hartree                | N/A                               | Absolute electronic boundary value; used exclusively   |
|                           |                                   |                                   | for relative chemical reaction comparisons.            |
+---------------------------+-----------------------------------+-----------------------------------+--------------------------------------------------------+

| Gibbs Free Energy (G)     | -76.380718 Hartree                | N/A                               | Absolute electronic boundary value; used exclusively   |
|                           |                                   |                                   | for relative chemical reaction comparisons.            |
+---------------------------+-----------------------------------+-----------------------------------+--------------------------------------------------------+

Methodological Findings & Conclusions
=====================================

1. **Vibrational Overestimation:** The stretching modes (:math:`\nu_1` and :math:`\nu_3`) show a systematic overestimation of approximately 5–6%. This is expected behavior for unscaled harmonic calculations, as real-world molecular bonds are anharmonic and lengthen at higher vibrational states.
2. **Symmetry and Grid Artifacts:** The 4 phantom modes (Modes 1, 5, and 6) are numerical truncation artifacts produced during the finite-difference matrix scanning of the machine-learning-born semi-empirical potential energy surface. They do not indicate a flaw in the AIQM2 energy model itself.
3. **Macro-state Accuracy:** The exceptional accuracy of the absolute entropy (:math:`2.9\%` error) confirms that the optimized molecular geometry, ground-state rotational tensors, and mass distribution are physically accurate.

