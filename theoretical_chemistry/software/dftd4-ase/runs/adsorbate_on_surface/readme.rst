============================
DFT-D4 on adsorption systems
============================

test coordinates
~~~~~~~~~~~~~~~~
~/work/software/dft-d4/dftd4/_build/app/dftd4     Pb_on_Se54_100.geopt_sozora_blyp-d3bj_tzp_sc_converged_geometry.xyz 

get disp energy
~~~~~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/dft-dispersion-corr/dft-d4/runs/adsorbate_on_surface/.~/work/software/dft-d4/dftd4/_build/app/dftd4 run -v Se54Fl1_relax.vasp -f
PBE0
                    ____  _____ _____     ____  _  _
      -------------|  _ \|  ___|_   _|---|  _ \| || |------------
     |             | | | | |_    | | ___ | | | | || |_           |
     |             | |_| |  _|   | ||___|| |_| |__   _|          |
     |             |____/|_|     |_|     |____/   |_|            |
     |             ===================================           |
     |            E. Caldeweyher, S. Ehlert & S. Grimme          |
     |          Mulliken Center for Theoretical Chemistry        |
     |                    University of Bonn                     |
      -----------------------------------------------------------

Rational (Becke-Johnson) damping: PBE0-D4-ATM
---------------------
  s6         1.0000
  s8         1.2007
  s9         1.0000
  a1         0.4009
  a2         5.0293
 alp        16.0000
--------------------

Dispersion energy:      -5.0687038846237E-01 Eh

[Info] Dispersion energy written to .EDISP


