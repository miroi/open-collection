WRF on labs.fpv.umb.sk Linux server
===================================

Download
--------
milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/. wget https://github.com/wrf-model/WRF/archive/refs/tags/v4.3.3.zip

Configuration 
-------------

export NETCDF=/usr
export NETCDF_classic=1

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WRF-4.3.3/../configure

Enter selection [1-75] : 32
Compile for nesting? (0=no nesting, 1=basic, 2=preset moves, 3=vortex following) [default 0]:

Configuration successful!

Compilation
-----------

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WRF-4.3.3/.less configure.wrf

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WRF-4.3.3/.compile -j 4 wrf

.
.
/usr/bin/ld: libwrflib.a(module_trajectory.o): in function `__module_trajectory_MOD_handle_ncerr.part.1':
module_trajectory.f90:(.text+0x8a5): undefined reference to `nf_strerror_'
/usr/bin/ld: libwrflib.a(module_trajectory.o): in function `def_vars.16614':
module_trajectory.f90:(.text+0xde8): undefined reference to `nf_def_var_'
/usr/bin/ld: module_trajectory.f90:(.text+0xf4e): undefined reference to `nf_put_att_text_'
/usr/bin/ld: module_trajectory.f90:(.text+0x109b): undefined reference to `nf_put_att_text_'
/usr/bin/ld: module_trajectory.f90:(.text+0x15d4): undefined reference to `nf_def_var_'
/usr/bin/ld: module_trajectory.f90:(.text+0x1720): undefined reference to `nf_put_att_text_'



netcdf
~~~~~~

see https://docs.unidata.ucar.edu/netcdf-fortran/current/

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/.nc-config --version
netCDF 4.6.2

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/.nc-config --all

This netCDF 4.6.2 has been built with the following features:







