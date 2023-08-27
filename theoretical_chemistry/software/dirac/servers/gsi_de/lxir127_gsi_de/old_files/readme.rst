=======================
DIRAC on lxir127.gsi.de
=======================

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/.module list
Currently Loaded Modulefiles:
  1) /compiler/intel/17.4           2) /ucx/intel/1.5_intel17.4       3) /openmpi/intel/4.0_intel17.4   4) /cmake/3.15.3

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/../setup --mpi --int64 --mkl=parallel --fc=mpif90 --cc=mpicc --cxx=mpicxx build_openmpi_intel_mklpar_i8

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/.which mpirun
/cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/bin/mpirun
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/.which mpif90
/cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/bin/mpif90

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/./cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/bin/mpif90 --version
ifort (IFORT) 17.0.4 20170411
Copyright (C) 1985-2017 Intel Corporation.  All rights reserved.


milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/build_openmpi_intel_mklpar_i8/.ldd dirac.x 
        linux-vdso.so.1 (0x00007fffa64fc000)
        libmkl_intel_ilp64.so => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64/libmkl_intel_ilp64.so (0x00007f9bcb0d7000)
        libmkl_intel_thread.so => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64/libmkl_intel_thread.so (0x00007f9bc9612000)
        libmkl_core.so => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl/lib/intel64/libmkl_core.so (0x00007f9bc7ae0000)
        libiomp5.so => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/compiler/lib/intel64/libiomp5.so (0x00007f9bc773c000)
        libmpi.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/lib/libmpi.so.40 (0x00007f9bc73f7000)
        libimf.so => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/compiler/lib/intel64/libimf.so (0x00007f9bc6f0a000)
        libsvml.so => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/compiler/lib/intel64/libsvml.so (0x00007f9bc5ff1000)
        libirng.so => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/compiler/lib/intel64/libirng.so (0x00007f9bc5c7c000)
        libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f9bc5971000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f9bc5670000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f9bc545a000)
        libirc.so => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/compiler/lib/intel64/libirc.so (0x00007f9bc51f0000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f9bc4fd3000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f9bc4c28000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f9bc4a24000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f9bc4809000)
        libmpi_usempif08.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/lib/libmpi_usempif08.so.40 (0x00007f9bc45d4000)
        libmpi_usempi_ignore_tkr.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/lib/libmpi_usempi_ignore_tkr.so.40 (0x00007f9bc43c9000)
        libmpi_mpifh.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/lib/libmpi_mpifh.so.40 (0x00007f9bc415f000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f9bcba58000)
        libopen-rte.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/lib/libopen-rte.so.40 (0x00007f9bc3e94000)
        libopen-pal.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/lib/libopen-pal.so.40 (0x00007f9bc3b53000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007f9bc3944000)
        libpciaccess.so.0 => /usr/lib/x86_64-linux-gnu/libpciaccess.so.0 (0x00007f9bc373a000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f9bc3532000)
        libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007f9bc332f000)
        libintlc.so.5 => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/compiler/lib/intel64/libintlc.so.5 (0x00007f9bc30c4000)
        libifport.so.5 => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/compiler/lib/intel64/libifport.so.5 (0x00007f9bc2e95000)
        libifcoremt.so.5 => /cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/compiler/lib/intel64/libifcoremt.so.5 (0x00007f9bc2b05000)


