============================
FDS installation on HPCC UMB
============================

OpenMPI first
-------------
 ##############################################################################################
 #          My newest OpenMPI-4.1.4 GNU 11.2.1 installation
 #         -------------------------------------------------
 #  milias@login.grid.umb.sk:~/bin/openmpi/openmpi-4.1.4_gnu11.2.1/../configure --prefix=$PWD CXX=g++ CC=gcc F77=gfortran FC=gfortran
 # extend_string PATH             /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/bin          $PATH
 #  extend_string MANPATH          /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/share/man    $MANPATH
 #  extend_string LD_LIBRARY_PATH  /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib          $LD_LIBRARY_PATH
 #  echo -e "\n  OpenMPI-4.1.4 GNU 11.2.1 variables PATH,MANPATH,LD_LIBRARY_PATH activated ! In /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1 ...  "
 ################################################################################################

 Then compile FDS
-------------------

module purge
export PATH=/home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/bin:$PATH
export LD_LIBRARY_PATH=/home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib:$LD_LIBRARY_PATH

ep
elp

milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/.mpirun --version
mpirun (Open MPI) 4.1.4

milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/.mpifort --version
GNU Fortran (GCC) 11.2.1 20220127 (Red Hat 11.2.1-9)

milias@login.grid.umb.sk:~/Work/software/firemodels/.wget https://github.com/firemodels/fds/archive/refs/tags/FDS6.7.9.zip
milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/../make_fds.sh
.
.
mpifort -c -m64 -O2 -std=f2018 -frecursive -ffpe-summary=none -fall-intrinsics -cpp -DGITHASH_PP=\"-\" -DGITDATE_PP=\""\"" -DBUILDDATE_PP=\""Jan 30, 2023  17:27:37\"" -DCOMPVER_PP=\""Gnu gfortran 11.2.1"\" -DWITH_MKL -I/mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/include  ../../Source/cons.f90
.
.


