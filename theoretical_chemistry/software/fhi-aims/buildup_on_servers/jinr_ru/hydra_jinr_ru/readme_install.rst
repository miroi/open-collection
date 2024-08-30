=========================
FHI-Aims on hydra.jinr.ru
=========================

https://fhi-aims.org/get-the-code-menu/downloads

manual
~~~~~~
https://fhi-aims.org/verify?file=FHI-aims.240507.pdf
https://fhi-aims-club.gitlab.io/tutorials/cmake-tutorial/cmake_tutorial/


milias@vm02.hydra.local:~/work/software/fhi-aims/fhi-aims.240507/.module add  intel/v2021.1
milias@vm02.hydra.local:~/work/software/fhi-aims/fhi-aims.240507/build_intelmpi/.module add CMake

milias@vm02.hydra.local:~/work/software/fhi-aims/fhi-aims.240507/build_intelmpi/.vim initial_cache.cmake

milias@vm02.hydra.local:~/work/software/fhi-aims/fhi-aims.240507/build_intelmpi/.emkl
Intel MKL library ? MKLROOT=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest

milias@vm02.hydra.local:~/work/software/fhi-aims/fhi-aims.240507/build_intelmpi/.ls ${MKLROOT}/lib/intel64


compilation
~~~~~~~~~~~
milias@vm02.hydra.local:~/work/software/fhi-aims/fhi-aims.240507/build_intelmpi/.make -j2
100%] Building Fortran object src/CMakeFiles/aims.dir/main.f90.o
/lustre/home/user/m/milias/work/software/fhi-aims/fhi-aims.240507/src/main.f90(226): remark #6536: All symbols from this module are already visible due to another USE; the ONLY clause will have no effect. Rename clauses, if any, will be honored.   [DIMENSIONS]
    use dimensions
--------^
[100%] Linking Fortran executable ../aims.240507.scalapack.mpi.x
[100%] Built target aims

milias@vm02.hydra.local:~/work/software/fhi-aims/fhi-aims.240507/build_intelmpi/.ldd aims.240507.scalapack.mpi.x 
        linux-vdso.so.1 =>  (0x00007fff7152e000)
        libmkl_intel_lp64.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so.1 (0x00007fafc0580000)
        libmkl_sequential.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_sequential.so.1 (0x00007fafbe975000)
        libmkl_core.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so.1 (0x00007fafb69af000)
        libmkl_blacs_intelmpi_lp64.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_blacs_intelmpi_lp64.so.1 (0x00007fafb6769000)
        libmkl_scalapack_lp64.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_scalapack_lp64.so.1 (0x00007fafb5e3e000)
        libirng.so => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin/libirng.so (0x00007fafb5ad4000)
        libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007fafb57cc000)
        libcilkrts.so.5 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin/libcilkrts.so.5 (0x00007fafb558f000)
        libmpifort.so.12 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1//lib/libmpifort.so.12 (0x00007fafb51d1000)
        libmpi.so.12 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1//lib/release/libmpi.so.12 (0x00007fafb3e58000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007fafb3c54000)
        librt.so.1 => /lib64/librt.so.1 (0x00007fafb3a4c000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fafb3830000)
        libm.so.6 => /lib64/libm.so.6 (0x00007fafb352e000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fafb3160000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007fafb2f4a000)
        libintlc.so.5 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/compiler/lib/intel64_lin/libintlc.so.5 (0x00007fafb2cd2000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fafc12bb000)
        libfabric.so.1 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1//libfabric/lib/libfabric.so.1 (0x00007fafb2a8c000)
milias@vm02.hydra.local:~/work/software/fhi-aims/fhi-aims.240507/build_intelmpi/.




