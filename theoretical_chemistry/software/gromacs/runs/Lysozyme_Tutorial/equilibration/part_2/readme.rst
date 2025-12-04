=====================
Equilibration, Part 2
=====================

http://www.mdtutorials.com/gmx/lysozyme/07_equil2.html

wget http://www.mdtutorials.com/gmx/lysozyme/Files/npt.mdp

 ~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi grompp -f npt.mdp -c ../nvt.gro -r ../nvt.gro -t ../nvt.cpt -p ../topol.top -o npt.tpr 

log in npt.tpr_logfile


run
---
 ~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi  mdrun -deffnm npt 

remote: warning: File theoretical_chemistry/software/gromacs/runs/Lysozyme_Tutorial/equilibration/part_2/npt.trr is 78.32 MB; this is larger than GitHub's recommended maximum file size of 50.00 MB

pressure progression analysis
-----------------------------

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Lysozyme_Tutorial/equilibration/part_2/.~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi energy -f npt.edr -o pressure.xvg
18 0

output harvested into  pressure.xvg_logfile


