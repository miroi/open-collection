===================
Wien2k_23.2 buildup
===================

/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas

Packages
--------
spack unload --all
spack load openmpi%gcc target=x86_64
spack load amdfftw%gcc target=x86_64
spack load elpa%gcc target=x86_64
spack load openblas%gcc target=x86_64
spack load amdscalapack%gcc target=x86_64

OpenMPI & GNU compilers
~~~~~~~~~~~~~~~~~~~~~~~~~
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

All loaded packages
~~~~~~~~~~~~~~~~~~~
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.spack find --loaded
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdfftw@3.0                         elpa@2021.11.001  libedit@3.1-20210216  lz4@1.9.4        openssl@1.1.1s        readline@8.1.2
amdscalapack@3.2                    expat@2.4.8       libevent@2.1.12       m4@1.4.19        pcre2@10.39           slurm@21-08-8-2
autoconf@2.69                       gawk@5.1.1        libffi@3.4.2          meson@0.63.3     perl@5.16.3           sqlite@3.39.4
autoconf-archive@2022.02.11         gdbm@1.23         libgcrypt@1.10.1      mpfr@4.1.0       pigz@2.7              tar@1.34
automake@1.16.5                     gettext@0.21.1    libgpg-error@1.46     munge@0.5.13     pkgconf@1.8.0         texinfo@6.5
bison@3.8.2                         glib@2.74.1       libiconv@1.16         ncurses@6.1      pmix@3.2.2            ucx@1.9.0
bzip2@1.0.8                         gmp@6.2.1         libmd@1.0.4           ninja@1.11.1     py-pip@22.2.2         util-linux-uuid@2.38.1
ca-certificates-mozilla@2022-10-11  hwloc@2.8.0       libpciaccess@0.16     numactl@2.0.14   py-setuptools@59.4.0  util-macros@1.19.3
cmake@3.24.3                        json-c@0.16       libsigsegv@2.13       openblas@0.3.21  py-wheel@0.37.1       xz@5.2.7
curl@7.85.0                         krb5@1.19.3       libtool@2.4.7         openmpi@4.1.5    python@3.10.8         zlib@1.2.13
diffutils@3.8                       libbsd@0.11.5     libxml2@2.10.1        openssh@9.1p1    rdma-core@22.4        zstd@1.5.2
==> 66 loaded packages

Wien2k Compilation
-------------------
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.gunzip *
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/.expand_lapw 
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2_gnu_openmpi_openblas/..siteconfig_lapw


LG
gfortran
gcc



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
  Your ELPA_OPT are:   -DELPA -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms//include/elpa_openmp-2021.11.001/elpa 
                           -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms//include/elpa_openmp-2021.11.001/modules 
  Your ELPA_LIBS are:  -lelpa_openmp -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms//lib -Wl,rpath=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms//lib

  These options derive from your chosen Settings:
   
  ELPAROOT:            /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms//
  ELPA_VERSION:        2021.11.001
  ELPA_LIB:            lib
  ELPA_LIBNAME:        elpa_openmp
  Is this correct?  (Y,n): Y


Parallel
~~~~~~~~~
  Current settings:

         Parallel compiler      : mpif90
         SCALAPACK_LIBS         : -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/ -lscalapack -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/ -lscalapack
         FFTW_PLIBS             : -lfftw3_mpi
         ELPA_OPT               : -DELPA -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms//include/elpa-2021.11.001/elpa 
                    -I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms//include/elpa-2021.11.001/modules
         ELPA_LIBS              : -lelpa -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms//lib -Wl,-rpath=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms//lib
         FPOPT(par.comp.options): -ffree-form -O2 -ftree-vectorize -march=native -ffree-line-length-none -ffpe-summary=none -fallow-argument-mismatch
         OMP_SWITCH             : -fopenmp
         MPIRUN command         : mpirun -np _NP_ -machinefile _HOSTS_ _EXEC_
       
   parallel execution:

         RP_LIBS                : /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/lib

     S   Accept, Save, and Quit
     R   Restart Configuration

   Please accept and save these settings or restart the configuration.
   If you want to change anything later on you can redo this whole configuration
   process or you can change single items in "Compiling Options".


