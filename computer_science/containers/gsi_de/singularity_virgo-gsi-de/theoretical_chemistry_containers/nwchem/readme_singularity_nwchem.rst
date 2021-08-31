NWChem Singularity containers
=============================

https://nwchemgit.github.io/Containers.html

https://cloud.sylabs.io/library/_container/5f87980b84a01836e439c3da

Download
--------

milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/projects/open-collection/computer_science/containers/gsi_de/singularity_virgo-gsi-de/theoretical_chemistry_containers/nwchem/.singularity pull library://edoapra/default/nwchem-702.ompi313.ivybridge:sha256.cf4e2661f224ae6e5822756b4204f76e51c4eaaca71f7ac96a3a3a464d0b68d7 
INFO:    Downloading library image
369.0MiB / 369.0MiB [============================================================================] 100 % 18.4 MiB/s 0s

in home dir is: 
nwchem-702.ompi313.ivybridge_sha256.cf4e2661f224ae6e5822756b4204f76e51c4eaaca71f7ac96a3a3a464d0b68d7.sif

Running
-------

singularity shell nwchem-702.ompi313.ivybridge_sha256.cf4e2661f224ae6e5822756b4204f76e51c4eaaca71f7ac96a3a3a464d0b68d7.sif

Singularity> mpirun -np 5 nwchem h2o_scf_6-31g.nw > out  # out is with 4 CPUs

singularity run ./nwchem-702.ompi313.ivybridge_sha256.cf4e2661f
224ae6e5822756b4204f76e51c4eaaca71f7ac96a3a3a464d0b68d7.sif  mpirun -np 5 nwchem h2o_scf_6-31g.nw > out_4

Better download
---------------
singularity pull $SINGULARITY_CONTAINERS/nwchem-702.impi313.sif
   library://edoapra/default/nwchem-702.ompi313.ivybridge:sha256.cf4e2661f224ae6e5822756b4204f76e51c4eaaca71f7ac96a3a3a464d0b68d7 



