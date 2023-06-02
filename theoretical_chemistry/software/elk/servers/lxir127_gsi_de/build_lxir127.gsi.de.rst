=====================
Elk on lxir127.gsi.de
=====================

milias@lxir127.gsi.de:~/Work/qch/software/elk/elk-6.8.4/.

Changes in make.inc:
~~~~~~~~~~~~~~~~~~~~
F90_OPTS = -O3 -ip  -qopenmp -mkl=parallel
F77_OPTS = -O3 -ip  -qopenmp -mkl=parallel
LIB_LPK =  ${MKLROOT}/lib/intel64_lin/libmkl_blas95_lp64.a ${MKLROOT}/lib/intel64_lin/libmkl_lapack95_lp64.a -liomp5 -lpthread -lm -ldl

