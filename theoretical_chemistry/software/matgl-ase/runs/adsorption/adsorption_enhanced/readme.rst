========================
Hg on Gold111 with MatGL
========================

python hg_adsorption_enhanced.py
======================================================================
ENHANCED Hg ADSORPTION ON Au(111)
======================================================================
Started: 2026-06-16 23:27:48

Parameters:
  Au lattice: 4.080 Å
  Vacuum: 15.0 Å
  Layers: 4
  Surface: 3×3
  Force convergence: 0.05 eV/Å

======================================================================
LOADING M3GNet POTENTIAL
======================================================================
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
✓ Model loaded

======================================================================
PURE Au(111) SLAB RELAXATION
======================================================================

Slab: 36 atoms
Cell: [ 8.654987    8.654987   37.06676729] Å
Fixed 9 bottom atoms
/home/miroi/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/runs/adsorption/adsorption_enhanced/hg_adsorption_enhanced.py:80: FutureWarning: Please use atoms.calc = calc
  slab.set_calculator(calc)

✓ Slab energy: -110.6313 eV
  Steps: 13

======================================================================
Hg REFERENCE ENERGY
======================================================================

Calculating isolated Hg atom energy...
/home/miroi/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/runs/adsorption/adsorption_enhanced/hg_adsorption_enhanced.py:103: FutureWarning: Please use atoms.calc = calc
  hg_atom.set_calculator(calc)
      Step     Time          Energy          fmax
BFGS:    0 23:27:51        0.071771        0.000000
Hg atom energy: 0.0718 eV
/home/miroi/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/runs/adsorption/adsorption_enhanced/hg_adsorption_enhanced.py:115: FutureWarning: Please use atoms.calc = calc
  hg_dimer.set_calculator(calc)
      Step     Time          Energy          fmax
BFGS:    0 23:27:51        0.060522        0.117363
BFGS:    1 23:27:51        0.060139        0.110995
BFGS:    2 23:27:51        0.056457        0.021433
BFGS:    3 23:27:51        0.056272        0.005407
Hg dimer energy: 0.0563 eV
Hg-Hg bond energy: 0.0436 eV (per bond)

Using isolated Hg atom as reference: 0.0718 eV

======================================================================
ADSORPTION ENERGY CALCULATION
======================================================================

Testing adsorption sites...

FCC SITE
----------------------------------------
/home/miroi/work/projects/open-collection/theoretical_chemistry/software/matgl-ase/runs/adsorption/adsorption_enhanced/hg_adsorption_enhanced.py:156: FutureWarning: Please use atoms.calc = calc
  adslab.set_calculator(calc)
  E_total: -110.8571 eV
  E_ads: -0.2976 eV
  Height: 2.458 Å
  Steps: 22

HCP SITE
----------------------------------------
  E_total: -110.8436 eV
  E_ads: -0.2841 eV
  Height: 2.355 Å
  Steps: 13

BRIDGE SITE
----------------------------------------
  E_total: -110.8136 eV
  E_ads: -0.2541 eV
  Height: 2.390 Å
  Steps: 14

ONTOP SITE
----------------------------------------
  E_total: -110.6823 eV
  E_ads: -0.1227 eV
  Height: 3.015 Å
  Steps: 23

======================================================================
RESULTS SUMMARY
======================================================================

Adsorption Energies:
------------------------------------------------------------
Site       |   E_ads (eV) |   Height (Å) |   Preference
------------------------------------------------------------
fcc        |       -0.298 |        2.458 |       ★ Best
hcp        |       -0.284 |        2.355 |         Good
bridge     |       -0.254 |        2.390 |         Good
ontop      |       -0.123 |        3.015 |         Good

======================================================================
ADDITIONAL ANALYSIS
======================================================================

Surface energy estimate: 0.202 eV/Å²
Adsorption density: 0.015 atoms/Å²
Adsorption energy per area: -0.005 eV/Å²

======================================================================
VISUALIZATION
======================================================================
✓ Plot saved: hg_adsorption_results.png

Saving final structures...
  ✓ au_hg_fcc_final.xyz
  ✓ au_hg_hcp_final.xyz
  ✓ au_hg_bridge_final.xyz
  ✓ au_hg_ontop_final.xyz
  ✓ au_hg_best.xyz (fcc site)

======================================================================
LITERATURE COMPARISON
======================================================================

Literature values for Hg on Au(111):
• DFT (PBE): -0.25 to -0.35 eV (fcc site)
• DFT (vdW-DF): -0.30 to -0.45 eV
• Experimental: -0.30 to -0.40 eV (physisorption)

Our results (M3GNet):

  fcc   :  -0.298 eV  (deviation: +0.002 eV)
  hcp   :  -0.284 eV  (deviation: +0.016 eV)
  bridge:  -0.254 eV  (deviation: +0.046 eV)
  ontop :  -0.123 eV  (deviation: +0.177 eV)

Best site: fcc with E_ads = -0.298 eV
This is within the expected range for physisorption of Hg on Au(111).

Notes:
• M3GNet may not capture van der Waals interactions perfectly
• More accurate results may require hybrid DFT or vdW-DFT
• Temperature effects not considered (0K calculation)
• Coverage dependence not explored


======================================================================
COMPLETE SUMMARY
======================================================================

Calculation completed: 2026-06-16 23:28:02

SUMMARY:
  • Adsorption system: Hg on Au(111)
  • Surface size: 3×3 with 4 layers
  • Most stable site: fcc
  • Adsorption energy: -0.298 eV
  • Height above surface: 2.458 Å

ADSORPTION ENERGY COMPARISON:
  fcc    : -0.298 eV (most stable)
  hcp    : -0.284 eV
  bridge : -0.254 eV
  ontop  : -0.123 eV

OUTPUT FILES:
  • au_slab_relaxed.xyz - Relaxed clean surface
  • au_hg_*_final.xyz - Final structures for each site
  • au_hg_best.xyz - Best adsorption geometry
  • hg_adsorption_results.png - Visualization plot
  • *.traj - Relaxation trajectories
  • *.log - Relaxation logs

RECOMMENDATIONS:
  1. For accurate adsorption energy, include vdW corrections
  2. Consider larger supercell (4×4) to reduce lateral interactions
  3. Study coverage dependence (0.25, 0.5, 1.0 ML)
  4. Calculate diffusion barriers between sites
  5. Compare with DFT for validation


======================================================================
✓ COMPLETE!
======================================================================


