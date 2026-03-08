=============================
Exercise 1: Protein in Water
=============================

following https://pubs.acs.org/doi/10.1021/acs.jpcb.4c04901 

Prepare the Protein Topology
----------------------------

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Introductory_Tutorials/inputs/01_ubiquitin/.gmx pdb2gmx -f 1UBQ.pdb -o ubiquitin.gro

8: CHARMM27 all-atom force field (CHARM22 plus CMAP for proteins)

 1: TIP3P   TIP 3-point, recommended


You have successfully generated a topology from: 1UBQ.pdb.

The Charmm27 force field and the tip3p water model are used.

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Introductory_Tutorials/inputs/01_ubiquitin/.ls
1UBQ.pdb  free_ener_plot/  inputs/  posre.itp  readme.rst  topol.top  ubiquitin.gro

        posre.itp
        topol.top
        ubiquitin.gro

Upon completion of pdb2gmx, the user will have the following files in the working directory:
1.	ubiquitin.gro: a force field-compliant structure that is protonated according to the assumptions described above.
2.	topol.top: the topology of the protein, and in this case, the crystallographic water molecules.
3.	posre.itp: an auxiliary topology file that specifies atoms that are restrained by default and their force constants. This file and its use will be discussed in detail later.

Define the Periodic Cell and Add Solvent
----------------------------------------

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Introductory_Tutorials/inputs/01_ubiquitin/.gmx editconf -f ubiquitin.gro -o box.gro -c -d 1.2 -bt dodecahedron > gmx_editconf.logfile 2>&1

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Introductory_Tutorials/inputs/01_ubiquitin/.gmx solvate -cp box.gro -casxx spc216.gro -o solv.gro -p topol.top > gms_solvate.logfile  2>&1

add ions (100 mM NaCl)
~~~~~~~~~~~~~~~~~~~~~~
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Introductory_Tutorials/inputs/01_ubiquitin/.gmx grompp -f inputs/ions.mdp  -c solv.gro  -p topol.top -o ions.tpr > gmx_grompp.logfile 2>&1  FIX ERROR...

choose group 13 (SQL) to replace water molecules with ions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Introductory_Tutorials/inputs/01_ubiquitin/.gmx genion -s ions.trp -o solv_ions.gro -p topol.tio -pname NA -nname CL -conc 0.1 > gmx_genion.logfile 2>&1







