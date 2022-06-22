QE-devel on Virgo cluster
=========================

log onto specific VAE
~~~~~~~~~~~~~~~~~~~~~
ssh virgo-debian10.hpc 

load modules
~~~~~~~~~~~~
spack load cmake@3.21.4 target=$(spack arch -t)
spack load openmpi@3.1.6 target=$(spack arch -t)
spack load openblas@0.3.18 target=$(spack arch -t)

buildup
~~~~~~~
cmake -DCMAKE_C_COMPILER=mpicc -DCMAKE_Fortran_COMPILER=mpif90  ..



