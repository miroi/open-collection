=============================
Exercise 1: Protein in Water
=============================

following https://pubs.acs.org/doi/10.1021/acs.jpcb.4c04901 

add charmm36 ff
~~~~~~~~~~~~~~~
https://mackerell.umaryland.edu/charmm_ff.shtml#gromacs
miroi@MIRO:~/work/software/gromacs/gromacs_cloned/share/top/.mv /mnt/c/Users/miroi/Downloads/charmm36-feb2026_cgenff-5.0.ff .
miroi@MIRO:~/work/software/gromacs/gromacs_cloned/share/top/charmm36.ff/.chmod ugo-x *

miroi@MIRO:~/work/software/gromacs/gromacs_cloned/share/top/charmm36.ff/.ls
aminoacids.arn    carb.hdb      cgenff.rtp                       ffbonded.itp            lipid.n.tdb   na.c.tdb         silicates.n.tdb  spc.itp
aminoacids.c.tdb  carb.n.tdb    charmm36-feb2026_cgenff-5.0.ff/  ffmissingdihedrals.itp  lipid.r2b     na.hdb           silicates.r2b    spce.itp
aminoacids.hdb    carb.r2b      cmap.itp                         ffnonbonded.itp         lipid.rtp     na.n.tdb         silicates.rtp    tip3p.itp
aminoacids.n.tdb  carb.rtp      ethers.c.tdb                     forcefield.doc          metals.c.tdb  na.r2b           solvent.c.tdb    tip3p_original.itp
aminoacids.r2b    cgenff.c.tdb  ethers.hdb                       forcefield.itp          metals.hdb    na.rtp           solvent.hdb      tip4p.itp
aminoacids.rtp    cgenff.hdb    ethers.n.tdb                     ions.itp                metals.n.tdb  nbfix.itp        solvent.n.tdb    tip4pew.itp
atomtypes.atp     cgenff.n.tdb  ethers.r2b                       lipid.c.tdb             metals.r2b    silicates.c.tdb  solvent.r2b      tip5p.itp
carb.c.tdb        cgenff.r2b    ethers.rtp                       lipid.hdb               metals.rtp    silicates.hdb    solvent.rtp      watermodels.dat

to ~/work/software/gromacs/gromacs_cloned/share/top/charmm36.ff/forcefield.doc : modified the first line "CHARMM36 all-atom force field, charmm36-feb2026_cgenff-5.0.ff"

BUT, error : https://github.com/Lemkul-Lab/gmx_tutorials_jpcb/issues/2

  1UBQ.pdb is the same in web database

Prepare the Protein Topology
----------------------------

export PATH=/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin:$PATH

gmx pdb2gmx -f 1UBQ.pdb -o ubiquitin.gro

gmx pdb2gmx -f 1UBQ.pdb -o ubiquitin.gro > gmx_pdb2gmx.logfile 2>&1
8
1

better:
~~~~~~~
gmx pdb2gmx -f 1UBQ.pdb -o ubiquitin.gro -ter -missing
9: CHARMM36 all-atom force field, charmm36-feb2026_cgenff-5.0.ff
1

NH3+ start, COO- end terminus



Upon completion of pdb2gmx, the user will have the following files in the working directory:
1.	ubiquitin.gro: a force field-compliant structure that is protonated according to the assumptions described above.
2.	topol.top: the topology of the protein, and in this case, the crystallographic water molecules.
3.	posre.itp: an auxiliary topology file that specifies atoms that are restrained by default and their force constants. This file and its use will be discussed in detail later.

Define the Periodic Cell and Add Solvent
----------------------------------------

gmx editconf -f ubiquitin.gro -o box.gro -c -d 1.2 -bt dodecahedron 
gmx editconf -f ubiquitin.gro -o box.gro -c -d 1.2 -bt dodecahedron > gmx_editconf.logfile 2>&1

gmx solvate -cp box.gro -cs spc216.gro -o solv.gro -p topol.top 
gmx solvate -cp box.gro -cs spc216.gro -o solv.gro -p topol.top > gms_solvate.logfile  2>&1

add ions (100 mM NaCl)
~~~~~~~~~~~~~~~~~~~~~~
gmx grompp -f inputs/ions.mdp  -c solv.gro  -p topol.top -o ions.tpr 
gmx grompp -f inputs/ions.mdp  -c solv.gro  -p topol.top -o ions.tpr > gmx_grompp.logfile 2>&1  

choose group 13 (SQL) to replace water molecules with ions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname NA -nname CL -conc 0.1 
gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname NA -nname CL -conc 0.1 > gmx_genion.logfile 2>&1
13

rewrapp unit cell
~~~~~~~~~~~~~~~~~
gmx grompp -f inputs/ions.mdp -c solv_ions.gro -p topol.top -o wrap.tpr > gmx_grompp2.logfile 2>&1

gmx trjconv -s wrap.tpr -f solve_ions.gro -o rewrap.gro -pbc mol -ur compact > gmx_trjconv.logfile 2>&1


Perform Energy Minimization
---------------------------


