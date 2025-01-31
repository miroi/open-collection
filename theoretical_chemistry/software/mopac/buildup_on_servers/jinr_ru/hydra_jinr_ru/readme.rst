======================
MOPAC on hydra.jinr.ru
======================

Installation
-------------
run-file:
https://gitlab-hybrilit.jinr.ru/hybrilit/hlit-user/-/issues/228

from source:
https://github.com/openmopac/mopac/releases/tag/v22.1.1

Linux run file from:
http://openmopac.net/Download_MOPAC_Executable_Step2.html:

milias@hydra.jinr.ru:~/work/software/mopac/.chmod u+x mopac-23.0.3-linux.run

milias@hydra.jinr.ru:~/work/software/mopac/../mopac-23.0.3-linux.run
qt.qpa.xcb: could not connect to display
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: minimal, xcb.

Aborted
milias@hydra.jinr.ru:~/work/software/mopac/.ldd mopac-23.0.3-linux.run
        linux-vdso.so.1 =>  (0x00007ffc31a93000)
        libutil.so.1 => /lib64/libutil.so.1 (0x00002b347c472000)
        libbz2.so.1 => /lib64/libbz2.so.1 (0x00002b347c675000)
        liblzma.so.5 => /lib64/liblzma.so.5 (0x00002b347c885000)
        libfontconfig.so.1 => /lib64/libfontconfig.so.1 (0x00002b347caab000)
        libfreetype.so.6 => /lib64/libfreetype.so.6 (0x00002b347cced000)
        libdbus-1.so.3 => /lib64/libdbus-1.so.3 (0x00002b347cfac000)
        libxcb-glx.so.0 => /lib64/libxcb-glx.so.0 (0x00002b347d1fc000)
        libX11-xcb.so.1 => /lib64/libX11-xcb.so.1 (0x00002b347d417000)
        libxcb-icccm.so.4 => /lib64/libxcb-icccm.so.4 (0x00002b347d619000)
        libxcb-image.so.0 => /lib64/libxcb-image.so.0 (0x00002b347d81e000)
        libxcb-shm.so.0 => /lib64/libxcb-shm.so.0 (0x00002b347da23000)
        libxcb-util.so.1 => /lib64/libxcb-util.so.1 (0x00002b347dc27000)
        libxcb-keysyms.so.1 => /lib64/libxcb-keysyms.so.1 (0x00002b347de2d000)
        libxcb-randr.so.0 => /lib64/libxcb-randr.so.0 (0x00002b347e030000)
        libxcb-render-util.so.0 => /lib64/libxcb-render-util.so.0 (0x00002b347e240000)
        libxcb-render.so.0 => /lib64/libxcb-render.so.0 (0x00002b347e444000)
        libxcb-shape.so.0 => /lib64/libxcb-shape.so.0 (0x00002b347e652000)
        libxcb-sync.so.1 => /lib64/libxcb-sync.so.1 (0x00002b347e856000)
        libxcb-xfixes.so.0 => /lib64/libxcb-xfixes.so.0 (0x00002b347ea5d000)
        libxcb-xinerama.so.0 => /lib64/libxcb-xinerama.so.0 (0x00002b347ec65000)
        libxcb-xkb.so.1 => /lib64/libxcb-xkb.so.1 (0x00002b347ee68000)
        libxcb.so.1 => /lib64/libxcb.so.1 (0x00002b347f084000)
        libXext.so.6 => /lib64/libXext.so.6 (0x00002b347f2ac000)
        libX11.so.6 => /lib64/libX11.so.6 (0x00002b347f4be000)
        libxkbcommon-x11.so.0 => /lib64/libxkbcommon-x11.so.0 (0x00002b347f7fc000)
        libxkbcommon.so.0 => /lib64/libxkbcommon.so.0 (0x00002b347fa04000)
        librt.so.1 => /lib64/librt.so.1 (0x00002b347fc44000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00002b347fe4c000)
        libGL.so.1 => /lib64/libGL.so.1 (0x00002b3480050000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00002b34802dc000)
        libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00002b34804f8000)
        libm.so.6 => /lib64/libm.so.6 (0x00002b3480800000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00002b3480b02000)
        libc.so.6 => /lib64/libc.so.6 (0x00002b3480d18000)
        /lib64/ld-linux-x86-64.so.2 (0x00002b347c24e000)
        libexpat.so.1 => /lib64/libexpat.so.1 (0x00002b34810e6000)
        libuuid.so.1 => /lib64/libuuid.so.1 (0x00002b3481311000)
        libz.so.1 => /lib64/libz.so.1 (0x00002b3481516000)
        libpng15.so.15 => /lib64/libpng15.so.15 (0x00002b348172c000)
        libsystemd.so.0 => /lib64/libsystemd.so.0 (0x00002b3481957000)
        libXau.so.6 => /lib64/libXau.so.6 (0x00002b3481b88000)
        libGLX.so.0 => /lib64/libGLX.so.0 (0x00002b3481d8c000)
        libGLdispatch.so.0 => /lib64/libGLdispatch.so.0 (0x00002b3481fbe000)
        libcap.so.2 => /lib64/libcap.so.2 (0x00002b3482274000)
        libselinux.so.1 => /lib64/libselinux.so.1 (0x00002b3482479000)
        liblz4.so.1 => /lib64/liblz4.so.1 (0x00002b34826a0000)
        libgcrypt.so.11 => /lib64/libgcrypt.so.11 (0x00002b34828af000)
        libgpg-error.so.0 => /lib64/libgpg-error.so.0 (0x00002b3482b30000)
        libresolv.so.2 => /lib64/libresolv.so.2 (0x00002b3482d35000)
        libdw.so.1 => /lib64/libdw.so.1 (0x00002b3482f4f000)
        libattr.so.1 => /lib64/libattr.so.1 (0x00002b34831a0000)
        libpcre.so.1 => /lib64/libpcre.so.1 (0x00002b34833a5000)
        libelf.so.1 => /lib64/libelf.so.1 (0x00002b3483607000)


GUI-enabled installation via vmXY.hydra.local
---------------------------------------------

milias@vm02.hydra.local:~/work/software/mopac/../mopac-23.0.3-linux.run 

installation folder = /lustre/home/user/m/milias/work/software/mopac/install

add MOPAC bin,lib to PATH, LD_LIBRARY_PATH




