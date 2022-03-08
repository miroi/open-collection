WRF on labs.fpv.umb.sk Linux server
===================================

Download
--------
milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/. wget https://github.com/wrf-model/WRF/archive/refs/tags/v4.3.3.zip

Configuration and Compilation
-----------------------------
export NETCDF=/usr
export NETCDF_classic=1

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WRF-4.3.3/../configure

Enter selection [1-75] : 32
Compile for nesting? (0=no nesting, 1=basic, 2=preset moves, 3=vortex following) [default 0]:

Configuration successful!

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WRF-4.3.3/.less configure.wrf

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WRF-4.3.3/.compile -j 4 wrf



netcdf
~~~~~~

see https://docs.unidata.ucar.edu/netcdf-fortran/current/

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/.nc-config --version
netCDF 4.6.2

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/.nc-config --all

This netCDF 4.6.2 has been built with the following features:







