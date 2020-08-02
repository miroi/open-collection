======================================
Singularity on Virgo: debian container
======================================

singularity pull $SINGULARITY_CONTAINERS/debian8.sif docker://debian:8
.
.
.
INFO:    Creating SIF file...
INFO:    Build complete: /lustre/ukt/milias/containers/debian8.sif


# .. access the GSI IT departments CVMFS repository
singularity exec --bind /cvmfs $SINGULARITY_CONTAINERS/debian8.sif ls -l /cvmfs/it.gsi.de
