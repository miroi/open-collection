DIRAC buildups on MogonII
=========================

OpenMPI
-------

module load lang/Python/3.6.1-intel-2017.02

mirilias@login23.mogon:~/work/software/open-mpi/openmpi-4.1.1/../configure --prefix=/home/mirilias/work/software/open-mpi/openmpi-4.1.1-intel-2017.02-i8 FC=ifort FCFLAGS=-i8  CC=icc CFLAGS=-m64 CXX=icpc CXXFLAGS=-m64 --enable-mpi-fortran=usempi  --enable-mpi1-compatibility

make -j16 all
make install

mirilias@login23.mogon:~/.ompi_info -a | grep 'Fort integer size'
       Fort integer size: 8


DIRAC with OpenMPI-Intel-i8
---------------------------

mirilias@login23.mogon:~/work/software/dirac/trunk_production/../setup --mpi --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx  --mkl=parallel  build_openmpi_intel_mklpar_i8

mirilias@login23.mogon:~/work/software/dirac/trunk_production/build_openmpi_intel_mklpar_i8/.m -j16

