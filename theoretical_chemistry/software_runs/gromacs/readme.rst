=======
Gromacs
=======


https://github.com/gromacs/gromacs

Installation
~~~~~~~~~~~~
milias@login.grid.umb.sk:~/Work/qch/software/gromacs/gromacs_master/build_openmpi/.cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON -DCMAKE_CXX_COMPILER=mpicxx -DCMAKE_C_COMPILER=mpicc  -DGMX_MPI=on -DGMX_FFT_LIBRARY=mkl 

