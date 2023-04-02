==============================
  NWChem on kelinux.saske.sk 
==============================

Modules
-------
ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/src/.module load imkl/2021.2.0-iimpi-2021a
ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/src/.module load ELPA/2021.11.001-foss-2022a 
ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/src/.module load ScaLAPACK

ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/src/.emkl
Intel MKL library ? MKLROOT=/lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0

ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/src/.module list

Currently Loaded Modules:
  1) prun/1.3                                12) libxml2/2.9.13-GCCcore-11.3.0     23) UCC/1.0.0-GCCcore-11.3.0
  2) gnu7/7.3.0                              13) libpciaccess/0.16-GCCcore-11.3.0  24) OpenMPI/4.1.4-GCC-11.3.0
  3) openmpi3/3.1.0                          14) hwloc/2.7.1-GCCcore-11.3.0        25) OpenBLAS/0.3.20-GCC-11.3.0
  4) ohpc                                    15) OpenSSL/1.1                       26) FlexiBLAS/3.2.0-GCC-11.3.0
  5) intel-compilers/2021.2.0                16) libevent/2.1.12-GCCcore-11.3.0    27) FFTW/3.3.10-GCC-11.3.0
  6) impi/2021.2.0-intel-compilers-2021.2.0  17) GCCcore/11.3.0                    28) gompi/2022a
  7) iimpi/2021a                             18) zlib/1.2.12-GCCcore-11.3.0        29) FFTW.MPI/3.3.10-gompi-2022a
  8) imkl/2021.2.0-iimpi-2021a               19) numactl/2.0.14-GCCcore-11.3.0     30) foss/2022a
  9) binutils/2.38-GCCcore-11.3.0            20) UCX/1.12.1-GCCcore-11.3.0         31) ELPA/2021.11.001-foss-2022a
 10) GCC/11.3.0                              21) libfabric/1.15.1-GCCcore-11.3.0   32) ScaLAPACK/2.2.0-gompi-2022a-fb
 11) XZ/5.2.5-GCCcore-11.3.0                 22) PMIx/4.1.2-GCCcore-11.3.0


NWChem clone and variables setting
-----------------------------------
from https://nwchemgit.github.io/Compiling-NWChem.html :

git clone -b release-7-2-0 https://github.com/nwchemgit/nwchem.git nwchem-7.2.0

export NWCHEM_TOP=/lustre/home/ilias/work/qch/software/nwchem/nwchem-7.2.0
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

make -j8
.
.

configure: WARNING: ScaLAPACK library not found, interfaces won't be defined
configure: WARNING: ELPA library not found, interfaces won't be defined
configure: WARNING: ELPA 2015 library not found, interfaces won't be defined
configure: WARNING: ELPA 2016 library not found, interfaces won't be defined
configure: WARNING: ELPA 2017 library not found, interfaces won't be defined


