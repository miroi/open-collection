==========================================
GULP install on WSL-Win11 Victus notebook
==========================================

https://wiki.fysik.dtu.dk/ase/ase/calculators/gulp.html#gulp

installing packages
~~~~~~~~~~~~~~~~~~~

sudo apt-cache search scalapack
sudo apt-get install  libscalapack-openmpi2.1  libscalapack-openmpi-dev scalapack-test-common
sudo apt install libfftw3-mpi-dev  libfftw3-dev
sudo apt install libkim-api-dev  libkim-api2


mkgulp configuration
~~~~~~~~~~~~~~~~~~~~~
get modified mkgulp for kim-api, fftw3, elpa, scalapack, liblapack objects !

ls /lib/x86_64-linux-gnu/kim-api/
mod/              model-drivers/    portable-models/  simulator-models/


ls /usr/lib/x86_64-linux-gnu/libscalapack-*
/usr/lib/x86_64-linux-gnu/libscalapack-mpich.so.2.1@   /usr/lib/x86_64-linux-gnu/libscalapack-openmpi.so.2.1@
/usr/lib/x86_64-linux-gnu/libscalapack-mpich.so.2.1.0  /usr/lib/x86_64-linux-gnu/libscalapack-openmpi.so.2.1.0
/usr/lib/x86_64-linux-gnu/libscalapack-openmpi.so@a

ls /usr/lib/x86_64-linux-gnu/liblapack*
/usr/lib/x86_64-linux-gnu/liblapack.a@   /usr/lib/x86_64-linux-gnu/liblapack.so.3@    /usr/lib/x86_64-linux-gnu/liblapack_pic.a
/usr/lib/x86_64-linux-gnu/liblapack.so@  /usr/lib/x86_64-linux-gnu/liblapack64.so.3@

ls  /usr/include/fftw3*
/usr/include/fftw3-mpi.f03  /usr/include/fftw3-mpi.h  /usr/include/fftw3l-mpi.f03

dpkg -S kim-api  | grep libkim-api.so
libkim-api2:amd64: /usr/lib/x86_64-linux-gnu/libkim-api.so.2
libkim-api2:amd64: /usr/lib/x86_64-linux-gnu/libkim-api.so.2.2.1
libkim-api-dev: /usr/lib/x86_64-linux-gnu/libkim-api.so

dpkg -S fftw3_mpi
libfftw3-mpi-dev:amd64: /usr/lib/x86_64-linux-gnu/libfftw3_mpi.a
libfftw3-mpi3:amd64: /usr/lib/x86_64-linux-gnu/libfftw3_mpi.so.3
libfftw3-mpi-dev:amd64: /usr/lib/x86_64-linux-gnu/libfftw3_mpi.so
libfftw3-mpi3:amd64: /usr/lib/x86_64-linux-gnu/libfftw3_mpi.so.3.5.8

dpkg -S fftw3


ls /usr/include/elpa/modules/
elpa.mod  elpa_api.mod  elpa_constants.mod

ls /lib/x86_64-linux-gnu/kim-api/mod
.
.
kim_charge_unit_module.mod                      kim_model_driver_create_module.mod
kim_collection_item_type_module.mod             kim_model_driver_headers_module.mod
.

compilation
~~~~~~~~~~~
...gulp/gulp-6.2/Src/.cp mkgulp mkgulp.orig
...gulp/gulp-6.2/Src/../mkgulp -e -f -k -m -j8

.
.
mpif90 -fallow-argument-mismatch  -O3 -ffpe-summary=invalid,zero,overflow  -I.. -I/usr/include/   -I/lib/x86_64-linux-gnu/kim-api/mod/ -I/usr/include/elpa/modules/  -DFLUSH -DNOFOX  -DMPI   -DKIM -DELPA -DFFTW3  -c ../property3.F90
.
.
... screenct.o reaxffctfunct.o kim_functions.o setkim.o kimmd.o trap_sigint.o m_gulp_interface.o  csignal.o  CS_dummy.o -L/usr/lib/x86_64-linux-gnu/ -lscalapack-openmpi -llapack -lblas -L/usr/lib/x86_64-linux-gnu/ -lfftw3 -lfftw3_mpi -L/usr/lib/x86_64-linux-gnu -lkim-api   -L/usr/lib/x86_64-linux-gnu/ -lelpa  zdotc.o   ../../Utils/pGFNFF/Src//libpGFNFF.a -o gulp

milias@Miro:~/work/software/gulp/gulp-6.2/Src/.ldd gulp
        linux-vdso.so.1 (0x00007ffdd35b3000)
        libscalapack-openmpi.so.2.1 => /lib/x86_64-linux-gnu/libscalapack-openmpi.so.2.1 (0x00007f40f7d5a000)
        liblapack.so.3 => /lib/x86_64-linux-gnu/liblapack.so.3 (0x00007f40f7695000)
        libblas.so.3 => /lib/x86_64-linux-gnu/libblas.so.3 (0x00007f40f7633000)
        libfftw3.so.3 => /lib/x86_64-linux-gnu/libfftw3.so.3 (0x00007f40f7418000)
        libfftw3_mpi.so.3 => /lib/x86_64-linux-gnu/libfftw3_mpi.so.3 (0x00007f40f73fe000)
        libkim-api.so.2 => /lib/x86_64-linux-gnu/libkim-api.so.2 (0x00007f40f72f6000)
        libelpa.so.17 => /lib/x86_64-linux-gnu/libelpa.so.17 (0x00007f40f71a6000)
        libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007f40f7140000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007f40f6e65000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f40f6d7e000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x00007f40f6c81000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f40f6c5f000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f40f6a36000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x00007f40f68ff000)
        libopenblas.so.0 => /lib/x86_64-linux-gnu/libopenblas.so.0 (0x00007f40f44b0000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f40f44ab000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f40f427d000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007f40f41ca000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f40f4182000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f40f9a6a000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007f40f40c5000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x00007f40f4067000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x00007f40f4032000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x00007f40f402d000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f40f4011000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007f40f3fe7000)
