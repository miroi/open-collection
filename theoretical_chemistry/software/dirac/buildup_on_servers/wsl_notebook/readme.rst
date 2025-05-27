===============
DIRAC on WSL PC
===============

MKL library
------------
sudo apt-get install intel-mkl-full libmkl-gf-ilp64 libmkl-gf-lp64 libmkl-gnu-thread libmkl-scalapack-ilp64 libmkl-scalapack-lp64

sudo  apt-get install hdf5-tools  libhdf5-openmpi-dev

mpif90 --version
GNU Fortran (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

mpicc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

mpicxx --version
g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

mpirun --version
mpirun (Open MPI) 4.1.2

buildup
~~~~~~~
./setup  -mpi  --fc=mpif90 --cc=mpicc --cxx=mpicxx  --cmake-options="-D ENABLE_PELIB=ON"  build_gnu_mkl_lp64

or 

./setup  --mpi --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx  --cmake-options="-D ENABLE_PELIB=OFF"  build_gnu_mkl_ilp64
.
.
[ 90%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamexp.F.o
[ 90%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamfck.F.o
[ 91%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamgrd.F.o
[ 91%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamogrd.F.o
[ 91%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamrsp.F.o
[ 92%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamstex.F.o
[ 92%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamnqcc.F.o
[ 92%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamtpa.F.o
[ 92%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamxpp.F.o
[ 92%] Building Fortran object src/prp/CMakeFiles/prp.dir/rspmpg.F.o
[ 93%] Building Fortran object src/prp/CMakeFiles/prp.dir/van_der_waals.F.o
[ 93%] Building Fortran object src/prp/CMakeFiles/prp.dir/bed_osc.F90.o
[ 93%] Building Fortran object src/prp/CMakeFiles/prp.dir/__/dirac/dirgrd.F.o
[ 94%] Building Fortran object src/prp/CMakeFiles/prp.dir/paminp.F90.o
[ 94%] Building Fortran object src/prp/CMakeFiles/prp.dir/pammag.F.o
[ 94%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamprp.F.o
[ 94%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamrvc.F.o
[ 94%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamset.F.o
[ 94%] Building Fortran object src/prp/CMakeFiles/prp.dir/london_reorth.F90.o
[ 94%] Building Fortran object src/prp/CMakeFiles/prp.dir/pamxlr.F.o
[ 94%] Built target prp
[ 95%] Linking Fortran static library libobjlib.dirac.x.a
[ 95%] Linking Fortran static library libobjlib.labread.x.a
[ 95%] Linking Fortran static library libobjlib.rspread.x.a
[ 95%] Linking Fortran static library libobjlib.dirac_mointegral_export.x.a
[ 95%] Built target objlib.rspread.x
[ 95%] Linking Fortran static library libobjlib.twofit.x.a
[ 95%] Built target objlib.labread.x
[ 95%] Built target objlib.dirac_mointegral_export.x
[ 95%] Built target objlib.dirac.x
[ 95%] Linking Fortran static library libobjlib.cfread.x.a
[ 95%] Linking Fortran static library libobjlib.cf_addlabels.x.a
[ 95%] Linking Fortran static library libobjlib.pcmo_addlabels.x.a
[ 95%] Built target objlib.twofit.x
[ 95%] Linking Fortran static library libobjlib.vibcal.x.a
[ 95%] Built target objlib.cf_addlabels.x
[ 95%] Built target objlib.cfread.x
[ 96%] Linking Fortran static library libobjlib.polfit.x.a
[ 96%] Linking Fortran static library libobjlib.mx2fit.x.a
[ 96%] Built target objlib.pcmo_addlabels.x
[ 96%] Linking Fortran static library libobjlib.diag.x.a
[ 96%] Built target objlib.vibcal.x
[ 96%] Linking Fortran static library libobjlib.test_allocator.x.a
[ 96%] Built target objlib.polfit.x
[ 96%] Built target objlib.mx2fit.x
Scanning dependencies of target dirac.x
[ 96%] Linking Fortran static library libobjlib.h5towfx.x.a
[ 96%] Building Fortran object CMakeFiles/dirac.x.dir/src/main/main.F90.o
[ 96%] Built target objlib.diag.x
Scanning dependencies of target dirac_mointegral_export.x
[ 96%] Building Fortran object CMakeFiles/dirac_mointegral_export.x.dir/utils/dirac_mointegral_export.F90.o
[ 96%] Linking Fortran executable dirac.x
INFO:basis set directories, basis*, synchronized into current installation directory
[ 96%] Built target objlib.test_allocator.x
Scanning dependencies of target rspread.x
[ 96%] Building Fortran object CMakeFiles/rspread.x.dir/utils/rspread.F90.o
[ 96%] Linking Fortran executable rspread.x
[ 96%] Built target objlib.h5towfx.x
Scanning dependencies of target labread.x
[ 97%] Building Fortran object CMakeFiles/labread.x.dir/utils/labread.F90.o
[ 97%] Linking Fortran executable dirac_mointegral_export.x
[ 97%] Linking Fortran executable labread.x
[ 97%] Built target dirac.x
Scanning dependencies of target twofit.x
[ 97%] Building Fortran object CMakeFiles/twofit.x.dir/utils/twofit.F90.o
[ 97%] Built target rspread.x
Scanning dependencies of target cfread.x
[ 97%] Building Fortran object CMakeFiles/cfread.x.dir/utils/cfread.F90.o
[ 97%] Linking Fortran executable cfread.x
[ 97%] Built target dirac_mointegral_export.x
Scanning dependencies of target cf_addlabels.x
[ 98%] Building Fortran object CMakeFiles/cf_addlabels.x.dir/utils/cf_addlabels.F90.o
[ 98%] Built target labread.x
Scanning dependencies of target pcmo_addlabels.x
[ 98%] Building Fortran object CMakeFiles/pcmo_addlabels.x.dir/utils/pcmo_addlabels.F90.o
[ 98%] Linking Fortran executable cf_addlabels.x
[ 98%] Linking Fortran executable pcmo_addlabels.x
[ 98%] Linking Fortran executable twofit.x
[ 98%] Built target cfread.x
Scanning dependencies of target vibcal.x
[ 98%] Building Fortran object CMakeFiles/vibcal.x.dir/utils/vibcal.F90.o
[ 98%] Built target cf_addlabels.x
Scanning dependencies of target polfit.x
[ 99%] Building Fortran object CMakeFiles/polfit.x.dir/utils/polfit.F90.o
[ 99%] Built target twofit.x
Scanning dependencies of target mx2fit.x
[ 99%] Building Fortran object CMakeFiles/mx2fit.x.dir/utils/mx2fit.F90.o
[ 99%] Built target pcmo_addlabels.x
Scanning dependencies of target diag.x
[ 99%] Building Fortran object CMakeFiles/diag.x.dir/utils/diag.F90.o
[ 99%] Linking Fortran executable diag.x
[ 99%] Linking Fortran executable polfit.x
[ 99%] Linking Fortran executable mx2fit.x
[100%] Linking Fortran executable vibcal.x
[100%] Built target diag.x
Scanning dependencies of target test_allocator.x
[100%] Building Fortran object CMakeFiles/test_allocator.x.dir/utils/test_allocator.F90.o
[100%] Built target polfit.x
[100%] Building CXX object CMakeFiles/h5towfx.x.dir/utils/h5towfx.cpp.o
[100%] Linking Fortran executable test_allocator.x
[100%] Built target mx2fit.x
[100%] Built target vibcal.x
[100%] Built target test_allocator.x
[100%] Linking CXX executable h5towfx.x
[100%] Built target h5towfx.x
miroi@MIRO:~/work/software/dirac/trunk/build_gnu_mkl_ilp64/.
miroi@MIRO:~/work/software/dirac/trunk/build_gnu_mkl_ilp64/.ldd dirac.x
        linux-vdso.so.1 (0x00007ffde79f3000)
        libmkl_gf_ilp64.so => /lib/x86_64-linux-gnu/libmkl_gf_ilp64.so (0x00007f0cc3a00000)
        libmkl_gnu_thread.so => /lib/x86_64-linux-gnu/libmkl_gnu_thread.so (0x00007f0cc1c00000)
        libmkl_core.so => /lib/x86_64-linux-gnu/libmkl_core.so (0x00007f0cbd400000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007f0cbd125000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f0cc46a5000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x00007f0cc1b03000)
        libhdf5_openmpi.so.103 => /lib/x86_64-linux-gnu/libhdf5_openmpi.so.103 (0x00007f0cbcd70000)
        libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007f0cc399a000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x00007f0cbcc39000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x00007f0cc1ab9000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f0cc4685000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f0cbca10000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f0cc3993000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f0cc398e000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f0cc1a71000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f0ce623d000)
        libcrypto.so.3 => /lib/x86_64-linux-gnu/libcrypto.so.3 (0x00007f0cbc5cc000)
        libcurl.so.4 => /lib/x86_64-linux-gnu/libcurl.so.4 (0x00007f0cbc525000)
        libsz.so.2 => /lib/x86_64-linux-gnu/libsz.so.2 (0x00007f0cc3987000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f0cc396b000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007f0cbc472000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007f0cbc3b5000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x00007f0cbc359000)
        libnghttp2.so.14 => /lib/x86_64-linux-gnu/libnghttp2.so.14 (0x00007f0cc1a47000)
        libidn2.so.0 => /lib/x86_64-linux-gnu/libidn2.so.0 (0x00007f0cbc338000)
        librtmp.so.1 => /lib/x86_64-linux-gnu/librtmp.so.1 (0x00007f0cbc319000)
        libssh.so.4 => /lib/x86_64-linux-gnu/libssh.so.4 (0x00007f0cbc2ac000)
        libpsl.so.5 => /lib/x86_64-linux-gnu/libpsl.so.5 (0x00007f0cbc298000)
        libssl.so.3 => /lib/x86_64-linux-gnu/libssl.so.3 (0x00007f0cbc1f4000)
        libgssapi_krb5.so.2 => /lib/x86_64-linux-gnu/libgssapi_krb5.so.2 (0x00007f0cbc1a0000)
        libldap-2.5.so.0 => /lib/x86_64-linux-gnu/libldap-2.5.so.0 (0x00007f0cbc140000)
        liblber-2.5.so.0 => /lib/x86_64-linux-gnu/liblber-2.5.so.0 (0x00007f0cbc12f000)
        libzstd.so.1 => /lib/x86_64-linux-gnu/libzstd.so.1 (0x00007f0cbc060000)
        libbrotlidec.so.1 => /lib/x86_64-linux-gnu/libbrotlidec.so.1 (0x00007f0cbc052000)
        libaec.so.0 => /lib/x86_64-linux-gnu/libaec.so.0 (0x00007f0cbc049000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x00007f0cbc014000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x00007f0cc3960000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007f0cbbfea000)
        libunistring.so.2 => /lib/x86_64-linux-gnu/libunistring.so.2 (0x00007f0cbbe40000)
        libgnutls.so.30 => /lib/x86_64-linux-gnu/libgnutls.so.30 (0x00007f0cbbc55000)
        libhogweed.so.6 => /lib/x86_64-linux-gnu/libhogweed.so.6 (0x00007f0cbbc0d000)
        libnettle.so.8 => /lib/x86_64-linux-gnu/libnettle.so.8 (0x00007f0cbbbc7000)
        libgmp.so.10 => /lib/x86_64-linux-gnu/libgmp.so.10 (0x00007f0cbbb45000)
        libkrb5.so.3 => /lib/x86_64-linux-gnu/libkrb5.so.3 (0x00007f0cbba7a000)
        libk5crypto.so.3 => /lib/x86_64-linux-gnu/libk5crypto.so.3 (0x00007f0cbba4b000)
        libcom_err.so.2 => /lib/x86_64-linux-gnu/libcom_err.so.2 (0x00007f0cbba45000)
        libkrb5support.so.0 => /lib/x86_64-linux-gnu/libkrb5support.so.0 (0x00007f0cbba37000)
        libsasl2.so.2 => /lib/x86_64-linux-gnu/libsasl2.so.2 (0x00007f0cbba1c000)
        libbrotlicommon.so.1 => /lib/x86_64-linux-gnu/libbrotlicommon.so.1 (0x00007f0cbb9f9000)
        libp11-kit.so.0 => /lib/x86_64-linux-gnu/libp11-kit.so.0 (0x00007f0cbb8be000)
        libtasn1.so.6 => /lib/x86_64-linux-gnu/libtasn1.so.6 (0x00007f0cbb8a6000)
        libkeyutils.so.1 => /lib/x86_64-linux-gnu/libkeyutils.so.1 (0x00007f0cbb89f000)
        libresolv.so.2 => /lib/x86_64-linux-gnu/libresolv.so.2 (0x00007f0cbb88b000)
        libffi.so.8 => /lib/x86_64-linux-gnu/libffi.so.8 (0x00007f0cbb87e000)

Tests
~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64/.export DIRAC_MPI_COMMAND="mpirun -np 2"
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64/.ctest -L short -j2
