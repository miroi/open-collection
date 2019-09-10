udocker on @login1.kelinux.saske.sk
===================================


udocker pull devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239

udocker run devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest bash # works

ilias@login1.kelinux.saske.sk:~/work/qch/projects/miro_ilias_qch_systems/containers/kelinux_saske_sk/udocker/.udocker run  --user=root  devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest bash # better way !

Create container
----------------

First, create my container "mirocon":

ilias@login1.kelinux.saske.sk:~/work/qch/projects/miro_ilias_qch_systems/containers/kelinux_saske_sk/udocker/.udocker create --name=mirocon  devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest
0a8ee5bc-b73e-38db-8720-5aa7d308b03c


Install software inside the container:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
udocker run  --user=root mirocon
root@login1:~# apt-get update
root@login1:~# apt-get install vim

udocker run  mirocon  # there is vim  and all other installed software !!!

Export the container to file
----------------------------
ilias@login1.kelinux.saske.sk:~/work/qch/projects/miro_ilias_qch_systems/containers/kelinux_saske_sk/udocker/.udocker export -o mirox.tar mirocon

...after installing more software export the container:

udocker export -o mirox1.tar mirocon

Remove image and container
--------------------------
ilias@login1.kelinux.saske.sk:~/work/qch/projects/miro_ilias_qch_systems/containers/kelinux_saske_sk/udocker/.udocker rmi devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest
Info: deleting image: devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest

ilias@login1.kelinux.saske.sk:~/work/qch/projects/miro_ilias_qch_systems/containers/kelinux_saske_sk/udocker/.udocker rm mirocon
Info: deleting container: 0a8ee5bc-b73e-38db-8720-5aa7d308b03c
ilias@login1.kelinux.saske.sk:~/work/qch/projects/miro_ilias_qch_systems/containers/kelinux_saske_sk/udocker/.

Again, import container:
------------------------
ilias@login1.kelinux.saske.sk:~/work/qch/projects/miro_ilias_qch_systems/containers/kelinux_saske_sk/udocker/.udocker import mirox1.tar  devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest
Info: added layer debff52fde9eb621621335264dfdaee823180036907c811027fe3572b469fda1  # image ID !


recreate the container !!!
~~~~~~~~~~~~~~~~~~~~~~~
ilias@login1.kelinux.saske.sk:~/work/qch/projects/miro_ilias_qch_systems/containers/kelinux_saske_sk/udocker/.udocker import --tocontainer mirox1.tar  
59029619-12f3-3778-9a18-accbd2946977  # container ID

run the container
~~~~~~~~~~~~~~~~~

udocker run  59029619-12f3-3778-9a18-accbd2946977 # as root
... there are all the files !!!  but not paths etc..


