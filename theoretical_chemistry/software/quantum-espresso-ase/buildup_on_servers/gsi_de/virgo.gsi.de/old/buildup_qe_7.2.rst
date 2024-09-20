=========================
QE-devel on Virgo cluster
=========================

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/qe-7.2/.


load modules
~~~~~~~~~~~~
spack load cmake@3.21.4 target=$(spack arch -t)
spack load openmpi@3.1.6 target=$(spack arch -t)
spack load openblas@0.3.18 target=$(spack arch -t)
spack load amdfftw@3.0 target=$(spack arch -t)

milias@lxbk0600.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/q-e_develop/build_openmpi_cpu/.spack find --loaded


buildup
~~~~~~~
cmake -DCMAKE_C_COMPILER=mpicc -DCMAKE_Fortran_COMPILER=mpif90  ..

-- Configuring done
-- Generating done
-- Build files have been written to: /lustre/ukt/milias/work/software/quantum-espresso/q-e_develop/build_openmpi_cpu

