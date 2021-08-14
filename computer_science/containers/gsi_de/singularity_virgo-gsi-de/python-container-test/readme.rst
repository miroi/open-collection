Singularity on Virgo
====================

# download the latest version of a Python container from DockerHub
singularity pull $SINGULARITY_CONTAINERS/python.sif docker://python:latest

milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/projects/open-collection/computer_science/containers/gsi_de/singularity_virgo-gsi-de/python-container-test/.singularity pull $SINGULARITY_CONTAINERS/python.sif docker://python:latest

ls /lustre/ukt/milias/containers/python.sif 

singularity exec $SINGULARITY_CONTAINERS/python.sif python --version
Python 3.8.5

milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/projects/open-collection/computer_science/containers/gsi_de/singularity_virgo-gsi-de/python-container-test/.singularity exec   $SINGULARITY_CONTAINERS/python.sif ./hello_world.py
hello world !

Own SBATCH file
---------------
sbatch virgo_slurm.01
