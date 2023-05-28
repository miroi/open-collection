Abinit on lxir127.gsi.de
========================

milias@lxir127.gsi.de:/data.local1/milias/software/abinit/abinit-8.10.3/../configure FC=mpif90 CC=mpicc  --with-mpi  --prefix=$PWD 
milias@lxir127.gsi.de:/data.local1/milias/software/abinit/abinit-8.10.3/.make check



milias@lxir127.gsi.de:/data.local1/milias/software/abinit/abinit-9.0.4/../configure FC=mpif90 CC=mpicc --with-hdf5 --with-libxc --with-netcdf  --with-netcdf_fortran   --with-mpi --prefix=$PWD ... needs netcdf fortran


master
~~~~~~
with fallback:

milias@lxir127.gsi.de:/data.local1/milias/software/abinit/abinit_master/../configure FC=mpif90 CC=mpicc CXX=mpicxx  --with-hdf5 --with-libxc=/data.local1/milias/software/abinit/abinit_master/fallbacks/install_fb/intel/17.0/libxc/4.2.3 --with-netcdf=/data.local1/milias/software/abinit/abinit_master/fallbacks/install_fb/intel/17.0/netcdf4/4.6.3  --with-netcdf-fortran=/data.local1/milias/software/abinit/abinit_master/fallbacks/install_fb/intel/17.0/netcdf4_fortran/4.5.2   --with-mpi --prefix=$PWD



We have
-------
milias@lxir127.gsi.de:/data.local1/milias/software/abinit/abinit-8.10.3/bin/
