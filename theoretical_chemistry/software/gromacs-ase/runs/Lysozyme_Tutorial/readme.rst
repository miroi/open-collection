==================================
Gromacs test run LYSOZYME Tutorial
==================================

http://www.mdtutorials.com/gmx/lysozyme/01_pdb2gmx.html
https://www.rcsb.org/structure/1AKI

Energy minimization
~~~~~~~~~~~~~~~~~~~











==========
On Govorun
==========

modules
~~~~~~~
module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1               3) gcc/v12.3.0              5) cuda/v12.1               7) GROMACS/v2024.3
  2) BASE/1.0                 4) openmpi/v5.0.3_gcc1230   6) Python/v3.10.13


gmx_mpi pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water tip3p   > 1AKI_processed.gro_logfile 2>&1

gmx_mpi editconf -f 1AKI_processed.gro -o 1AKI_newbox.gro -c -d 1.2 -bt cubic > 1AKI_newbox.gro_logfile  2>&1

gmx_mpi solvate -cp 1AKI_newbox.gro -cs spc216.gro -o 1AKI_solv.gro -p topol.top > 1AKI_solv.gro_logfile  2>&1

download ions
~~~~~~~~~~~~~
wget http://www.mdtutorials.com/gmx/lysozyme/Files/ions.mdp




