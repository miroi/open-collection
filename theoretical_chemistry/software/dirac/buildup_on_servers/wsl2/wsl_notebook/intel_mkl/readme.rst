===============
DIRAC on WSL PC
===============

Uninstall MKL library packages
------------------------------
sudo apt-get remove intel-mkl-full libmkl-gf-ilp64 libmkl-gf-lp64 libmkl-gnu-thread libmkl-scalapack-ilp64 libmkl-scalapack-lp64

sudo  apt-get install hdf5-tools  libhdf5-openmpi-dev


kick on intel-mpi
------------------
source  /opt/intel/oneapi/2025.3/oneapi-vars.sh

mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2021.17 Build 20251215 (id: 2ac2f63)
Copyright 2003-2025, Intel Corporation.

miroi@MIRO:~/work/software/dirac/trunk_cloned/.mpiifx --version
ifx (IFX) 2025.3.2 20260112
Copyright (C) 1985-2026 Intel Corporation. All rights reserved.

miroi@MIRO:~/work/software/dirac/trunk_cloned/.mpiicx --version
Intel(R) oneAPI DPC++/C++ Compiler 2025.3.2 (2025.3.2.20260112)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/intel/oneapi/compiler/2025.3/bin/compiler
Configuration file: /opt/intel/oneapi/compiler/2025.3/bin/compiler/../icx.cfg

miroi@MIRO:~/work/software/dirac/trunk_cloned/.mpiicpx  --version
Intel(R) oneAPI DPC++/C++ Compiler 2025.3.2 (2025.3.2.20260112)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/intel/oneapi/compiler/2025.3/bin/compiler
Configuration file: /opt/intel/oneapi/compiler/2025.3/bin/compiler/../icpx.cfg


buildup
-------
./setup  --mpi --int64 --fc=mpiifx --cc=mpiicx --cxx=mpiicpx  --cmake-options="-D ENABLE_PELIB=OFF"  build_intelmpi_mkl_ilp64

miroi@MIRO:~/work/software/dirac/trunk_cloned/../setup  --mpi --int64 --fc=mpiifx --cc=mpiicx --cxx=mpiicpx  --cmake-options="-D ENABLE_PELIB=OFF"  build_intelmpi_mkl_ilp64   > build_intelmpi_mkl_ilp64.log 2>&1

compilation
~~~~~~~~~~~
miroi@MIRO:~/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/.make -j4 
.
.
.
[ 96%] Building Fortran object src/prp/CMakeFiles/prp.dir/london_reorth.F90.o
[ 97%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamxlr.F.o
[ 97%] Linking Fortran static library libprp.a
[ 97%] Built target prp
[ 97%] Linking Fortran static library libdiracobj.a
[ 97%] Built target diracobj
[ 98%] Building Fortran object CMakeFiles/dirac_mointegral_export.x.dir/utils/dirac_mointegral_export.F90.o
[ 98%] Building Fortran object CMakeFiles/dirac.x.dir/src/main/main.F90.o
[ 98%] Building Fortran object CMakeFiles/twofit.x.dir/utils/twofit.F90.o
[ 98%] Building Fortran object CMakeFiles/rspread.x.dir/utils/rspread.F90.o
[ 98%] Linking Fortran executable rspread.x
[ 98%] Linking Fortran executable dirac.x
[ 98%] Linking Fortran executable twofit.x
[ 98%] Built target rspread.x
[ 98%] Building Fortran object CMakeFiles/cfread.x.dir/utils/cfread.F90.o
[ 98%] Built target twofit.x
[ 98%] Building Fortran object CMakeFiles/cf_addlabels.x.dir/utils/cf_addlabels.F90.o
[ 98%] Linking Fortran executable dirac_mointegral_export.x
[ 98%] Linking Fortran executable cfread.x
INFO:basis set directories, basis*, synchronized into current installation directory
[ 98%] Linking Fortran executable cf_addlabels.x
[ 98%] Built target dirac_mointegral_export.x
[ 98%] Building Fortran object CMakeFiles/pcmo_addlabels.x.dir/utils/pcmo_addlabels.F90.o
[ 98%] Built target cfread.x
[ 98%] Building Fortran object CMakeFiles/vibcal.x.dir/utils/vibcal.F90.o
[ 98%] Built target cf_addlabels.x
[ 98%] Linking Fortran executable pcmo_addlabels.x
[ 98%] Building Fortran object CMakeFiles/polfit.x.dir/utils/polfit.F90.o
[ 98%] Linking Fortran executable polfit.x
[ 98%] Linking Fortran executable vibcal.x
[ 98%] Built target pcmo_addlabels.x
[ 99%] Building Fortran object CMakeFiles/mx2fit.x.dir/utils/mx2fit.F90.o
[ 99%] Built target dirac.x
[100%] Building Fortran object CMakeFiles/diag.x.dir/utils/diag.F90.o
[100%] Linking Fortran executable diag.x
[100%] Built target polfit.x
[100%] Building Fortran object CMakeFiles/test_allocator.x.dir/utils/test_allocator.F90.o
[100%] Built target vibcal.x
[100%] Building CXX object CMakeFiles/h5towfx.x.dir/utils/h5towfx.cpp.o
[100%] Linking Fortran executable mx2fit.x
[100%] Linking Fortran executable test_allocator.x
[100%] Built target mx2fit.x
[100%] Built target test_allocator.x
[100%] Built target diag.x
[100%] Linking CXX executable h5towfx.x
[100%] Built target h5towfx.x

verifying linked libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~
miroi@MIRO:~/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/.ldd dirac.x
        linux-vdso.so.1 (0x00007ffdf9983000)
        libmkl_intel_ilp64.so.2 => /opt/intel/oneapi/2025.3/lib/libmkl_intel_ilp64.so.2 (0x00007e3203400000)
        libmkl_intel_thread.so.2 => /opt/intel/oneapi/2025.3/lib/libmkl_intel_thread.so.2 (0x00007e3200c00000)
        libmkl_core.so.2 => /opt/intel/oneapi/2025.3/lib/libmkl_core.so.2 (0x00007e31fca00000)
        libimf.so => /opt/intel/oneapi/2025.3/lib/libimf.so (0x00007e31fc400000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007e32042b2000)
        libhdf5_serial.so.103 => /lib/x86_64-linux-gnu/libhdf5_serial.so.103 (0x00007e31fc000000)
        libcrypto.so.3 => /lib/x86_64-linux-gnu/libcrypto.so.3 (0x00007e31fba00000)
        libcurl.so.4 => /lib/x86_64-linux-gnu/libcurl.so.4 (0x00007e320333f000)
        libsz.so.2 => /lib/x86_64-linux-gnu/libsz.so.2 (0x00007e32042ab000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007e320428f000)
        libirng.so => /opt/intel/oneapi/2025.3/lib/libirng.so (0x00007e3200b07000)
        libmpi_ilp64.so => /opt/intel/oneapi/2025.3/lib/libmpi_ilp64.so (0x00007e31fb600000)
        libmpifort.so.12 => /opt/intel/oneapi/2025.3/lib/libmpifort.so.12 (0x00007e31fb200000)
        libmpi.so.12 => /opt/intel/oneapi/2025.3/lib/libmpi.so.12 (0x00007e31f1000000)
        libiomp5.so => /opt/intel/oneapi/2025.3/lib/libiomp5.so (0x00007e31f0a00000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007e31f0600000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007e3203311000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007e3204286000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007e3204281000)
        libintlc.so.5 => /opt/intel/oneapi/2025.3/lib/libintlc.so.5 (0x00007e32032ae000)
        /lib64/ld-linux-x86-64.so.2 (0x00007e32043b5000)
        libnghttp2.so.14 => /lib/x86_64-linux-gnu/libnghttp2.so.14 (0x00007e3203283000)
        libidn2.so.0 => /lib/x86_64-linux-gnu/libidn2.so.0 (0x00007e31fc9de000)
        librtmp.so.1 => /lib/x86_64-linux-gnu/librtmp.so.1 (0x00007e31fc9c0000)
        libssh.so.4 => /lib/x86_64-linux-gnu/libssh.so.4 (0x00007e31fc94f000)
        libpsl.so.5 => /lib/x86_64-linux-gnu/libpsl.so.5 (0x00007e320426b000)
        libssl.so.3 => /lib/x86_64-linux-gnu/libssl.so.3 (0x00007e31fc8a5000)
        libgssapi_krb5.so.2 => /lib/x86_64-linux-gnu/libgssapi_krb5.so.2 (0x00007e31fc851000)
        libldap.so.2 => /lib/x86_64-linux-gnu/libldap.so.2 (0x00007e31fc3a2000)
        liblber.so.2 => /lib/x86_64-linux-gnu/liblber.so.2 (0x00007e3203273000)
        libzstd.so.1 => /lib/x86_64-linux-gnu/libzstd.so.1 (0x00007e31fbf46000)
        libbrotlidec.so.1 => /lib/x86_64-linux-gnu/libbrotlidec.so.1 (0x00007e3200af9000)
        libaec.so.0 => /lib/x86_64-linux-gnu/libaec.so.0 (0x00007e31fc848000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007e31fc843000)
        libunistring.so.5 => /lib/x86_64-linux-gnu/libunistring.so.5 (0x00007e31fb853000)
        libgnutls.so.30 => /lib/x86_64-linux-gnu/libgnutls.so.30 (0x00007e31f0406000)
        libhogweed.so.6 => /lib/x86_64-linux-gnu/libhogweed.so.6 (0x00007e31fb1b8000)
        libnettle.so.8 => /lib/x86_64-linux-gnu/libnettle.so.8 (0x00007e31fb163000)
        libgmp.so.10 => /lib/x86_64-linux-gnu/libgmp.so.10 (0x00007e31fb0df000)
        libkrb5.so.3 => /lib/x86_64-linux-gnu/libkrb5.so.3 (0x00007e31f0f37000)
        libk5crypto.so.3 => /lib/x86_64-linux-gnu/libk5crypto.so.3 (0x00007e31fc376000)
        libcom_err.so.2 => /lib/x86_64-linux-gnu/libcom_err.so.2 (0x00007e31fc83d000)
        libkrb5support.so.0 => /lib/x86_64-linux-gnu/libkrb5support.so.0 (0x00007e31fc830000)
        libsasl2.so.2 => /lib/x86_64-linux-gnu/libsasl2.so.2 (0x00007e31fbf2c000)
        libbrotlicommon.so.1 => /lib/x86_64-linux-gnu/libbrotlicommon.so.1 (0x00007e31f0f14000)
        libp11-kit.so.0 => /lib/x86_64-linux-gnu/libp11-kit.so.0 (0x00007e31f085c000)
        libtasn1.so.6 => /lib/x86_64-linux-gnu/libtasn1.so.6 (0x00007e31fbf16000)
        libkeyutils.so.1 => /lib/x86_64-linux-gnu/libkeyutils.so.1 (0x00007e31fc829000)
        libresolv.so.2 => /lib/x86_64-linux-gnu/libresolv.so.2 (0x00007e31fb840000)
        libffi.so.8 => /lib/x86_64-linux-gnu/libffi.so.8 (0x00007e31fb0d3000)


Tests
~~~~~
miroi@MIRO:~/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/.export DIRAC_MPI_COMMAND="mpirun -np 2"

miroi@MIRO:~/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/.ctest -L short -j2
Test project /home/miroi/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64
.
.


