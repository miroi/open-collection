=====================
NWChem on WSL2-Ubuntu
=====================

milias@DESKTOP-7OTLCGO:~/work/software/nwchem/.git clone git@github.com:nwchemgit/nwchem.git nwchem_git

check MKL libraries
~~~~~~~~~~~~~~~~~~~

dpkg -S libmkl

ls -l /usr/lib/x86_64-linux-gnu/libmkl_*


compile
~~~~~~~

nohup compile_wsl2_bash.01* & 


milias@DESKTOP-7OTLCGO:~/work/software/nwchem/nwchem_git/bin/LINUX64/.ldd nwchem
        linux-vdso.so.1 (0x00007ffd0cfdf000)
        libmkl_intel_ilp64.so => /lib/x86_64-linux-gnu/libmkl_intel_ilp64.so (0x00007f41fb400000)
        libmkl_intel_thread.so => /lib/x86_64-linux-gnu/libmkl_intel_thread.so (0x00007f41f7a00000)
        libmkl_core.so => /lib/x86_64-linux-gnu/libmkl_core.so (0x00007f41f3200000)
        libomp.so.5 => /lib/x86_64-linux-gnu/libomp.so.5 (0x00007f41f78e0000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007f41f2f25000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f41fb319000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x00007f41f2e28000)
        libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007f41f787a000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x00007f41f2cf1000)
        libpython3.10.so.1.0 => /lib/x86_64-linux-gnu/libpython3.10.so.1.0 (0x00007f41f271a000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f41fc086000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f41f24f1000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f41fb312000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f41fb30d000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f420b985000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f41f24a9000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007f41f23f6000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007f41f2339000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x00007f41f22dd000)
        libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007f41f7849000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f41fb2ef000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x00007f41f22a8000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x00007f41f7844000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007f41f227e000)





