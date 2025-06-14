====================
QE on Govorun's GPUs
====================

see https://gitlab.com/QEF/q-e/-/blob/develop/README_GPU.md
also https://gitlab.com/QEF/q-e/-/wikis/Developers/CMake-build-system

CUDA
~~~~
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/cuda/v12.1/Linux_x86_64/23.5/compilers/bin/nvc 

NVHPC compiler is mandatory when CUDA is enabled due QE is based on CUDA

--   No package 'mpi-fort' found
-- Could NOT find MPI_Fortran (missing: MPI_Fortran_LIB_NAMES MPI_Fortran_F77_HEADER_DIR MPI_Fortran_MODULE_DIR MPI_Fortran_WORKS)
CMake Error at /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/share/cmake-3.29/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find MPI (missing: MPI_Fortran_FOUND Fortran)
Call Stack (most recent call first):
  /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/share/cmake-3.29/Modules/FindPackageHandleStandardArgs.cmake:600 (_FPHSA_FAILURE_MESSAGE)
  /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/CMake/v3.29.2/share/cmake-3.29/Modules/FindMPI.cmake:1837 (find_package_handle_standard_args)




