Nitrogen on copper
==================

https://wiki.fysik.dtu.dk/ase/gettingstarted/surface.html

We will calculate the adsorption energy of a nitrogen molecule on a copper surface. 

This is done by calculating the total energy for the isolated slab and for the isolated molecule.

The adsorbate is then added to the slab and relaxed, and the total energy for this composite system is calculated. 

The adsorption energy is obtained as the sum of the isolated energies minus the energy of the composite system.

Devana
~~~~~~
milias@login02.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/Nitrogen_on_copper/.python N2Cu.py
                Step[ FC]     Time          Energy          fmax
*Force-consistent energies used in optimization.
BFGSLineSearch:    0[  0] 19:45:35       11.689927*       1.0797
BFGSLineSearch:    1[  2] 19:45:35       11.670814*       0.4090
BFGSLineSearch:    2[  4] 19:45:35       11.625880*       0.0409
Adsorption energy: 0.32351942231800734


