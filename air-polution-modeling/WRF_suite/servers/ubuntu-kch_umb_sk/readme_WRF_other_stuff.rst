========================
WRF on ubuntu-kch server
========================

see  https://www2.mmm.ucar.edu/wrf/users/download/get_sources_new.php

git clone https://github.com/wrf-model/WRF

see https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php

see https://www2.mmm.ucar.edu/wrf/users/docs/user_guide_v4/v4.3/users_guide_chap2.html#_Required_Compilers_and_1


NetCDF
------
sudo apt-get install  libnetcdf-dev python3-h5netcdf pnetcdf-bin libnetcdf-mpi-dev
nc-config --all
export NETCDF=/usr/lib/x86_64-linux-gnu


NETCDF4 IO features are requested, but this installation of NetCDF
  /usr
Please make sure NETCDF version is 4.1.3 or later and was built with
--enable-netcdf4

NetCDF own installation
-----------------------

NetCDF-C
~~~~~~~~

see https://downloads.unidata.ucar.edu/netcdf/


milias@194.160.44.72:~/work/software/air_pollution/WRF_suite/netcdf_c_suite/.wget https://downloads.unidata.ucar.edu/netcdf-c/4.8.1/netcdf-c-4.8.1.zip

milias@194.160.44.72:~/work/software/air_pollution/WRF_suite/netcdf_c_suite/netcdf-c-4.8.1/../configure --prefix=/home/milias/work/software/air_pollution/WRF_suite/netcdf_c_suite/  --disable-hdf5

milias@194.160.44.72:~/work/software/air_pollution/WRF_suite/netcdf_c_suite/netcdf-c-4.8.1/.make -j4; make install
 ... Congratulations! You have successfully installed netCDF! 

NetCDF-Fortran
~~~~~~~~~~~~~~
wget https://downloads.unidata.ucar.edu/netcdf-fortran/4.5.4/netcdf-fortran-4.5.4.zip

vyzaduje netcdf-c !!!

milias@194.160.44.72:~/work/software/air_pollution/WRF_suite/netcdf_fortran_suite/netcdf-fortran-4.5.4/../configure  --prefix=/home/milias/work/software/air_pollution/WRF_suite/netcdf_fortran_suite --disable-hdf5

configure: error: netcdf-c version 4.7.4 or greater is required


milias@194.160.44.72:~/work/software/air_pollution/WRF_suite/netcdf_c_suite/include/.cp /usr/include/netcdf.inc . 



Jasper
~~~~~~
https://jasper-software.github.io/jasper/
sudo apt-get install jasper
dpkg -S jasper

sudo apt-get install  jasper libequinox-jsp-jasper-java  libequinox-jsp-jasper-registry-java 




