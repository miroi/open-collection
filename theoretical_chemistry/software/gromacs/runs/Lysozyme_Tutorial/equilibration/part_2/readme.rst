=====================
Equilibration, Part 2
=====================

http://www.mdtutorials.com/gmx/lysozyme/07_equil2.html

wget http://www.mdtutorials.com/gmx/lysozyme/Files/npt.mdp

 ~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi grompp -f npt.mdp -c ../nvt.gro -r ../nvt.gro -t ../nvt.cpt -p ../topol.top -o npt.tpr 

log in npt.tpr_logfile


run
---
 ~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi  mdrun -deffnm npt > npt.logfile  

          :-) GROMACS - gmx mdrun, 2026.0-dev-20251031-ee5fdd7dba (-:

Executable:   /home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi
Data prefix:  /home/miroi/work/software/gromacs/gromacs_cloned (source tree)
Working dir:  /home/miroi/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Lysozyme_Tutorial/equilibration/part_2
Command line:
  gmx_mpi mdrun -deffnm npt

Reading file npt.tpr, VERSION 2026.0-dev-20251031-ee5fdd7dba (single precision)
Changing nstlist from 10 to 50, rlist from 1 to 1.107

Using 1 MPI process
Using 12 OpenMP threads

starting mdrun 'LYSOZYME in water'
50000 steps,    100.0 ps.

Writing final coordinates.

               Core t (s)   Wall t (s)        (%)
       Time:     4654.942      387.913     1200.0
                 (ns/day)    (hour/ns)    (ms/step)  (Matom*steps/s)
Performance:       22.273        1.078        7.758            4.367

GROMACS reminds you: "You Got to Relate to It" (A.E. Torda)


