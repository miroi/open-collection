Singulatity at Peregrine
========================

https://redmine.hpc.rug.nl/redmine/projects/peregrine/wiki/Singularity_detailed_walkthrough#Exercise-1-Install-Singularity

Rather here:
https://sylabs.io/guides/2.6/user-guide/quick_start.html#shell

https://sylabs.io/guides/3.2/user-guide/


singularity --debug run shub://GodloveD/lolcow

singularity run --containall shub://GodloveD/lolcow

Download pre-build image:
------------------------
singularity pull shub://vsoch/hello-world 

singularity pull --name hello.simg shub://vsoch/hello-world   # pull with custom name

singularity pull --name funny.simg docker://godlovedc/lolcow

Building images
---------------
singularity build hello-world.simg shub://vsoch/hello-world

singularity build lolcow.simg docker://godlovedc/lolcow

Shell
-----
singularity shell hello-world.simg  # trying Linux commands whoami, id, date, which who, exit

singularity shell shub://vsoch/hello-world

Executing commands
------------------
singularity exec hello-world.simg ls /
singularity exec hello-world.simg date; echo "hello world"; du -h -s .

Problem:
singularity --debug  build ubuntu.simg  shub://singularityhub/ubuntu

singularity pull --name avocado_container.sif shub://RyanAshbaugh/ubuntu-leaves-17.04
cat /etc/os-release

Running a container
--------------------
singularity run hello-world.simg
./hello-world.simg
singularity run shub://GodloveD/lolcow

Build images from scratch
-------------------------
singularity build --sandbox ubuntu/ docker://ubuntu # creates directory ubuntu/

singularity build --sandbox lolcow/ library://sylabs-jms/testing/lolcow





