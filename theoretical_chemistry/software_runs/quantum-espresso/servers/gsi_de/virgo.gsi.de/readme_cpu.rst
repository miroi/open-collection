QE-devel on Virgo cluster
=========================

log onto specific VAE
~~~~~~~~~~~~~~~~~~~~~
ssh virgo-debian10.hpc 

load modules
~~~~~~~~~~~~
spack load cmake@3.21.4 target=$(spack arch -t)
spack load openmpi@3.1.6 target=$(spack arch -t)
spack load openblas@0.3.18 target=$(spack arch -t)
spack load amdfftw@3.0 target=$(spack arch -t)

milias@lxbk0600.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/q-e_develop/build_openmpi_cpu/.spack find --loaded

==> 40 loaded packages
-- linux-debian10-zen / gcc@8.3.0 -------------------------------
amdfftw@3.0   gettext@0.21    libffi@3.3         libpciaccess@0.16  openblas@0.3.18  python@3.8.12    texinfo@6.5
bzip2@1.0.8   glib@2.70.0     libgcrypt@1.9.3    libxml2@2.9.12     openmpi@3.1.6    rdma-core@20     util-linux-uuid@2.36.2
cmake@3.21.4  hwloc@1.11.13   libgpg-error@1.42  lz4@1.9.3          openssl@1.1.1l   readline@8.1     xz@5.2.5
curl@7.79.0   json-c@0.15     libiconv@1.16      munge@0.5.13       pcre@8.44        slurm@18-08-9-1  zlib@1.2.11
expat@2.4.1   libbsd@0.11.3   libmd@1.0.3        ncurses@6.1        perl@5.28.1      sqlite@3.36.0
gdbm@1.21     libevent@2.1.8  libnl@3.3.0        numactl@2.0.14     pmix@2.2.2       tar@1.34


buildup
~~~~~~~
cmake -DCMAKE_C_COMPILER=mpicc -DCMAKE_Fortran_COMPILER=mpif90  ..



