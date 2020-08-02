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

Script launch
-------------

./os_info.sh 
NAME="CentOS Linux"
VERSION="7 (Core)"
lxbk0595 3.10.0-1062.18.1.el7.x86_64


singularity exec $SINGULARITY_CONTAINERS/debian8.sif ./os_info.sh 
PRETTY_NAME="Debian GNU/Linux 8 (jessie)"
NAME="Debian GNU/Linux"
lxbk0595 3.10.0-1062.18.1.el7.x86_64

srun --partition=debug singularity exec  $SINGULARITY_CONTAINERS/debian8.sif ./os_info.sh 
PRETTY_NAME="Debian GNU/Linux 8 (jessie)"
NAME="Debian GNU/Linux"
lxbk0595 3.10.0-1062.18.1.el7.x86_64

