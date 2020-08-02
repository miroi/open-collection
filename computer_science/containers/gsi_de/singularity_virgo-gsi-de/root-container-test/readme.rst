Singularity on Virgo
====================

https://hpc.gsi.de/virgo/#singularity-containers

singularity pull $SINGULARITY_CONTAINERS/root.sif docker://rootproject/root

singularity exec $SINGULARITY_CONTAINERS/root.sif g++ --version
