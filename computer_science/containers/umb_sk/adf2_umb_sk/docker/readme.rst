Docker at ADF2
==============

[root@adf2 adf2_umb_singularity]# service docker restart
Redirecting to /bin/systemctl restart docker.service

https://docker-curriculum.com/

service docker status

docker run hello-world

docker pull busybox  # Status: Downloaded newer image for docker.io/busybox:latest

docker images

docker run busybox echo "hello from busybox"

docker ps -a

docker run -it busybox sh # shell

docker rm $(docker ps -a -q -f status=exited) # deletes all exited containers

docker container prune


Static Sites
------------
docker run --rm prakhar1989/static-site

docker run -d -P --name static-site prakhar1989/static-site
docker port static-site # on adf2 open http://localhost:32769 in your browser

docker stop static-site

docker pull ubuntu:18.04

docker run -it ubuntu bash # interactive run

