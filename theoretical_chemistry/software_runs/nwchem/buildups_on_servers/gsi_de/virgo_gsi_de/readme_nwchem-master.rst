=======================
NWChem on Virgo at GSI
=======================

Virgo modules
-------------
https://hpc.gsi.de/virgo/preface.html

spack load intel-parallel-studio@professional.2020.1
spack load openmpi target=$(spack arch -t)
spack load amdscalapack target=$(spack arch -t) 

NWChem clone and variables setting
-----------------------------------
from https://nwchemgit.github.io/Compiling-NWChem.html :

milias@lxbk0600.gsi.de:/lustre/ukt/milias/work/software/nwchem/.git clone https://github.com/nwchemgit/nwchem.git nwchem-master

export NWCHEM_TOP=/lustre/ukt/milias/work/software/nwchem/nwchem-master
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

milias@lxbk0600.gsi.de:/lustre/ukt/milias/work/software/nwchem/nwchem-master/src/.make -j24
.
.
.
configure: WARNING: ScaLAPACK library not found, interfaces won't be defined
configure: WARNING: ELPA library not found, interfaces won't be defined
configure: WARNING: ELPA 2015 library not found, interfaces won't be defined
configure: WARNING: ELPA 2016 library not found, interfaces won't be defined
configure: WARNING: ELPA 2017 library not found, interfaces won't be defined


