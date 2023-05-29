=========================
Wien2k on @lxir127.gsi.de
=========================

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.tar xvf WIEN2k_21.1.tar 
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/gunzip *
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.expand_lapw 
.
.
case.win   linked to   template.win
python found at /usr/bin/python.

WIEN is now expanded. The shell-script commands were copied and links created.
To configure your Fortran-executables run:

./siteconfig_lapw

Packages
--------
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.spack load intel-mkl@2020.4.304
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.spack load intel-parallel-studio@professional.2020.1

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.export PATH=/u/milias/bin/openmpi/bin:$PATH
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.export LD_LIBRARY_PATH=/u/milias/bin/openmpi/lib:$LD_LIBRARY_PATH


milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.spack find --loaded
==> 6 loaded packages
-- linux-debian10-broadwell / gcc@8.3.0 -------------------------
cmake@3.21.4  ncurses@6.1  openssl@1.1.1l  zlib@1.2.11

-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
intel-mkl@2020.4.304  intel-parallel-studio@professional.2020.1

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.which mpif90
/u/milias/bin/openmpi/bin/mpif90
milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.which mpirun
/u/milias/bin/openmpi/bin/mpirun

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.mpif90 --version
ifort (IFORT) 19.1.1.217 20200306
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl/.mpirun --version
mpirun (Open MPI) 3.1.0

Report bugs to http://www.open-mpi.org/community/help/

Wien2k configuration
--------------------
LI
mpif90
mpicc
MKL_TARGET_ARCH was set to intel64
could not find fftw3

