================
Gromacs test run
================

/home/milias/Work/qch/software/gromacs/gromacs_master/build_openmpi-4.0.1_gnu6.3/bin


LYSOZYME Tutorial
-----------------
see http://www.mdtutorials.com/gmx/lysozyme/01_pdb2gmx.html


https://www.rcsb.org/structure/1AKI

..visualize the structure using a viewing program such as VMD, Chimera, PyMOL, etc.

..strip out the crystal waters:
grep -v HOH 1aki.pdb > 1AKI_clean.pdb

gmx pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water spce ... this is crashing with OpenMPI





