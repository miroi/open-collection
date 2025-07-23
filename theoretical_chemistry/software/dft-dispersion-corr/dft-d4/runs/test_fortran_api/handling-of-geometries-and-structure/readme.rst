===============
Compile and run
===============

https://dftd4.readthedocs.io/en/latest/reference/fortran.html#handling-of-geometries-and-structure

Desktop PC
~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/dft-dispersion-corr/dft-d4/runs/test_fortran_api/handling-of-geometries-and-structure/.gfortran -c -I /home/milias/work/software/dft-d4/dftd4/_build/_deps/mctc-lib-build/include example.f90

gfortran -I /home/milias/work/software/dft-d4/dftd4/_build/_deps/mctc-lib-build/include example.f90 -L/home/milias/work/software/dft-d4/dftd4/_build/_deps/mctc-lib-build -lmctc-lib


Notebook
~~~~~~~~~
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/dft-dispersion-corr/dft-d4/runs/test_fortran_api/handling-of-geometries-and-structure/.gfortran -I /home/miroi/work/software/dftd4/dftd4_cloned/_build/_deps/mctc-lib-build/include example.f90 -L/home/miroi/work/software/dftd4/dftd4_cloned/_build/_d
eps/mctc-lib-build -lmctc-lib

./a.out
