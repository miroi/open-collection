======================
DIRAC on Virgo cluster
======================

Packages
~~~~~~~~
spack find | grep intel

spack load intel-parallel-studio@professional.2020.1 target=x86_64
spack find --loaded

milias@lxbk0598.gsi.de:/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/.icc -V
Intel(R) C Intel(R) 64 Compiler for applications running on Intel(R) 64, Version 19.1.1.217 Build 20200306

milias@lxbk0598.gsi.de:/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/.ifort -V 
Intel(R) Fortran Intel(R) 64 Compiler for applications running on Intel(R) 64, Version 19.1.1.217 Build 20200306


OpenMPI
~~~~~~~
/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/.

/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/../configure --prefix=/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4   F77=ifort FC=ifort FFLAGS=-i8 FCFLAGS=-i8 CXX=icpc CC=icc CFLAGS=-m64 CXXFLAGS=-m64 --enable-mpi-fortran=usempi  --enable-mpi1-compatibility 
.
.
.
Open MPI configuration:
 -----------------------
Version: 4.1.4
Build MPI C bindings: yes
Build MPI C++ bindings (deprecated): no
Build MPI Fortran bindings: mpif.h, use mpi
MPI Build Java bindings (experimental): no
Build Open SHMEM support: false (no spml)
Debug build: no
Platform file: (none)

Miscellaneous
 -----------------------
CUDA support: no
HWLOC support: internal
Libevent support: internal
Open UCC: no
PMIx support: Internal
 
Transports
 -----------------------
Cisco usNIC: no
Cray uGNI (Gemini/Aries): no
Intel Omnipath (PSM2): no
Intel TrueScale (PSM): no
Mellanox MXM: no
Open UCX: no
OpenFabrics OFI Libfabric: no
OpenFabrics Verbs: yes
Portals4: no
Shared memory/copy in+copy out: yes
Shared memory/Linux CMA: yes
Shared memory/Linux KNEM: no
Shared memory/XPMEM: no
TCP: yes
 
Resource Managers
 -----------------------
Cray Alps: no
Grid Engine: no
LSF: no
Moab: no
Slurm: yes
ssh/rsh: yes
Torque: no
 
OMPIO File Systems
 -----------------------
DDN Infinite Memory Engine: no
Generic Unix FS: yes
IBM Spectrum Scale/GPFS: no
Lustre: no
PVFS2/OrangeFS: no
 
milias@lxbk0598.gsi.de:/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/.make -j8 all install

# ...activate only for DIRAC compilation ! otherwise put into SLURM run file for Virgo  
#  extend_string PATH             /lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/bin          $PATH
#  extend_string MANPATH          /lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/share/man    $MANPATH
#  extend_string LD_LIBRARY_PATH  /lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/lib          $LD_LIBRARY_PATH

DIRAC buildup
-------------
export PATH=/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/bin:$PATH
export MANPATH=/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/share/man:$MANPATH
export LD_LIBRARY_PATH=/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/lib:$LD_LIBRARY_PATH

spack load intel-parallel-studio@professional.2020.1 target=x86_64
spack load intel-mkl@2020.4.304 target=x86_64

milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/devel_trunk/.emkl
Intel MKL library ? MKLROOT=/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-mkl-2020.4.304-wcz55b7qqq66b7lh5vqt6qt7ftlkwa3z/compilers_and_libraries_2020.4.304/linux/mkl

milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/devel_trunk/.spack find --loaded
==> 2 loaded packages
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
intel-mkl@2020.4.304  intel-parallel-studio@professional.2020.1

milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/devel_trunk/.ompi_info -a | grep 'integer size'
       Fort integer size: 8

milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/devel_trunk/.which mpif90
/lustre/ukt/milias/bin/openmpi-4.1.4-intel2020-i8/openmpi-4.1.4/bin/mpif90

Compilation
~~~~~~~~~~~
spack load cmake@3.21.4 target=x86_64

milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/devel_trunk/.which cmake
/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/cmake-3.21.4-enblber3hx4opwmwlknv7i3vd522t3ln/bin/cmake
milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/devel_trunk/.cmake --version
cmake version 3.21.4

milias@lxbk0598.gsi.de:/lustre/ukt/milias/work/software/dirac/devel_trunk/../setup --mpi --mkl=parallel --int64 --fc=mpif90 --cc=mpicc --cxx=mpicxx build_openmpi4.1.4_intel20mkl_i8


