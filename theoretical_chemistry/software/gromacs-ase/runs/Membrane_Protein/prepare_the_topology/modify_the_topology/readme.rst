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

solution:
https://github.com/fuentesdt/MembraneProtein

wget https://raw.githubusercontent.com/fuentesdt/MembraneProtein/refs/heads/master/dppc128.pdb
wget https://raw.githubusercontent.com/fuentesdt/MembraneProtein/refs/heads/master/dppc.itp
wget https://github.com/fuentesdt/MembraneProtein/blob/master/lipid.itp

miroi@MIRO:~/work/software/gromacs/gromacs_cloned/share/top/.cp -R gromos53a6.ff  gromos53a6_lipid.ff

modify  gromos53a6_lipid.ff/ffnonbonded.itp

modify topol.top

