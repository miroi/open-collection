=======================
NWChem on Virgo at GSI
=======================

Virgo modules
-------------
https://hpc.gsi.de/virgo/platform/software.html#available-software

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/src/.spack find openmpi%intel
-- linux-debian10-x86_64 / intel@19.1.1.217 ---------------------
openmpi@4.1.5
==> 1 installed package
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/src/.spack load openmpi%intel

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/.spack load elpa@2021.11.001 target=x86_64
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/.spack load amdscalapack target=x86_64


#milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/.spack load openmpi%gcc target=x86_64
#milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/.spack unload openmpi%gcc

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/.spack find --loaded

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/src/.spack find --loaded
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdscalapack@3.2                    gdbm@1.23             libiconv@1.16      numactl@2.0.14        python@3.10.8
autoconf@2.69                       gettext@0.21.1        libmd@1.0.4        openblas@0.3.21       rdma-core@22.4
autoconf-archive@2022.02.11         glib@2.74.1           libpciaccess@0.16  openmpi@4.1.5         readline@8.1.2
automake@1.16.5                     gmp@6.2.1             libsigsegv@2.13    openssh@9.1p1         slurm@21-08-8-2
bison@3.8.2                         hwloc@2.8.0           libtool@2.4.7      openssl@1.1.1s        sqlite@3.39.4
bzip2@1.0.8                         json-c@0.16           libxml2@2.10.1     pcre2@10.39           tar@1.34
ca-certificates-mozilla@2022-10-11  krb5@1.19.3           lz4@1.9.4          perl@5.16.3           texinfo@6.5
cmake@3.24.3                        libbsd@0.11.5         m4@1.4.19          pigz@2.7              ucx@1.9.0
curl@7.85.0                         libedit@3.1-20210216  meson@0.63.3       pkgconf@1.8.0         util-linux-uuid@2.38.1
diffutils@3.8                       libevent@2.1.12       mpfr@4.1.0         pmix@3.2.2            util-macros@1.19.3
elpa@2021.11.001                    libffi@3.4.2          munge@0.5.13       py-pip@22.2.2         xz@5.2.7
expat@2.4.8                         libgcrypt@1.10.1      ncurses@6.1        py-setuptools@59.4.0  zlib@1.2.13
gawk@5.1.1                          libgpg-error@1.46     ninja@1.11.1       py-wheel@0.37.1       zstd@1.5.2

-- linux-debian10-x86_64 / intel@19.1.1.217 ---------------------
openmpi@4.1.5  pkgconf@1.8.0
==> 67 loaded packages
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/src/.


milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/.emkl
Intel MKL library ? MKLROOT=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-ibhuetil7ipyeb4qfw4xldp4ib42v3ca/compilers_and_libraries_2020.1.217/linux/mkl


NWChem clone and variables setting
-----------------------------------
from https://nwchemgit.github.io/Compiling-NWChem.html :

milias@lxbk0600.gsi.de:/lustre/ukt/milias/work/software/nwchem/.git clone -b release-7-2-0 https://github.com/nwchemgit/nwchem.git nwchem-7.2.0

export NWCHEM_TOP=/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0
export NWCHEM_TARGET=LINUX64
export ARMCI_NETWORK=MPI-PR
export USE_MPI=y
export NWCHEM_MODULES="all python"
export USE_NOFSCHECK=TRUE
export USE_SCALAPACK=y
export BLAS_SIZE=8
export SCALAPACK_SIZE=8
export BLASOPT="-L${MKLROOT}/lib/intel64_lin -lmkl_blas95_ilp64 -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread -lm -ldl"
export LAPACK_LIB="-L${MKLROOT}/lib/intel64_lin -lmkl_lapack95_ilp64 -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread -lm -ldl"

Compiling:
~~~~~~~~~~
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0/src/.make -j16
.
.



