==================================
Gromacs test run LYSOZYME Tutorial
==================================

http://www.mdtutorials.com/gmx/lysozyme/01_pdb2gmx.html

https://www.rcsb.org/structure/1AKI

..visualize the structure using a viewing program such as VMD, Chimera, PyMOL, etc.

modules
~~~~~~~
module add GROMACS/v2024.3

module list

Currently Loaded Modulefiles:
  1) GVR/v1.0-1               3) gcc/v12.3.0              5) cuda/v12.1               7) GROMACS/v2024.3
  2) BASE/1.0                 4) openmpi/v5.0.3_gcc1230   6) Python/v3.10.13


gmx_mpi pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water tip3p   > 1AKI_processed.gro_logfile 2>&1


removing water molecules
~~~~~~~~~~~~~~~~~~~~~~~~

..strip out the crystal waters:

grep -v HOH 1AKI.pdb > 1AKI_clean.pdb 

process gromacs
~~~~~~~~~~~~~~~
gmx_mpi pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water tip3p 

picked 9 ... all-atom CHARMM36 force field,

rather picked 2 ... 2: AMBER94 force field (Cornell et al., JACS 117, 5179-5197, 1995)

generates topol.top file



saved into pdb2gmx.logfile

define the box
~~~~~~~~~~~~~~~
gmx_mpi editconf -f 1AKI_processed.gro -o 1AKI_newbox.gro -c -d 1.0 -bt cubic  > 1AKI_newbox.gro_logfile 2>&1

solvation
~~~~~~~~~
gmx_mpi solvate -cp 1AKI_newbox.gro -cs spc216.gro -o 1AKI_solv.gro -p topol.top > 1AKI_solv.gro_logfile 2>&1

adding ions
~~~~~~~~~~~

GMXLIB/share/gromacs/top
export GMXLIB=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/GROMACS/v2024.3
export PATH=$GMXLIB/share/gromacs/top:$PATH
less /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/GROMACS/v2024.3/share/gromacs/top/gromos43a1.ff/tip3p.itp
echo $GMXLIB
less $GMXLIB/share/gromacs/top/gromos43a1.ff/tip3p.itp
ln -sf $GMXLIB/share/gromacs/top/gromos43a1.ff .

download ions: wget http://www.mdtutorials.com/gmx/lysozyme/Files/ions.mdp

gmx_mpi grompp -f ions.mdp -c 1AKI_solv.gro -p topol.top -o ions.tpr > ions.tpr_logfile 2>&1

ERROR 1 [file tip3p.itp, line 8]:
  Atomtype HW not found ... FIX: use amber94 force field

gmx_mpi  genion -s ions.tpr -o 1AKI_solv_ions.gro -p topol.top -pname NA -nname CL -neutral > 1AKI_solv_ions.gro_logfile   2>&1


