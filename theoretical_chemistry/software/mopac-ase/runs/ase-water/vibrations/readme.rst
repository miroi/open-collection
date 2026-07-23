H2O geometry optimization + vibrations
======================================

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mopac-ase/runs/ase-water/vibrations/.python water_pm7_asegeopt_vib_03.py

--- ASE prepared H2O molecule geometry ---
O-H1 Bond Length : 0.969 Å
O-H2 Bond Length : 0.969 Å
H-O-H Bond Angle : 104.0°

Starting geometry optimization...

--- Optimized Geometry Results ---
O-H1 Bond Length : 0.955 Å
O-H2 Bond Length : 0.955 Å
H-O-H Bond Angle : 105.4°

Optimized structure saved to 'optimized_water.xyz'

--- Running Vibrational Analysis ---

--- Computational Environment ---
MOPAC Executable : /home/miroi/work/software/mopac/mopac-23.1.2-linux/bin/mopac

--- Thermodynamic Results ---
Heat of Formation: -57.79478 kcal/mol

--- Net Atomic Charges ---
Atom  1 (O ) : -0.651948 e
Atom  2 (H ) : 0.325900 e
Atom  3 (H ) : 0.326047 e

--- Vibrational Stability Check ---
Calculated Normal Modes (cm⁻¹):
  Mode 0:      0.5i cm⁻¹ (negligible - numerical noise)
  Mode 1:      0.1i cm⁻¹ (negligible - numerical noise)
  Mode 2:      0.2  cm⁻¹
  Mode 3:     25.3  cm⁻¹
  Mode 4:     27.5  cm⁻¹
  Mode 5:     31.1  cm⁻¹
  Mode 6:   1395.1  cm⁻¹
  Mode 7:   2809.9  cm⁻¹
  Mode 8:   2856.1  cm⁻¹

Structure verification status:
✓ SUCCESS: No significant imaginary modes (>10 cm⁻¹) found.
  Structure is a valid LOCAL MINIMUM.

Frequencies saved to 'frequencies.txt'
