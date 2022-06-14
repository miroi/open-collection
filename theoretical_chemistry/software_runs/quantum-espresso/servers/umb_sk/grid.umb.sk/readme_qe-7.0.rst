QE-7.0
======

module load mpi/openmpi3-x86_64

see https://gitlab.com/QEF/q-e/-/wikis/Developers/CMake-build-system


milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-7.0/build_openmpi/.cmake -DCMAKE_C_COMPILER=mpicc -DCMAKE_Fortran_COMPILER=mpif90 ..
.
.
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/Work/qch/software/quantum-espresso/qe-7.0/build_openmpi

milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-7.0/build_openmpi/.m -j4
.
.



