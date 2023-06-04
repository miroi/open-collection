===================
Wien2k_23.2 buildup
===================

Packages
--------
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack load intel-mkl@2019.1.144
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack load openmpi@4.1.5%intel
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack load amdfftw target=x86_64
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack load elpa@2021.11.001 target=x86_64
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack unload openmpi@4.1.5%gcc

OpenMPI & Intel compilers
~~~~~~~~~~~~~~~~~~~~~~~~~
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.which mpif90
/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/intel-19.1.1.217/openmpi-4.1.5-iyp4vbqhi3yfm7vqqslzvpmgjjsggx7u/bin/mpif90

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.mpif90 --version
ifort (IFORT) 19.1.1.217 20200306

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.mpicc --version
icc (ICC) 19.1.1.217 20200306

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.mpirun  --version
mpirun (Open MPI) 4.1.5

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.emkl
Intel MKL library ? MKLROOT=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl

MKL
~~~
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64/
libmkl_avx2.so*                  libmkl_blacs_sgimpt_ilp64.a    libmkl_gf_ilp64.so*      libmkl_lapack95_lp64.a      libmkl_tbb_thread.a
libmkl_avx512_mic.so*            libmkl_blacs_sgimpt_ilp64.so*  libmkl_gf_lp64.a         libmkl_mc3.so*              libmkl_tbb_thread.so*
libmkl_avx512.so*                libmkl_blacs_sgimpt_lp64.a     libmkl_gf_lp64.so*       libmkl_mc.so*               libmkl_vml_avx2.so*
libmkl_avx.so*                   libmkl_blacs_sgimpt_lp64.so*   libmkl_gnu_thread.a      libmkl_pgi_thread.a         libmkl_vml_avx512_mic.so*
libmkl_blacs_intelmpi_ilp64.a    libmkl_blas95_ilp64.a          libmkl_gnu_thread.so*    libmkl_pgi_thread.so*       libmkl_vml_avx512.so*
libmkl_blacs_intelmpi_ilp64.so*  libmkl_blas95_lp64.a           libmkl_intel_ilp64.a     libmkl_rt.so*               libmkl_vml_avx.so*
libmkl_blacs_intelmpi_lp64.a     libmkl_cdft_core.a             libmkl_intel_ilp64.so*   libmkl_scalapack_ilp64.a    libmkl_vml_cmpt.so*
libmkl_blacs_intelmpi_lp64.so*   libmkl_cdft_core.so*           libmkl_intel_lp64.a      libmkl_scalapack_ilp64.so*  libmkl_vml_def.so*
libmkl_blacs_openmpi_ilp64.a     libmkl_core.a                  libmkl_intel_lp64.so*    libmkl_scalapack_lp64.a     libmkl_vml_mc2.so*
libmkl_blacs_openmpi_ilp64.so*   libmkl_core.so*                libmkl_intel_thread.a    libmkl_scalapack_lp64.so*   libmkl_vml_mc3.so*
libmkl_blacs_openmpi_lp64.a      libmkl_def.so*                 libmkl_intel_thread.so*  libmkl_sequential.a         libmkl_vml_mc.so*
libmkl_blacs_openmpi_lp64.so*    libmkl_gf_ilp64.a              libmkl_lapack95_ilp64.a  libmkl_sequential.so*       locale/


FFTW3 library
~~~~~~~~~~~~~
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack find --loaded | grep fftw
amdfftw@3.0

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack find --paths amdfftw target=x86_64
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdfftw@3.0  /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb
==> 1 installed package

ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib/
cmake/                   libfftw3f_omp.so@        libfftw3f.so.3@      libfftw3_mpi.so.3.5.8*  libfftw3.so@
libfftw3f_mpi.so@        libfftw3f_omp.so.3@      libfftw3f.so.3.5.8*  libfftw3_omp.so@        libfftw3.so.3@
libfftw3f_mpi.so.3@      libfftw3f_omp.so.3.5.8*  libfftw3_mpi.so@     libfftw3_omp.so.3@      libfftw3.so.3.5.8*
libfftw3f_mpi.so.3.5.8*  libfftw3f.so@            libfftw3_mpi.so.3@   libfftw3_omp.so.3.5.8*  pkgconfig/


ELPA
~~~~
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack find --loaded | grep elpa
elpa@2021.11.001

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.spack find --paths  elpa@2021.11.001  target=x86_64-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
elpa@2021.11.001  /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms
==> 1 installed package
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/
bin/  include/  lib/  share/
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_intelopenmpi_mkl/.ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib/
libelpa_openmp.a  libelpa_openmp.so@  libelpa_openmp.so.17@  libelpa_openmp.so.17.0.0*  pkgconfig/

Wien2k Compilation
-------------------
LS
mpif90
mpicc

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
  F   FFTW options:            -DFFTW3 -DFFTW_OMP -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib/include
      FFTW-LIBS:               -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib/ -lfftw3 -lfftw3_omp
      FFTW-PLIBS:              -lfftw3_mpi
  X   LIBX options:
      LIBXC-LIBS:


Scalapack
~~~~~~~~~
   Your current ScaLAPACK options are:
   
   SCALAPACK_LIBS:             -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64// -lmkl_scalapack_lp64 -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64// -lmkl_blacs_openmpi_lp64
   
   which are derived from following settings:
   
   R   SCALAPACKROOT:          /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64/
   S   SCALAPACK_LIBNAME:      mkl_scalapack_lp64
   BR  BLACSROOT:              /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64/
   BL  BLACS_LIBNAME:          mkl_blacs_openmpi_lp64
   M   MKL_TARGET_ARCH:        /

   RS  Reset complete ScaLAPACK setup
   X   Delete all settings
   
   B   Back to parallel options

ELPA
~~~~
   Your current ELPA options are:
   
   ELPA_OPT:             -DELPA -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa_openmp-2021.11.001/elpa 
                  -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa_openmp-2021.11.001/modules
   ELPA_LIBS:            -lelpa_openmp -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib -Wl,-rpath=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib
   
   which are derived from following settings:
   
   R  ELPAROOT:          /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/
   V  ELPA_VERSION:      2021.11.001
   L  ELPA_LIB:          lib
   N  ELPA_LIBNAME:      elpa_openmp
   
   RS Reset complete ELPA setup
   X  Delete all settings
   
   B  Back to parallel options


   *             Specify parallel options and library settings           *
   ***********************************************************************

   Your current parallel settings (options and libraries) are:
   
     C   Parallel Compiler:          mpif90
     FP  Parallel Compiler Options:  -O -FR -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback -assume buffered_io -I$(MKLROOT)/include
     MP  MPIRUN command:             srun -K -N_nodes_ -n_NP_ -r_offset_ _PINNING_ _EXEC_
     O   Parallel OpenMP switch:     -qopenmp

   Additional setting for SLURM batch systems (is set to 1 otherwise):
 
     CN  Number of Cores:            16

   Libraries:
 
     Sp  SCALAPACK:                   -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64// 
                                                     -lmkl_scalapack_lp64 
                                                     -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl/lib/intel64// -lmkl_blacs_openmpi_lp64
     E   ELPA options:                -DELPA -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa-2021.11.001/elpa 
                                                     -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa-2021.11.001/modules
         ELPA-LIBS:                   -lelpa -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib -Wl,-rpath=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib

     RP  Parallel-Libs:      $(R_LIBS)


     B   Back to compiler/linker options   




