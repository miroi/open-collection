https://wiki.fysik.dtu.dk/gpaw/tutorialsexercises/structureoptimization/gettingstarted/gettingstarted.html

A structure optimization, also called a relaxation, is a series of calculations used to determine the minimum-energy structure of a given system. 
This involves multiple calculations of the atomic forces with respect to the atomic positions
as the atoms are moved downhill according to an optimization algorithm.

The following script uses the EMT calculator to optimize the structure of H2.


lx-pool
-------
milias@lxi090.gsi.de:~/Work/qch/projects/open-collection/theoretical_chemistry/software/ase/runs/gpaw-ase/simple_relaxation_H2/.python3 H2_relaxation.py 
                Step[ FC]     Time          Energy          fmax
*Force-consistent energies used in optimization.
BFGSLineSearch:    0[  0] 13:11:54        2.299030*       8.0358
BFGSLineSearch:    1[  2] 13:11:54        1.129250*       2.9257
BFGSLineSearch:    2[  4] 13:11:54        1.070800*       0.2142
BFGSLineSearch:    3[  5] 13:11:54        1.070549*       0.0367
milias@lxi090.gsi.de:~/Work/qch/projects/open-collection/theoretical_chemistry/software/ase/runs/gpaw-ase/simple_relaxation_H2/.

