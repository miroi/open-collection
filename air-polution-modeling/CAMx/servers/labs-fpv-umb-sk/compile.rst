==================
CAMx, www.camx.com
==================

milias@labs.fpv.umb.sk; milias@194.160.44.72
--------------------------------------------

in Makefile:
~~~~~~~~~~~~
#MPI_INST = /usr/local/mpich3
MPI_INST = /usr
#NCF_INST = /usr/local/netcdf
NCF_INST = /usr

change of v6-50/MPI/util/Makefile:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#MPI_INST = /usr/local/mpich3
MPI_INST = /usr

LIBNAME = libparlib.a

CC = gcc

#LIB = -L$(MPI_INST)/lib -lmpich
LIB = -L$(MPI_INST)/lib -lmpi

INC = $(MPI_INST)/include/mpi

Compilation v.7.10
------------------
make COMPILER=gfortran MPI=openmpi NCF=NCF4
milias@labs.fpv.umb.sk:~/work/software/air_pollution/CAMx/v7.10/src.v7.10/.make COMPILER=gfortran MPI=openmpi NCF=NCF4

 MPI will be built in using OpenMPI                            *
 NetCDF will be built in using version 4, with compression     *
 The IEEE option NOT will be used                              *
 Executable is: CAMx.v7.10.openMPI.NCF4.gfortran

make COMPILER=gfortran NCF=NCF4
