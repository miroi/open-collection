============================
DIRAC buildup with Intel MKL
============================

Loading packages
~~~~~~~~~~~~~~~~
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack unload 
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack find loaded
==> No package matches the query: loaded

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack arch -t
broadwell

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack load intel-mkl@2020.4.304

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack find --loaded
==> 1 loaded package
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
intel-mkl@2020.4.304
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.which ifort
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.which icc
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.emkl
Intel MKL library ? MKLROOT=/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-mkl-2020.4.304-wcz55b7qqq66b7lh5vqt6qt7ftlkwa3z/compilers_and_libraries_2020.4.304/linux/mkl

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack load intel-parallel-studio@professional.2020.1

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack find --loaded
==> 2 loaded packages
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
intel-mkl@2020.4.304  intel-parallel-studio@professional.2020.1

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.which ifort
/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/bin/intel64/ifort
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.which icc
/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/bin/intel64/icc

we have serial Intel compilers, with MKL library

Add OpenMPI-i8
~~~~~~~~~~~~~~~~
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.export PATH=/u/milias/bin/openmpi-i8/bin:$PATH
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.export LD_LIBRARY_PATH=/u/milias/bin/openmpi-i8/lib:$LD_LIBRARY_PATH

Add CMake:
~~~~~~~~~~~
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack load cmake@3.21.4 target=$(spack arch -t)

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack load cmake arch=x86_64
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.which cmake
/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/cmake-3.24.3-lfuhsd4ed4ghj6iejxba2kxbc2iaqybs/bin/cmake
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.cmake --version


Own build:
~~~~~~~~~~
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/../setup --int64 --mkl=parallel --mpi build_intelompi_mklpar_i8
.
.
.
   configure step is done
   now you need to compile the sources:
   $ cd build_intelompi_mklpar_i8
   $ make

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/build_intelompi_mklpar_i8/.make -j12
.
.
100%] Building Fortran object CMakeFiles/dirac.x.dir/src/main/main.F90.o
[100%] Built target cfread.x
[100%] Built target pcmo_addlabels.x
[100%] Built target twofit.x
[100%] Linking Fortran executable labread.x
[100%] Linking Fortran executable dirac.x
[100%] Built target dirac_mointegral_export.x
[100%] Built target rspread.x
[100%] Built target cf_addlabels.x
[100%] Built target mx2fit.x
INFO:basis set directories, basis*, synchronized into current installation directory
[100%] Built target vibcal.x
[100%] Built target h5towfx.x
[100%] Built target labread.x
[100%] Built target dirac.x
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/build_intelompi_mklpar_i8/.ldd dirac.x
        linux-vdso.so.1 (0x00007ffff3306000)
        libmkl_intel_ilp64.so => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64_lin/libmkl_intel_ilp64.so (0x00007faf392fd000)
        libmkl_intel_thread.so => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64_lin/libmkl_intel_thread.so (0x00007faf36d68000)
        libmkl_core.so => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64_lin/libmkl_core.so (0x00007faf329e8000)
        libiomp5.so => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/compiler/lib/intel64_lin/libiomp5.so (0x00007faf325e8000)
        libmpi.so.40 => /u/milias/bin/openmpi-i8/lib/libmpi.so.40 (0x00007faf322c0000)
        libimf.so => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/compiler/lib/intel64_lin/libimf.so (0x00007faf31c3d000)
        libsvml.so => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/compiler/lib/intel64_lin/libsvml.so (0x00007faf30111000)
        libirng.so => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/compiler/lib/intel64_lin/libirng.so (0x00007faf2fda7000)
        libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007faf2fbe3000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007faf2fa60000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007faf2fa46000)
        libirc.so => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/compiler/lib/intel64_lin/libirc.so (0x00007faf2f7ce000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007faf2f7ad000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007faf2f5ed000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007faf2f5e8000)
        libz.so.1 => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-broadwell/gcc-8.3.0/zlib-1.2.11-pqdidq3pxucqbvyxnlf552vxypl6zxvs/lib/libz.so.1 (0x00007faf2f5cf000)
        libhdf5_serial.so.103 => /usr/lib/x86_64-linux-gnu/libhdf5_serial.so.103 (0x00007faf2f24a000)
        libsz.so.2 => /usr/lib/x86_64-linux-gnu/libsz.so.2 (0x00007faf2f047000)
        libmpi_usempif08.so.40 => /u/milias/bin/openmpi-i8/lib/libmpi_usempif08.so.40 (0x00007faf2ee17000)
        libmpi_usempi_ignore_tkr.so.40 => /u/milias/bin/openmpi-i8/lib/libmpi_usempi_ignore_tkr.so.40 (0x00007faf2ec0e000)
        libmpi_mpifh.so.40 => /u/milias/bin/openmpi-i8/lib/libmpi_mpifh.so.40 (0x00007faf2e9a1000)
        /lib64/ld-linux-x86-64.so.2 (0x00007faf39dc6000)
        libopen-rte.so.40 => /u/milias/bin/openmpi-i8/lib/libopen-rte.so.40 (0x00007faf2e6d9000)
        libopen-pal.so.40 => /u/milias/bin/openmpi-i8/lib/libopen-pal.so.40 (0x00007faf2e3a5000)
        libnuma.so.1 => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-broadwell/gcc-8.3.0/numactl-2.0.14-4wi6aqw2wy5jj2n5u3eassukodoswf3q/lib/libnuma.so.1 (0x00007faf2e398000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007faf2e38e000)
        libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007faf2e389000)
        libintlc.so.5 => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/compiler/lib/intel64_lin/libintlc.so.5 (0x00007faf2e111000)
        libaec.so.0 => /usr/lib/x86_64-linux-gnu/libaec.so.0 (0x00007faf2df09000)
        libifport.so.5 => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/compiler/lib/intel64_lin/libifport.so.5 (0x00007faf2dcdb000)
        libifcoremt.so.5 => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/compiler/lib/intel64_lin/libifcoremt.so.5 (0x00007faf2d940000)
        libatomic.so.1 => /usr/lib/x86_64-linux-gnu/libatomic.so.1 (0x00007faf2d936000)
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/build_intelompi_mklpar_i8/

Control DIRAC run
-----------------
milias@lxir127.gsi.de:/data.local1/milias/projects/open-collection/theoretical_chemistry/software_runs/dirac/servers/gsi_de/lxir127_gsi_de/.nohup lxir127_intel-openmpi_i8_mklpar_01.bash > lxir127_intel-openmpi_i8_mklpar_01.logfile 2>&1 

