mpi-test-suite
==============

milias@DESKTOP-7OTLCGO:~/work/software/mpi-test-suite/.git clone git@github.com:open-mpi/mpi-test-suite.git
Cloning into 'mpi-test-suite'...
remote: Enumerating objects: 1595, done.
remote: Counting objects: 100% (52/52), done.
remote: Compressing objects: 100% (33/33), done.
remote: Total 1595 (delta 21), reused 19 (delta 19), pack-reused 1543 (from 2)
Receiving objects: 100% (1595/1595), 544.70 KiB | 464.00 KiB/s, done.
Resolving deltas: 100% (1212/1212), done.

see error https://github.com/open-mpi/mpi-test-suite/issues/24#issuecomment-4236466820

milias@DESKTOP-7OTLCGO:~/work/software/mpi-test-suite/mpi-test-suite/../autogen.sh -v
autoreconf: export WARNINGS=
autoreconf: Entering directory '.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: aclocal --force
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: configure.ac: not using Intltool
autoreconf: configure.ac: not using Gtkdoc
autoreconf: running: /usr/bin/autoconf --force
configure.ac:14: warning: The macro "`AC_GNU_SOURCE'` is obsolete.
configure.ac:14: You should run autoupdate.
./lib/autoconf/specific.m4:312: AC_GNU_SOURCE is expanded from...
configure.ac:14: the top level
configure.ac:67: warning: The macro `AC_HEADER_STDC' is obsolete.
configure.ac:67: You should run autoupdate.
./lib/autoconf/headers.m4:704: AC_HEADER_STDC is expanded from...
configure.ac:67: the top level
autoreconf: running: /usr/bin/autoheader --force
autoreconf: running: automake --add-missing --copy --force-missing
configure.ac:14: installing './compile'
configure.ac:94: installing './config.guess'
configure.ac:94: installing './config.sub'
configure.ac:7: installing './install-sh'
configure.ac:7: installing './missing'
autoreconf: Leaving directory '.'
`
milias@DESKTOP-7OTLCGO:~/work/software/mpi-test-suite/mpi-test-suite/../configure --help
`configure' configures mpi_test_suite 1.1.1 to adapt to many kinds of systems.

Usage: ./configure [OPTION]... [VAR=VALUE]...

To assign environment variables (e.g., CC, CFLAGS...), specify them as
VAR=VALUE.  See below for descriptions of some of the useful variables.

Defaults for the options are specified in brackets.

Configuration:
  -h, --help              display this help and exit
      --help=short        display options specific to this package
      --help=recursive    display the short help of all the included packages
  -V, --version           display version information and exit
  -q, --quiet, --silent   do not print `checking ...' messages
      --cache-file=FILE   cache test results in FILE [disabled]
  -C, --config-cache      alias for `--cache-file=config.cache'
  -n, --no-create         do not create output files
      --srcdir=DIR        find the sources in DIR [configure dir or `..']

Installation directories:
  --prefix=PREFIX         install architecture-independent files in PREFIX
                          [/usr/local]
  --exec-prefix=EPREFIX   install architecture-dependent files in EPREFIX
                          [PREFIX]

By default, `make install' will install all the files in
`/usr/local/bin', `/usr/local/lib' etc.  You can specify
an installation prefix other than `/usr/local' using `--prefix',
for instance `--prefix=$HOME'.

For better control, use the options below.

Fine tuning of the installation directories:
  --bindir=DIR            user executables [EPREFIX/bin]
  --sbindir=DIR           system admin executables [EPREFIX/sbin]
  --libexecdir=DIR        program executables [EPREFIX/libexec]
  --sysconfdir=DIR        read-only single-machine data [PREFIX/etc]
  --sharedstatedir=DIR    modifiable architecture-independent data [PREFIX/com]
  --localstatedir=DIR     modifiable single-machine data [PREFIX/var]
  --runstatedir=DIR       modifiable per-process data [LOCALSTATEDIR/run]
  --libdir=DIR            object code libraries [EPREFIX/lib]
  --includedir=DIR        C header files [PREFIX/include]
  --oldincludedir=DIR     C header files for non-gcc [/usr/include]
  --datarootdir=DIR       read-only arch.-independent data root [PREFIX/share]
  --datadir=DIR           read-only architecture-independent data [DATAROOTDIR]
  --infodir=DIR           info documentation [DATAROOTDIR/info]
  --localedir=DIR         locale-dependent data [DATAROOTDIR/locale]
  --mandir=DIR            man documentation [DATAROOTDIR/man]
  --docdir=DIR            documentation root [DATAROOTDIR/doc/mpi_test_suite]
  --htmldir=DIR           html documentation [DOCDIR]
  --dvidir=DIR            dvi documentation [DOCDIR]
  --pdfdir=DIR            pdf documentation [DOCDIR]
  --psdir=DIR             ps documentation [DOCDIR]

Program names:
  --program-prefix=PREFIX            prepend PREFIX to installed program names
  --program-suffix=SUFFIX            append SUFFIX to installed program names
  --program-transform-name=PROGRAM   run sed PROGRAM on installed program names

System types:
  --build=BUILD     configure for building on BUILD [guessed]
  --host=HOST       cross-compile to build programs to run on HOST [BUILD]

Optional Features:
  --disable-option-checking  ignore unrecognized --enable/--with options
  --disable-FEATURE       do not include FEATURE (same as --enable-FEATURE=no)
  --enable-FEATURE[=ARG]  include FEATURE [ARG=yes]
  --enable-silent-rules   less verbose build output (undo: "make V=1")
  --disable-silent-rules  verbose build output (undo: "make V=0")
  --enable-mpi2           Build MPI2 tests [[default=yes]]
  --enable-mpi2-one-side  Build tests for MPI2 one-sided communication
                          [[default=yes]]
  --enable-mpi2-io        Build tests for MPI2 I/O [[default=yes]]
  --enable-mpi2-threads   Build tests for MPI2 thread support [[default=no]]
  --enable-mpi2-dynamic   Build tests for MPI2 dynamic process management
                          [[default=no]]
  --enable-mpi4-partitioned-p2p
                          Build tests for MPI4 partitioned P2P [[default=yes]]

Some influential environment variables:
  CC          C compiler command
  CFLAGS      C compiler flags
  LDFLAGS     linker flags, e.g. -L<lib dir> if you have libraries in a
              nonstandard directory <lib dir>
  LIBS        libraries to pass to the linker, e.g. -l<library>
  CPPFLAGS    (Objective) C/C++ preprocessor flags, e.g. -I<include dir> if
              you have headers in a nonstandard directory <include dir>
  CPP         C preprocessor
  MPICC       MPI C compiler command

Use these variables to override the choices made by `configure' or to help
it to find libraries and programs with nonstandard names/locations.

Report bugs to the package provider.
`

buildup
=======

milias@DESKTOP-7OTLCGO:~/work/software/mpi-test-suite/mpi-test-suite/../configure  --prefix=/home/milias/work/software/mpi-test-suite CC=mpicc

sudo apt-get install gengetopt

make 
.
.
comm.o tst_file.o tst_output.o tst_tests.o tst_threads.o tst_types.o
/usr/bin/ld: threaded/tst_threaded_ring_partitioned.o: in function `wait_for_partition':
/home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned.c:83:(.text+0x74): undefined reference to `MPI_Parrived'
/usr/bin/ld: threaded/tst_threaded_ring_partitioned.o: in function `tst_threaded_ring_partitioned_run':
/home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned.c:197:(.text+0x550): undefined reference to `MPI_Pready'
/usr/bin/ld: /home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned.c:154:(.text+0x6c9): undefined reference to `MPI_Psend_init'
/usr/bin/ld: /home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned.c:156:(.text+0x702): undefined reference to `MPI_Precv_init'
/usr/bin/ld: /home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned.c:175:(.text+0xa10): undefined reference to `MPI_Pready'
/usr/bin/ld: threaded/tst_threaded_ring_partitioned_many_to_one.o: in function `wait_for_partition':
/home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned_many_to_one.c:87:(.text+0x74): undefined reference to `MPI_Parrived'
/usr/bin/ld: threaded/tst_threaded_ring_partitioned_many_to_one.o: in function `tst_threaded_ring_partitioned_many_to_one_run':
/home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned_many_to_one.c:160:(.text+0x4da): undefined reference to `MPI_Psend_init'
/usr/bin/ld: /home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned_many_to_one.c:162:(.text+0x51a): undefined reference to `MPI_Precv_init'
/usr/bin/ld: /home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned_many_to_one.c:207:(.text+0x69a): undefined reference to `MPI_Pready'
/usr/bin/ld: /home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned_many_to_one.c:181:(.text+0x780): undefined reference to `MPI_Pready'
/usr/bin/ld: /home/milias/work/software/mpi-test-suite/mpi-test-suite/threaded/tst_threaded_ring_partitioned_many_to_one.c:181:(.text+0x8db): undefined reference to `MPI_Pready'
collect2: error: ld returned 1 exit status
make[1]: *** [Makefile:765: mpi_test_suite] Error 1
make[1]: Leaving directory '/home/milias/work/software/mpi-test-suite/mpi-test-suite'
make: *** [Makefile:522: all] Error 2
milias@DESKTOP-7OTLCGO:~/work/software/mpi-test-suite/mpi-test-suite/.


e libopenmpi-dev package version provided in the official Ubuntu 24.04 (Noble) repositories is 4.1.6-7ubuntu2. 
This version is the root cause of your error. Open MPI 4.1.x does not fully support the MPI_Pready, MPI_Parrived, and related partitioned communication functions, as these were standardized in MPI-4.0 and require Open MPI 5.0+. 

NEEDS NEWER PACKAGES !!!
https://ubuntu.pkgs.org/25.10/ubuntu-universe-arm64/openmpi-bin_5.0.8-8ubuntu1_arm64.deb.html
