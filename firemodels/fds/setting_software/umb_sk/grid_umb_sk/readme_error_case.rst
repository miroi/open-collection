FDS installation on HPCC UMB
============================

milias@login.grid.umb.sk:~/Work/software/firemodels/.wget https://github.com/firemodels/fds/archive/refs/tags/FDS6.7.9.zip

module load mpi/openmpi3-x86_64

milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/.module list
Currently Loaded Modulefiles:
  1) mpi/openmpi3-x86_64

milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/.mpirun --version
mpirun (Open MPI) 1.10.7

milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/.which mpif90; mpif90 --version
/usr/lib64/openmpi3/bin/mpif90
GNU Fortran (GCC) 11.2.1 20220127 (Red Hat 11.2.1-9)

milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/../make_fds.sh
.
.
.
mpifort -c -m64 -O2 -std=f2018 -frecursive -ffpe-summary=none -fall-intrinsics -cpp -DGITHASH_PP=\"-\" -DGITDATE_PP=\""\"" -DBUILDDATE_PP=\""Jan 30, 2023  15:43:33\"" -DCOMPVER_PP=\""Gnu gfortran 11.2.1"\" -DWITH_MKL -I/mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/include  ../../Source/cons.f90
mpifort -c -m64 -O2 -std=f2018 -frecursive -ffpe-summary=none -fall-intrinsics -cpp -DGITHASH_PP=\"-\" -DGITDATE_PP=\""\"" -DBUILDDATE_PP=\""Jan 30, 2023  15:43:33\"" -DCOMPVER_PP=\""Gnu gfortran 11.2.1"\" -DWITH_MKL -I/mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/include  ../../Source/imkl.f90
../../Source/cons.f90:9:5:

    9 | USE MPI_F08
      |     1
Fatal Error: Cannot open module file 'mpi_f08.mod' for reading at (1): No such file or directory
compilation terminated.
make: *** [../makefile:135: cons.o] Error 1
make: *** Waiting for unfinished jobs....
../../Source/imkl.f90:110:14:

  110 |          USE MPI_F08
      |              1
Fatal Error: Cannot open module file 'mpi_f08.mod' for reading at (1): No such file or directory
compilation terminated.
make: *** [../makefile:135: imkl.o] Error 1
milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/.gfortran --version
GNU Fortran (GCC) 11.2.1 20220127 (Red Hat 11.2.1-9)
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

