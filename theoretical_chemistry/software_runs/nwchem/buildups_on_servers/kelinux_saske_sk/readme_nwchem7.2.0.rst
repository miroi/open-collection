=======================
NWChem on kelinux.saske.sk 
=======================

Modules
---------

NWChem clone and variables setting
-----------------------------------
from https://nwchemgit.github.io/Compiling-NWChem.html :

git clone -b release-7-2-0 https://github.com/nwchemgit/nwchem.git nwchem-7.2.0

export NWCHEM_TOP=/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0
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

make -j24
.
.



