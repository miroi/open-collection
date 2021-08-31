NWChem Singularity containers
=============================

https://nwchemgit.github.io/Containers.html

https://cloud.sylabs.io/library/_container/5f87980b84a01836e439c3da

Download
--------
singularity pull $SINGULARITY_CONTAINERS/nwchem-702.impi313.sif library://edoapra/default/nwchem-702.ompi313.ivybridge:sha256.cf4e2661f224ae6e5822756b4204f76e51c4eaaca71f7ac96a3a3a464d0b68d7

INFO:    Downloading library image
369.0MiB / 369.0MiB [==============================================================================] 100 % 9.0 MiB/s 0s
ilias@login1.kelinux.saske.sk:~/work/qch/projects/open-collection/computer_science/containers/kelinux_saske_sk/singularity/nwchem/.

Check
-----
singularity shell  $SINGULARITY_CONTAINERS/nwchem-702.impi313.sif
Singularity> which nwchem
/opt/nwchem-7.0.2/bin/LINUX64/nwchem
Singularity> ldd /opt/nwchem-7.0.2/bin/LINUX64/nwchem
        linux-vdso.so.1 (0x00007ffc2919a000)
        libmpi_mpifh.so.40 => /opt/ompi/lib/libmpi_mpifh.so.40 (0x00007fa998d72000)
        libmpi.so.40 => /opt/ompi/lib/libmpi.so.40 (0x00007fa998c66000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007fa998c56000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fa998c33000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007fa99896b000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fa99881c000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x00007fa9987ee000)
        libpython3.8.so.1.0 => /lib/x86_64-linux-gnu/libpython3.8.so.1.0 (0x00007fa998298000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fa9980a6000)
        libopen-pal.so.40 => /opt/ompi/lib/libopen-pal.so.40 (0x00007fa997fa4000)
        libopen-rte.so.40 => /opt/ompi/lib/libopen-rte.so.40 (0x00007fa997eea000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fa9a8080000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007fa997ea0000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fa997e83000)
        libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007fa997e55000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007fa997e39000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fa997e33000)
        libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007fa997e2e000)
Singularity> which mpirun
/opt/ompi/bin/mpirun


Run
---
Singularity> mpirun -np 3 nwchem h2o_scf_6-31g.nw 

singularity run $SINGULARITY_CONTAINERS/nwchem-702.impi313.sif mpirun -np 5 nwchem h2o_scf_6-31g.nw > out_4

