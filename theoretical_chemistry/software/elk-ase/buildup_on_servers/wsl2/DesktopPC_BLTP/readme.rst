===========================
WSL2 milias@DESKTOP-7OTLCGO
===========================

https://elk.sourceforge.io/

https://elk.sourceforge.io/elk.pdf

donwload
--------
https://sourceforge.net/projects/elk/files/latest/download

milias@DESKTOP-7OTLCGO:~/work/software/elk/.tar -xvzf elk-11.0.2.tgz


buildup
-------

make.inc
~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/elk/elk-11.0.2/.cp make.inc make.inc_orig

# GNU Fortran compiler with OpenBLAS, LAPACK and FFTW.
F90 = mpif90
F90_OPTS = -Ofast -march=native -mtune=native -fopenmp -ffpe-summary=none -Wno-lto-type-mismatch
F90_LIB = -lopenblas -llapack -lfftw3 -lfftw3f
SRC_OBLAS =


Ubuntu packages
~~~~~~~~~~~~~~~
sudo apt-get install liblapack3 liblapack-dev libfftw3-dev libfftw3-bin libfftw3-doc
sudo apt install libopenblas-dev libopenblas0-openmp libopenblas64-0-openmp

man fftw-wisdom

ls /usr/lib/x86_64-linux-gnu/openblas-openmp/
libblas.so.3  liblapack.so.3  libopenblas.so.0@  libopenblasp-r0.3.26.so

ls /usr/lib/x86_64-linux-gnu/openblas64-openmp/
libblas64.so.3  liblapack64.so.3  libopenblas64.so.0@  libopenblas64p-r0.3.26.so

compilation
~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/elk/elk-11.0.2/.make all

milias@DESKTOP-7OTLCGO:~/work/software/elk/elk-11.0.2/.ldd src/elk
        linux-vdso.so.1 (0x00007569a0340000)
        libopenblas.so.0 => /lib/x86_64-linux-gnu/libopenblas.so.0 (0x000075699da20000)
        libfftw3.so.3 => /lib/x86_64-linux-gnu/libfftw3.so.3 (0x000075699d600000)
        libfftw3f.so.3 => /lib/x86_64-linux-gnu/libfftw3f.so.3 (0x000075699d200000)
        libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007569a02c7000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x000075699ce00000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007569a01dc000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x000075699d927000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x000075699d8d1000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007569a01ae000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x000075699ca00000)
        /lib64/ld-linux-x86-64.so.2 (0x00007569a0342000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x000075699d4ce000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x000075699d14c000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x000075699cd44000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x000075699d870000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x000075699d83b000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x00007569a01a5000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x000075699d4b2000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x000075699d47f000)
        libcap.so.2 => /lib/x86_64-linux-gnu/libcap.so.2 (0x00007569a0198000)

tests
~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/elk/elk-11.0.2/.make  VERBOSE=1  test-all >  make-test-all.log 2>&1



