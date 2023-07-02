===================
Wien2k_23.2 buildup
===================

in /lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas

Packages
--------
spack unload --all
spack load gcc@10.2.0 target=x86_64; spack load openmpi%gcc target=x86_64; spack load amdfftw%gcc target=x86_64; spack load elpa%gcc target=x86_64; spack load openblas%gcc target=x86_64; spack load amdscalapack%gcc target=x86_64


All loaded packages
~~~~~~~~~~~~~~~~~~~
spack find --loaded
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.spack find --loaded
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
autoconf@2.69                diffutils@3.8  gmp@6.2.1        libtool@2.4.7  mpfr@4.1.0   readline@8.1.2  zstd@1.5.2
autoconf-archive@2022.02.11  gawk@5.1.1     libiconv@1.16    m4@1.4.19      ncurses@6.1  texinfo@6.5
automake@1.16.5              gcc@10.2.0     libsigsegv@2.13  mpc@1.2.1      perl@5.16.3  zlib@1.2.13

-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdfftw@3.0                         gdbm@1.23             libmd@1.0.4        openmpi@4.1.5         slurm@21-08-8-2
amdscalapack@3.2                    gettext@0.21.1        libpciaccess@0.16  openssh@9.1p1         sqlite@3.39.4
autoconf@2.69                       glib@2.74.1           libsigsegv@2.13    openssl@1.1.1s        tar@1.34
autoconf-archive@2022.02.11         gmp@6.2.1             libtool@2.4.7      pcre2@10.39           texinfo@6.5
automake@1.16.5                     hwloc@2.8.0           libxml2@2.10.1     perl@5.16.3           ucx@1.9.0
bison@3.8.2                         json-c@0.16           lz4@1.9.4          pigz@2.7              util-linux-uuid@2.38.1
bzip2@1.0.8                         krb5@1.19.3           m4@1.4.19          pkgconf@1.8.0         util-macros@1.19.3
ca-certificates-mozilla@2022-10-11  libbsd@0.11.5         meson@0.63.3       pmix@3.2.2            xz@5.2.7
cmake@3.24.3                        libedit@3.1-20210216  mpfr@4.1.0         py-pip@22.2.2         zlib@1.2.13
curl@7.85.0                         libevent@2.1.12       munge@0.5.13       py-setuptools@59.4.0  zstd@1.5.2
diffutils@3.8                       libffi@3.4.2          ncurses@6.1        py-wheel@0.37.1
elpa@2021.11.001                    libgcrypt@1.10.1      ninja@1.11.1       python@3.10.8
expat@2.4.8                         libgpg-error@1.46     numactl@2.0.14     rdma-core@22.4
gawk@5.1.1                          libiconv@1.16         openblas@0.3.21    readline@8.1.2
==> 85 loaded packages



OpenMPI & GNU compilers
~~~~~~~~~~~~~~~~~~~~~~~~~
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.which gfortran
/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/gcc-10.2.0-agxjp3zexhitnb3g6czo5p4im3hi74ht/bin/gfortran

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.gfortran --version
GNU Fortran (Spack GCC) 10.2.0

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.which mpif90
/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/bin/mpif90
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.mpif90 --version
GNU Fortran (Spack GCC) 10.2.0

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.which mpicc; mpicc --version
/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/bin/mpicc
gcc (Spack GCC) 10.2.0

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.which mpirun; mpirun --version
/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/bin/mpirun
mpirun (Open MPI) 4.1.5


OpenBLAS library
~~~~~~~~~~~~~~~~~
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.spack find --paths openblas%gcc  target=x86_64
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
openblas@0.3.21  /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib/


FFTW3 library
~~~~~~~~~~~~~
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.spack find --paths amdfftw%gcc  target=x86_64
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdfftw@3.0  /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib/
cmake/                   libfftw3f_omp.so@        libfftw3f.so.3@      libfftw3_mpi.so.3.5.8*  libfftw3.so@
libfftw3f_mpi.so@        libfftw3f_omp.so.3@      libfftw3f.so.3.5.8*  libfftw3_omp.so@        libfftw3.so.3@
libfftw3f_mpi.so.3@      libfftw3f_omp.so.3.5.8*  libfftw3_mpi.so@     libfftw3_omp.so.3@      libfftw3.so.3.5.8*
libfftw3f_mpi.so.3.5.8*  libfftw3f.so@            libfftw3_mpi.so.3@   libfftw3_omp.so.3.5.8*  pkgconfig/

ELPA
~~~~
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.spack find --paths elpa%gcc target=x86_64
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
elpa@2021.11.001  /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib/
libelpa_openmp.a  libelpa_openmp.so@  libelpa_openmp.so.17@  libelpa_openmp.so.17.0.0*  pkgconfig/

scalapack
~~~~~~~~~
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.spack find --paths amdscalapack%gcc target=x86_64
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdscalapack@3.2  /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/
cmake/  libscalapack.so  pkgconfig/

Wien2k Compilation
-------------------
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.gunzip *
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.expand_lapw 
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/..siteconfig_lapw


LG
mpif90
mpicc

Compiler and linker options
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Recommended options for system linuxgfortran are:
      OpenMP switch:           -fopenmp
      Compiler options:        -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none
      Linker Flags:            $(FOPT) -L../SRC_lib
      Preprocessor flags:      '-DParallel'
      R_LIB (LAPACK+BLAS):     /usr/lib64/libopenblas_openmp.so.0 -lpthread

 Current settings:
  M   OpenMP switch:           -fopenmp
  O   Compiler options:        -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none
  L   Linker Flags:            $(FOPT) -L../SRC_lib -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib -lfftw3 -lfftw3_omp
  P   Preprocessor flags       '-DParallel'
  R   R_LIBS (LAPACK+BLAS):    -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib -lopenblas
  F   FFTW options:            -DFFTW3 -DFFTW_OMP -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/include
      FFTW-LIBS:               -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib -lfftw3 -lfftw3_omp
      FFTW-PLIBS:              -lfftw3_mpi
  X   LIBX options:
      LIBXC-LIBS:

 Your current parallel settings (options and libraries) are:
   
     C   Parallel Compiler:          mpif90
     FP  Parallel Compiler Options:  -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none -fallow-argument-mismatch
     MP  MPIRUN command:             mpirun -np _NP_ -machinefile _HOSTS_ _EXEC_
     O   Parallel OpenMP switch:     -fopenmp

   Additional setting for SLURM batch systems (is set to 1 otherwise):
 
     CN  Number of Cores:            1

   Libraries:
 
     Sp  SCALAPACK:                   -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/ 
                                                     -lscalapack 
                                                     -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/ -lscalapack
     E   ELPA options:                -DELPA -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa-2021.11.001/elpa 
                                                     -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa-2021.11.001/modules
         ELPA-LIBS:                   -lelpa -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib -Wl,-rpath=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib

     RP  Parallel-Libs:      -lfftw3 -lfftw3_omp -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib -lopenblas -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/lib -lmpi

     B   Back to compiler/linker options   

FFTW
~~~~
 The OMP parallel version of your FFTW library will be used.

  Your FFTW_OPT are:   -DFFTW3 -DFFTW_OMP -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/include 
  Your FFTW_LIBS are:  -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib -lfftw3 -lfftw3_omp
  Your FFTW_PLIBS are: -lfftw3_mpi

  These options derive from your chosen settings:
   
  FFTWROOT:            /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/
  FFTW_VERSION:        FFTW3
  FFTW_LIB:            lib
  FFTW_LIBNAME:        fftw3
  Is this correct? (Y,n): 

Scalapack
~~~~~~~~~
Your SCALAPACK_LIBS are:    -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/ -lscalapack -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/ -lscalapack

  These options derive from your chosen settings:
   
  SCALAPACKROOT:       /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/
  SCALAPACK_LIBNAME:   scalapack
  BLACSROOT:           /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/
  BLACS_LIBNAME:       scalapack
  MKL_TARGET_ARCH:     
 Is this correct? (Y,n): 


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

Dimensions
~~~~~~~~~~
The present values are:
      PARAMETER          (NMATMAX=   100000)
      PARAMETER          (NUME=   10000)


Check
-----
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.less SRC*/compile.msg | grep error
..none !


