=======================
DIRAC on lxir127.gsi.de
=======================

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/.module list
Currently Loaded Modulefiles:
  1) /compiler/intel/17.4           2) /ucx/intel/1.5_intel17.4       3) /openmpi/intel/4.0_intel17.4   4) /cmake/3.15.3

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/../setup --mpi --int64 --mkl=parallel --fc=mpif90 --cc=mpicc --cxx=mpicxx build_openmpi_intel_mklpar_i8

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/.which mpirun
/cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/bin/mpirun
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/.which mpif90
/cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/bin/mpif90

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/trunk_master/./cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4/bin/mpif90 --version
ifort (IFORT) 17.0.4 20170411
Copyright (C) 1985-2017 Intel Corporation.  All rights reserved.






