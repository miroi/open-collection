Docker at adf2 server
======================

Start the service
-----------------

[root@adf2 adf2_umb_singularity]# service docker restart
Redirecting to /bin/systemctl restart docker.service

Tutorial
--------

https://docker-curriculum.com/

Check service
~~~~~~~~~~~~~~
milias@adf2:~/work/projects/open-collection/computer_science/containers/umb_sk/adf2_umb_sk/docker/.service docker status
.
.
   Active: active (running) since Sat 2019-09-14 13:07:49 CEST; 48s ago
     Docs: http://docs.docker.com



docker run hello-world

docker pull busybox  # Status: Downloaded newer image for docker.io/busybox:latest

docker images

docker run busybox echo "hello from busybox"

docker ps -a

docker run -it busybox sh # shell

docker rm $(docker ps -a -q -f status=exited) # deletes all exited containers

docker container prune


docker run --rm prakhar1989/static-site

docker run -d -P --name static-site prakhar1989/static-site
docker port static-site # on adf2 open http://localhost:32769 in your browser

docker stop static-site

docker pull ubuntu:18.04

docker run -it ubuntu bash # interactive run

Create image for DIRAC buildup
------------------------------
milias@adf2:~/work/projects/open-collection/computer_science/containers/umb_sk/adf2_umb_sk/docker/.docker pull ubuntu
Using default tag: latest
Trying to pull repository docker.io/library/ubuntu ... 
latest: Pulling from docker.io/library/ubuntu
Digest: sha256:d1d454df0f579c6be4d8161d227462d69e163a8ff9d20a847533989cf0c94d90
Status: Image is up to date for docker.io/ubuntu:latest

docker run -it ubuntu bash # interactive run as ROOT



Login onto Docker Hub
---------------------
milias@adf2:~/work/projects/open-collection/computer_science/containers/umb_sk/adf2_umb_sk/docker/.docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username (miroilias): 
Password: 
Login Succeeded

