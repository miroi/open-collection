========================
WRF on ubuntu-kch server
========================

see  https://www2.mmm.ucar.edu/wrf/users/download/get_sources_new.php

git clone https://github.com/wrf-model/WRF

Configuration
-------------

see https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php

Error : Not found /usr/lib/x86_64-linux-gnu/include/netcdf.inc
        Please check this installation of NetCDF and re-run this configure script


NetCDF
~~~~~~
sudo apt-get install  libnetcdf-dev python3-h5netcdf pnetcdf-bin libnetcdf-mpi-dev


nc-config --libdir
export NETCDF="/usr/lib/x86_64-linux-gnu"

HDF5 not set in environment
PHDF5 not set in environment
$JASPERLIB or $JASPERINC not found in environment


Jasper
~~~~~~
https://jasper-software.github.io/jasper/
sudo apt-get install jasper
dpkg -S jasper

sudo apt-get install  jasper libequinox-jsp-jasper-java  libequinox-jsp-jasper-registry-java 



Compilation
-----------









