==============
GROMACS cloned
==============

clone
-----
milias@DESKTOP-7OTLCGO:~/work/software/gromacs/git_cloned/.git clone git@gitlab.com:gromacs/gromacs.git

build
-----
milias@DESKTOP-7OTLCGO:~/work/software/gromacs/git_cloned/gromacs/build_gnu/.cmake ..

CMake Error at CMakeLists.txt:34 (cmake_minimum_required):
  CMake 3.28 or higher is required.  You are running version 3.22.1

Ubuntu 24.04
~~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/gromacs/cloned/gromacs/.cmake --version
cmake version 3.28.3

milias@DESKTOP-7OTLCGO:~/work/software/gromacs/cloned/gromacs/build_gnu/.cmake -DGMX_MPI=ON .. > cmake.logile

milias@DESKTOP-7OTLCGO:~/work/software/gromacs/cloned/gromacs/build_gnu/.m -j8
.
.
milias@DESKTOP-7OTLCGO:~/work/software/gromacs/cloned/gromacs/build_gnu/.ldd bin/gmx_mpi
        linux-vdso.so.1 (0x00007ffda7bd8000)
        libgromacs_mpi.so.12 => /home/milias/work/software/gromacs/cloned/gromacs/build_gnu/bin/../lib/libgromacs_mpi.so.12 (0x000071789b000000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x000071789c96c000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x000071789ac00000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x000071789c93e000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x000071789a800000)
        libmpi_cxx.so.40 => /lib/x86_64-linux-gnu/libmpi_cxx.so.40 (0x000071789c923000)
        libfftw3f.so.3 => /lib/x86_64-linux-gnu/libfftw3f.so.3 (0x000071789a400000)
        libblas.so.3 => /lib/x86_64-linux-gnu/libblas.so.3 (0x000071789af59000)
        liblapack.so.3 => /lib/x86_64-linux-gnu/liblapack.so.3 (0x0000717899c00000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x000071789ab17000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x000071789af03000)
        libmuparser.so.2 => /home/milias/work/software/gromacs/cloned/gromacs/build_gnu/bin/../lib/../lib/libmuparser.so.2 (0x000071789aea4000)
        /lib64/ld-linux-x86-64.so.2 (0x000071789cac1000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x000071789aa5b000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x000071789a74c000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x000071789a6eb000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x0000717899800000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x000071789c903000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x000071789aa26000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x000071789c8fe000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x000071789a6b8000)
        libcap.so.2 => /lib/x86_64-linux-gnu/libcap.so.2 (0x000071789c8f1000)


CTests
------
milias@DESKTOP-7OTLCGO:~/work/software/gromacs/cloned/gromacs/build_gnu/.make -j8 tests

milias@DESKTOP-7OTLCGO:~/work/software/gromacs/cloned/gromacs/build_gnu/.make -j8 test
Running tests...
Test project /home/milias/work/software/gromacs/cloned/gromacs/build_gnu
        Start   1: GmxapiExternalInterfaceTests
  1/101 Test   #1: GmxapiExternalInterfaceTests ..............   Passed    1.22 sec
        Start   2: GmxapiMpiTests
  2/101 Test   #2: GmxapiMpiTests ............................   Passed    1.26 sec.
.
.
.








