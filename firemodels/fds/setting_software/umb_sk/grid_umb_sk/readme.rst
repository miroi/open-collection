FDS installation on HPCC UMB
============================


milias@login.grid.umb.sk:~/Work/software/firemodels/.wget https://github.com/firemodels/fds/archive/refs/tags/FDS6.7.9.zip

 ##############################################################################################
 #          My newest OpenMPI-4.1.4 GNU 11.2.1 installation
 #         -------------------------------------------------
 #  milias@login.grid.umb.sk:~/bin/openmpi/openmpi-4.1.4_gnu11.2.1/../configure --prefix=$PWD CXX=g++ CC=gcc F77=gfortran FC=gfortran
 # extend_string PATH             /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/bin          $PATH
 #  extend_string MANPATH          /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/share/man    $MANPATH
 #  extend_string LD_LIBRARY_PATH  /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib          $LD_LIBRARY_PATH
 #  echo -e "\n  OpenMPI-4.1.4 GNU 11.2.1 variables PATH,MANPATH,LD_LIBRARY_PATH activated ! In /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1 ...  "
 ################################################################################################

module clean

export PATH=/home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/bin:$PATH
export LD_LIBRARY_PATH=/home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib:$LD_LIBRARY_PATH

ep
elp

milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/../make_fds.sh



