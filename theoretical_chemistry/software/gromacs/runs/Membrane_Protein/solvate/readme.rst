===================================================
Step Three: Defining the Unit Cell & Adding Solvent
===================================================

solvate
-------
wget http://www.mdtutorials.com/gmx/membrane_protein/Files/minim.mdp
wget http://www.mdtutorials.com/gmx/membrane_protein/Files/topol_dppc.top


/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi  grompp -maxwarn 1 -f  minim.mdp -c  ../prepare_the_topology/modify_the_topology/dppc128.pdb -p topol_dppc.top -o dppc.tpr

..output harvested into  dppc.tpr_logfile

trjconv to remove periodicity
------------------------------
/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi trjconv -s dppc.tpr -f ../prepare_the_topology/modify_the_topology/dppc128.pdb -o dppc128_whole.gro -pbc mol -ur compact

..output harvested into  dppc128_whole.gro_logfile
