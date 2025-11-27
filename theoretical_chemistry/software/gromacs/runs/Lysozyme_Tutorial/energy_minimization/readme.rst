===================
Energy minimization
===================

http://www.mdtutorials.com/gmx/lysozyme/05_EM.html


wget http://www.mdtutorials.com/gmx/lysozyme/Files/minim.mdp


gmx_mpi grompp -f minim.mdp -c 1AKI_solv_ions.gro -p topol.top -o em.tpr > em.tpr_logfile  2>&1

generates binary "em.tpr" file

run
~~~
sbatch hydra_slurm_gromacs.01

to fix:
/zfs/scratch/HybriLITWorkshop2025/milias/software/gromacs/git_cloned/gromacs/build_intelmpi/bin/gmx_mpi -h :
MPI startup(): PMI server not found. Please set I_MPI_PMI_LIBRARY variable if it is not a singleton case.

see https://pm.jinr.ru/issues/10244


