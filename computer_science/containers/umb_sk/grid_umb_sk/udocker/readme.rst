=============================
udocker on @login.grid.umb.sk
=============================

Download image
--------------
milias@comp03:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker pull devcafe/ubuntu16.04-gcc5.3.1-openmpi1.10-mkl2017.4.239

milias@comp03:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker images
REPOSITORY
devcafe/ubuntu16.04-gcc5.3.1-openmpi1.10-mkl2017.4.239:lates .

Create own container and modify it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
milias@comp03:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.nohup udocker create --name=miro devcafe/ubuntu16.04-gcc5.3.1-openmpi1.10-mkl2017.4.239:latest
0cc05965-3a3e-3dc1-8a83-44e284582796 (in nohup.out)

milias@comp03:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker ps
CONTAINER ID                         P M NAMES              IMAGE
3f8bcb87-6ba6-310e-be12-e2f593dbcc55 . W                    devcafe/ubuntu16.04-gcc5.3.1-openmpi1.10-mkl2017.4.239:latest
0cc05965-3a3e-3dc1-8a83-44e284582796 . W ['miro']           devcafe/ubuntu16.04-gcc5.3.1-openmpi1.10-mkl2017.4.239:latest

But error upon running: 
https://github.com/indigo-dc/udocker/issues/223 
https://github.com/krallin/tini/issues/141

Another image download
----------------------
milias@comp03:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker pull devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0

Create container, run and modify it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
milias@comp03:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker create --name=miro2 devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0:latest
8ce9a717-19b2-3872-940a-69f7f352f751

milias@comp03:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker run miro2
FATAL: kernel too old

milias@comp03:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker run mirotini bash
FATAL: kernel too old

Scientific Linux 6 Image
========================
See https://hub.docker.com/_/sl?tab=tags

udocker pull sl # downloads the latest SL

udocker pull sl:6 # downloads SL 6

Create container upon SL:latest
-------------------------------
milias@login.grid.umb.sk:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker create --name=mirosl sl:latest
55ca64ba-da26-31af-ae20-cca0a8b0a3bd

milias@login.grid.umb.sk:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker ps
ONTAINER ID                         P M NAMES              IMAGE
55ca64ba-da26-31af-ae20-cca0a8b0a3bd . W ['mirosl']         sl:latest  # my image 

milias@login.grid.umb.sk:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker run mirosl bash
 *               STARTING 55ca64ba-da26-31af-ae20-cca0a8b0a3bd                * 
 executing: bash
55ca64ba# whoami # <---- root
yum install vim # install package  with all dependencies !

milias@login.grid.umb.sk:~/Work/open-collection/computer_science/containers/umb_sk/grid_umb_sk/udocker/.udocker run --user=gridumbuser  mirosl bash
Warning: non-existing user will be created
 *               STARTING 55ca64ba-da26-31af-ae20-cca0a8b0a3bd                * 
 executing: bash
55ca64ba$ whoami
gridumbuser

SL:last has the same packages as cluster kernel, no need to use containers !!!
------------------------------------------------------------------------------


