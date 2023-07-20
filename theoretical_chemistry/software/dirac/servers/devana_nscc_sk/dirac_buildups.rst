DIRAC buildups on Devana
=========================

/home/milias/work/software/dirac/dirac_public

modules
-------

OpenMPI-Intel
~~~~~~~~~~~~~
module load OpenMPI/4.1.1-intel-compilers-2021.4.0

milias@login02.devana.local:~/work/software/dirac/dirac_public/.which mpif90
/storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90
milias@login02.devana.local:~/work/software/dirac/dirac_public/.mpif90 --version
ifort (IFORT) 2021.4.0 20210910

milias@login02.devana.local:~/work/software/dirac/dirac_public/.which mpirun
/storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpirun
milias@login02.devana.local:~/work/software/dirac/dirac_public/.mpirun --version
mpirun (Open MPI) 4.1.1


MKL
~~~
milias@login02.devana.local:~/work/software/dirac/dirac_public/.module load mkl/latest
Loading mkl version 2023.0.0
Loading tbb version 2021.8.0
Loading compiler-rt version 2023.0.0

see: ls /storage-apps/intel-v.2023/oneapi/mkl/2023.0.0/lib/intel64/


CMake
~~~~~~
milias@login02.devana.local:~/work/software/dirac/dirac_public/.module load CMake/3.24.3-GCCcore-12.2.0

The following have been reloaded with a version change:
  1) GCCcore/11.2.0 => GCCcore/12.2.0
  2) XZ/5.2.5-GCCcore-11.2.0 => XZ/5.2.7-GCCcore-12.2.0
  3) zlib/1.2.11-GCCcore-11.2.0 => zlib/1.2.12-GCCcore-12.2.0

milias@login02.devana.local:~/work/software/dirac/dirac_public/.module list

Currently Loaded Modules:
  1) binutils/2.37-GCCcore-11.2.0            13) tbb/2021.8.0
  2) intel-compilers/2021.4.0                14) compiler-rt/2023.0.0
  3) numactl/2.0.14-GCCcore-11.2.0           15) mkl/latest
  4) libxml2/2.9.10-GCCcore-11.2.0           16) GCCcore/12.2.0
  5) libpciaccess/0.16-GCCcore-11.2.0        17) ncurses/6.3-GCCcore-12.2.0
  6) hwloc/2.5.0-GCCcore-11.2.0              18) zlib/1.2.12-GCCcore-12.2.0
  7) OpenSSL/1.1                             19) bzip2/1.0.8-GCCcore-12.2.0
  8) libevent/2.1.12-GCCcore-11.2.0          20) cURL/7.86.0-GCCcore-12.2.0
  9) UCX/1.11.2-GCCcore-11.2.0               21) XZ/5.2.7-GCCcore-12.2.0
 10) libfabric/1.13.2-GCCcore-11.2.0         22) libarchive/3.6.1-GCCcore-12.2.0
 11) PMIx/4.1.0-GCCcore-11.2.0               23) CMake/3.24.3-GCCcore-12.2.0
 12) OpenMPI/4.1.1-intel-compilers-2021.4.0



DIRAC with OpenMPI-Intel-i8
---------------------------

milias@login02.devana.local:~/work/software/dirac/dirac_public/../setup --mpi --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx  --mkl=parallel  build_openmpi_intel_mklpar_i8


