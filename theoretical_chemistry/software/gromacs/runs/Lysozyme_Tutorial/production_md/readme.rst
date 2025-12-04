=========================
Step Eight: Production MD
=========================

http://www.mdtutorials.com/gmx/lysozyme/08_MD.html

wget http://www.mdtutorials.com/gmx/lysozyme/Files/md.mdp


~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi -h

~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi grompp -f  md.mdp  -c ../equilibration/part_2/npt.gro  -t ../equilibration/part_2/npt.cpt  -p ../equilibration/topol.top  -o md_0_10.tpr





