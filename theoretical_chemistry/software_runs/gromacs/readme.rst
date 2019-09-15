=======
Gromacs
=======


https://github.com/gromacs/gromacs

Installation
~~~~~~~~~~~~
http://manual.gromacs.org/documentation/2019.3/install-guide/index.html

# Own OpenMPI-4.0.1 with GNU 6.3:
export PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/bin:$PATH
export LD_LIBRARY_PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/lib:$LD_LIBRARY_PATH

# with Intel MKL 11.1, linking for C compiler based on https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor
milias@login.grid.umb.sk:~/Work/qch/software/gromacs/gromacs_master/build_openmpi-4.0.1_gnu6.3/.cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON -DCMAKE_CXX_COMPILER=mpicxx -DCMAKE_C_COMPILER=mpicc  -DGMX_MPI=on -DGMX_FFT_LIBRARY=mkl -DMKL_LIBRARIES="-L${MKLROOT}/lib/mic -lmkl_scalapack_lp64 -lmkl_cdft_core -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_lp64 -liomp5 -lpthread -lm -ldl" -DMKL_INCLUDE_DIR="$MKLROOT/include"



