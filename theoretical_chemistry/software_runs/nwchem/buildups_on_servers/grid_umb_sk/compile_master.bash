#!/bin/bash

#        NWChem on grid.umb.sk
#  /home/milias/Work/qch/software/nwchem_suite/nwchem_master


#  nohup compile_master.bash &> compile_master.log &

  echo -e "\n***   NWChem environmental variables for login.grid.umb.sk:   ***"

  export NWCHEM_TOP=/home/milias/Work/qch/software/nwchem_suite/nwchem_master
 # export NWCHEM_TOP=/home/milias/Work/qch/software/nwchem_suite/nwchem_release
  echo -e "NWCHEM_TOP=$NWCHEM_TOP"

  export NWCHEM_TARGET="LINUX64"
  echo -e "NWCHEM_TARGET=$NWCHEM_TARGET"

  # server's Intel compiler
  export FC=ifort
  echo -e "FC=$FC"


  #export CC=icc
  export MPI_F90=mpif90
  echo -e "MPI_F90=$MPI_F90"
  which mpif90
  which mpirun

 # export MPI_CC=mpicc
 # export MPI_CXX=mpicxx
 ### based on "mpif90 -show"
 # export LIBMPI="-lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi"
 # export MPI_LIB="/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib -Wl,-rpath  /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib -Wl,--enable-new-dtags -L/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib"
 # export MPI_INCLUDE="/home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/include /home/milias/bin/openmpi-4.0.1_suites/openmpi-4.0.1_Intel14_GNU6.3g++/lib -Wl,-rpath -Wl"

  echo -e "MKL library, MKLROOT=${MKLROOT}"

  #export BLASOPT="-L/usr/lib -lblas"
  #export BLASOPT="${MKLROOT}/lib/mic/libmkl_blas95_ilp64.a -L${MKLROOT}/lib/mic -lmkl_scalapack_ilp64 -lmkl_cdft_core -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_ilp64 -liomp5 -lpthread -lm -ldl"
  export BLASOPT="-mkl -i8"
  echo -e "BLASOPT=$BLASOPT"

#  export LAPACK_LIB="-L/usr/lib -llapack"
  #export LAPACK_LIB="${MKLROOT}/lib/mic/libmkl_lapack95_ilp64.a -L${MKLROOT}/lib/mic -lmkl_scalapack_ilp64 -lmkl_cdft_core -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_ilp64 -liomp5 -lpthread -lm -ldl"
  export LAPACK_LIB="-mkl -i8"
  echo -e "LAPACK_LIB=$LAPACK_LIB"

  export USE_64TO32="n" # see http://www.nwchem-sw.org/index.php/Special:AWCforum/sp/id7260
  echo -e "USE_64TO32=$USE_64TO32"

  export BLAS_SIZE=8
  echo -e "BLAS_SIZE=$BLAS_SIZE"

  export LAPACK_SIZE=8
  echo -e "LAPACK_SIZE=$LAPACK_SIZE"

  export USE_MPI=y
  echo -e "USE_MPI=$USE_MPI"

  export LARGE_FILES=1
  echo -e "LARGE_FILES=$LARGE_FILES"

  #export PYTHONVERSION=2.6
  export USE_NOFSCHECK=1
  echo -e "USE_NOFSCHECK=$USE_NOFSCHECK"

  export NWCHEM_LONG_PATHS=1
  echo -e "NWCHEM_LONG_PATHS=$NWCHEM_LONG_PATHS"

  #export PYTHONHOME=/opt/rh/devtoolset-6/root/usr/lib64/python2.6/site-packages:/opt/rh/devtoolset-6/root/usr/lib/python2.6/site-packages
  #export PYTHONHOME=/opt/rh/devtoolset-6/root/usr/lib64/python2.6/site-packages
  #export NWCHEM_MODULES="all python"

  export NWCHEM_MODULES="all" # remove python
  echo -e "NWCHEM_MODULES=$NWCHEM_MODULES"

  export NWCHEM_EXECUTABLE=$NWCHEM_TOP/bin/LINUX64/nwchem
  echo -e "NWCHEM_EXECUTABLE=$NWCHEM_EXECUTABLE"

  export NWCHEM_BASIS_LIBRARY=$NWCHEM_TOP/src/basis/libraries.bse
  echo -e "NWCHEM_BASIS_LIBRARY=$NWCHEM_BASIS_LIBRARY"

  echo -e "\nNWChem environmental variables were defined for login.grid.umb.sk - GOING TO COMPILE:"


  cd $NWCHEM_TOP/src
  echo -e "\n I am in :\c";pwd;ls -lt
  # clean out !!!
  echo -e "make clean:"; make clean
  echo -e " make nwchem_config: ";make nwchem_config 
  echo -e "\n  launching make -j4 :"; make -j4

  # build the version info
   echo -e "\n build the version info :"
   cd $NWCHEM_TOP/src/util
   make version
   make
   cd $NWCHEM_TOP/src
   make link


   echo -e "\n After the NWCHem compilation:"
   echo -e "   ls -l $NWCHEM_TOP/bin/LINUX64: "
   ls -l $NWCHEM_TOP/bin/LINUX64       
   echo -e "   ls -l $NWCHEM_TOP/lib/LINUX64:"
   ls -l $NWCHEM_TOP/lib/LINUX64   
  
  
  exit 0
