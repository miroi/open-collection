DIRAC on MogonII
================

With OpenMPI-Intel
------------------
module load mpi/OpenMPI/3.1.1-iccifort-2018.3.222-GCC-6.3.0
module load numlib/imkl/2018.3.222-iimpi-2018.03

mirilias@login23.mogon:~/work/software/dirac/trunk_master/.echo $MKLROOT
/cluster/easybuild/broadwell/software/imkl/2018.3.222-iimpi-2018.03/mkl

mirilias@login23.mogon:~/work/software/dirac/trunk_master/../setup --mpi --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx  --mkl=parallel  build_openmpi_intel_mklpar_i8

With Intel-MPI
---------------

module load lang/Python/3.6.1-intel-2017.02 



mirilias@login23.mogon:~/work/software/dirac/trunk_master/../setup --mpi --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx  --mkl=parallel  build_openmpi_intel_mklpar_i8

