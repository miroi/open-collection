ELPA buildup
============

https://elpa.mpcdf.mpg.de/software/tarball-archive/Releases/2023.05.001/elpa-2023.05.001.tar.gz

see  https://gitlab.mpcdf.mpg.de/elpa/elpa/-/blob/master/documentation/INSTALL.md

Spack packages
~~~~~~~~~~~~~~~
spack unload --all
spack load gcc@10.2.0 target=x86_64; spack load openmpi%gcc target=x86_64

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/elpa/elpa-2023.05.001/.spack find --loaded
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
autoconf@2.69                automake@1.16.5  gawk@5.1.1  gmp@6.2.1      libsigsegv@2.13  m4@1.4.19  mpfr@4.1.0   perl@5.16.3     texinfo@6.5  zstd@1.5.2
autoconf-archive@2022.02.11  diffutils@3.8    gcc@10.2.0  libiconv@1.16  libtool@2.4.7    mpc@1.2.1  ncurses@6.1  readline@8.1.2  zlib@1.2.13

-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
autoconf@2.69                       diffutils@3.8   json-c@0.16           libiconv@1.16      meson@0.63.3    openssl@1.1.1s        py-wheel@0.37.1  ucx@1.9.0
autoconf-archive@2022.02.11         expat@2.4.8     krb5@1.19.3           libmd@1.0.4        mpfr@4.1.0      pcre2@10.39           python@3.10.8    util-linux-uuid@2.38.1
automake@1.16.5                     gawk@5.1.1      libbsd@0.11.5         libpciaccess@0.16  munge@0.5.13    perl@5.16.3           rdma-core@22.4   util-macros@1.19.3
bison@3.8.2                         gdbm@1.23       libedit@3.1-20210216  libsigsegv@2.13    ncurses@6.1     pigz@2.7              readline@8.1.2   xz@5.2.7
bzip2@1.0.8                         gettext@0.21.1  libevent@2.1.12       libtool@2.4.7      ninja@1.11.1    pkgconf@1.8.0         slurm@21-08-8-2  zlib@1.2.13
ca-certificates-mozilla@2022-10-11  glib@2.74.1     libffi@3.4.2          libxml2@2.10.1     numactl@2.0.14  pmix@3.2.2            sqlite@3.39.4    zstd@1.5.2
cmake@3.24.3                        gmp@6.2.1       libgcrypt@1.10.1      lz4@1.9.4          openmpi@4.1.5   py-pip@22.2.2         tar@1.34
curl@7.85.0                         hwloc@2.8.0     libgpg-error@1.46     m4@1.4.19          openssh@9.1p1   py-setuptools@59.4.0  texinfo@6.5
==> 81 loaded packages


milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/elpa/elpa-2023.05.001/.gfortran --version
GNU Fortran (Spack GCC) 10.2.0
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/elpa/elpa-2023.05.001/.mpif90 --version
GNU Fortran (Spack GCC) 10.2.0

export LD_LIBRARY_PATH=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/lib
export LD_LIBRARY_PATH=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/gcc-10.2.0-agxjp3zexhitnb3g6czo5p4im3hi74ht/lib/gcc/x86_64-pc-linux-gnu/10.2.0:$LD_LIBRARY_PATH


elpa buildup
~~~~~~~~~~~~
milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/software/wien2k/elpa/elpa-2023.05.001/../configure --prefix=$PWD --with-mpi=yes --enable-openmp
.
.
.
checking for function MPI_Init... no
checking for function MPI_Init in -lmpi... no
checking for function MPI_Init in -lmpich... no
configure: error: Could not compile an MPI C program

