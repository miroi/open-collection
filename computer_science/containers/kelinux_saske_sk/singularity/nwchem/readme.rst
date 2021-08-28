NWCHem in container
===================

Download
---------
https://hub.docker.com/r/nwchemorg/nwchem-702.mpipr.nersc

ilias@login1.kelinux.saske.sk:~/work/qch/projects/open-collection/computer_science/containers/kelinux_saske_sk/singularity/nwchem/.singularity pull $SINGULARITY_CONTAINERS/nwchem.sif docker://nwchemorg/nwchem-702.mpipr.nersc
.
.
2021/08/28 18:07:53  info unpack layer: sha256:cadb02169db62b58185ae002dac457bd0e7ebdf79468ef6c5a13db393b5e87a8
INFO:    Creating SIF file...


Runs
----
ilias@login1.kelinux.saske.sk:~/work/qch/projects/open-collection/computer_science/containers/kelinux_saske_sk/singularity/nwchem/.singularity run $SINGULARITY_CONTAINERS/nwchem.sif h2o_scf_6-31g.nw > out

Program received signal SIGILL: Illegal instruction.

Backtrace for this error:
#0  0x7fc30820fd01 in ???
#1  0x7fc30820eed5 in ???
#2  0x7fc30797020f in ???
#3  0x5618fb0c15ef in ???

