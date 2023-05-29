
Packages
--------

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack unload openmpi@4.1.5%gcc
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.mpif90 --version
ifort (IFORT) 19.1.1.217 20200306
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.mpicc --version
icc (ICC) 19.1.1.217 20200306
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.emkl
Intel MKL library ? MKLROOT=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack find --loaded | grep elpa
elpa@2021.11.001
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack find --loaded | grep fftw
amdfftw@3.0

SRC_vecpratt/compile.msg:W2kutils.c(20): catastrophic error: cannot open source file "sys/types.h"
SRC_vecpratt/compile.msg:make[1]: *** [Makefile:145: W2kutils.o] Error 4
SRC_vecpratt/compile.msg:make: *** [Makefile:75: real] Error 2
SRC_vecpratt/compile.msg:W2kutils.c(20): catastrophic error: cannot open source file "sys/types.h"
SRC_vecpratt/compile.msg:make[1]: *** [Makefile:145: W2kutils.o] Error 4
SRC_vecpratt/compile.msg:make: *** [Makefile:78: complex] Error 2
SRC_structeditor/SRC_ncmsymmetry/compile.msg:ifort: error #10236: File not found:  'KLROOT/lib/intel64/libmkl_blas95_lp64.a'
SRC_structeditor/SRC_ncmsymmetry/compile.msg:ifort: error #10236: File not found:  'KLROOT/lib/intel64/libmkl_lapack95_lp64.a'
SRC_structeditor/SRC_ncmsymmetry/compile.msg:make: *** [Makefile:55: ncmsymmetry] Error 1
SRC_structeditor/SRC_readwrite/compile.msg:make: *** [Makefile:13: readwrite] Error 1
SRC_structeditor/SRC_struct2mol/compile.msg:make: *** [Makefile:54: struct2mol] Error 1
SRC_structeditor/SRC_structgen/compile.msg:make: *** [Makefile:15: structgen] Error 1


Check file   compile.msg   in the corresponding SRC_* directory for the 
compilation log and more info on any compilation problem.

     Press RETURN to continue

