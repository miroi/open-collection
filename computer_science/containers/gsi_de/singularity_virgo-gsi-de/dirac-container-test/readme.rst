Singularity on Virgo.gsi.de cluster
===================================

https://github.com/dev-cafe/docker-images

milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/projects/open-collection/computer_science/containers/gsi_de/singularity_virgo-gsi-de/dirac-container-test/

singularity pull $SINGULARITY_CONTAINERS/devcafe-ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239.sif docker://devcafe/ubuntu18.04-gcc7.3.0-openmpi2.1.0-mkl2017.4.239

singularity pull $SINGULARITY_CONTAINERS/devcafe-ubuntu16.04-intel2018.1.sif  docker://devcafe/ubuntu16.04-intel2018.1

# overwrite existing sif file
singularity pull -F  $SINGULARITY_CONTAINERS/devcafe-ubuntu16.04-intel2018.1.sif  docker://devcafe/ubuntu16.04-intel2018.1 

# run commands
singularity exec $SINGULARITY_CONTAINERS/devcafe-ubuntu16.04-intel2018.1.sif ls -lt /opt/intel
singularity exec $SINGULARITY_CONTAINERS/devcafe-ubuntu16.04-intel2018.1.sif git --version
singularity exec $SINGULARITY_CONTAINERS/devcafe-ubuntu16.04-intel2018.1.sif gfortran --version


singularity pull $SINGULARITY_CONTAINERS/devcafe-ubuntu16.04-pgi17.4.sif  docker://devcafe/ubuntu16.04-pgi17.4.sif


milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/projects/open-collection/computer_science/containers/gsi_de/singularity_virgo-gsi-de/dirac-container-test/.singularity pull  $SINGULARITY_CONTAINERS/devcafe-ubuntu16.04-gcc5.3.1-openmpi1.10-mkl2017.4.239.sif    docker://devcafe/ubuntu16.04-gcc5.3.1-openmpi1.1
0-mkl2017.4.239

singularity shell $SINGULARITY_CONTAINERS/devcafe-ubuntu16.04-gcc5.3.1-openmpi1.10-mkl2017.4.239.sif cat /etc/issue


https://github.com/bast/dockerfile-openmpi-i8
---------------------------------------------
singularity  pull  $SINGULARITY_CONTAINERS/bast-openmpi-i8:4.0.4-gcc-9.3.0.sif   docker://quay.io/bast/openmpi-i8:4.0.4-gcc-9.3.0 

singularity exec $SINGULARITY_CONTAINERS/bast-openmpi-i8:4.0.4-gcc-9.3.0.sif ompi_info -a | grep 'Fort integer size'
       Fort integer size: 8

singularity exec $SINGULARITY_CONTAINERS/bast-openmpi-i8:4.0.4-gcc-9.3.0.sif cmake --version
cmake version 3.16.3

singularity exec $SINGULARITY_CONTAINERS/bast-openmpi-i8:4.0.4-gcc-9.3.0.sif gfortran --version
GNU Fortran (Ubuntu 9.3.0-10ubuntu2) 9.3.0

singularity exec $SINGULARITY_CONTAINERS/bast-openmpi-i8:4.0.4-gcc-9.3.0.sif cmake --version
cmake version 3.16.3


