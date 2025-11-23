=
=================
Hg@Se54 with CHGNet
===================

prepare input structure
~~~~~~~~~~~~~~~~~~~~~~~
HgSe54_chgnet_startstruct.vasp from Se54_slab_full_relaxation/Se54_final_relaxed_structure_chgnet.vasp + Hg coordinates form HgSe54_QEoptimized.vasp

run
~~~

keep lattice parames, relax only geometry

python  Hg_on_Se54_relaxation_chgnet.py > Hg_on_Se54_relaxation_chgnet.py_logfile


adsorption energy
-----------------
HgSe54 = -192.46742725372314 eV
Se54 = -190.43199062347412
Hg = 0.33789288997650146

Eads = E(HgSe54) - E(Se54) - E(Hg)
Eads = -192.46742725372314-(-190.43199062347412)-(0.33789288997650146)
Eads = -2.3733 eV   QE values: -0.584 eV
