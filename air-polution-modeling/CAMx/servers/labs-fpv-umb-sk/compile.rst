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

Compilation
~~~~~~~~~~~
make COMPILER=gfortran MPI=openmpi NCF=NCF4
make COMPILER=gfortran NCF=NCF4

