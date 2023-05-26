============================
Wien2k_21.2 on virgo cluster
============================

Loading Spack Packages
----------------------
https://git.gsi.de/SDEGroup/SIR/-/issues/57
https://git.gsi.de/SDEGroup/SIR/-/issues/58

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack find | grep intel
intel-parallel-studio@professional.2020.1
intel-mkl@2019.1.144
intel-mkl@2020.4.304
-- linux-debian10-x86_64 / intel@19.1.1.217 ---------------------

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack load intel-mkl@2020.4.304
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack unload intel-parallel-studio@professional.2020.1 patchelf@0.16.1 

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack load gcc@10.2.0
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack load openmpi%gcc target=x86_64
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack load elpa@2021.11.001 target=x86_64
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack load amdscalapack target=x86_64

Check packages
~~~~~~~~~~~~~~
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack find --loaded
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
autoconf@2.69                diffutils@3.8  gmp@6.2.1        libtool@2.4.7  mpfr@4.1.0   readline@8.1.2  zstd@1.5.2
autoconf-archive@2022.02.11  gawk@5.1.1     libiconv@1.16    m4@1.4.19      ncurses@6.1  texinfo@6.5
automake@1.16.5              gcc@10.2.0     libsigsegv@2.13  mpc@1.2.1      perl@5.16.3  zlib@1.2.13

-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdscalapack@3.2                    gmp@6.2.1             lz4@1.9.4        py-pip@22.2.2
autoconf@2.69                       hwloc@2.8.0           m4@1.4.19        py-setuptools@59.4.0
autoconf-archive@2022.02.11         intel-mkl@2020.4.304  meson@0.63.3     py-wheel@0.37.1
automake@1.16.5                     json-c@0.16           mpfr@4.1.0       python@3.10.8
bison@3.8.2                         krb5@1.19.3           munge@0.5.13     rdma-core@22.4
bzip2@1.0.8                         libbsd@0.11.5         ncurses@6.1      readline@8.1.2
ca-certificates-mozilla@2022-10-11  libedit@3.1-20210216  ninja@1.11.1     slurm@21-08-8-2
cmake@3.24.3                        libevent@2.1.12       numactl@2.0.14   sqlite@3.39.4
cpio@2.13                           libffi@3.4.2          openblas@0.3.21  tar@1.34
curl@7.85.0                         libgcrypt@1.10.1      openmpi@4.1.5    texinfo@6.5
diffutils@3.8                       libgpg-error@1.46     openssh@9.1p1    ucx@1.9.0
elpa@2021.11.001                    libiconv@1.16         openssl@1.1.1s   util-linux-uuid@2.38.1
expat@2.4.8                         libmd@1.0.4           pcre2@10.39      util-macros@1.19.3
gawk@5.1.1                          libpciaccess@0.16     perl@5.16.3      xz@5.2.7
gdbm@1.23                           libsigsegv@2.13       pigz@2.7         zlib@1.2.13
gettext@0.21.1                      libtool@2.4.7         pkgconf@1.8.0    zstd@1.5.2
glib@2.74.1                         libxml2@2.10.1        pmix@3.2.2
==> 86 loaded packages

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.gfortran --version
GNU Fortran (Spack GCC) 10.2.0
Copyright (C) 2020 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.mpif90  --version
GNU Fortran (Spack GCC) 10.2.0
Copyright (C) 2020 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


Check MKL library
~~~~~~~~~~~~~~~~~
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.emkl
Intel MKL library ? MKLROOT=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/intel-mkl-2020.4.304-r45z63ewc7vmz55z5lvij6digu73dcvn/compilers_and_libraries_2020.4.304/linux/mkl


Compiling
---------
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.gunzip *
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.expand_lapw
.
.
python found at /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/python-3.10.8-w3seq5fimmis3tivdxlalwqegg5s6api/bin/python.

WIEN is now expanded. The shell-script commands were copied and links created.
To configure your Fortran-executables run:

./siteconfig_lapw

Configuration
--------------
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.siteconfig_lapw

gfortran
gcc

