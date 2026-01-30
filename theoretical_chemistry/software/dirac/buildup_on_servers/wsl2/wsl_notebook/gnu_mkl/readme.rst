===============
DIRAC on WSL PC
===============

MKL library
------------
sudo apt-get install intel-mkl-full libmkl-gf-ilp64 libmkl-gf-lp64 libmkl-gnu-thread libmkl-scalapack-ilp64 libmkl-scalapack-lp64

sudo  apt-get install hdf5-tools  libhdf5-openmpi-dev

mpif90 --version
GNU Fortran (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

mpicc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

mpicxx --version
g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

mpirun --version
mpirun (Open MPI) 4.1.2

buildup
~~~~~~~
./setup  --mpi  --fc=mpif90 --cc=mpicc --cxx=mpicxx  --cmake-options="-D ENABLE_PELIB=ON"  build_gnu_mkl_lp64

or 

./setup  --mpi --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx  --cmake-options="-D ENABLE_PELIB=OFF"  build_gnu_mkl_ilp64


Tests
~~~~~
...dirac/build_gnu_mkl_ilp64/.export DIRAC_MPI_COMMAND="mpirun -np 2"
...dirac/build_gnu_mkl_ilp64/.ctest -L short -j2


