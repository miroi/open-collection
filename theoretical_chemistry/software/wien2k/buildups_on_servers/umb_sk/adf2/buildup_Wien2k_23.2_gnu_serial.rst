==============
Wien2k on adf2
==============

Yum packages
------------
yum install elpa fftw...

[root@adf2 ~]# yum install elpa-openmpi-devel.x86_64 elpa-openmpi.x86_64 

module load mpi/openmpi3-x86_64
milias@adf2:~/work/software/wien2k/wien2k_23.2_openmpi/.module list
Currently Loaded Modulefiles:
  1) mpi/openmpi3-x86_64

Check packages
~~~~~~~~~~~~~~
milias@adf2:~/work/projects/open-collection/theoretical_chemistry/software/wien2k/buildups_on_servers/umb_sk/adf2/.ls /usr/lib64/libpthread*  /usr/lib64/libopenblas*
/usr/lib64/libopenblas-r0.3.3.so*     /usr/lib64/libopenblas64_.so.0@        /usr/lib64/libopenblaso64_.so@        /usr/lib64/libopenblasp64_-r0.3.3.so*
/usr/lib64/libopenblas.so@            /usr/lib64/libopenblaso-r0.3.3.so*     /usr/lib64/libopenblaso64_.so.0@      /usr/lib64/libopenblasp64_.so@
/usr/lib64/libopenblas.so.0@          /usr/lib64/libopenblaso.so@            /usr/lib64/libopenblasp-r0.3.3.so*    /usr/lib64/libopenblasp64_.so.0@
/usr/lib64/libopenblas64-r0.3.3.so*   /usr/lib64/libopenblaso.so.0@          /usr/lib64/libopenblasp.so@           /usr/lib64/libpthread-2.17.so*
/usr/lib64/libopenblas64.so@          /usr/lib64/libopenblaso64-r0.3.3.so*   /usr/lib64/libopenblasp.so.0@         /usr/lib64/libpthread.so
/usr/lib64/libopenblas64.so.0@        /usr/lib64/libopenblaso64.so@          /usr/lib64/libopenblasp64-r0.3.3.so*  /usr/lib64/libpthread.so.0@
/usr/lib64/libopenblas64_-r0.3.3.so*  /usr/lib64/libopenblaso64.so.0@        /usr/lib64/libopenblasp64.so@         /usr/lib64/libpthread_nonshared.a
/usr/lib64/libopenblas64_.so@         /usr/lib64/libopenblaso64_-r0.3.3.so*  /usr/lib64/libopenblasp64.so.0@
milias@adf2:~/work/projects/open-collection/theoretical_chemistry/software/wien2k/buildups_on_servers/umb_sk/adf2/.

milias@adf2:~/work/projects/open-collection/theoretical_chemistry/software/wien2k/buildups_on_servers/umb_sk/adf2/.ls /usr/lib64/libfftw*
/usr/lib64/libfftw.a           /usr/lib64/libfftw3_omp.so.3.3.2*      /usr/lib64/libfftw3f_omp.so.3@          /usr/lib64/libfftw3l_omp.so@
/usr/lib64/libfftw.so@         /usr/lib64/libfftw3_threads.a          /usr/lib64/libfftw3f_omp.so.3.3.2*      /usr/lib64/libfftw3l_omp.so.3@
/usr/lib64/libfftw.so.2@       /usr/lib64/libfftw3_threads.so@        /usr/lib64/libfftw3f_threads.a          /usr/lib64/libfftw3l_omp.so.3.3.2*
/usr/lib64/libfftw.so.2.0.7*   /usr/lib64/libfftw3_threads.so.3@      /usr/lib64/libfftw3f_threads.so@        /usr/lib64/libfftw3l_threads.a
/usr/lib64/libfftw3.a          /usr/lib64/libfftw3_threads.so.3.3.2*  /usr/lib64/libfftw3f_threads.so.3@      /usr/lib64/libfftw3l_threads.so@
/usr/lib64/libfftw3.so@        /usr/lib64/libfftw3f.a                 /usr/lib64/libfftw3f_threads.so.3.3.2*  /usr/lib64/libfftw3l_threads.so.3@
/usr/lib64/libfftw3.so.3@      /usr/lib64/libfftw3f.so@               /usr/lib64/libfftw3l.a                  /usr/lib64/libfftw3l_threads.so.3.3.2*
/usr/lib64/libfftw3.so.3.3.2*  /usr/lib64/libfftw3f.so.3@             /usr/lib64/libfftw3l.so@                /usr/lib64/libfftw_threads.a
/usr/lib64/libfftw3_omp.a      /usr/lib64/libfftw3f.so.3.3.2*         /usr/lib64/libfftw3l.so.3@              /usr/lib64/libfftw_threads.so@
/usr/lib64/libfftw3_omp.so@    /usr/lib64/libfftw3f_omp.a             /usr/lib64/libfftw3l.so.3.3.2*          /usr/lib64/libfftw_threads.so.2@
/usr/lib64/libfftw3_omp.so.3@  /usr/lib64/libfftw3f_omp.so@           /usr/lib64/libfftw3l_omp.a              /usr/lib64/libfftw_threads.so.2.0.7*



Compilation
-----------
LG


Openblas
~~~~~~~~~
ilias@adf2:~/work/software/wien2k/wien2k_23.2_openmpi/.rpm -ql openblas-devel.x86_64
/usr/include/openblas
/usr/include/openblas/cblas.h
/usr/include/openblas/f77blas.h
/usr/include/openblas/lapacke.h
/usr/include/openblas/lapacke_config.h
/usr/include/openblas/lapacke_mangling.h
/usr/include/openblas/lapacke_utils.h
/usr/include/openblas/openblas_config.h
/usr/lib64/libopenblas.so
/usr/lib64/libopenblas64.so
/usr/lib64/libopenblas64_.so
/usr/lib64/libopenblaso.so
/usr/lib64/libopenblaso64.so
/usr/lib64/libopenblaso64_.so
/usr/lib64/libopenblasp.so
/usr/lib64/libopenblasp64.so
/usr/lib64/libopenblasp64_.so


Recommended options for system linuxgfortran are:
      OpenMP switch:           -fopenmp
      Compiler options:        -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none
      Linker Flags:            $(FOPT) -L../SRC_lib
      Preprocessor flags:      '-DParallel'
      R_LIB (LAPACK+BLAS):     /usr/lib64/libopenblas_openmp.so.0 -lpthread

 Current settings:
  M   OpenMP switch:           -fopenmp
  O   Compiler options:        -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none
  L   Linker Flags:            $(FOPT) -L../SRC_lib
  P   Preprocessor flags       '-DParallel'
  R   R_LIBS (LAPACK+BLAS):    -L/usr/lib64 -lopenblas -lpthread
  F   FFTW options:            -DFFTW3 -DFFTW_OMP -I/usr/include
      FFTW-LIBS:               -L/usr/lib64 -lfftw3 -lfftw3_omp
  X   LIBX options:
      LIBXC-LIBS:

  PO  Parallel options

