===================
Energy minimization
===================

http://www.mdtutorials.com/gmx/lysozyme/05_EM.html


wget http://www.mdtutorials.com/gmx/lysozyme/Files/minim.mdp


gmx_mpi grompp -f minim.mdp -c 1AKI_solv_ions.gro -p topol.top -o em.tpr > em.tpr_logfile  2>&1

generates binary "em.tpr" file

run intelmpi GROMACS
~~~~~~~~~~~~~~~~~~~~
sbatch hydra_slurm_gromacs.01

to fix:
/zfs/scratch/HybriLITWorkshop2025/milias/software/gromacs/git_cloned/gromacs/build_intelmpi/bin/gmx_mpi -h :
MPI startup(): PMI server not found. Please set I_MPI_PMI_LIBRARY variable if it is not a singleton case.

see https://pm.jinr.ru/issues/10244

Steepest Descents converged to Fmax < 1000 in 754 steps
Potential Energy  = -5.2632875e+05
Maximum force     =  9.5769556e+02 on atom 1958
Norm of force     =  2.0654620e+01

run openmpi GROMACS
~~~~~~~~~~~~~~~~~~~~
sbatch hydra_slurm_gromacs.02

Steepest Descents converged to Fmax < 1000 in 754 steps
Potential Energy  = -5.2640431e+05
Maximum force     =  8.8038019e+02 on atom 1958
Norm of force     =  2.0546556e+01

