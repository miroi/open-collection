=====================================
GULP install on WSL-Win10 Desktop PC  
=====================================

https://wiki.fysik.dtu.dk/ase/ase/calculators/gulp.html#gulp

installing packages
~~~~~~~~~~~~~~~~~~~


milias@pc7321b:~/work/software/gulp/gulp-6.2/Src/.ls /lib/x86_64-linux-gnu/kim-api/
mod/              model-drivers/    portable-models/  simulator-models/

sudo apt-cache search scalapack
sudo apt-get install  libscalapack-openmpi2.1  libscalapack-openmpi-dev scalapack-test-common

mkgulp configuration
~~~~~~~~~~~~~~~~~~~~~
modify mkgulp for kim-api, fftw3, elpa, scalapack, liblapack objects !

milias@pc7321b:~/work/software/gulp/gulp-6.2/Src/.ls /usr/lib/x86_64-linux-gnu/libscalapack-*
/usr/lib/x86_64-linux-gnu/libscalapack-mpich.so.2.1@   /usr/lib/x86_64-linux-gnu/libscalapack-openmpi.so.2.1@
/usr/lib/x86_64-linux-gnu/libscalapack-mpich.so.2.1.0  /usr/lib/x86_64-linux-gnu/libscalapack-openmpi.so.2.1.0
/usr/lib/x86_64-linux-gnu/libscalapack-openmpi.so@a

milias@pc7321b:~/work/software/gulp/gulp-6.2/Src/.ls /usr/lib/x86_64-linux-gnu/liblapack*
/usr/lib/x86_64-linux-gnu/liblapack.a@   /usr/lib/x86_64-linux-gnu/liblapack.so.3@    /usr/lib/x86_64-linux-gnu/liblapack_pic.a
/usr/lib/x86_64-linux-gnu/liblapack.so@  /usr/lib/x86_64-linux-gnu/liblapack64.so.3@


milias@pc7321b:~/work/software/gulp/gulp-6.2/Src/.cp mkgulp mkgulp.orig

milias@pc7321b:~/work/software/gulp/gulp-6.2/Src/.dpkg -S kim-api  | grep libkim-api.so
libkim-api2:amd64: /usr/lib/x86_64-linux-gnu/libkim-api.so.2
libkim-api2:amd64: /usr/lib/x86_64-linux-gnu/libkim-api.so.2.2.1
libkim-api-dev: /usr/lib/x86_64-linux-gnu/libkim-api.so

milias@pc7321b:~/work/software/gulp/gulp-6.2/Src/.dpkg -S fftw3_mpi
libfftw3-mpi-dev:amd64: /usr/lib/x86_64-linux-gnu/libfftw3_mpi.a
libfftw3-mpi3:amd64: /usr/lib/x86_64-linux-gnu/libfftw3_mpi.so.3
libfftw3-mpi-dev:amd64: /usr/lib/x86_64-linux-gnu/libfftw3_mpi.so
libfftw3-mpi3:amd64: /usr/lib/x86_64-linux-gnu/libfftw3_mpi.so.3.5.8

dpkg -S fftw3

milias@pc7321b:~/work/software/gulp/gulp-6.2/Src/.cp  mkgulp /mnt/c/Users/milias/Documents/git-projects/open-collection/theoretical_chemistry/software/gulp-ase/buildup_on_servers/jinr_ru/wsl-win10-desktopPC/.

compilation
~~~~~~~~~~~
milias@pc7321b:~/work/software/gulp/gulp-6.2/Src/../mkgulp -e -f -k -m -j8

.
.
mpif90 -fallow-argument-mismatch  -O3 -ffpe-summary=invalid,zero,overflow  -I.. -I/usr/include/   -I/lib/x86_64-linux-gnu/kim-api/mod/ -I/usr/include/elpa/modules/  -DFLUSH -DNOFOX  -DMPI   -DKIM -DELPA -DFFTW3  -c ../property3.F90
.
.
... screenct.o reaxffctfunct.o kim_functions.o setkim.o kimmd.o trap_sigint.o m_gulp_interface.o  csignal.o  CS_dummy.o -L/usr/lib/x86_64-linux-gnu/ -lscalapack-openmpi -llapack -lblas -L/usr/lib/x86_64-linux-gnu/ -lfftw3 -lfftw3_mpi -L/usr/lib/x86_64-linux-gnu -lkim-api   -L/usr/lib/x86_64-linux-gnu/ -lelpa  zdotc.o   ../../Utils/pGFNFF/Src//libpGFNFF.a -o gulp

milias@pc7321b:~/work/software/gulp/gulp-6.2/Src/.ldd gulp
        linux-vdso.so.1 (0x00007ffee5fe8000)
        libscalapack-openmpi.so.2.1 => /lib/x86_64-linux-gnu/libscalapack-openmpi.so.2.1 (0x00007fef2432f000)
        liblapack.so.3 => /lib/x86_64-linux-gnu/liblapack.so.3 (0x00007fef23c6a000)
        libblas.so.3 => /lib/x86_64-linux-gnu/libblas.so.3 (0x00007fef23c08000)
        libfftw3.so.3 => /lib/x86_64-linux-gnu/libfftw3.so.3 (0x00007fef239ed000)
        libfftw3_mpi.so.3 => /lib/x86_64-linux-gnu/libfftw3_mpi.so.3 (0x00007fef239d3000)
        libkim-api.so.2 => /lib/x86_64-linux-gnu/libkim-api.so.2 (0x00007fef238cb000)
        libelpa.so.17 => /lib/x86_64-linux-gnu/libelpa.so.17 (0x00007fef2377b000)
        libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007fef23715000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007fef2343a000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fef23353000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x00007fef23256000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fef23234000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fef2300b000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x00007fef22ed4000)
        libopenblas.so.0 => /lib/x86_64-linux-gnu/libopenblas.so.0 (0x00007fef20a80000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fef22ecf000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fef20852000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007fef2079f000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007fef20757000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fef2602c000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007fef2069a000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x00007fef2063e000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x00007fef20607000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x00007fef20602000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007fef205e6000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007fef205bc000)
milias@pc7321b:~/work/software/gulp/gulp-6.2/Src/.

