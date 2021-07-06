DIRAC buildups on MogonII
=========================

OpenMPI
-------

module load lang/Python/3.6.1-intel-2017.02

mirilias@login23.mogon:~/work/software/open-mpi/openmpi-4.1.1/../configure --prefix=/home/mirilias/work/software/open-mpi/openmpi-4.1.1-intel-2017.02-i8 FC=ifort FCFLAGS=-i8  CC=icc CFLAGS=-m64 CXX=icpc CXXFLAGS=-m64 --enable-mpi-fortran=usempi  --enable-mpi1-compatibility

make -j16 all install


DIRAC with OpenMPI-Intel-i8
---------------------------

