=====================
NWChem on grid.umb.sk
=====================

/home/milias/Work/qch/software/nwchem_suite/nwchem_master
---------------------------------------------------------


  export NWCHEM_TOP=/home/milias/Work/qch/software/nwchem_suite/nwchem_master
 # export NWCHEM_TOP=/home/milias/Work/qch/software/nwchem_suite/nwchem_release
  export NWCHEM_TARGET=LINUX64
  export FC=ifort
  #export CC=icc
  export MPI_F90=mpif90
 # export MPI_CC=mpicc
 # export MPI_CXX=mpicxx
 ### based on "mpif90 -show"
 # export LIBMPI="-lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi"
 # export MPI_LIB="/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib -Wl,-rpath  /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib -Wl,--enable-new-dtags -L/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib"
 # export MPI_INCLUDE="/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/include /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib -Wl,-rpath -Wl"

  #export BLASOPT="-L/usr/lib -lblas"
  export BLASOPT="${MKLROOT}/lib/mic/libmkl_blas95_ilp64.a -L${MKLROOT}/lib/mic -lmkl_scalapack_ilp64 -lmkl_cdft_core -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_ilp64 -liomp5 -lpthread -lm -ldl"

  export LAPACK_LIB="-L/usr/lib -llapack"
  #export LAPACK_LIB="${MKLROOT}/lib/mic/libmkl_lapack95_ilp64.a -L${MKLROOT}/lib/mic -lmkl_scalapack_ilp64 -lmkl_cdft_core -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_ilp64 -liomp5 -lpthread -lm -ldl"

 #export USE_64TO32=n # see http://www.nwchem-sw.org/index.php/Special:AWCforum/sp/id7260
  export BLAS_SIZE=8
  export LAPACK_SIZE=8
  export USE_MPI=y
  export LARGE_FILES=1
  #export PYTHONVERSION=2.6
  export USE_NOFSCHECK=1
  #export PYTHONHOME=/opt/rh/devtoolset-6/root/usr/lib64/python2.6/site-packages:/opt/rh/devtoolset-6/root/usr/lib/python2.6/site-packages
  #export PYTHONHOME=/opt/rh/devtoolset-6/root/usr/lib64/python2.6/site-packages
  #export NWCHEM_MODULES="all python"

  export NWCHEM_MODULES="all" # problem with Python!
  export NWCHEM_EXECUTABLE=$NWCHEM_TOP/bin/LINUX64/nwchem
  export NWCHEM_BASIS_LIBRARY=$NWCHEM_TOP/src/basis/libraries.bse
  echo -e "\nNWChem environmental variables defined for login.grid.umb.sk\n"


