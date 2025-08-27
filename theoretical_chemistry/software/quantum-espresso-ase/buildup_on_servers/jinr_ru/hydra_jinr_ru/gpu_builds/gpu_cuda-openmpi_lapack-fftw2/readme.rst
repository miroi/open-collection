===========
QE with GPU
===========


https://pm.jinr.ru/issues/10120#note-20

I connected MPI module (e.g., openmpi/v5.0.3_gcc1230) and cuda/v12.4 (cuda + NVHPC) and compile QE with GPU and MPI support with flags1

$ cmake -DCMAKE_C_COMPILER=$(which mpicc) -DCMAKE_Fortran_COMPILER=$(which mpif90) -DQE_ENABLE_CUDA=ON -DQE_ENABLE_MPI_GPU_AWARE=ON -DQE_ENABLE_OPENMP=ON ..

$ which mpicc
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/cuda/v12.4/Linux_x86_64/24.5/comm_libs/mpi/bin/mpicc

$ which mpif90
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/cuda/v12.4/Linux_x86_64/24.5/comm_libs/mpi/bin/mpif90

