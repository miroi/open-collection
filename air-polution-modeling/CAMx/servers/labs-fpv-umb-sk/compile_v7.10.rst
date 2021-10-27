=========
CAMx 7.10
=========

in Makefile:
~~~~~~~~~~~~
milias@labs.fpv.umb.sk:~/work/software/air_pollution/CAMx/v7.10/src.v7.10/Makefile :

#MPI_INST = /usr/local/mpich3
MPI_INST = /usr
#NCF_INST = /usr/local/netcdf
NCF_INST = /usr

Compilation v.7.10
------------------
make COMPILER=gfortran NCF=NCF4

make COMPILER=gfortran MPI=openmpi NCF=NCF4
milias@labs.fpv.umb.sk:~/work/software/air_pollution/CAMx/v7.10/src.v7.10/.make COMPILER=gfortran MPI=openmpi NCF=NCF4
.
.
.

 MPI will be built in using OpenMPI                            *
 NetCDF will be built in using version 4, with compression     *
 The IEEE option NOT will be used                              *
 Executable is: CAMx.v7.10.openMPI.NCF4.gfortran
.
.
.

milias@labs.fpv.umb.sk:~/work/software/air_pollution/CAMx/v7.10/src.v7.10/.ldd CAMx.v7.10.openMPI.NCF4.gfortran
        linux-vdso.so.1 (0x00007ffcff741000)
        libnetcdff.so.6 => /lib/x86_64-linux-gnu/libnetcdff.so.6 (0x00007f726d7c0000)
        libnetcdf.so.13 => /lib/x86_64-linux-gnu/libnetcdf.so.13 (0x00007f726d67f000)
        libmpi_usempif08.so.40 => /lib/x86_64-linux-gnu/libmpi_usempif08.so.40 (0x00007f726d646000)
        libmpi_usempi_ignore_tkr.so.40 => /lib/x86_64-linux-gnu/libmpi_usempi_ignore_tkr.so.40 (0x00007f726d63a000)
        libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007f726d5dc000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x00007f726d4d3000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007f726d263000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f726d0e0000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f726d0c6000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f726d084000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f726d063000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f726cea2000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f726ce9b000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f726cc7d000)
        libcurl-gnutls.so.4 => /lib/x86_64-linux-gnu/libcurl-gnutls.so.4 (0x00007f726cbef000)
        libhdf5_serial_hl.so.100 => /lib/x86_64-linux-gnu/libhdf5_serial_hl.so.100 (0x00007f726cbc9000)
        libhdf5_serial.so.103 => /lib/x86_64-linux-gnu/libhdf5_serial.so.103 (0x00007f726c844000)
        libsz.so.2 => /lib/x86_64-linux-gnu/libsz.so.2 (0x00007f726c641000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f726c635000)
        libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007f726c630000)
        libhwloc.so.5 => /lib/x86_64-linux-gnu/libhwloc.so.5 (0x00007f726c5ee000)
        libevent-2.1.so.6 => /lib/x86_64-linux-gnu/libevent-2.1.so.6 (0x00007f726c398000)
        libevent_pthreads-2.1.so.6 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.6 (0x00007f726c195000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007f726c0e8000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007f726c02e000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f72adbeb000)
        libnghttp2.so.14 => /lib/x86_64-linux-gnu/libnghttp2.so.14 (0x00007f726c006000)
        libidn2.so.0 => /lib/x86_64-linux-gnu/libidn2.so.0 (0x00007f726bfe7000)
        librtmp.so.1 => /lib/x86_64-linux-gnu/librtmp.so.1 (0x00007f726bdca000)
        libssh2.so.1 => /lib/x86_64-linux-gnu/libssh2.so.1 (0x00007f726bd9c000)
        libpsl.so.5 => /lib/x86_64-linux-gnu/libpsl.so.5 (0x00007f726bd87000)
        libnettle.so.6 => /lib/x86_64-linux-gnu/libnettle.so.6 (0x00007f726bd4f000)
        libgnutls.so.30 => /lib/x86_64-linux-gnu/libgnutls.so.30 (0x00007f726bba2000)
        libgssapi_krb5.so.2 => /lib/x86_64-linux-gnu/libgssapi_krb5.so.2 (0x00007f726bb55000)
        libkrb5.so.3 => /lib/x86_64-linux-gnu/libkrb5.so.3 (0x00007f726ba75000)
        libk5crypto.so.3 => /lib/x86_64-linux-gnu/libk5crypto.so.3 (0x00007f726ba41000)
        libcom_err.so.2 => /lib/x86_64-linux-gnu/libcom_err.so.2 (0x00007f726ba39000)
        libldap_r-2.4.so.2 => /lib/x86_64-linux-gnu/libldap_r-2.4.so.2 (0x00007f726b9e5000)
        liblber-2.4.so.2 => /lib/x86_64-linux-gnu/liblber-2.4.so.2 (0x00007f726b9d4000)
        libaec.so.0 => /lib/x86_64-linux-gnu/libaec.so.0 (0x00007f726b7cc000)
        libnuma.so.1 => /lib/x86_64-linux-gnu/libnuma.so.1 (0x00007f726b7be000)
        libltdl.so.7 => /lib/x86_64-linux-gnu/libltdl.so.7 (0x00007f726b7b1000)
        libunistring.so.2 => /lib/x86_64-linux-gnu/libunistring.so.2 (0x00007f726b62d000)
        libhogweed.so.4 => /lib/x86_64-linux-gnu/libhogweed.so.4 (0x00007f726b5f4000)
        libgmp.so.10 => /lib/x86_64-linux-gnu/libgmp.so.10 (0x00007f726b571000)
        libgcrypt.so.20 => /lib/x86_64-linux-gnu/libgcrypt.so.20 (0x00007f726b453000)
        libp11-kit.so.0 => /lib/x86_64-linux-gnu/libp11-kit.so.0 (0x00007f726b322000)
        libtasn1.so.6 => /lib/x86_64-linux-gnu/libtasn1.so.6 (0x00007f726b10f000)
        libkrb5support.so.0 => /lib/x86_64-linux-gnu/libkrb5support.so.0 (0x00007f726b100000)
        libkeyutils.so.1 => /lib/x86_64-linux-gnu/libkeyutils.so.1 (0x00007f726b0f9000)
        libresolv.so.2 => /lib/x86_64-linux-gnu/libresolv.so.2 (0x00007f726b0df000)
        libsasl2.so.2 => /lib/x86_64-linux-gnu/libsasl2.so.2 (0x00007f726b0c0000)
        libgpg-error.so.0 => /lib/x86_64-linux-gnu/libgpg-error.so.0 (0x00007f726b09d000)
        libffi.so.6 => /lib/x86_64-linux-gnu/libffi.so.6 (0x00007f726b093000)

