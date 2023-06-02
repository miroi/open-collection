Elk on Virgo GSI cluster
=======================

setup
-----

 milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/software/elk/elk-7.1.14/../setup -h
Choose compiler:

  1. Intel Fortran (ifort) with OpenMP
  2. GNU Fortran (gfortran) with OpenMP
  3. Portland Group Fortran (pgf90) with OpenMP
  4. G95 (g95)
  5. NAG Fortran (nagfor)
  6. IBM Fortran (xlf90_r) with OpenMP

 20. Intel Fortran profiling (debug only)
 21. GNU Fortran code check (debug only)
 22. G95 code check (debug only)

  o. Other       x. Exit

1

You can now edit the compiler options in 'make.inc' to use optimised
BLAS/LAPACK/FFT libraries, MPI parallelisation and Libxc.
See the Elk manual for details.

Then run 'make' to compile the code.


To enable syntax highlighting in vim run 'make vim'


make.inc modification
---------------------

#F90_OPTS = -O3 -ip -unroll -no-prec-div -qopenmp
F90_OPTS = -O3 -ip  -qopenmp -mkl=parallel
# LAPACK and BLAS libraries
#LIB_LPK = lapack.a blas.a
LIB_LPK =  ${MKLROOT}/lib/intel64_lin/libmkl_blas95_lp64.a ${MKLROOT}/lib/intel64_lin/libmkl_lapack95_lp64.a -liomp5 -lpthread -lm -ldl


compilation
-----------

make clean 

module load openmpi/intel/4.0.3_intel19.0
make -j12


milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/software/elk/elk-7.1.14/.ls -lt src/elk
-rwxr-xr-x. 1 milias ukt 6106712 Apr  2 13:06 src/elk*
milias@lxbk0595.gsi.de:/lustre/ukt/milias/work/software/elk/elk-7.1.14/.ldd src/elk
        linux-vdso.so.1 =>  (0x00007fff8f7e1000)
        libmkl_intel_lp64.so => /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so (0x00007f7a220d7000)
        libmkl_intel_thread.so => /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_intel_thread.so (0x00007f7a1fbfb000)
        libmkl_core.so => /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64_lin/libmkl_core.so (0x00007f7a1b926000)
        libiomp5.so => /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/compiler/lib/intel64_lin/libiomp5.so (0x00007f7a1b53c000)
        libpthread.so.0 => /usr/lib64/libpthread.so.0 (0x00007f7a1b320000)
        libm.so.6 => /usr/lib64/libm.so.6 (0x00007f7a1b01e000)
        libdl.so.2 => /usr/lib64/libdl.so.2 (0x00007f7a1ae1a000)
        libmpi_usempif08.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.3_intel19.0/lib/libmpi_usempif08.so.40 (0x00007f7a1abe4000)
        libmpi_usempi_ignore_tkr.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.3_intel19.0/lib/libmpi_usempi_ignore_tkr.so.40 (0x00007f7a1a9d9000)
        libmpi_mpifh.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.3_intel19.0/lib/libmpi_mpifh.so.40 (0x00007f7a1a76e000)
        libmpi.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.3_intel19.0/lib/libmpi.so.40 (0x00007f7a1a42e000)
        libc.so.6 => /usr/lib64/libc.so.6 (0x00007f7a1a060000)
        libgcc_s.so.1 => /usr/lib64/libgcc_s.so.1 (0x00007f7a19e4a000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f7a22c4f000)
        libopen-rte.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.3_intel19.0/lib/libopen-rte.so.40 (0x00007f7a19b84000)
        libopen-pal.so.40 => /cvmfs/it.gsi.de/openmpi/intel/4.0.3_intel19.0/lib/libopen-pal.so.40 (0x00007f7a19844000)
        libudev.so.1 => /usr/lib64/libudev.so.1 (0x00007f7a1962e000)
        libpciaccess.so.0 => /usr/lib64/libpciaccess.so.0 (0x00007f7a19424000)
        librt.so.1 => /usr/lib64/librt.so.1 (0x00007f7a1921c000)
        libutil.so.1 => /usr/lib64/libutil.so.1 (0x00007f7a19019000)
        libz.so.1 => /usr/lib64/libz.so.1 (0x00007f7a18e03000)
        libifport.so.5 => /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/compiler/lib/intel64_lin/libifport.so.5 (0x00007f7a18bd5000)
        libifcoremt.so.5 => /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/compiler/lib/intel64_lin/libifcoremt.so.5 (0x00007f7a18840000)
        libimf.so => /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/compiler/lib/intel64_lin/libimf.so (0x00007f7a182a0000)
        libintlc.so.5 => /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/compiler/lib/intel64_lin/libintlc.so.5 (0x00007f7a1802e000)
        libsvml.so => /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/compiler/lib/intel64_lin/libsvml.so (0x00007f7a1668a000)
        libirng.so => /cvmfs/it.gsi.de/compiler/intel/19.0/compilers_and_libraries_2019.4.243/linux/compiler/lib/intel64_lin/libirng.so (0x00007f7a16318000)
        libcap.so.2 => /usr/lib64/libcap.so.2 (0x00007f7a16113000)
        libdw.so.1 => /usr/lib64/libdw.so.1 (0x00007f7a15ec2000)
        libattr.so.1 => /usr/lib64/libattr.so.1 (0x00007f7a15cbd000)
        libelf.so.1 => /usr/lib64/libelf.so.1 (0x00007f7a15aa5000)
        liblzma.so.5 => /usr/lib64/liblzma.so.5 (0x00007f7a1587f000)
        libbz2.so.1 => /usr/lib64/libbz2.so.1 (0x00007f7a1566f000)

