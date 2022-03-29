===================================
WRF on labs.fpv.umb.sk Linux server
===================================

see  https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php

Download
--------
milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/. wget https://github.com/wrf-model/WRF/archive/refs/tags/v4.3.3.zip

Configuration 
-------------

Check netcdf installation:  nc-config  --all

export NETCDF=/usr; export NETCDF_classic=1

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WRF-4.3.3/../configure

set dmpar (34) :  means Distributed Memory Parallel (MPI)
Enter selection [1-75] : 34
Compile for nesting? (0=no nesting, 1=basic, 2=preset moves, 3=vortex following) [default 0]:


Configuration successful!

Compilation
-----------


milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WRF-4.3.3/.vim configure.wrf

 LIB_EXTERNAL    = \
                      -L$(WRF_SRC_ROOT_DIR)/external/io_netcdf -lwrfio_nf -L/usr/lib  \
                      -L/usr/lib/x86_64-linux-gnu -L/usr/lib/x86_64-linux-gnu/hdf5/serial -lnetcdf -lhdf5_hl -lhdf5 -lpthread -lsz -lz -ldl -lm -lcurl -L/usr/lib -lnetcdff


milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WRF-4.3.3/.compile -j 4 wrf

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/WRF/.ldd main/wrf.exe


netcdf
~~~~~~
see https://docs.unidata.ucar.edu/netcdf-fortran/current/

milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/.nc-config --version
netCDF 4.6.2
milias@labs.fpv.umb.sk:~/work/software/air_pollution/WRF_suite/.nc-config --all





