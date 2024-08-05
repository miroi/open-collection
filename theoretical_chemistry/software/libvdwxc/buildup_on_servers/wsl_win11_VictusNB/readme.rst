========
libvdwxc
========

https://gitlab.com/libvdwxc/libvdwxc


milias@Miro:~/work/software/libvdwxc/.git clone git@gitlab.com:libvdwxc/libvdwxc.git libvdwxc_cloned

milias@Miro:~/work/software/libvdwxc/libvdwxc_cloned/../autogen.sh
Generating aclocal.m4...
done.
Generating config.h.in...
done.
Generating configure script...
configure.ac:25: warning: 'AM_CONFIG_HEADER': this macro is obsolete.
configure.ac:25: You should use the 'AC_CONFIG_HEADERS' macro instead.
./lib/autoconf/general.m4:2434: AC_DIAGNOSE is expanded from...
aclocal.m4:9799: AM_CONFIG_HEADER is expanded from...
configure.ac:25: the top level
configure.ac:522: warning: AC_OUTPUT should be used without arguments.
configure.ac:522: You should run autoupdate.
done.
Generating libtool scripts...
done.
Generating Makefile.in for each directory...
configure.ac:311: installing 'config/gnu/compile'
configure.ac:23: installing 'config/gnu/config.guess'
configure.ac:23: installing 'config/gnu/config.sub'
configure.ac:24: installing 'config/gnu/install-sh'
configure.ac:24: installing 'config/gnu/missing'
src/Makefile.am: installing 'config/gnu/depcomp'
done.

milias@Miro:~/work/software/libvdwxc/libvdwxc_cloned/../configure --prefix=$PWD  --with-mpi  --with-fftw3

make
make install


milias@Miro:~/work/software/libvdwxc/libvdwxc_cloned/.ls bin/
libvdwxc_fdtest*  libvdwxc_info*  libvdwxc_maintest*  libvdwxc_q0test*  libvdwxc_q0test2*
milias@Miro:~/work/software/libvdwxc/libvdwxc_cloned/.ls lib/
libvdwxc.a    libvdwxc.so@    libvdwxc.so.0.0.0*  libvdwxcfort.la*  libvdwxcfort.so.0@      pkgconfig/
libvdwxc.la*  libvdwxc.so.0@  libvdwxcfort.a      libvdwxcfort.so@  libvdwxcfort.so.0.0.0*
milias@Miro:~/work/software/libvdwxc/libvdwxc_cloned/.ls include/
vdwxc.h  vdwxc_mpi.h  vdwxc_version.h  vdwxcfort.f90
milias@Miro:~/work/software/libvdwxc/libvdwxc_cloned/.ls lib
libvdwxc.a    libvdwxc.so@    libvdwxc.so.0.0.0*  libvdwxcfort.la*  libvdwxcfort.so.0@      pkgconfig/
libvdwxc.la*  libvdwxc.so.0@  libvdwxcfort.a      libvdwxcfort.so@  libvdwxcfort.so.0.0.0*
milias@Miro:~/work/software/libvdwxc/libvdwxc_cloned/.


Tests
~~~~~
milias@Miro:~/work/software/libvdwxc/libvdwxc_cloned/bin/.ls
libvdwxc_fdtest*  libvdwxc_info*  libvdwxc_maintest*  libvdwxc_q0test*  libvdwxc_q0test2*

pkg-config
~~~~~~~~~~
milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/libvdwxc/buildup_on_servers/wsl_win11_VictusNB/.export PKG_CONFIG_PATH=/home/milias/work/software/libvdwxc/libvdwxc_cloned/lib/pkgconfig

pkg-config --libs libvdwxc
-L/home/milias/work/software/libvdwxc/libvdwxc_cloned/lib -lvdwxc -lfftw3

