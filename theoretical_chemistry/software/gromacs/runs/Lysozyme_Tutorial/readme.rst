================
Gromacs test run
LYSOZYME Tutorial
================

umb.sk:
--------
/home/milias/Work/qch/software/gromacs/gromacs_master/build_openmpi-4.0.1_gnu6.3/bin

see http://www.mdtutorials.com/gmx/lysozyme/01_pdb2gmx.html

https://www.rcsb.org/structure/1AKI

..visualize the structure using a viewing program such as VMD, Chimera, PyMOL, etc.

..strip out the crystal waters:
grep -v HOH 1aki.pdb > 1AKI_clean.pdb

gmx pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water spce ... this is crashing with OpenMPI


WSL
----
milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/gromacs/runs/Lysozyme_Tutorial/.gmx pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water spce

define the box
~~~~~~~~~~~~~~~
gmx editconf -f 1AKI_processed.gro -o 1AKI_newbox.gro -c -d 1.0 -bt cubic

solvation
~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/gromacs/runs/Lysozyme_Tutorial/.gmx solvate -cp 1AKI_newbox.gro -cs spc216.gro -o 1AKI_solv.gro -p topol.top












