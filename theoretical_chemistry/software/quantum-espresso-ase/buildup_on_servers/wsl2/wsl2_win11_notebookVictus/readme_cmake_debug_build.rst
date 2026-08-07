===================
QE build with debug
===================

miroi@MIRO:~/work/software/quantum_espresso/q-e/build_gnu_mkl_dbg/.cmake -DQE_ENABLE_MPI=OFF -DCMAKE_Fortran_COMPILER=gfortran  -DQE_FFTW_VENDOR=Intel_FFTW3 -DCMAKE_BUILD_TYPE=RelWithDebInfo ..

see https://gitlab.com/QEF/q-e/-/issues/786#note_2497177919

miroi@MIRO:~/work/software/quantum_espresso/q-e/build_gnu_mkl_dbg/.ldd bin/pw.x
        linux-vdso.so.1 (0x00007ffd10f1d000)
        libmkl_gf_lp64.so => /lib/x86_64-linux-gnu/libmkl_gf_lp64.so (0x00007f8647e00000)
        libmkl_sequential.so => /lib/x86_64-linux-gnu/libmkl_sequential.so (0x00007f8646000000)
        libmkl_core.so => /lib/x86_64-linux-gnu/libmkl_core.so (0x00007f8641800000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007f8641525000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f8648b52000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f8648b30000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f86412fc000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f8648b2b000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f8648b26000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f8647db8000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f864a96d000)

