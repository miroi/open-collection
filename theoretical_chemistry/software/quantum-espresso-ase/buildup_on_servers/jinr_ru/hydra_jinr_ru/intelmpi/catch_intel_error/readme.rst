========================
QE-develop with IntelMPI
========================

needs git
~~~~~~~~~
source /cvmfs/nica.jinr.ru/sw/os/login.sh
module add git


build
~~~~~~
cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON -DCMAKE_C_COMPILER=icc -DCMAKE_CXX_COMPILER=icpc -DCMAKE_Fortran_COMPILER=mpiifort -DCMAKE_Fortran_FLAGS="-g -parallel -xHost"  ..

