NWCHem in container
===================

Download
---------

milias@adf2:~/work/projects/open-collection/computer_science/containers/umb_sk/adf2_umb_sk/singularity/nwchem/.singularity pull $SINGULARITY_CONTAINERS/nwchem.sif docker://nwchemorg/nwchem-702.mpipr.nersc
INFO:    Converting OCI blobs to SIF format
INFO:    Starting build...
.
.
2021/08/29 12:40:42  info unpack layer: sha256:cadb02169db62b58185ae002dac457bd0e7ebdf79468ef6c5a13db393b5e87a8
INFO:    Creating SIF file...


Runs
----
milias@adf2:~/work/projects/open-collection/computer_science/containers/umb_sk/adf2_umb_sk/singularity/nwchem/.singularity run $SINGULARITY_CONTAINERS/nwchem.sif h2o_scf_6-31g.nw > out


Problem: https://github.com/nwchemgit/nwchem-dockerfiles/issues/13


