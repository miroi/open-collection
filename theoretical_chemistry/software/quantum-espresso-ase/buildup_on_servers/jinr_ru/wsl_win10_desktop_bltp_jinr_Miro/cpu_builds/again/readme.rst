========================
QE local buildup on WSL2
========================

cloning
-------
milias@DESKTOP-7OTLCGO:~/work/software/qe/.git clone git@gitlab.com:QEF/q-e.git  q-e-devel-official

milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel-official/.git submodule update --init --recursive

buildup
-------

installed packages
~~~~~~~~~~~~~~~~~~~
openmpi-bin gfortran  libopenmpi-dev libfftw3-bin libfftw3-mpi-dev

mpif90 --version
GNU Fortran (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0

mpirun --version
mpirun (Open MPI) 4.1.2

mkl library:
~~~~~~~~~~~~
ls /usr/lib/x86_64-linux-gnu/libmkl_*
dpkg -L libmkl-* 

cmake configuration
~~~~~~~~~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/qe/q-e-devel-official/build_openmpi/.cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON  -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_Fortran_COMPILER=mpif90  -DQE_FFTW_VENDOR=Internal    ..

compilation
~~~~~~~~~~~

ctest run
~~~~~~~~~



ctest
~~~~~

