==============
Wien2k on adf1
==============

Yum packages
------------
yum install elpa fftw...

[root@adf2 ~]# yum install elpa-openmpi-devel.x86_64 elpa-openmpi.x86_64 

module load mpi/openmpi3-x86_64
milias@adf2:~/work/software/wien2k/wien2k_23.2_openmpi/.module list
Currently Loaded Modulefiles:
  1) mpi/openmpi3-x86_64


FFTW3 from CP2K
~~~~~~~~~~~~~~~~
 The OMP parallel version of your FFTW library will be used.

  Your FFTW_OPT are:   -DFFTW3 -DFFTW_OMP -I/home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/fftw-3.3.8/include 
  Your FFTW_LIBS are:  -L/home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/fftw-3.3.8/lib -lfftw3 -lfftw3_omp
  Your FFTW_PLIBS are: -lfftw3_mpi

  These options derive from your chosen settings:
   
  FFTWROOT:            /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/fftw-3.3.8/
  FFTW_VERSION:        FFTW3
  FFTW_LIB:            lib
  FFTW_LIBNAME:        fftw3
  Is this correct? (Y,n): Y


Elpa
~~~~~
[root@adf2 ~]# yum install elpa-common.noarch elpa-devel.noarch elpa-openmpi-devel.x86_64  elpa-openmpi.x86_64

milias@adf2:~/work/software/wien2k/wien2k_23.2_openmpi/.rpm -ql elpa-openmpi.x86_64
/usr/lib64/openmpi/bin/elpa2_print_kernels
/usr/lib64/openmpi/lib/libelpa.so.4
/usr/lib64/openmpi/lib/libelpa.so.4.0.0

milias@adf2:~/work/software/wien2k/.ls /usr/include/elpa-2015.11.001/elpa/
elpa.h  elpa_generated.h  elpa_kernel_constants.h

  Your ELPA_OPT are:   -DELPA -I/usr/include/elpa-2015.11.001/elpa 
                           -I/usr/include/elpa-2015.11.001/modules 
  Your ELPA_LIBS are:  -lelpa -L/usr/lib64/openmpi -Wl,rpath=/usr/lib64/openmpi

  These options derive from your chosen Settings:
   
  ELPAROOT:            /usr/
  ELPA_VERSION:        2015.11.001
  ELPA_LIB:            lib64/openmpi
  ELPA_LIBNAME:        elpa
  Is this correct?  (Y,n): Y


scalapack & blacs
~~~~~~~~~~~~~~~~~
milias@adf2:~/work/software/wien2k/wien2k_23.2_openmpi/.rpm -ql scalapack-openmpi.x86_64
/usr/lib64/openmpi/lib/libscalapack.so.2
/usr/lib64/openmpi/lib/libscalapack.so.2.0.0
milias@adf2:~/work/software/wien2k/wien2k_23.2_openmpi/.rpm -ql scalapack-openmpi3.x86_64
/usr/lib64/openmpi3/lib/libscalapack.so.2
/usr/lib64/openmpi3/lib/libscalapack.so.2.0.0

ls /usr/lib64/openmpi/lib/libmpiblacs.so.2
/usr/lib64/openmpi/lib/libmpiblacs.so.2*
ls /usr/lib64/openmpi/lib/libscalapack.*  
/usr/lib64/openmpi/lib/libscalapack.a  /usr/lib64/openmpi/lib/libscalapack.so@  /usr/lib64/openmpi/lib/libscalapack.so.2@  /usr/lib64/openmpi/lib/libscalapack.so.2.0.0*


  Your SCALAPACK_LIBS are:    -L/usr/lib64/openmpi/lib/ -lscalapack -L/usr/lib64/openmpi/lib/ -lmpiblacs

  These options derive from your chosen settings:
   
  SCALAPACKROOT:       /usr/lib64/openmpi/lib/
  SCALAPACK_LIBNAME:   scalapack
  BLACSROOT:           /usr/lib64/openmpi/lib/
  BLACS_LIBNAME:       mpiblacs




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


  *                     Summary of parallel settings                    *
   ***********************************************************************

   Current settings:

         Parallel compiler      : mpif90
         SCALAPACK_LIBS         : -L/usr/lib64/openmpi/lib/ -lscalapack -L/usr/lib64/openmpi/lib/ -lmpiblacs
         FFTW_PLIBS             : -lfftw3_mpi
         ELPA_OPT               : -DELPA -I/usr/include/elpa-2015.11.001/elpa 
                    -I/usr/include/elpa-2015.11.001/modules
         ELPA_LIBS              : -lelpa -L/usr/lib64/openmpi -Wl,-rpath=/usr/lib64/openmpi
         FPOPT(par.comp.options): -O
         OMP_SWITCH             : 
         MPIRUN command         : mpirun -np _NP_ -machinefile _HOSTS_ _EXEC_
       
   parallel execution:

         RP_LIBS                : -L/usr/local/SCALAPACK -L/usr/local/BLACS/LIB -lpblas -lredist -ltools -lscalapack -lfblacs -lblacs -lmpi

     S   Accept, Save, and Quit
     R   Restart Configuration



Buildup
-------
milias@adf2:~/work/software/wien2k/wien2k_23.2_openmpi/.expand_lapw

./siteconfig_lapw

LG linuxgfortran
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

*                     Compiler and linker options                     *
 ***********************************************************************


 Recommended options for system linuxgfortran are:
      OpenMP switch:           -fopenmp
      Compiler options:        -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none
      Linker Flags:            $(FOPT) -L../SRC_lib
      Preprocessor flags:      '-DParallel'
      R_LIB (LAPACK+BLAS):     /usr/lib64/libopenblas_openmp.so.0 -lpthread

 Current settings:
  M   OpenMP switch:           
  O   Compiler options:        -O
  L   Linker Flags:            -L../SRC_lib
  P   Preprocessor flags       '-DParallel'
  R   R_LIBS (LAPACK+BLAS):    -L/usr/lib64 -lopenblas
  F   FFTW options:            -DFFTW3 -I/usr/lib64/include
      FFTW-LIBS:               -L/usr/lib64/lib64 -lfftw3
  X   LIBX options:
      LIBXC-LIBS:

  PO  Parallel options

  S   Save and Quit
  Q   Quit and abandon changes



Specify parallel options and library settings           *

   Your current parallel settings (options and libraries) are:
     C   Parallel Compiler:          mpif90
     FP  Parallel Compiler Options:  -O
     MP  MPIRUN command:             mpirun -np _NP_ -machinefile _HOSTS_ _EXEC_
     O   Parallel OpenMP switch:     

   Additional setting for SLURM batch systems (is set to 1 otherwise):
 
     CN  Number of Cores:            1

   Libraries:
 
     Sp  SCALAPACK:                   -L/usr/lib64/openmpi/lib/ 
                                                     -lscalapack 
                                                     -L/usr/lib64/openmpi/lib/ -lmpiblacs
     E   ELPA options:                -DELPA -I/usr/include/elpa-2015.11.001/elpa 
                                                     -I/usr/include/elpa-2015.11.001/modules
         ELPA-LIBS:                   -lelpa -L/usr/lib64/openmpi -Wl,-rpath=/usr/lib64/openmpi

     RP  Parallel-Libs:      -L/usr/local/SCALAPACK -L/usr/local/BLACS/LIB -lpblas -lredist -ltools -lscalapack -lfblacs -lblacs -lmpi

