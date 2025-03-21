======================
Wien2k_23.2 on kelinux
======================

Modules
--------
module use /lustre/home/utils/easybuild_old/modules/all
module purge
module load FFTW.MPI/3.3.10-gompi-2022a
module load ScaLAPACK/2.2.0-gompi-2022a-fb
module load ELPA/2021.11.001-foss-2022a

module list

Currently Loaded Modules:
  1) GCCcore/11.3.0                     9) hwloc/2.7.1-GCCcore-11.3.0       17) gompi/2022a
  2) zlib/1.2.12-GCCcore-11.3.0        10) OpenSSL/1.1                      18) FFTW/3.3.10-GCC-11.3.0
  3) binutils/2.38-GCCcore-11.3.0      11) libevent/2.1.12-GCCcore-11.3.0   19) FFTW.MPI/3.3.10-gompi-2022a
  4) GCC/11.3.0                        12) UCX/1.12.1-GCCcore-11.3.0        20) OpenBLAS/0.3.20-GCC-11.3.0
  5) numactl/2.0.14-GCCcore-11.3.0     13) libfabric/1.15.1-GCCcore-11.3.0  21) FlexiBLAS/3.2.0-GCC-11.3.0
  6) XZ/5.2.5-GCCcore-11.3.0           14) PMIx/4.1.2-GCCcore-11.3.0        22) ScaLAPACK/2.2.0-gompi-2022a-fb
  7) libxml2/2.9.13-GCCcore-11.3.0     15) UCC/1.0.0-GCCcore-11.3.0         23) foss/2022a
  8) libpciaccess/0.16-GCCcore-11.3.0  16) OpenMPI/4.1.4-GCC-11.3.0         24) ELPA/2021.11.001-foss-2022a

Check compilers and libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
which mpif90; mpif90 --version
/lustre/home/utils/easybuild_old/software/OpenMPI/4.1.4-GCC-11.3.0/bin/mpif90
GNU Fortran (GCC) 11.3.0

which mpirun; mpirun --version
/lustre/home/utils/easybuild_old/software/OpenMPI/4.1.4-GCC-11.3.0/bin/mpirun
mpirun (Open MPI) 4.1.4

module show OpenBLAS/0.3.20-GCC-11.3.0  
ls /lustre/home/utils/easybuild_old/software/OpenBLAS/0.3.20-GCC-11.3.0/lib

module show ScaLAPACK/2.2.0-gompi-2022a-fb
ls /lustre/home/utils/easybuild_old/software/ScaLAPACK/2.2.0-gompi-2022a-fb/lib

module show ELPA/2021.11.001-foss-2022a
ls /lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/lib

module show FFTW.MPI/3.3.10-gompi-2022a
ls /lustre/home/utils/easybuild_old/software/FFTW.MPI/3.3.10-gompi-2022a/lib

module show FFTW/3.3.10-GCC-11.3.0 
ls /lustre/home/utils/easybuild_old/software/FFTW.MPI/3.3.10-gompi-2022a/lib

Wien2k buildup
--------------

./siteconfig_lapw

LG linuxgfortran
C: mpif90, mpicc
MKL_TARGET_ARCH was set to intel64
O:
P:

Compiler options:
-----------------
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
  R   R_LIBS (LAPACK+BLAS):    -L/lustre/home/utils/easybuild_old/software/OpenBLAS/0.3.20-GCC-11.3.0/lib -lopenblas -lpthread
  F   FFTW options:            -DFFTW3 -I/lustre/home/utils/easybuild_old/software/FFTW.MPI/3.3.10-gompi-2022a/include
      FFTW-LIBS:               -L/lustre/home/utils/easybuild_old/software/FFTW.MPI/3.3.10-gompi-2022a/lib -lfftw3
      FFTW-PLIBS:              -lfftw3_mpi
  X   LIBX options:
      LIBXC-LIBS:


FFTW
~~~~
 F   FFTW options:            -DFFTW3 -I/lustre/home/utils/easybuild_old/software/FFTW.MPI/3.3.10-gompi-2022a/include
      FFTW-LIBS:               -L/lustre/home/utils/easybuild_old/software/FFTW.MPI/3.3.10-gompi-2022a/lib -lfftw3
      FFTW-PLIBS:              -lfftw3_mpi

ELPA
~~~~
  Your ELPA_OPT are:   -DELPA -I/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/include/elpa_openmp-2021.11.001/elpa 
                           -I/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/include/elpa_openmp-2021.11.001/modules 
  Your ELPA_LIBS are:  -lelpa_openmp -L/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/lib -Wl,rpath=/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/lib

  These options derive from your chosen Settings:
   
  ELPAROOT:            /lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/
  ELPA_VERSION:        2021.11.001
  ELPA_LIB:            lib
  ELPA_LIBNAME:        elpa_openmp


ScaLAPACK
~~~~~~~~~
    Sp  SCALAPACK:                   -L/lustre/home/utils/easybuild_old/software/ScaLAPACK/2.2.0-gompi-2022a-fb/lib/ 
                                                     -lscalapack


Parallel
~~~~~~~~~
     C   Parallel Compiler:          mpif90
     FP  Parallel Compiler Options:  -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none -fallow-argument-mismatch
     MP  MPIRUN command:             mpirun -np _NP_ -machinefile _HOSTS_ _EXEC_
     O   Parallel OpenMP switch:     -fopenmp
     Sp  SCALAPACK:                   -L/lustre/home/utils/easybuild_old/software/ScaLAPACK/2.2.0-gompi-2022a-fb/lib/ 
                                                     -lscalapack
     E   ELPA options:                -DELPA -I/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/include/elpa-2021.11.001/elpa 
                                                     -I/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/include/elpa-2021.11.001/modules
         ELPA-LIBS:                   -lelpa -L/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/lib -Wl,-rpath=/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/lib

### I had to extend it manually for missing libs to get mpi-based executables compiled!!!

     RP  Parallel-Libs:  -L/lustre/home/utils/easybuild_old/software/FFTW.MPI/3.3.10-gompi-2022a/lib -lfftw3 -lfftw3_mpi -L/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/lib -lelpa -lelpa_openmp -L/lustre/home/utils/easybuild_old/software/OpenBLAS/0.3.20-GCC-11.3.0/lib -lopenblas -lpthread


Dimensions
~~~~~~~~~~
set value for NMATMAX=60000


Check of compilation
--------------------
ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_gnu_openmpi_openblas/.cat SRC*/compile.msg | grep error

cat SRC*/compile.msg | less | grep 

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_gnu_openmpi_openblas/.ls *mpi
dstart_mpi*  hfc_mpi*  hf_mpi*  lapw0_mpi*  lapw1c_mpi*  lapw1_mpi*  lapw2c_mpi*  lapw2_mpi*  lapwso_mpi*  nlvdw_mpi*  nmrc_mpi*  nmr_mpi*

ilias@login1.kelinux.saske.sk:~/work/qch/software/wien2k/WIEN2k_23.2_gnu_openmpi_openblas/.ls dstart lapw* mixer 
dstart*     lapw0para_lapw*  lapw1cpara@      lapw2*       lapw2_mpi*       lapw3c*  lapw7c*       lapwdmpara@       lapwso_mpi*
lapw0*      lapw1*           lapw1_mpi*       lapw2c*      lapw2para@       lapw5*   lapwdm*       lapwdmpara_lapw*  lapwsopara@
lapw0_mpi*  lapw1c*          lapw1para@       lapw2c_mpi*  lapw2para_lapw*  lapw5c*  lapwdmc*      lapwso*           lapwsopara_lapw*
lapw0para@  lapw1c_mpi*      lapw1para_lapw*  lapw2cpara@  lapw3*           lapw7*   lapwdmcpara@  lapwsocpara@      mixer*

