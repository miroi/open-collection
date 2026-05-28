=========================
Elk with intelmpi2023.1.0
=========================

/lustre/projects/m/milias/work/software/elk/intelmpi2023.1.0/elk-10.9.5


milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/elk/intelmpi2023.1.0/elk-10.9.5/.  make VERBOSE=1  > build.log 2>&1

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/elk/intelmpi2023.1.0/elk-10.9.5/.ldd src/elk
        linux-vdso.so.1 (0x00007fffae0b8000)
        libmkl_intel_lp64.so.2 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mkl/2023.1.0/lib/intel64/libmkl_intel_lp64.so.2 (0x00007f432b000000)
        libmkl_intel_thread.so.2 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mkl/2023.1.0/lib/intel64/libmkl_intel_thread.so.2 (0x00007f4327800000)
        libmkl_core.so.2 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mkl/2023.1.0/lib/intel64/libmkl_core.so.2 (0x00007f4323400000)
        libiomp5.so => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/compiler/2023.1.0/linux/compiler/lib/intel64_lin/libiomp5.so (0x00007f4322e00000)
        libm.so.6 => /lib64/libm.so.6 (0x00007f4323325000)
        libmpifort.so.12 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mpi/2021.9.0//lib/libmpifort.so.12 (0x00007f4322a00000)
        libmpi.so.12 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mpi/2021.9.0//lib/release/libmpi.so.12 (0x00007f4321000000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f4320c00000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f432c2c8000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f432c2c3000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f432c2be000)
        librt.so.1 => /lib64/librt.so.1 (0x00007f432c2b9000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f432c2f2000)


