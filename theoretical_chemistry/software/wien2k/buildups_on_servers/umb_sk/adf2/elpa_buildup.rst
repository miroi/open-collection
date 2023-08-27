ELPA buildup
============

milias@adf2:~/work/software/elpa/elpa-2023.05.001.rc1/.module list   
Currently Loaded Modulefiles:
  1) mpi/openmpi3-x86_64

milias@adf2:~/work/software/elpa/elpa-2023.05.001.rc1/../configure --prefix=$PWD --enable-openmp

checking whether the compiler supports GNU Fortran... yes
checking whether gfortran accepts -g... yes
checking for function MPI_INIT... no
checking for function MPI_INIT in -lmpichf90... no
checking for function MPI_INIT in -lfmpi... no
checking for function MPI_INIT in -lfmpich... no
configure: error: Could not compile an MPI Fortran program


