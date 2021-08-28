Theoretical chemistry containers - NWChem
===========================================

About
------
https://hub.docker.com/r/nwchemorg/nwchem-702.mpipr.nersc
see https://github.com/nwchemgit/nwchem-dockerfiles/issues/10

Download
---------
singularity pull $SINGULARITY_CONTAINERS/nwchem.sif  docker://nwchemorg/nwchem-702.mpipr.nersc

milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/projects/open-collection/computer_science/containers/gsi_de/singularity_virgo-gsi-de/theoretical_chemistry_containers/nwchem/.singularity pull -F  $SINGULARITY_CONTAINERS/nwchem.sif  docker://nwchemorg/nwchem-702.mpipr.nersc
INFO:    Using cached SIF image

Usage
-----
singularity run $SINGULARITY_CONTAINERS/nwchem.sif h2o_scf_6-31g.nw > out

or SBATCH script ...


