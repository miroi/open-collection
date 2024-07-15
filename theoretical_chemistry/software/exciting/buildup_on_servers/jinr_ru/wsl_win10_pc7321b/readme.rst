=======================================
Exciting buildup on WSL-Win10-DesktopPC
=======================================

from https://exciting-code.org/neon

milias@pc7321b:~/work/software/exciting/.wget https://exciting-code.org/uploads/exciting/exciting.neon-21.tar.gz

see http://exciting.wikidot.com/neon-download-and-compile-exciting

sudo apt install xsltproc

LibXC
~~~~~
https://libxc.gitlab.io/
sudo apt-get install -y libxc-dev

https://ubuntu.pkgs.org/22.04/ubuntu-universe-arm64/libxc-dev_5.1.7-1ubuntu1_arm64.deb.html

milias@pc7321b:~/work/software/exciting/exciting_neon_21/build/.xc-info blyp
libxc version 5.1.7

installation
~~~~~~~~~~~~
milias@pc7321b:~/work/software/exciting/exciting_neon_21/.cp build/platforms/make.inc.gfortran10+ build/make.inc

make
.

milias@pc7321b:~/work/software/exciting/exciting_neon_21/.ls -l bin/
total 32216
lrwxrwxrwx 1 milias milias       15 Jul 15 20:35 exciting -> exciting_mpismp*
-rwxr-xr-x 1 milias milias 16530112 Jul 15 20:35 exciting_mpismp*
-rwxr-xr-x 1 milias milias 16457640 Jul 15 20:36 exciting_smp*
milias@pc7321b:~/work/software/exciting/exciting_neon_21/.ls -l bin/exciting
lrwxrwxrwx 1 milias milias 15 Jul 15 20:35 bin/exciting -> exciting_mpismp*
milias@pc7321b:~/work/software/exciting/exciting_neon_21/.ldd bin/exciting
        linux-vdso.so.1 (0x00007ffcfa397000)
        libmpi_usempif08.so.40 => /lib/x86_64-linux-gnu/libmpi_usempif08.so.40 (0x00007f32d2047000)
        libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007f32d1fe1000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007f32d1d06000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f32d1c1f000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x00007f32d1b22000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x00007f32d1ad6000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f32d1ab6000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f32d188d000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x00007f32d1756000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007f32d16a3000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f32d165b000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f32d318f000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007f32d159c000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x00007f32d1540000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x00007f32d150b000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x00007f32d1506000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f32d14ea000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007f32d14be000)






