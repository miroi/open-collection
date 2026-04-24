===========
QE with ASE
===========

from Dip's /lustre/projects/d/dsen/2026_calcs/test/2/.

avoids srun: warning: can't honor --ntasks-per-node set to 4 which doesn't match the requested tasks 8 and -mpack, which forces min number of nodes to 1   
#SBATCH --distribution=block:block,nopack 

N1,n8    13.59s WALL ( oversubscription detected: 8 processes will be placed on 4 cores)
N2,n8    12.98s WALL ( oversubscription detected: 4 processes will be placed on 2 cores, n05p027 , n05p028)
N2,n4    25.77s WALL
N1,n4    25.77s WALL

