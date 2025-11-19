============
ORCA buildup
============

https://www.faccts.de/orca/

download and unpack
-------------------
https://www.faccts.de/customer/software/orca/6.1.0-f.0/orca-6.1.0-f.0_linux_x86-64_openmpi41.tar.xz

milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/orca/.tar -xvf  orca-6.1.0-f.0_linux_x86-64_openmpi41.tar.xz


milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/orca/orca-6.1.0-f.0_linux_x86-64/.ldd bin/orca
        linux-vdso.so.1 =>  (0x00007ffee27fb000)
        liborca_tools-87695a6.so.6 => /zfs/scratch/HybriLITWorkshop2025/milias/software/orca/orca-6.1.0-f.0_linux_x86-64/bin/../lib/liborca_tools-87695a6.so.6 (0x00007fa29ab20000)
        libint2-stable-87695a6.so.2 => /zfs/scratch/HybriLITWorkshop2025/milias/software/orca/orca-6.1.0-f.0_linux_x86-64/bin/../lib/libint2-stable-87695a6.so.2 (0x00007fa2946ed000)
        libopenblas-87695a6.so.0 => /zfs/scratch/HybriLITWorkshop2025/milias/software/orca/orca-6.1.0-f.0_linux_x86-64/bin/../lib/libopenblas-87695a6.so.0 (0x00007fa2922ff000)
        libstdc++-87695a6.so.6 => /zfs/scratch/HybriLITWorkshop2025/milias/software/orca/orca-6.1.0-f.0_linux_x86-64/bin/../lib/libstdc++-87695a6.so.6 (0x00007fa291ff0000)
        libm.so.6 => /lib64/libm.so.6 (0x00007fa291cee000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007fa291ad8000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fa2918bc000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fa2914ee000)
        libgfortran-87695a6.so.5 => /zfs/scratch/HybriLITWorkshop2025/milias/software/orca/orca-6.1.0-f.0_linux_x86-64/bin/../lib/libgfortran-87695a6.so.5 (0x00007fa2911d1000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fa2a98bf000)
        libquadmath-87695a6.so.0 => /zfs/scratch/HybriLITWorkshop2025/milias/software/orca/orca-6.1.0-f.0_linux_x86-64/bin/../lib/libquadmath-87695a6.so.0 (0x00007fa2a9a81000)


tests
-----
... no autotests ...
