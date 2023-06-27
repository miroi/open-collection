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

FFTW
~~~~

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
Your SCALAPACK_LIBS are:    -L/lustre/home/utils/easybuild_old/software/ScaLAPACK/2.2.0-gompi-2022a-fb/lib/ -llibscalapack.so
  SCALAPACKROOT:       /lustre/home/utils/easybuild_old/software/ScaLAPACK/2.2.0-gompi-2022a-fb/lib/
  SCALAPACK_LIBNAME:   libscalapack.so

Parallel
~~~~~~~~~
         Parallel compiler      : mpif90
         SCALAPACK_LIBS         : -L/lustre/home/utils/easybuild_old/software/ScaLAPACK/2.2.0-gompi-2022a-fb/lib/ -llibscalapack.so
         FFTW_PLIBS             : -lfftw3_mpi
         ELPA_OPT               : -DELPA -I/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/include/elpa-2021.11.001/elpa 
                    -I/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/include/elpa-2021.11.001/modules
         ELPA_LIBS              : -lelpa -L/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/lib -Wl,-rpath=/lustre/home/utils/easybuild_old/software/ELPA/2021.11.001-foss-2022a/lib
         FPOPT(par.comp.options): -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none -fallow-argument-mismatch
         OMP_SWITCH             : -fopenmp
         MPIRUN command         : mpirun -np _NP_ -machinefile _HOSTS_ _EXEC_


Dimensions
~~~~~~~~~~
 set value for NMATMAX=60000
