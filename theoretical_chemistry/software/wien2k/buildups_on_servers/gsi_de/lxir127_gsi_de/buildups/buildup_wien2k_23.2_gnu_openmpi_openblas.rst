===================
Wien2k_23.2 buildup
===================

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/gnu_openmpi_openblas/.

Packages
--------
spack unload --all
spack load openmpi%gcc target=x86_64; spack load amdfftw%gcc target=x86_64; spack load elpa%gcc target=x86_64
spack load openblas%gcc target=x86_64; spack load amdscalapack%gcc target=x86_64

All loaded packages
~~~~~~~~~~~~~~~~~~~
spack find --loaded

-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdfftw@3.0                         curl@7.85.0       hwloc@2.8.0           libiconv@1.16      mpfr@4.1.0       pcre2@10.39           rdma-core@22.4          xz@5.2.7
amdscalapack@3.2                    diffutils@3.8     json-c@0.16           libmd@1.0.4        munge@0.5.13     perl@5.16.3           readline@8.1.2          zlib@1.2.13
autoconf@2.69                       elpa@2021.11.001  krb5@1.19.3           libpciaccess@0.16  ncurses@6.1      pigz@2.7              slurm@21-08-8-2         zstd@1.5.2
autoconf-archive@2022.02.11         expat@2.4.8       libbsd@0.11.5         libsigsegv@2.13    ninja@1.11.1     pkgconf@1.8.0         sqlite@3.39.4
automake@1.16.5                     gawk@5.1.1        libedit@3.1-20210216  libtool@2.4.7      numactl@2.0.14   pmix@3.2.2            tar@1.34
bison@3.8.2                         gdbm@1.23         libevent@2.1.12       libxml2@2.10.1     openblas@0.3.21  py-pip@22.2.2         texinfo@6.5
bzip2@1.0.8                         gettext@0.21.1    libffi@3.4.2          lz4@1.9.4          openmpi@4.1.5    py-setuptools@59.4.0  ucx@1.9.0
ca-certificates-mozilla@2022-10-11  glib@2.74.1       libgcrypt@1.10.1      m4@1.4.19          openssh@9.1p1    py-wheel@0.37.1       util-linux-uuid@2.38.1
cmake@3.24.3                        gmp@6.2.1         libgpg-error@1.46     meson@0.63.3       openssl@1.1.1s   python@3.10.8         util-macros@1.19.3
==> 66 loaded packages

OpenMPI & GNU compilers
~~~~~~~~~~~~~~~~~~~~~~~~~
which mpif90; mpif90 --version
/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/bin/mpif90
GNU Fortran (Spack GCC) 10.2.0

which mpicc; mpicc --version
/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/bin/mpicc
gcc (Spack GCC) 10.2.0

which mpirun; mpirun --version
/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/bin/mpirun
mpirun (Open MPI) 4.1.5


OpenBLAS library
~~~~~~~~~~~~~~~~~
spack find --paths openblas%gcc  target=x86_64
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
openblas@0.3.21  /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34

ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib/


FFTW3 library
~~~~~~~~~~~~~
spack find --paths amdfftw%gcc  target=x86_64
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdfftw@3.0  /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb

ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib/
cmake/                   libfftw3f_omp.so@        libfftw3f.so.3@      libfftw3_mpi.so.3.5.8*  libfftw3.so@
libfftw3f_mpi.so@        libfftw3f_omp.so.3@      libfftw3f.so.3.5.8*  libfftw3_omp.so@        libfftw3.so.3@
libfftw3f_mpi.so.3@      libfftw3f_omp.so.3.5.8*  libfftw3_mpi.so@     libfftw3_omp.so.3@      libfftw3.so.3.5.8*
libfftw3f_mpi.so.3.5.8*  libfftw3f.so@            libfftw3_mpi.so.3@   libfftw3_omp.so.3.5.8*  pkgconfig/

ELPA
~~~~
spack find --paths elpa%gcc target=x86_64
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
elpa@2021.11.001  /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms

ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib/
libelpa_openmp.a  libelpa_openmp.so@  libelpa_openmp.so.17@  libelpa_openmp.so.17.0.0*  pkgconfig/

scalapack
~~~~~~~~~
spack find --paths amdscalapack%gcc target=x86_64
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdscalapack@3.2  /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm
ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/
cmake/  libscalapack.so  pkgconfig/

Wien2k Compilation
-------------------
gunzip *
expand_lapw 
siteconfig_lapw


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
  R   R_LIBS (LAPACK+BLAS):    -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib -lopenblas -lpthread
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

Summary of parallel settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

   Current settings:

         Parallel compiler      : mpif90
         SCALAPACK_LIBS         : -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/ -lscalapack
         FFTW_PLIBS             : -lfftw3_mpi
         ELPA_OPT               : -DELPA -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa-2021.11.001/elpa 
                    -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa-2021.11.001/modules
         ELPA_LIBS              : -lelpa -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib -Wl,-rpath=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib
         FPOPT(par.comp.options): -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none -fallow-argument-mismatch
         OMP_SWITCH             : -fopenmp
         MPIRUN command         : mpirun -np _NP_ -machinefile _HOSTS_ _EXEC_
       
   parallel execution:

         RP_LIBS                : 

     S   Accept, Save, and Quit


Dimensions
~~~~~~~~~~
WIEN2k uses dynamical allocation of most arrays according to the requirements of 
your example. However, to avoid that the programs grow larger than the memory of 
your computer, there are two limiting parameters, NMATMAX (the maximum matrix
size) and NUME (number of eigenvalues), which should be set corresponding to your 
hardware. 

A matrix of 20000x20000 requires 4 (8) Gb of memory for a single lapw1 (using 10 
(20) bytes for real (complex) numbers to account for overheads). 

Thus set NMATMAX to  sqrt(MEMORY/10)  (MEMORY in Bytes)!

NMATMAX=20000 ==>   4GB (real) (==> cells with about 50-150 atoms/unitcell)
    ==> for lapw1c:    NMATMAX will be reduced internally to NMATMAX/sqrt2
    ==> for lapw1_mpi: NMATMAX will be increased internally to NMATMAX*sqrt(NP)

NUME determines the number of states to output. As a rule of thumb one can estimate 
100 basis functions per atom in the cell and 10 occupied states per atom, so set    

NUME=NMATMAX/10!

The present values are:
      PARAMETER          (NMATMAX=   60000)
      PARAMETER          (NUME=   6000)

    Change parameters in:

    1   lapw1/2  (e.g. NMATMAX, NUME, RESTRICT_OUTPUT)
    A   all programs (usually not necessary)

    Q   to quit

     Selection: A

      PARAMETER          (NMATMAX=   60000)
      PARAMETER          (NUME=   6000)
      PARAMETER          (RESTRICT_OUTPUT= 9999) ! 1 for mpi with less output-files

Which parameter to change? (q to quit): 


  PO  Parallel options

  S   Save and Quit
  Q   Quit and abandon changes

Check
-----

SRC_lapw0/Makefile.orig modified a little , but on Virgo no need to modify, just mixed links
.../Wien2k_23.2_gnu_openmpi_openblas/.less SRC*/compile.msg | grep error
