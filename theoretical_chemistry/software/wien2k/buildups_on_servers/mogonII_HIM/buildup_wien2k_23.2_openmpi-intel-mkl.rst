WIEN2k_23.2 buildup
===================

mirilias@login23.mogon:~/work/software/wien2k/.module load mpi/OpenMPI/3.1.1-iccifort-2018.3.222-GCC-6.3.0
mirilias@login23.mogon:~/work/software/wien2k/.module load numlib/FFTW/3.3.8-intel-2018.03

mirilias@login23.mogon:~/work/software/wien2k/.which mpirun  
/cluster/easybuild/broadwell/software/mpi/impi/2018.3.222-iccifort-2018.3.222-GCC-6.3.0/bin64/mpirun
mirilias@login23.mogon:~/work/software/wien2k/.mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2018 Update 3 Build 20180411 (id: 18329)

mirilias@login23.mogon:~/work/software/wien2k/.mpiifort --version
ifort (IFORT) 18.0.3 20180410

mirilias@login23.mogon:~/work/software/wien2k/.emkl
Intel MKL library ? MKLROOT=/cluster/easybuild/broadwell/software/imkl/2018.3.222-iimpi-2018.03/mkl

#module load math/ELPA/2021.05.001-foss-2021b

mirilias@login23.mogon:~/work/software/wien2k/.module list  

Currently Loaded Modules:
  1) compiler/GCCcore/6.3.0
  2) compiler/icc/2018.3.222-GCC-6.3.0
  3) compiler/ifort/2018.3.222-GCC-6.3.0
  4) toolchain/iccifort/2018.3.222-GCC-6.3.0
  5) mpi/OpenMPI/3.1.1-iccifort-2018.3.222-GCC-6.3.0
  6) mpi/impi/2018.3.222-iccifort-2018.3.222-GCC-6.3.0
  7) toolchain/iimpi/2018.03
  8) numlib/imkl/2018.3.222-iimpi-2018.03
  9) toolchain/intel/2018.03
 10) numlib/FFTW/3.3.8-intel-2018.03

Your MKLROOT variable is: 
/cluster/easybuild/broadwell/software/imkl/2018.3.222-iimpi-2018.03/mkl
LS
mpiifort
mpiicc
MKL_TARGET_ARCH was set to intel64

 Finding the required fftw3 library-files in /usr/lib64, /usr/local and /opt ....
 
/usr/lib64/libfftw3.so
/usr/lib64/libfftw3_omp.a
/usr/lib64/libfftw3.a
/usr/lib64/libfftw3_omp.so

 Your present FFTW choice is: FFTW3

   Your current FFTW options are:
   
   FFTW_OPT:             -DFFTW3 -DFFTW_OMP -I/usr/include
   FFTW_LIBS:            -L/usr/lib64 -lfftw3 -lfftw3_omp
   
   which are derived from following settings:
   
   R  FFTWROOT:          /usr/
   V  FFTW_VERSION:      FFTW3
   L  FFTW_LIB:          lib64
   N  FFTW_LIBNAME:      fftw3

 Recommended options for system linuxifs are:
      OpenMP switch:           -qopenmp
      Compiler options:        -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I$(MKLROOT)/include
      Linker Flags:            $(FOPT) -L$(MKLROOT)/lib/$(MKL_TARGET_ARCH) -lpthread -lm -ldl -liomp5
      Preprocessor flags:      '-DParallel'
      R_LIB (LAPACK+BLAS):     -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core

 Current settings:
  M   OpenMP switch:           -qopenmp
  O   Compiler options:        -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I$(MKLROOT)/include
  L   Linker Flags:            $(FOPT) -L$(MKLROOT)/lib/$(MKL_TARGET_ARCH) -lpthread -lm -ldl -liomp5
  P   Preprocessor flags       '-DParallel'
  R   R_LIBS (LAPACK+BLAS):    -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core
  F   FFTW options:            -DFFTW3 -DFFTW_OMP -I/usr/include
      FFTW-LIBS:               -L/usr/lib64 -lfftw3 -lfftw3_omp
  X   LIBX options:
      LIBXC-LIBS:

  S   Save and Quit

