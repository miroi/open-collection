========================================
GROMACS Tutorial Step Six: Equilibration
========================================

http://www.mdtutorials.com/gmx/lysozyme/06_equil.html

em.gro, topol.top from previous ../energy_minimization/ dir.

cp ../prepare_gro_file/posre.itp .

wget http://www.mdtutorials.com/gmx/lysozyme/Files/nvt.mdp

run
---
sbatch hydra_slurm_gromacs.01

new files:  nvt.edr, ...

temperature progression
-----------------------

MIRO Notebook Victus
~~~~~~~~~~~~~~~~~~~~
~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi  -h

~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi  energy -f nvt.edr -o temperature.xvg

16 0

