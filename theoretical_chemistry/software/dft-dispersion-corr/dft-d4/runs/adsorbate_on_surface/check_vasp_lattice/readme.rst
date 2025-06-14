================================
DFTD4 check VASP lattice change
================================

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/dft-dispersion-corr/dft-d4/runs/adsorbate_on_surface/check_vasp_lattice/.~/work/software/dft-d4/dftd4/_build/app/dftd4 run Se54Fl1_relax.vasp -f PBE0

Dispersion energy:      -5.0687038846237E-01 Eh

~/work/software/dft-d4/dftd4/_build/app/dftd4 run Se54Fl1_relax_mod.vasp -f PBE0

Dispersion energy:      -3.5419040251225E-01 Eh


check params
~~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/dft-dispersion-corr/dft-d4/runs/adsorbate_on_surface/check_vasp_lattice/.~/work/software/dft-d4/dftd4/_build/app/dftd4 -v Se54Fl1_relax.vasp  > out1
milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/dft-dispersion-corr/dft-d4/runs/adsorbate_on_surface/check_vasp_lattice/.~/work/software/dft-d4/dftd4/_build/app/dftd4 -v Se54Fl1_relax_mod.vasp  > out2

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/dft-dispersion-corr/dft-d4/runs/adsorbate_on_surface/check_vasp_lattice/.diff out1  out2
<  molecular C6              694034.5735
<  molecular C8            49843695.9208
---
>  molecular C6              690532.6485
>  molecular C8            49593291.6094
