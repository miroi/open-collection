===================
Energy minimization
===================

http://www.mdtutorials.com/gmx/lysozyme/05_EM.html


wget http://www.mdtutorials.com/gmx/lysozyme/Files/minim.mdp


gmx_mpi grompp -f minim.mdp -c 1AKI_solv_ions.gro -p topol.top -o em.tpr > em.tpr_logfile  2>&1

generates binary "em.tpr" file


