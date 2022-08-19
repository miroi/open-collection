milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/production_trunk/.spack load intel-parallel-studio@professional.2020.1 target=x86_64
milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/production_trunk/.spack load intel-mkl@2020.4.304 target=x86_64
milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/production_trunk/.spack load cmake@3.21.4 target=x86_64
milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/production_trunk/.spack load hdf5@1.10.7 target=x86_64
milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/production_trunk/.spack unload openmpi
milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/production_trunk/.spack find --loaded
==> 40 loaded packages
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
bzip2@1.0.8                                libffi@3.3         perl@5.28.1
cmake@3.21.4                               libgcrypt@1.9.3    pkgconf@1.8.0
curl@7.79.0                                libgpg-error@1.42  pmix@2.2.2
expat@2.4.1                                libiconv@1.16      python@3.8.12
gdbm@1.21                                  libmd@1.0.3        rdma-core@20
gettext@0.21                               libnl@3.3.0        readline@8.1
glib@2.70.0                                libpciaccess@0.16  slurm@18-08-9-1
hdf5@1.10.7                                libxml2@2.9.12     sqlite@3.36.0
hwloc@1.11.13                              lz4@1.9.3          tar@1.34
intel-mkl@2020.4.304                       munge@0.5.13       util-linux-uuid@2.36.2
intel-parallel-studio@professional.2020.1  ncurses@6.1        xz@5.2.5
json-c@0.15                                numactl@2.0.14     zlib@1.2.11
libbsd@0.11.3                              openssl@1.1.1l
libevent@2.1.8                             pcre@8.44
milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/production_trunk/.which mpif90
/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/bin/mpif90

milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/production_trunk/../setup --mpi --mkl=parallel --int64  --fc=mpif90 --cc=mpicc --cxx=mpicxx build_openmpi4.1.4_intel20mkl_i8 



