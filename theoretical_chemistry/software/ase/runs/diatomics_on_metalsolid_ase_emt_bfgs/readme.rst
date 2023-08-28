Nitrogen on copper
==================

https://wiki.fysik.dtu.dk/ase/gettingstarted/surface.html

We will calculate the adsorption energy of a nitrogen molecule on a copper surface. 

This is done by calculating the total energy for the isolated slab and for the isolated molecule.

The adsorbate is then added to the slab and relaxed, and the total energy for this composite system is calculated. 

The adsorption energy is obtained as the sum of the isolated energies minus the energy of the composite system.

Devana
~~~~~~
milias@login01.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/nitrogen_on_copper/.module load Python/3.9.5-GCCcore-10.3.0
milias@login01.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/nitrogen_on_copper/.python N2Cu.py
                Step[ FC]     Time          Energy          fmax
*Force-consistent energies used in optimization.
BFGSLineSearch:    0[  0] 09:15:19       11.689927*       1.0797
BFGSLineSearch:    1[  2] 09:15:20       11.670814*       0.4090
BFGSLineSearch:    2[  4] 09:15:20       11.625880*       0.0409
Adsorption energy: 0.32351942231800734

Extension - oxygen on copper
----------------------------


milias@login01.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/nitrogen_on_copper/.python O2onCu.py
                Step[ FC]     Time          Energy          fmax
*Force-consistent energies used in optimization.
BFGSLineSearch:    0[  0] 10:30:31       12.234783*       1.1606
BFGSLineSearch:    1[  1] 10:30:31       12.068900*       0.6802
BFGSLineSearch:    2[  2] 10:30:31       12.025178*       1.3633
BFGSLineSearch:    3[  4] 10:30:31       11.982437*       0.1485
BFGSLineSearch:    4[  6] 10:30:32       11.980870*       0.0254
Adsorption energy: 0.2089710233342359

On gold - fully relaxed
-----------------------
milias@login01.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/diatomics_on_metalsolid_ase_emt_bfgs/.module load Python/3.9.5-GCCcore-10.3.0
milias@login01.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/diatomics_on_metalsolid_ase_emt_bfgs/.python O2onAu_fullyrelaxed.py
                Step[ FC]     Time          Energy          fmax
*Force-consistent energies used in optimization.
BFGSLineSearch:    0[  0] 12:04:34        9.863910*       7.3727
BFGSLineSearch:    1[  1] 12:04:34        8.531985*       2.5853
BFGSLineSearch:    2[  3] 12:04:35        8.119025*       1.7713
BFGSLineSearch:    3[  5] 12:04:35        7.845813*       1.0550
BFGSLineSearch:    4[  6] 12:04:35        7.814597*       0.3347
BFGSLineSearch:    5[  8] 12:04:35        7.794041*       0.6174
BFGSLineSearch:    6[ 10] 12:04:35        7.778744*       0.2225
BFGSLineSearch:    7[ 12] 12:04:35        7.769697*       0.1717
BFGSLineSearch:    8[ 14] 12:04:35        7.766018*       0.1247
BFGSLineSearch:    9[ 16] 12:04:35        7.762210*       0.0440
Adsorption energy: 1.1340346241939594


