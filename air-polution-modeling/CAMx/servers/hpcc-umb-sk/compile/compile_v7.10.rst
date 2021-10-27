=========
CAMx 7.10
=========

Added Packages
--------------
netcdf.x86_64                         4.3.3.1-5.el7              @epel
netcdf-devel.x86_64                   4.3.3.1-5.el7              @epel
netcdf-fortran.x86_64                 4.2-16.el7                 @epel
netcdf-fortran-devel.x86_64           4.2-16.el7                 @epel
netcdf-fortran-openmpi.x86_64         4.2-16.el7                 @epel
netcdf-fortran-openmpi-devel.x86_64   4.2-16.el7                 @epel
netcdf-openmpi.x86_64                 4.3.3.1-5.el7              @epel
netcdf-openmpi-devel.x86_64           4.3.3.1-5.el7              @epel
netcdf-static.x86_64                  4.3.3.1-5.el7              @epel


Setting OpenMPI
---------------

export PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/bin:$PATH
export LD_LIBRARY_PATH=/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/lib:$LD_LIBRARY_PATH

Checking
~~~~~~~~
milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/.which mpif90
/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/bin/mpif90
milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/.which mpirun
/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/bin/mpirun
milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/.mpif90 --version
GNU Fortran (GCC) 9.3.1 20200408 (Red Hat 9.3.1-2)
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/.mpirun --version
mpirun (Open MPI) 4.0.1


in Makefile:
~~~~~~~~~~~~
/home/milias/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/Makefile:

#MPI_INST = /usr/local/mpich3
MPI_INST = /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3
#NCF_INST = /usr/local/netcdf
NCF_INST = /usr

Compilation v.7.10
------------------
#make COMPILER=gfortran NCF=NCF4
make COMPILER=gfortran MPI=openmpi NCF=NCF4

.
.
.

milias@login.grid.umb.sk:~/Work/software/air-pollution-modeling/CAMx_suite/v7.10/src.v7.10/.ldd CAMx.v7.10.openMPI.NCF4.gfortran
        linux-vdso.so.1 =>  (0x00007ffc2f3a9000)
        libnetcdff.so.5 => /lib64/libnetcdff.so.5 (0x00007f8ba52e5000)
        libnetcdf.so.7 => /lib64/libnetcdf.so.7 (0x00007f8ba1ef4000)
        libmpi_usempif08.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/lib/libmpi_usempif08.so.40 (0x00007f8ba1cc1000)
        libmpi_usempi_ignore_tkr.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/lib/libmpi_usempi_ignore_tkr.so.40 (0x00007f8ba1ab9000)
        libmpi_mpifh.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/lib/libmpi_mpifh.so.40 (0x00007f8ba185c000)
        libmpi.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/lib/libmpi.so.40 (0x00007f8ba1530000)
        libgfortran.so.5 => /lib64/libgfortran.so.5 (0x00007f8ba10b8000)
        libm.so.6 => /lib64/libm.so.6 (0x00007f8ba0db6000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f8ba0ba0000)
        libquadmath.so.0 => /lib64/libquadmath.so.0 (0x00007f8ba0964000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f8ba0748000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f8ba037a000)
        libgfortran.so.3 => /lib64/libgfortran.so.3 (0x00007f8ba0058000)
        libhdf5_hl.so.8 => /lib64/libhdf5_hl.so.8 (0x00007f8b9fe27000)
        libhdf5.so.8 => /lib64/libhdf5.so.8 (0x00007f8b9f981000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f8b9f77d000)
        libz.so.1 => /lib64/libz.so.1 (0x00007f8b9f567000)
        libcurl.so.4 => /lib64/libcurl.so.4 (0x00007f8b9f2fd000)
        libjpeg.so.62 => /lib64/libjpeg.so.62 (0x00007f8b9f0a8000)
        libopen-rte.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/lib/libopen-rte.so.40 (0x00007f8b9eded000)
        libopen-pal.so.40 => /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_gnu6.3/lib/libopen-pal.so.40 (0x00007f8b9eadc000)
        librt.so.1 => /lib64/librt.so.1 (0x00007f8b9e8d4000)
        libutil.so.1 => /lib64/libutil.so.1 (0x00007f8b9e6d1000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f8ba5551000)
        libsz.so.2 => /lib64/libsz.so.2 (0x00007f8b9e4ce000)
        libidn.so.11 => /lib64/libidn.so.11 (0x00007f8b9e29b000)
        libssh2.so.1 => /lib64/libssh2.so.1 (0x00007f8b9e06e000)
        libssl3.so => /lib64/libssl3.so (0x00007f8b9de11000)
        libsmime3.so => /lib64/libsmime3.so (0x00007f8b9dbe9000)
        libnss3.so => /lib64/libnss3.so (0x00007f8b9d8b5000)
        libnssutil3.so => /lib64/libnssutil3.so (0x00007f8b9d685000)
        libplds4.so => /lib64/libplds4.so (0x00007f8b9d481000)
        libplc4.so => /lib64/libplc4.so (0x00007f8b9d27c000)
        libnspr4.so => /lib64/libnspr4.so (0x00007f8b9d03e000)
        libgssapi_krb5.so.2 => /lib64/libgssapi_krb5.so.2 (0x00007f8b9cdf1000)
        libkrb5.so.3 => /lib64/libkrb5.so.3 (0x00007f8b9cb08000)
        libk5crypto.so.3 => /lib64/libk5crypto.so.3 (0x00007f8b9c8d5000)
        libcom_err.so.2 => /lib64/libcom_err.so.2 (0x00007f8b9c6d1000)
        liblber-2.4.so.2 => /lib64/liblber-2.4.so.2 (0x00007f8b9c4c2000)
        libldap-2.4.so.2 => /lib64/libldap-2.4.so.2 (0x00007f8b9c26d000)
        libaec.so.0 => /lib64/libaec.so.0 (0x00007f8b9c065000)
        libssl.so.10 => /lib64/libssl.so.10 (0x00007f8b9bdf3000)
        libcrypto.so.10 => /lib64/libcrypto.so.10 (0x00007f8b9b990000)
        libkrb5support.so.0 => /lib64/libkrb5support.so.0 (0x00007f8b9b780000)
        libkeyutils.so.1 => /lib64/libkeyutils.so.1 (0x00007f8b9b57c000)
        libresolv.so.2 => /lib64/libresolv.so.2 (0x00007f8b9b362000)
        libsasl2.so.3 => /lib64/libsasl2.so.3 (0x00007f8b9b145000)
        libselinux.so.1 => /lib64/libselinux.so.1 (0x00007f8b9af1e000)
        libcrypt.so.1 => /lib64/libcrypt.so.1 (0x00007f8b9ace7000)
        libpcre.so.1 => /lib64/libpcre.so.1 (0x00007f8b9aa85000)
        libfreebl3.so => /lib64/libfreebl3.so (0x00007f8b9a882000)

