WPS on labs.fpv.umb.sk
======================

From https://www2.mmm.ucar.edu/wrf/users/download/get_sources_new.php :

git clone https://github.com/wrf-model/WPS

Configuration
-------------

3.  Linux x86_64, gfortran    (dmpar)

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WPS/../configure 

Enter selection [1-40] : 3
Configuration successful. To build the WPS, type: compile



Compilation
-----------

vim configure.wps: add -lnetcdff !!!!
WRF_LIB         =  -L$(NETCDF)/lib  -lnetcdf   -lnetcdff

./compile

 geogrid.exe -> geogrid/src/geogrid.exe
metgrid.exe -> metgrid/src/metgrid.exe

ungrib ???


