 ***********************************************************************
 *                     Compiler and linker options                     *
 ***********************************************************************

 Since intel changes the name of the mkl-libraries from version to version,
 you may find the linking options for the most recent ifort version at
 http://software.intel.com/en-us/articles/intel-mkl-link-line-advisor/

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
  F   FFTW options:            -DFFTW3 -DFFTW_OMP -I/cluster/easybuild/broadwell/software/numlib/FFTW/3.3.8-intel-2018.03/include
      FFTW-LIBS:               -L/cluster/easybuild/broadwell/software/numlib/FFTW/3.3.8-intel-2018.03/lib -lfftw3 -lfftw3_omp
      FFTW-PLIBS:              -lfftw3_mpi
  X   LIBX options:
      LIBXC-LIBS:

  PO  Parallel options

  S   Save and Quit
  Q   Quit and abandon changes

      To change an item select option.

Selection: 

Selection: PO

   ***********************************************************************
   *             Specify parallel options and library settings           *
   ***********************************************************************

   Your current parallel settings (options and libraries) are:
   
     C   Parallel Compiler:          mpiifort
     FP  Parallel Compiler Options:  -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I$(MKLROOT)/include
     MP  MPIRUN command:             srun -K -N_nodes_ -n_NP_ -r_offset_ _PINNING_ _EXEC_
     O   Parallel OpenMP switch:     -qopenmp

   Additional setting for SLURM batch systems (is set to 1 otherwise):
 
     CN  Number of Cores:            40

   Libraries:
 
     Sp  SCALAPACK:
     E   ELPA options:
         ELPA-LIBS:

     RP  Parallel-Libs:      $(R_LIBS)


     B   Back to compiler/linker options   

       To change an item select option.

