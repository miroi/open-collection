Singularity container
=====================

See https://sylabs.io/guides/2.6/user-guide/quick_start.html

milias@lxbk0200.gsi.de:~/Work/qch/projects/miro_ilias_qch_systems/gsi_singularity/.singularity pull shub://vsoch/hello-world 
Progress |===================================| 100.0% 
Done. Container is at: /u/milias/Work/qch/projects/miro_ilias_qch_systems/gsi_singularity/vsoch-hello-world-master-latest.simg
milias@lxbk0200.gsi.de:~/Work/qch/projects/miro_ilias_qch_systems/gsi_singularity/.du -h -s .
65M	.
milias@lxbk0200.gsi.de:~/Work/qch/projects/miro_ilias_qch_systems/gsi_singularity/.ls -lt
total 65540
-rwxr-xr-x 1 milias kc 62652447 Aug 19 13:45 vsoch-hello-world-master-latest.simg*
-rw-r--r-- 1 milias kc      103 Aug 19 13:34 readme.rst



milias@lxbk0200.gsi.de:~/Work/qch/projects/miro_ilias_qch_systems/gsi_singularity/.singularity pull docker://godlovedc/lolcow 
WARNING: pull for Docker Hub is not guaranteed to produce the
WARNING: same image on repeated pull. Use Singularity Registry
WARNING: (shub://) to pull exactly equivalent images.
Docker image path: index.docker.io/godlovedc/lolcow:latest
Cache folder set to /u/milias/.singularity/docker
[6/6] |===================================| 100.0% 
Importing: base Singularity environment
Exploding layer: sha256:9fb6c798fa41e509b58bccc5c29654c3ff4648b608f5daa67c1aab6a7d02c118.tar.gz
Exploding layer: sha256:3b61febd4aefe982e0cb9c696d415137384d1a01052b50a85aae46439e15e49a.tar.gz
Exploding layer: sha256:9d99b9777eb02b8943c0e72d7a7baec5c782f8fd976825c9d3fb48b3101aacc2.tar.gz
Exploding layer: sha256:d010c8cf75d7eb5d2504d5ffa0d19696e8d745a457dd8d28ec6dd41d3763617e.tar.gz
Exploding layer: sha256:7fac07fb303e0589b9c23e6f49d5dc1ff9d6f3c8c88cabe768b430bdb47f03a9.tar.gz
Exploding layer: sha256:8e860504ff1ee5dc7953672d128ce1e4aa4d8e3716eb39fe710b849c64b20945.tar.gz
Exploding layer: sha256:736a219344fbca3099ce5bd1d2dbfea74b22b830bac0e85ecca812c2983390cd.tar.gz
WARNING: Building container as an unprivileged user. If you run this container as root
WARNING: it may be missing some functionality.
Building Singularity image...
Singularity container built: ./lolcow.simg
Cleaning up...
Done. Container is at: ./lolcow.simg
milias@lxbk0200.gsi.de:~/Work/qch/projects/miro_ilias_qch_systems/gsi_singularity/.du -h -s lolcow.simg 
128M	lolcow.simg


milias@lxbk0200.gsi.de:~/Work/qch/projects/miro_ilias_qch_systems/gsi_singularity/.singularity build hello-world.simg shub://vsoch/hello-world
Cache folder set to /u/milias/.singularity/shub
Progress |===================================| 100.0% 
Building from local image: /u/milias/.singularity/shub/vsoch-hello-world-master-latest.simg
WARNING: Building container as an unprivileged user. If you run this container as root
WARNING: it may be missing some functionality.
Building Singularity image...
Singularity container built: hello-world.simg
Cleaning up...


singularity build --sandbox ubuntu/ docker://ubuntu


singularity pull --name funny.simg docker://godlovedc/lolcow # Done. Container is at: ./funny.simg


singularity build hello-world.simg shub://vsoch/hello-world # works 


