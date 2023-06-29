=======================
=======================
NWChem on Virgo at GSI
=======================

spack modules
-------------
https://hpc.gsi.de/virgo/platform/software.html#available-software

spack load openmpi%gcc target=x86_64
mpif90 --version
GNU Fortran (Spack GCC) 10.2.0
mpirun --version
mpirun (Open MPI) 4.1.5

spack load amdfftw%gcc target=x86_64
spack load elpa%gcc target=x86_64
spack load amdscalapack%gcc target=x86_64
spack load openblas%gcc target=x86_64

spack find --loaded
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdfftw@3.0                         gmp@6.2.1             m4@1.4.19        py-setuptools@59.4.0
amdscalapack@3.2                    hwloc@2.8.0           meson@0.63.3     py-wheel@0.37.1
autoconf@2.69                       json-c@0.16           mpfr@4.1.0       python@3.10.8
autoconf-archive@2022.02.11         krb5@1.19.3           munge@0.5.13     rdma-core@22.4
automake@1.16.5                     libbsd@0.11.5         ncurses@6.1      readline@8.1.2
bison@3.8.2                         libedit@3.1-20210216  ninja@1.11.1     slurm@21-08-8-2
bzip2@1.0.8                         libevent@2.1.12       numactl@2.0.14   sqlite@3.39.4
ca-certificates-mozilla@2022-10-11  libffi@3.4.2          openblas@0.3.21  tar@1.34
cmake@3.24.3                        libgcrypt@1.10.1      openmpi@4.1.5    texinfo@6.5
curl@7.85.0                         libgpg-error@1.46     openssh@9.1p1    ucx@1.9.0
diffutils@3.8                       libiconv@1.16         openssl@1.1.1s   util-linux-uuid@2.38.1
elpa@2021.11.001                    libmd@1.0.4           pcre2@10.39      util-macros@1.19.3
expat@2.4.8                         libpciaccess@0.16     perl@5.16.3      xz@5.2.7
gawk@5.1.1                          libsigsegv@2.13       pigz@2.7         zlib@1.2.13
gdbm@1.23                           libtool@2.4.7         pkgconf@1.8.0    zstd@1.5.2
gettext@0.21.1                      libxml2@2.10.1        pmix@3.2.2
glib@2.74.1                         lz4@1.9.4             py-pip@22.2.2
==> 66 loaded packages


NWChem clone and variables setting
-----------------------------------
from https://nwchemgit.github.io/Compiling-NWChem.html :

milias@lxbk0600.gsi.de:/lustre/ukt/milias/work/software/nwchem/.git clone -b release-7-2-0 https://github.com/nwchemgit/nwchem.git nwchem-7.2.0

setting variables
~~~~~~~~~~~~~~~~~~

export NWCHEM_TOP=/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0
export LARGE_FILES=TRUE
export NWCHEM_TARGET=LINUX64
export ARMCI_NETWORK=MPI-PR
export USE_MPI=y
export NWCHEM_MODULES="all python"
export USE_NOFSCHECK=TRUE
export USE_SCALAPACK=y
export BLAS_SIZE=4
export SCALAPACK_SIZE=4
export USE_64TO32=y
export HAS_BLAS=yes
export BLASOPT="-L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib -lopenblas "
export LAPACK_LIB=$BLASOPT
export SCALAPACK_SIZE=4
export SCALAPACK="-L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib -lscalapack"
export SCALAPACK_LIB=$SCALAPACK
export ELPA="-I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa_openmp-2021.11.001/modules/ -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib/ -lelpa_openmp"

compiling
~~~~~~~~~~
see also https://groups.google.com/g/nwchem-forum/c/Ec4xe3f9IoI/m/MiECLJinCAAJ

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/src/make nwchem_config
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/src/make 64_to_32
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/src/make -j16 2>&1 | tee make.log
.
.


