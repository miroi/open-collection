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

ilias@login1.kelinux.saske.sk:~/work/qch/projects/open-collection/computer_science/containers/kelinux_saske_sk/singularity/nwchem/.singularity exec  $SINGULARITY_CONTAINERS/nwchem.sif /bin/sh

Singularity> ls
h2o_scf_6-31g.nw  out_error  readme.rst

Singularity> which nwchem
/opt/nwchem-7.0.2/bin/LINUX64/nwchem
Singularity> ldd /opt/nwchem-7.0.2/bin/LINUX64/nwchem
        linux-vdso.so.1 (0x00007ffe1d7e5000)
        libmpifort.so.12 => /usr/local/lib/libmpifort.so.12 (0x00007f172d526000)
        libmpi.so.12 => /usr/local/lib/libmpi.so.12 (0x00007f172d1cf000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f172d1c4000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f172d1a1000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007f172ced9000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f172cd8a000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x00007f172cd5c000)
        libpython3.8.so.1.0 => /lib/x86_64-linux-gnu/libpython3.8.so.1.0 (0x00007f172c806000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f172c614000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f172c5f9000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f173c853000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f172c5af000)
        libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007f172c57f000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f172c563000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f172c55d000)
        libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007f172c558000)
Singularity> 

