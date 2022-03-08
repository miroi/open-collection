WRF on HPCC UMB cluster
=======================

Download
--------
milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/WRF_suite/.wget https://github.com/wrf-model/WRF/archive/refs/tags/v4.3.3.zip

Configuration and Compilation
-----------------------------
milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/WRF_suite/WRF-4.3.3/.export NETCDF=/usr/bin/
export NETCDF_classic=1

milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/WRF_suite/WRF-4.3.3/../configure

Enter selection [1-75] : 13
Compile for nesting? (0=no nesting, 1=basic, 2=preset moves, 3=vortex following) [default 0]:

milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/WRF_suite/WRF-4.3.3/.compile -j 4 wrf


netcdf
~~~~~~

see https://docs.unidata.ucar.edu/netcdf-fortran/current/

milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/WRF_suite/WRF-4.3.3/.nc-config --version
netCDF 4.3.3.1

milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/WRF_suite/WRF-4.3.3/.nc-config --all





