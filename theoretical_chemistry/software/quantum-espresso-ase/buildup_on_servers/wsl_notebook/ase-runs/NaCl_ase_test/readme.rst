QE ase test
===========

configure
~~~~~~~~~
https://wiki.fysik.dtu.dk/ase/ase/calculators/calculators.html#calculator-configuration
https://wiki.fysik.dtu.dk/ase/ase/calculators/espresso.html

get PP: https://www.quantum-espresso.org/pseudopotentials/

place them into commpon PP dir:
  sudo cp cl_pbe_v1.4.uspp.F.UPF na_pbe_v1.5.uspp.F.UPF  /usr/share/espresso/pseudo/.

run
~~~
for hint see https://gitlab.com/ase/ase/-/issues/1546#note_2152201647

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/buildup_on_servers/wsl_notebook/ase-runs/NaCl_ase_test/.python3 ase-rocksalt.py
unptimized rocksalt lattice constant a= 6.0
       Step     Time          Energy          fmax
LBFGS:    0 15:44:09    -1750.250480        2.274927
LBFGS:    1 15:44:10    -1750.459055        2.010169
LBFGS:    2 15:44:11    -1751.262469        0.766752
LBFGS:    3 15:44:12    -1751.454381        0.275210
LBFGS:    4 15:44:13    -1751.491306        0.084493
LBFGS:    5 15:44:14    -1751.494509        0.006087
QE optimized rocksalt lattice constant a= 7.534520921896282

