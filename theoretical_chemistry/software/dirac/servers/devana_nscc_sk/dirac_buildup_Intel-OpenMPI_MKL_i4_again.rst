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
module load CMake


HDF5
~~~~
module load HDF5/1.10.7-iompi-2021a

LibC
~~~~
milias@login01.devana.local:~/work/software/dirac/dirac_public/.ml load  libcerf/2.1-GCCcore-11.3.0

The following have been reloaded with a version change:
  1) GCCcore/10.3.0 => GCCcore/11.3.0


All modules
~~~~~~~~~~~
module list

Currently Loaded Modules:
  1) tbb/2021.8.0                            11) libpciaccess/0.16-GCCcore-10.3.0        21) GCCcore/12.2.0
  2) compiler-rt/2023.0.0                    12) hwloc/2.4.1-GCCcore-10.3.0              22) zlib/1.2.12-GCCcore-12.2.0
  3) mkl/latest                              13) libevent/2.1.12-GCCcore-10.3.0          23) XZ/5.2.7-GCCcore-12.2.0
  4) OpenSSL/1.1                             14) UCX/1.10.0-GCCcore-10.3.0               24) ncurses/6.3-GCCcore-12.2.0
  5) impi/2021.6.0-intel-compilers-2022.1.0  15) libfabric/1.12.1-GCCcore-10.3.0         25) bzip2/1.0.8-GCCcore-12.2.0
  6) iimpi/2022a                             16) PMIx/3.2.3-GCCcore-10.3.0               26) cURL/7.86.0-GCCcore-12.2.0
  7) binutils/2.36.1-GCCcore-10.3.0          17) OpenMPI/4.1.1-intel-compilers-2021.2.0  27) libarchive/3.6.1-GCCcore-12.2.0
  8) intel-compilers/2021.2.0                18) iompi/2021a                             28) CMake/3.24.3-GCCcore-12.2.0
  9) numactl/2.0.14-GCCcore-10.3.0           19) Szip/2.1.1-GCCcore-10.3.0
 10) libxml2/2.9.10-GCCcore-10.3.0           20) HDF5/1.10.7-iompi-2021a



DIRAC with OpenMPI-Intel-i4
---------------------------
milias@login02.devana.local:~/work/software/dirac/dirac_public/../setup --mpi --fc=mpif90 --cc=mpicc --cxx=mpicxx  --mkl=parallel  build_openmpi_intel_mklpar_i4




