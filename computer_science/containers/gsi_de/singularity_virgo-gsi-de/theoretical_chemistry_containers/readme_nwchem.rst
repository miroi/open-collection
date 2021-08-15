Theoretical chemistry containers
================================

https://hub.docker.com/r/nwchemorg/nwchem-702.mpipr.nersc

singularity pull $SINGULARITY_CONTAINERS/nwchem.sif  docker://nwchemorg/nwchem-702.mpipr.nersc

INFO:    Converting OCI blobs to SIF format
WARNING: 'nodev' mount option set on /lustre, it could be a source of failure during build process
INFO:    Starting build...
Getting image source signatures
Copying blob a70d879fa598 done  
Copying blob c4394a92d1f8 done  
Copying blob 10e6159c56c0 done  
Copying blob 6e0504f0a452 done  
Copying blob 035e55ce1439 done  
Copying blob 486fb39bdcb7 done  
Copying blob 599392ec553d done  
Copying blob cadb02169db6 done  
Copying config 62e5699f78 done  
Writing manifest to image destination
Storing signatures
2021/08/14 22:18:39  info unpack layer: sha256:a70d879fa5984474288d52009479054b8bb2993de2a1859f43b5480600cecb24
2021/08/14 22:18:40  warn xattr{etc/gshadow} ignoring ENOTSUP on setxattr "user.rootlesscontainers"
2021/08/14 22:18:40  warn xattr{/lustre/ukt/milias/containers/tmp/build-temp-430410332/rootfs/etc/gshadow} destination filesystem does not support xattrs, further warnings will be suppressed
2021/08/14 22:22:09  info unpack layer: sha256:c4394a92d1f8760cf7d17fee0bcee732c94c5b858dd8d19c7ff02beecf3b4e83
2021/08/14 22:22:10  info unpack layer: sha256:10e6159c56c084c858f5de2416454ac0a49ddda47b764e4379c5d5a147c9bf5f
2021/08/14 22:22:10  info unpack layer: sha256:6e0504f0a45214c9fab9229abafb38563f2323d235c3ce6c4bf46acca9ee6c13
2021/08/14 22:22:10  warn xattr{etc/gshadow} ignoring ENOTSUP on setxattr "user.rootlesscontainers"
2021/08/14 22:22:10  warn xattr{/lustre/ukt/milias/containers/tmp/build-temp-430410332/rootfs/etc/gshadow} destination filesystem does not support xattrs, further warnings will be suppressed
2021/08/14 22:35:13  info unpack layer: sha256:035e55ce1439bde34e2dddc89d0cb1494b3a55dcd3f41348b716137064b6c015
2021/08/14 22:36:22  info unpack layer: sha256:486fb39bdcb7e60f20111ab127d157bca4c804f520811644b0ef17dc721b6e52
2021/08/14 22:36:22  warn xattr{opt/nwchem-7.0.2/INSTALL} ignoring ENOTSUP on setxattr "user.rootlesscontainers"
2021/08/14 22:36:22  warn xattr{/lustre/ukt/milias/containers/tmp/build-temp-430410332/rootfs/opt/nwchem-7.0.2/INSTALL} destination filesystem does not support xattrs, further warnings will be suppressed

2021/08/14 23:13:22  info unpack layer: sha256:599392ec553daa1b782b105f6e33632a95995dee5daa6d9259418f32c4531a20
2021/08/14 23:13:25  warn xattr{var/cache/apt/archives/partial} ignoring ENOTSUP on setxattr "user.rootlesscontainers"
2021/08/14 23:13:25  warn xattr{/lustre/ukt/milias/containers/tmp/build-temp-430410332/rootfs/var/cache/apt/archives/partial} destination filesystem does not support xattrs, further warnings will be suppressed
2021/08/14 23:13:25  info unpack layer: sha256:cadb02169db62b58185ae002dac457bd0e7ebdf79468ef6c5a13db393b5e87a8
INFO:    Creating SIF file...

