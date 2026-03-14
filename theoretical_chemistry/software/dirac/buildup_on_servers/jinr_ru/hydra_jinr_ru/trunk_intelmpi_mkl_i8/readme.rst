DIRAC with IntelMPI+MKL+int8
============================

interactie build
----------------

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk_cloned/build_intelmpi2023_mkl_i8/.module list

Currently Loaded Modules:
  1) CMake/v4.2.3   2) intel/v2023.1.0   3) Python/v3.12.13


milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk_cloned/build_intelmpi2023_mkl_i8/../setup --mpi --exatensor=OFF --pcmsolver=OFF  --pelib=OFF  --fc=mpiifort --cc=mpiicc --cxx=mpiicpc  build_intelmpi2023_mkl_i8

[100%] Linking Fortran executable test_allocator.x
[100%] Built target mx2fit.x
[100%] Built target vibcal.x
[100%] Built target test_allocator.x
[100%] Built target diag.x
INFO:basis set directories, basis*, synchronized into current installation directory
[100%] Built target dirac.x

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk_cloned/build_intelmpi2023_mkl_i8/.ldd dirac.x
        linux-vdso.so.1 (0x00007fde7936b000)
        libmkl_intel_lp64.so.2 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mkl/2023.1.0/lib/intel64/libmkl_intel_lp64.so.2 (0x00007fde78000000)
        libmkl_intel_thread.so.2 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mkl/2023.1.0/lib/intel64/libmkl_intel_thread.so.2 (0x00007fde74800000)
        libmkl_core.so.2 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mkl/2023.1.0/lib/intel64/libmkl_core.so.2 (0x00007fde70400000)
        libm.so.6 => /lib64/libm.so.6 (0x00007fde7927e000)
        libmpifort.so.12 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mpi/2021.9.0/lib/libmpifort.so.12 (0x00007fde70000000)
        libmpi.so.12 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mpi/2021.9.0/lib/release/libmpi.so.12 (0x00007fde6e600000)
        libirng.so => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/compiler/2023.1.0/linux/compiler/lib/intel64_lin/libirng.so (0x00007fde6e200000)
        libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007fde6de00000)
        libiomp5.so => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/compiler/2023.1.0/linux/compiler/lib/intel64_lin/libiomp5.so (0x00007fde6d800000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fde6d400000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007fde79262000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007fde7925d000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fde79258000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fde7936d000)
        librt.so.1 => /lib64/librt.so.1 (0x00007fde79253000)
        libintlc.so.5 => /cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/compiler/2023.1.0/linux/compiler/lib/intel64_lin/libintlc.so.5 (0x00007fde77f89000)
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk_cloned/build_intelmpi2023_mkl_i8/.

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk_cloned/build_intelmpi2023_mkl_i8/.export DIRAC_MPI_COMMAND="mpirun -np 2"

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk_cloned/build_intelmpi2023_mkl_i8/.which mpirun
/cvmfs/hlit.jinr.ru/alma9/intel/v2023.1.0/mpi/2021.9.0/bin/mpirun
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk_cloned/build_intelmpi2023_mkl_i8/.mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2021.9 Build 20230307 (id: d82b3071db)
Copyright 2003-2023, Intel Corporation.

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk_cloned/build_intelmpi2023_mkl_i8/.ctest -VV  -j4  > ctest.log 2>&1


