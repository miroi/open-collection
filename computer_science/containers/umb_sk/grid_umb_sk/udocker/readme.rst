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



