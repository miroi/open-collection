==============
Wien2k on adf1
==============

Yum packages
------------
yum install elpa fftw2...


Buildup
-------
milias@adf1:~/Work/software/wien2k_23.2/wien2k_23.2_gnu_serial/.gunzip *
milias@adf1:~/Work/software/wien2k_23.2/wien2k_23.2_gnu_serial/../expand_lapw
./siteconfig_lapw

LG, linuxgfortran
gfortran
gcc

You have the following OpenBlas libraries in /opt /usr/lib or /usr/lib64
and must select one of them in the R_LIBS:

/usr/lib64/libopenblasp.so.0
/usr/lib64/libopenblas.so.0
/usr/lib64/libopenblasp-r0.3.3.so
/usr/lib64/libopenblas-r0.3.3.so

 O   Compiler options:        -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none
 L   Linker Flags:            $(FOPT) -L../SRC_lib
 P   Preprocessor flags       '-DParallel'
 R   R_LIBS (LAPACK+BLAS):    /usr/lib64/libopenblas_openmp.so.0 -lpthread

 F   FFTW options:            -DFFTW3 -DFFTW_OMP -I/usr/include
     FFTW-LIBS:               -L/usr/lib64 -lfftw3 -lfftw3_omp
.
.
SRC_wplot/compile.msg:gfortran: error: /usr/lib64/libopenblas_openmp.so.0: No such file or directory
SRC_wplot/compile.msg:make: *** [Makefile:125: wplot] Error 1

yum install openblas-openmp.x86_64 ... 
there is no libopenblas_openmp.so.0 ... !
 replace with :
 R   R_LIBS (LAPACK+BLAS):    /usr/lib64/libopenblas.so.0 -lpthread

GOT compiled !!!




