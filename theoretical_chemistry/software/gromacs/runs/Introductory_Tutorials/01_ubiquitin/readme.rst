=============================
Exercise 1: Protein in Water
=============================

following https://pubs.acs.org/doi/10.1021/acs.jpcb.4c04901 

Prepare the Protein Topology
----------------------------

export PATH=/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin:$PATH

gmx pdb2gmx -f 1UBQ.pdb -o ubiquitin.gro

gmx pdb2gmx -f 1UBQ.pdb -o ubiquitin.gro > gmx_pdb2gmx.logfile 2>&1
8
1

Upon completion of pdb2gmx, the user will have the following files in the working directory:
1.	ubiquitin.gro: a force field-compliant structure that is protonated according to the assumptions described above.
2.	topol.top: the topology of the protein, and in this case, the crystallographic water molecules.
3.	posre.itp: an auxiliary topology file that specifies atoms that are restrained by default and their force constants. This file and its use will be discussed in detail later.

Define the Periodic Cell and Add Solvent
----------------------------------------

gmx editconf -f ubiquitin.gro -o box.gro -c -d 1.2 -bt dodecahedron > gmx_editconf.logfile 2>&1

gmx solvate -cp box.gro -cs spc216.gro -o solv.gro -p topol.top > gms_solvate.logfile  2>&1

add ions (100 mM NaCl)
~~~~~~~~~~~~~~~~~~~~~~
gmx grompp -f inputs/ions.mdp  -c solv.gro  -p topol.top -o ions.tpr > gmx_grompp.logfile 2>&1  

choose group 13 (SQL) to replace water molecules with ions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname NA -nname CL -conc 0.1 > gmx_genion.logfile 2>&1
13

rewrapp unit cell
~~~~~~~~~~~~~~~~~
gmx grompp -f inputs/ions.mdp -c solv_ions.gro -p topol.top -o wrap.tpr > gmx_grompp.logfile 2>&1

gmx trjconv -s wrap.tpr -f solve_ions.gro -o rewrap.gro -pbc mol -ur compact > gmx_trjconv.logfile 2>&1


Perform Energy Minimization
---------------------------


