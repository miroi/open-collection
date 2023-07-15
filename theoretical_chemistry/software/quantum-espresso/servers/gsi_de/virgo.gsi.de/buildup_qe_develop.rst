=========================
QE-devel on Virgo cluster
=========================

/lustre/ukt/milias/work/software/quantum-espresso/q-e_develop


spack modules
~~~~~~~~~~~~~
spack unload --all; spack load openmpi%gcc target=x86_64; spack load amdfftw%gcc target=x86_64; spack load elpa%gcc target=x86_64; spack load amdscalapack%gcc target=x86_64; spack load openblas%gcc target=x86_64

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

buildup with CMake
~~~~~~~~~~~~~~~~~~
see https://gitlab.com/QEF/q-e/-/wikis/Developers/CMake-build-system

mkdir build_gnu_openmpi_openblas
cd build_gnu_openmpi_openblas

cmake -DQE_ENABLE_OPENMP=ON -DQE_ENABLE_SCALAPACK=ON -DQE_ENABLE_ELPA=ON -DBLA_VENDOR=OpenBLAS -DCMAKE_C_COMPILER=mpicc -DCMAKE_Fortran_COMPILER=mpif90  ..


