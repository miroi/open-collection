QE ase test
===========

https://wiki.fysik.dtu.dk/ase/ase/calculators/espresso.html

get PP: https://www.quantum-espresso.org/pseudopotentials/

place them into commpon PP dir:

sudo cp cl_pbe_v1.4.uspp.F.UPF na_pbe_v1.5.uspp.F.UPF  /usr/share/espresso/pseudo/.

run
~~~~
python3 ase-rocksalt.py
       Step     Time          Energy          fmax
LBFGS:    0 00:55:18    -1750.250480        0.000000
6.0

...forces not calculated, to be fixed ! 
