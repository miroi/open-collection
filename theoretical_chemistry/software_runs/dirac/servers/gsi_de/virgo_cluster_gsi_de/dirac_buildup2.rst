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
milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/production_trunk/../setup --mpi --mkl=parallel --int64 --extra-fc-flags=-xHost --extra-cc-flags=-xHost --extra-cxx-flags=-xHost   --fc=mpif90 --cc=mpicc --cxx=mpicxx build_openmpi4.1.4_intel20mkl_i8 
cmake -DCMAKE_Fortran_COMPILER=mpif90 -DEXTRA_FCFLAGS="-xHost" -DCMAKE_C_COMPILER=mpicc -DEXTRA_CFLAGS="-xHost" -DCMAKE_CXX_COMPILER=mpicxx -DEXTRA_CXXFLAGS="-xHost" -DPREPROCESSOR_DEFINITIONS="''" -DPYTHON_INTERPRETER="''" -DENABLE_BLAS=auto -DENABLE_LAPACK=auto -DMKL_FLAG=parallel -DMATH_LIB_SEARCH_ORDER="MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE" -DBLAS_LANG=Fortran -DLAPACK_LANG=Fortran -DENABLE_MPI=True -DENABLE_OPENMP=True -DENABLE_CODE_COVERAGE=False -DENABLE_STATIC_LINKING=False -DENABLE_PROFILING=False -DENABLE_RUNTIMECHECK=False -DENABLE_64BIT_INTEGERS=True -DEXPLICIT_LIBS="off" -DENABLE_EXATENSOR=ON -DENABLE_PCMSOLVER=ON -DPCMSOLVER_ROOT='' -DCMAKE_BUILD_TYPE=release -G"Unix Makefiles" -H/lustre/ukt/milias/work/software/dirac/production_trunk -Bbuild_openmpi4.1.4_intel20mkl_i8


