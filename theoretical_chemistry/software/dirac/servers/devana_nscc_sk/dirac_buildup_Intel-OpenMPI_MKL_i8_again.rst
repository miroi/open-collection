DIRAC buildups on Devana
=========================

/home/milias/work/software/dirac/dirac_public

modules
-------

OpenMPI-Intel
~~~~~~~~~~~~~
module load OpenMPI/4.1.1-intel-compilers-2021.4.0

which mpif90
/storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpif90
mpif90 --version
ifort (IFORT) 2021.4.0 20210910

which mpirun
/storage-apps/easybuild/software/OpenMPI/4.1.1-intel-compilers-2021.4.0/bin/mpirun
milias@login02.devana.local:~/work/software/dirac/dirac_public/.mpirun --version
mpirun (Open MPI) 4.1.1


MKL
~~~
module load mkl/latest
Loading mkl version 2023.0.0
Loading tbb version 2021.8.0
Loading compiler-rt version 2023.0.0

ls /storage-apps/intel-v.2023/oneapi/mkl/2023.0.0/lib/intel64/


CMake
~~~~~~
milias@login02.devana.local:~/work/software/dirac/dirac_public/.module load CMake/3.20.1-GCCcore-10.3.0


HDF5
~~~~
module load HDF5/1.10.7-iompi-2021a

All modules
~~~~~~~~~~~
module list

Currently Loaded Modules:
  1) OpenSSL/1.1                 10) XZ/5.2.5-GCCcore-10.3.0           19) libevent/2.1.12-GCCcore-10.3.0
  2) tbb/2021.8.0                11) libarchive/3.5.1-GCCcore-10.3.0   20) UCX/1.10.0-GCCcore-10.3.0
  3) compiler-rt/2023.0.0        12) CMake/3.20.1-GCCcore-10.3.0       21) libfabric/1.12.1-GCCcore-10.3.0
  4) mkl/latest                  13) binutils/2.36.1-GCCcore-10.3.0    22) PMIx/3.2.3-GCCcore-10.3.0
  5) GCCcore/10.3.0              14) intel-compilers/2021.2.0          23) OpenMPI/4.1.1-intel-compilers-2021.2.0
  6) ncurses/6.2-GCCcore-10.3.0  15) numactl/2.0.14-GCCcore-10.3.0     24) iompi/2021a
  7) zlib/1.2.11-GCCcore-10.3.0  16) libxml2/2.9.10-GCCcore-10.3.0     25) Szip/2.1.1-GCCcore-10.3.0
  8) bzip2/1.0.8-GCCcore-10.3.0  17) libpciaccess/0.16-GCCcore-10.3.0  26) HDF5/1.10.7-iompi-2021a
  9) cURL/7.76.0-GCCcore-10.3.0  18) hwloc/2.4.1-GCCcore-10.3.0



DIRAC with OpenMPI-Intel-i8
---------------------------

milias@login02.devana.local:~/work/software/dirac/dirac_public/../setup --mpi --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx  --mkl=parallel  build_openmpi_intel_mklpar_i8


m -j16

