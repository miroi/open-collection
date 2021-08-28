Singularity on kelinux cluster
==============================

see https://github.com/lammps/lammps/issues/2877#issuecomment-898982740:
 "docker pull lammps/lammps:patch_8Apr2021_ubuntu20.04_openmpi_py3"

ilias@login1.kelinux.saske.sk:~/work/qch/projects/open-collection/computer_science/containers/kelinux_saske_sk/singularity/.singularity pull $SINGULARITY_CONTAINERS/lammps.sif docker://lammps/lammps:patch_8Apr2021_ubuntu20.04_openmpi_py3
INFO:    Converting OCI blobs to SIF format
INFO:    Starting build...
Getting image source signatures
Copying blob 345e3491a907 done  
Copying blob 57671312ef6f done  
Copying blob 5e9250ddb7d0 done  
Copying blob 91be876641b1 done  
Copying blob 85ffa4edf58a done  
Copying blob ecfac003439d done  
Copying blob 5ab64a109241 done  
Copying blob 6f997b823e69 done  
Copying blob 484626fccd96 done  
Copying blob 423c1ac3935b done  
Copying blob df2bb51d4a7c done  
Copying blob 17fe427ace9d done  
Copying blob 4e120ce0ba44 done  
Copying blob ff0d0caf0de2 done  
Copying blob 16f002004578 done  
Copying blob e4a586f05aff done  
Copying config 8b7b0f8f7d done  
Writing manifest to image destination
Storing signatures
2021/08/15 10:38:10  info unpack layer: sha256:345e3491a907bb7c6f1bdddcf4a94284b8b6ddd77eb7d93f09432b17b20f2bbe
2021/08/15 10:38:11  warn xattr{etc/gshadow} ignoring ENOTSUP on setxattr "user.rootlesscontainers"
2021/08/15 10:38:11  warn xattr{/lustre/home/ilias/containers/tmp/build-temp-226229579/rootfs/etc/gshadow} destination filesystem does not support xattrs, further warnings will be suppressed
2021/08/15 10:42:54  info unpack layer: sha256:484626fccd96a0a0fe100dbde26ed894613c142ea781aa6117caac948cbae850
2021/08/15 10:42:54  info unpack layer: sha256:423c1ac3935bad06efb026ca45d55ff63c1051c05d706a00f9b35cf5abb52b93
2021/08/15 10:42:55  info unpack layer: sha256:df2bb51d4a7cf735528d3162051909a28f8248c1b5e65c1a6b1d150bbe7858c6
2021/08/15 10:43:00  info unpack layer: sha256:17fe427ace9d87b5552971ac531dac41fd598e26ddd4cf86d68e0a061ae68092
2021/08/15 10:43:01  info unpack layer: sha256:4e120ce0ba44ca6904330ca5b66553220ff5dc9af60b0e3b9bf896ed3a10eea4
2021/08/15 10:43:01  info unpack layer: sha256:ff0d0caf0de2184f97dc2ef7afe749a2c70928e02eca5425be965b01916b354c
2021/08/15 10:43:02  info unpack layer: sha256:16f0020045787fc76f37251b80243aa571225d5b9f91deaf894b8ae7d52d9ea6
2021/08/15 10:43:02  info unpack layer: sha256:e4a586f05affdb32dc3f62c01d776a2466a3f7f607714050b54a7a3d6eb98ecd
2021/08/15 10:43:02  warn xattr{usr/local/lib/python3.8} ignoring ENOTSUP on setxattr "user.rootlesscontainers"
2021/08/15 10:43:02  warn xattr{/lustre/home/ilias/containers/tmp/build-temp-226229579/rootfs/usr/local/lib/python3.8} destination filesystem does not support xattrs, further warnings will be suppressed
INFO:    Creating SIF file...
ilias@login1.kelinux.saske.sk:~/work/qch/projects/open-collection/computer_science/containers/kelinux_saske_sk/singularity/.


ilias@login1.kelinux.saske.sk:~/work/qch/projects/open-collection/computer_science/containers/kelinux_saske_sk/singularity/lammps_software/.singularity run  $SINGULARITY_CONTAINERS/lammps.sif 
LAMMPS (8 Apr 2021)
OMP_NUM_THREADS environment is not set. Defaulting to 1 thread. (src/comm.cpp:94)
  using 1 OpenMP thread(s) per MPI task



