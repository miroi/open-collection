=========
CAMx 7.10
=========

in Makefile:
~~~~~~~~~~~~
milias@labs.fpv.umb.sk:~/work/software/air_pollution/CAMx/v7.10/src.v7.10/Makefile :

#MPI_INST = /usr/local/mpich3
MPI_INST = /usr
#NCF_INST = /usr/local/netcdf
NCF_INST = /usr

Compilation v.7.10
------------------
make COMPILER=gfortran NCF=NCF4

make COMPILER=gfortran MPI=openmpi NCF=NCF4
milias@labs.fpv.umb.sk:~/work/software/air_pollution/CAMx/v7.10/src.v7.10/.make COMPILER=gfortran MPI=openmpi NCF=NCF4

 MPI will be built in using OpenMPI                            *
 NetCDF will be built in using version 4, with compression     *
 The IEEE option NOT will be used                              *
 Executable is: CAMx.v7.10.openMPI.NCF4.gfortran

milias@labs.fpv.umb.sk:~/work/software/air_pollution/CAMx/v7.10/src.v7.10/.ldd CAMx.v7.10.openMPI.NCF4.gfortran

