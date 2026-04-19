===========
QE with ASE
===========

from Dip's /lustre/projects/d/dsen/2026_calcs/test/2/.


This:
~~~~~
#SBATCH --distribution=block:block,nopack 

avoids srun: warning: can't honor --ntasks-per-node set to 4 which doesn't match the requested tasks 8 and -mpack, which forces min number of nodes to 1   
