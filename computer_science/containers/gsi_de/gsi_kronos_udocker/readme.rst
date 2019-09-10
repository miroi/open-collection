udocker at Kronos.gsi.de
=========================

 /lustre/nyx/ukt/milias/work/software/udocker-tool


Download and list images
------------------------
$ udocker pull devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239

$ udocker images
REPOSITORY
devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:late .

Create container "mirocontainer"
--------------------------------
$ udocker create --name=mirocontainer devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest
09b3894d-214b-3ff5-89ab-3680ad3074fa


Interactive session with image
------------------------------
$ udocker run devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239:latest bash  # very slow !
. /opt/intel/mkl/bin/mklvars.sh intel64 ilp64 # Initialize MKL
echo $MKLROOT


Interactive session with container
----------------------------------
$ udocker run --user=root mirocontainer # as root for installing packages
# STARTING 09b3894d-214b-3ff5-89ab-3680ad3074fa
 ... Could not connect to security.ubuntu.com:80 (91.189.91.26). - connect (111: Connection refused)

