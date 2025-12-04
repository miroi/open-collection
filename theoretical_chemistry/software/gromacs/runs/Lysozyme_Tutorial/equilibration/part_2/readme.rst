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



