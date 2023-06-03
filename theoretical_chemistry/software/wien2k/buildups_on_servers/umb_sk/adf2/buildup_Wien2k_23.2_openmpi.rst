==============
Wien2k on adf1
==============

Yum packages
------------
yum install elpa fftw...

[root@adf2 ~]# yum install elpa-openmpi-devel.x86_64 elpa-openmpi.x86_64 


Buildup
-------
milias@adf2:~/work/software/wien2k/wien2k_23.2_openmpi/.expand_lapw

./siteconfig_lapw

G generic
mpif90
mpicc

 Finding the required fftw3 library-files in /usr/lib64, /usr/local and /opt ....
 
/usr/lib64/libfftw3_omp.so
/usr/lib64/libfftw3_omp.a
/usr/lib64/libfftw3.a
/usr/lib64/libfftw3.so

 Your present FFTW choice is: FFTW3

 The OMP parallel version of your FFTW library will be used.

  Your FFTW_OPT are:   -DFFTW3 -DFFTW_OMP -I/usr/include 
  Your FFTW_LIBS are:  -L/usr/lib64 -lfftw3 -lfftw3_omp

  These options derive from your chosen settings:
   
  FFTWROOT:            /usr/
  FFTW_VERSION:        FFTW3
  FFTW_LIB:            lib64
  FFTW_LIBNAME:        fftw3
  Is this correct? (Y,n): 

 Recommended options for system generic are:
      OpenMP switch:           
      Compiler options:        -O
      Linker Flags:            -L../SRC_lib
      Preprocessor flags:      '-DParallel'
      R_LIB (LAPACK+BLAS):     -llapack_lapw -lblas_lapw

 Current settings:
  M   OpenMP switch:           
  O   Compiler options:        -O
  L   Linker Flags:            -L../SRC_lib
  P   Preprocessor flags       '-DParallel'
  R   R_LIBS (LAPACK+BLAS):    -llapack_lapw -lblas_lapw
  F   FFTW options:            -DFFTW3 -DFFTW_OMP -I/usr/include
      FFTW-LIBS:               -L/usr/lib64 -lfftw3 -lfftw3_omp
  X   LIBX options:
      LIBXC-LIBS:

  S   Save and Quit

