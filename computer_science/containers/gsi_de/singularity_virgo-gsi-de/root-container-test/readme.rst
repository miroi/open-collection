Singularity on Virgo
====================

https://hpc.gsi.de/virgo/#singularity-containers

singularity pull $SINGULARITY_CONTAINERS/root.sif docker://rootproject/root
.
.
INFO:    Creating SIF file...
INFO:    Build complete: /lustre/ukt/milias/containers/root.sif


singularity exec $SINGULARITY_CONTAINERS/root.sif g++ --version

singularity exec $SINGULARITY_CONTAINERS/root.sif g++ ./hello_world.cpp -o hello_world

