=================
QE 7.0 on lxir127
=================

from https://github.com/QEF/q-e/releases

https://github.com/QEF/q-e/releases/download/qe-7.0/qe-7.0-ReleasePack.tgz

milias@lxir127.gsi.de:/data.local1/milias/software/quantum-epresso/qe-7.0/

see https://gitlab.com/QEF/q-e/-/tree/qe-7.0

compilation
-----------
module load openmpi/gcc/4.0.3_gcc8 ... mpif90 does not work 
module load openmpi/intel/4.0.3_intel19.0

build_openmpi/.FC=mpif90 cmake .. not working ...

milias@lxir127.gsi.de:/data.local1/milias/software/quantum-epresso/qe-7.0/../configure   ... not working ...

module load openmpi/gcc/3.1_gcc8 ... not working ...

another try
~~~~~~~~~~~

module load compiler/intel/17.4  ; plus OpenMPI3.1-Intel installation

milias@lxir127.gsi.de:/data.local1/milias/software/quantum-epresso/qe-7.0/build_mpi/.cmake -DCMAKE_C_COMPILER=mpicc -DCMAKE_Fortran_COMPILER=mpif90  ..

but https://gitlab.com/QEF/q-e/-/issues/503

works
~~~~~
module load openmpi/gcc/4.0.3_gcc8

milias@lxir127.gsi.de:/data.local1/milias/software/quantum-epresso/qe-7.0/build_openmpi/.cmake -DCMAKE_C_COMPILER=mpicc -DCMAKE_Fortran_COMPILER=mpif90  ..





