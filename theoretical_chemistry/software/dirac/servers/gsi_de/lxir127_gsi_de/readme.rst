DIRAC on @lxir127.gsi.de
========================

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.

OpenMPI-64bit
--------------
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack find  openmpi target=broadwell
==> 1 installed package
-- linux-debian10-broadwell / gcc@8.3.0 -------------------------
openmpi@3.1.6

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack find  openblas target=broadwell
==> 1 installed package
-- linux-debian10-broadwell / gcc@8.3.0 -------------------------
openblas@0.3.18

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack load openmpi@3.1.6 target=$(spack arch -t)

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack find --loaded
==> 38 loaded packages
-- linux-debian10-broadwell / gcc@8.3.0 -------------------------
bzip2@1.0.8   glib@2.70.0     libgcrypt@1.9.3    libxml2@2.9.12   openmpi@3.1.6   rdma-core@20            xz@5.2.5
cmake@3.21.4  hwloc@1.11.13   libgpg-error@1.42  lz4@1.9.3        openssl@1.1.1l  readline@8.1            zlib@1.2.11
curl@7.79.0   json-c@0.15     libiconv@1.16      munge@0.5.13     pcre@8.44       slurm@18-08-9-1
expat@2.4.1   libbsd@0.11.3   libmd@1.0.3        ncurses@6.1      perl@5.28.1     sqlite@3.36.0
gdbm@1.21     libevent@2.1.8  libnl@3.3.0        numactl@2.0.14   pmix@2.2.2      tar@1.34
gettext@0.21  libffi@3.3      libpciaccess@0.16  openblas@0.3.18  python@3.8.12   util-linux-uuid@2.36.2

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/../setup --mpi --int64 build_ompi_openblas_i8
.
.
openblas not for int64 !!!!

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/../setup --mpi  build_ompi_openblas
.
.
[ 43%] Performing update step for 'exatensor'
[ 43%] No patch step for 'exatensor'
[ 44%] Performing configure step for 'exatensor'
[ 44%] Performing build step for 'exatensor'
/usr/bin/ld: cannot find -lopenblas
collect2: error: ld returned 1 exit status
make[4]: *** [Makefile:469: talsh] Error 1
make[3]: *** [Makefile:114: ExaTensor] Error 2
make[2]: *** [CMakeFiles/exatensor.dir/build.make:89: exatensor/src/exatensor-stamp/exatensor-build] Error 2
make[1]: *** [CMakeFiles/Makefile2:2647: CMakeFiles/exatensor.dir/all] Error 2
make: *** [Makefile:146: all] Error 2




