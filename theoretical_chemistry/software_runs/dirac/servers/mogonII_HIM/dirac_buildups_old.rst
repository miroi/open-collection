DIRAC on MogonII
================

With OpenMPI-Intel
------------------
module load mpi/OpenMPI/3.1.1-iccifort-2018.3.222-GCC-6.3.0
module load numlib/imkl/2018.3.222-iimpi-2018.03

mirilias@login23.mogon:~/work/software/dirac/trunk_master/.echo $MKLROOT
/cluster/easybuild/broadwell/software/imkl/2018.3.222-iimpi-2018.03/mkl

mirilias@login23.mogon:~/work/software/dirac/trunk_master/../setup --mpi --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx  --mkl=parallel  build_openmpi_intel_mklpar_i8

NOT WORKING ! Maybe due to Python2 ?

With OpenMPI-GNU
-----------------
module load lang/Python/3.6.6-foss-2018b

./setup --mpi --fc=mpif90 --cc=mpicc --cxx=mpicxx --int64 build_openmpi_gnu_i8/


With Intel-MPI
---------------

module load lang/Python/3.6.1-intel-2017.02 

mirilias@login23.mogon:~/work/software/dirac/trunk_master/build_intelmpi_mklpar_i8/.module list
Currently Loaded Modulefiles:
 1) compiler/GCCcore/6.3.0                              6) toolchain/iimpi/2017.02-GCC-6.3.0               
 2) compiler/icc/2017.2.174-GCC-6.3.0                   7) numlib/imkl/2017.2.174-iimpi-2017.02-GCC-6.3.0  
 3) compiler/ifort/2017.2.174-GCC-6.3.0                 8) toolchain/intel/2017.02                         
 4) toolchain/iccifort/2017.2.174-GCC-6.3.0             9) lang/Python/3.6.1-intel-2017.02                 
 5) mpi/impi/2017.2.174-iccifort-2017.2.174-GCC-6.3.0  

mirilias@login23.mogon:~/work/software/dirac/trunk_master/build_intelmpi_mklpar_i8/.cmake --version
cmake version 3.11.4

mirilias@login23.mogon:~/work/software/dirac/trunk_master/build_intelmpi_mklpar_i8/../setup --mpi --int64 --fc=mpiifort --cc=mpiicc --cxx=mpiicpc  --mkl=parallel  build_intelmpi_mklpar_i8

