Singularity on Virgo
====================

singularity pull $SINGULARITY_CONTAINERS/gcc-10.1.0.sif docker://gcc:10.1.0
.
.
INFO:    Creating SIF file...
INFO:    Build complete: /lustre/ukt/milias/containers/gcc-10.1.0.sif

# start a shell within the container environment
singularity shell $SINGULARITY_CONTAINERS/gcc-10.1.0.sif




