labs.fpv.umb.sk
===============

from https://ftp.gnu.org/gnu/gcc/gcc-9.5.0/

see https://gcc.gnu.org/wiki/InstallingGCC

milias@labs.fpv.umb.sk:~/work/software/gnu_fortran/.wget https://ftp.gnu.org/gnu/gcc/gcc-9.5.0/gcc-9.5.0.tar.gz
tar xvzf gcc-9.5.0.tar.gzgcc-9.5.0.tar.gz

milias@labs.fpv.umb.sk:~/work/software/gnu_fortran/objdir/.$PWD/../gcc-9.5.0/configure --prefix=$HOME/work/software/gnu_fortran/gcc-9.5.0  --enable-languages=c,c++,fortran,go

crashed:
collect2: error: ld returned 1 exit status
configure: error: I suspect your system does not have 32-bit development libraries (libc and headers). If you have them, rerun configure with --enable-multilib. If you do not have them, and want to build a 64-bit-only compiler, rerun configure with --disable-multilib.





