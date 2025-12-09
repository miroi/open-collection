=========================
Step Eight: Production MD
=========================

http://www.mdtutorials.com/gmx/lysozyme/08_MD.html

wget http://www.mdtutorials.com/gmx/lysozyme/Files/md.mdp


prepare tpr file
----------------
~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi -h

~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi grompp -f  md.mdp  -c ../equilibration/part_2/npt.gro  -t ../equilibration/part_2/npt.cpt  -p ../equilibration/topol.top  -o md_0_10.tpr

...output harvested into  md_0_10.tpr_logfile

execute mdrun
-------------

~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi mdrun -deffnm md_0_10

... output harvested into md_0_10.SAVED

DesktopPC
~~~~~~~~~
/home/milias/work/software/gromacs/cloned/gromacs/build_gnu/bin/gmx_mpi -h

milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Lysozyme_Tutorial/production_md/./home/milias/work/software/gromacs/cloned/gromacs/build_gnu/bin/gmx_mpi help commands

ilias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Lysozyme_Tutorial/production_md/./home/milias/work/software/gromacs/cloned/gromacs/build_gnu/bin/gmx_mpi  mdrun -deffnm md_0_10

          :-) GROMACS - gmx mdrun, 2027.0-dev-20251202-15e0cf6836 (-:

Executable:   /home/milias/work/software/gromacs/cloned/gromacs/build_gnu/bin/gmx_mpi
Data prefix:  /home/milias/work/software/gromacs/cloned/gromacs (source tree)
Working dir:  /home/milias/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Lysozyme_Tutorial/production_md
Command line:
  gmx_mpi mdrun -deffnm md_0_10

Reading file md_0_10.tpr, VERSION 2026.0-dev-20251031-ee5fdd7dba (single precision)
Changing nstlist from 10 to 50, rlist from 1 to 1.107

Using 1 MPI process
Using 20 OpenMP threads
.
.




