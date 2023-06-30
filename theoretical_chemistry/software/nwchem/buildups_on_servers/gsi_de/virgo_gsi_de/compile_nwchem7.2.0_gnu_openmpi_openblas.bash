#!/bin/bash

#  nohup compile_nwchem7.2.0_gnu_openmpi_openblas.bash &> compile_nwchem7.2.0_gnu_openmpi_openblas.log &

#  NWChem on Virgo

# load and present spack modules
echo -e "\n openmpi%gcc target=x86_64 :"
spack load openmpi%gcc target=x86_64
ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/lib

echo -e "\n amdfftw%gcc target=x86_64"
spack load amdfftw%gcc target=x86_64
ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib

echo -e "\n elpa%gcc target=x86_64"
spack load elpa%gcc target=x86_64
ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib

echo -e "\n amdscalapack%gcc target=x86_64"
spack load amdscalapack%gcc target=x86_64
ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib

echo -e "\n openblas%gcc target=x86_64"
spack load openblas%gcc target=x86_64
ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib

echo -e "\n all spack loaded modules:"
spack find --loaded


echo -e "\n***   NWChem environmental variables for Virgo cluster at GSI.de   ***"

#   https://nwchemgit.github.io/Compiling-NWChem.html#setting-up-the-proper-environment-variables

  export NWCHEM_TOP=/lustre/ukt/milias/work/software/nwchem/nwchem-7.2.0_gnu_openmpi_openblas
  echo -e "NWCHEM_TOP=$NWCHEM_TOP"

  export NWCHEM_TARGET="LINUX64"
  echo -e "NWCHEM_TARGET=$NWCHEM_TARGET"

  export ARMCI_NETWORK=MPI-PR
  echo -e "ARMCI_NETWORK=$ARMCI_NETWORK"

  # server's Intel compiler
  export FC=gfortran
  echo -e "FC=$FC"
  export MPI_F90=mpif90
  echo -e "MPI_F90=$MPI_F90"
  which mpif90; mpif90 --version
  which mpirun; mpirun --version

  export BLASOPT="-L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib -lopenblas -lgfortran"
  echo -e "BLASOPT=$BLASOPT"
  
  export LAPACK_LIB=$BLASOPT
  echo -e "LAPACK_LIB=$LAPACK_LIB"

  export USE_64TO32="y" #
  echo -e "USE_64TO32=$USE_64TO32"

  export BLAS_SIZE=4
  echo -e "BLAS_SIZE=$BLAS_SIZE"

  export LAPACK_SIZE=4
  echo -e "LAPACK_SIZE=$LAPACK_SIZE"

# NWChem can also take advantage of the ScaLAPACK library if it is installed on your system
  export USE_SCALAPACK=y
  export SCALAPACK_SIZE=4
  export USE_64TO32="y"
  export SCALAPACK="-L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib -lscalapack -lgfortran"
  export SCALAPACK_LIB=$SCALAPACK
  echo -e "SCALAPACK_LIB=$SCALAPACK_LIB"

  export ELPA="-I/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa_openmp-2021.11.001/modules/ -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib -lelpa_openmp"
  echo -e "ELPA=$ELPA"
 
  export USE_MPI="y"
  echo -e "USE_MPI=$USE_MPI"

  export LARGE_FILES=1
  echo -e "LARGE_FILES=$LARGE_FILES"

# USE_NOFSCHECK can be set to avoid NWChem creating files for each process when testing the size of the scratch directory (a.k.a. creation of junk files)
  export USE_NOFSCHECK=TRUE
  echo -e "USE_NOFSCHECK=$USE_NOFSCHECK"

  export MRCC_METHODS=TRUE
  export CCSDTQ=TRUE

  export NWCHEM_LONG_PATHS=1
  echo -e "NWCHEM_LONG_PATHS=$NWCHEM_LONG_PATHS"

  export NWCHEM_MODULES="all" # remove python
  echo -e "NWCHEM_MODULES=$NWCHEM_MODULES"

  export NWCHEM_EXECUTABLE=$NWCHEM_TOP/bin/LINUX64/nwchem
  echo -e "NWCHEM_EXECUTABLE=$NWCHEM_EXECUTABLE"

  export NWCHEM_BASIS_LIBRARY=$NWCHEM_TOP/src/basis/libraries.bse
  echo -e "NWCHEM_BASIS_LIBRARY=$NWCHEM_BASIS_LIBRARY"

  echo -e "\nNWChem environmental variables were defined for login.grid.umb.sk - GOING TO COMPILE:"


  cd $NWCHEM_TOP/src
  echo -e "\n I am in :\c";pwd;ls -lt
 # echo -e "make clean:"; make clean
  echo -e " make V=1 nwchem_config: ";make V=1 nwchem_config 
  echo -e "make V=1 64_to_32 :";make V=1 64_to_32
  echo -e "\n  launching make -j4 :"; make -j16

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
