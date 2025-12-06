=============================
Step Two: Modify the Topology
=============================


http://www.mdtutorials.com/gmx/membrane_protein/02_topology.html

https://people.ucalgary.ca/~tieleman/download.html

problem:  https://gromacs.bioexcel.eu/t/missing-files-while-following-the-membrane-protein-tutorial/6508/4

download the following files:

dppc128.pdb - the structure of a 128-lipid DPPC bilayer
dppc.itp - the [moleculetype] definition for DPPC
lipid.itp - Berger lipid parameters

try solution:
https://github.com/fuentesdt/MembraneProtein

wget https://raw.githubusercontent.com/fuentesdt/MembraneProtein/refs/heads/master/dppc128.pdb
wget https://raw.githubusercontent.com/fuentesdt/MembraneProtein/refs/heads/master/dppc.itp
wget https://github.com/fuentesdt/MembraneProtein/blob/master/lipid.itp

miroi@MIRO:~/work/software/gromacs/gromacs_cloned/share/top/.cp -R gromos53a6.ff  gromos53a6_lipid.ff

modify  gromos53a6_lipid.ff/ffnonbonded.itp

modify more ...

solvate
-------
wget http://www.mdtutorials.com/gmx/membrane_protein/Files/minim.mdp
wget http://www.mdtutorials.com/gmx/membrane_protein/Files/topol_dppc.top

run on WSL Notebook
~~~~~~~~~~~~~~~~~~~
/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi  grompp -f minim.mdp -c dppc128.pdb -p topol_dppc.top -o dppc.tpr

./home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi  grompp -f minim.mdp -c dppc128.pdb -p topol_dppc.top -o dppc.tpr
          :-) GROMACS - gmx grompp, 2027.0-dev-20251202-15e0cf6836 (-:

Executable:   /home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi
Data prefix:  /home/miroi/work/software/gromacs/gromacs_cloned (source tree)
Working dir:  /home/miroi/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Membrane_Protein/prepare_the_topology/modify_the_topology
Command line:
  gmx_mpi grompp -f minim.mdp -c dppc128.pdb -p topol_dppc.top -o dppc.tpr

Ignoring obsolete mdp entry 'ns_type'
Setting the LD random seed to 1878859761

Generated 915 of the 2346 non-bonded parameter combinations

ERROR 1 [file dppc.itp, line 112]:
  No default LJ-14 types for interaction
  '1     6     1'.


ERROR 2 [file dppc.itp, line 113]:
  No default LJ-14 types for interaction
  '2     6     1'.

... getting error ! needs further modifications
