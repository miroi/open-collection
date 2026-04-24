===========
QE with ASE
===========

from Dip's /lustre/projects/d/dsen/2026_calcs/test/2/.

avoids srun: warning: can't honor --ntasks-per-node set to 4 which doesn't match the requested tasks 8 and -mpack, which forces min number of nodes to 1   
#SBATCH --distribution=block:block,nopack 

N2,n12   9.64s WALL  ( oversubscription detected: 10 processes will be placed on 5 cores, 2 processes will be placed on 1 cores)
N4,n8    12.73s WALL ( oversubscription detected: 2 processes will be placed on 1 cores, on 4 nodes)
N2,n8    12.98s WALL ( oversubscription detected: 4 processes will be placed on 2 cores, on 2 nodes)
N1,n8    13.59s WALL ( oversubscription detected: 8 processes will be placed on 4 cores, on 1 node)
N2,n4    25.77s WALL ( oversubscription detected: 2 processes will be placed on 1 cores, on 2 nodes)
N1,n4    25.77s WALL (  oversubscription detected: 4 processes will be placed on 2 cores, on 1 node  )

only physical CPUs

N2,n8    10.93s WALL
