==============================
Step One: Prepare the Topology
==============================

http://www.mdtutorials.com/gmx/membrane_protein/01_pdb2gmx.html

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Membrane_Protein/prepare_the_topology/.wget http://www.mdtutorials.com/gmx/membrane_protein/Files/KALP-15_princ.pdb

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Membrane_Protein/prepare_the_topology/.~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi pdb2gmx -f KALP-15_princ.pdb -o KALP-15_processed.gro -ignh -ter -water spc

...manually captured output into  topology.logfile




