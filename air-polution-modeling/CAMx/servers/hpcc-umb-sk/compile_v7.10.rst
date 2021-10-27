=========
CAMx 7.10
=========

Setting OpenMPI
---------------

export PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/bin:$PATH
export LD_LIBRARY_PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/lib:$LD_LIBRARY_PATH

Checking
~~~~~~~~
milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/.which mpif90
/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/bin/mpif90
milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/.which mpirun
/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/bin/mpirun
milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/.mpif90 --version
GNU Fortran (GCC) 9.3.1 20200408 (Red Hat 9.3.1-2)
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/.mpirun --version
mpirun (Open MPI) 4.0.1


in Makefile:
~~~~~~~~~~~~
/home/milias/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/Makefile:

#MPI_INST = /usr/local/mpich3
MPI_INST = /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3
#NCF_INST = /usr/local/netcdf
NCF_INST = /usr

Compilation v.7.10
------------------
#make COMPILER=gfortran NCF=NCF4

make COMPILER=gfortran MPI=openmpi NCF=NCF4

.
.
.
missing /usr/include/netcdf.inc !!!

