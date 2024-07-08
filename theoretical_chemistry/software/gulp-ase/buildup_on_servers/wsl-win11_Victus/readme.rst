==========================================
GULP install on WSL-Win11 Victus notebook
==========================================

https://wiki.fysik.dtu.dk/ase/ase/calculators/gulp.html#gulp

installing packages
~~~~~~~~~~~~~~~~~~~

sudo apt-cache search scalapack
sudo apt-get install  libscalapack-openmpi2.1  libscalapack-openmpi-dev scalapack-test-common
sudo apt install libfftw3-mpi-dev  libfftw3-dev


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

ldd gulp

