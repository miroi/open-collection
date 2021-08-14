ubuntu-dockerfile
==================

Based on https://github.com/dev-cafe/docker-images

Source file for Docker file based on most recent LTS Ubuntu 20.04
Many usefull packages are inside.

Build on local machine:
milias@adf2:~/work/projects/open-collection/computer_science/containers/umb_sk/adf2_umb_sk/docker/ubuntu-dockerfile/.docker build  .  
Sending build context to Docker daemon  8.192kB
Step 1/11 : FROM ubuntu:20.04
20.04: Pulling from library/ubuntu
Digest: sha256:82becede498899ec668628e7cb0ad87b6e1c371cb8a1e597d83a47fac21d6af3
Status: Downloaded newer image for ubuntu:20.04
 ---> 1318b700e415
.
.
Removing intermediate container d172290fb91a
 ---> 1c4a1aff531b
Successfully built 1c4a1aff531b
milias@adf2:~/work/projects/open-collection/computer_science/containers/umb_sk/adf2_umb_sk/docker/ubuntu-dockerfile/.


How I use it:
-------------
milias@adf2:~/work/projects/open-collection/computer_science/containers/umb_sk/adf2_umb_sk/docker/ubuntu-dockerfile/.docker run -it  1c4a1aff531b

mightybuilder@9a4ca0593d52:~$  python3 -V
Python 3.8.10
mightybuilder@9a4ca0593d52:~$ whoami
mightybuilder




