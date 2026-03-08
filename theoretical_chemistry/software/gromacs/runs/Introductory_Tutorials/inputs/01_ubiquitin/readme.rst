=============================
Exercise 1: Protein in Water
=============================

following https://pubs.acs.org/doi/10.1021/acs.jpcb.4c04901 


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
