===================
CFOUR program suite
===================

http://cfour.de/
http://slater.chemie.uni-mainz.de/cfour/index.php?n=Main.GitLab

Download
--------
see https://cfour.chem.ufl.edu/cfour-public/cfour-public

git clone git@cfour.chem.ufl.edu:cfour-public/cfour-public.git

Software installation
---------------------

see examples http://slater.chemie.uni-mainz.de/cfour/index.php?n=Main.Examples

@login.grid.umb.sk, HPCC at Matej Bel University, Slovakia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
milias@login.grid.umb.sk:~/Work/qch/software/cfour/.git clone git@cfour.chem.ufl.edu:cfour-public/cfour-public.git cfour-public_openmpi_intel_g++_mkl_i8

milias@login.grid.umb.sk:~/Work/qch/software/cfour/cfour-public_openmpi_intel_g++_mkl_i8/. CC=icc CXX=g++ FC=ifort F77=ifort MPIFC=mpif90 MPICC=mpicc MPICXX=mpicxx ./configure --prefix=$PWD  --with-blas="${MKLROOT}/lib/mic/libmkl_blas95_ilp64.a -L${MKLROOT}/lib/mic -lmkl_scalapack_ilp64 -lmkl_cdft_core -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_ilp64 -liomp5 -lpthread -lm -ldl" --enable-mpi=openmpi  --with-mpirun="mpirun -np \$CFOUR_NUM_CORES"  --with-exenodes="mpirun -np \$CFOUR_NUM_CORES"

make -j4

@lxir127.gsi.de at GSI.de
~~~~~~~~~~~~~~~~~~~~~~~~~
module load openmpi/intel/4.0_mp1compat_intel17.4

milias@lxir127.gsi.de:~/.echo $MKLROOT
/cvmfs/it.gsi.de/compiler/intel/17.0/compilers_and_libraries_2017.4.196/linux/mkl


based on https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor : Intel MKL 2017.0
 ::
${MKLROOT}/lib/mic/libmkl_blas95_ilp64.a -L${MKLROOT}/lib/mic -lmkl_scalapack_ilp64 -lmkl_cdft_core -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_ilp64 -liomp5 -lpthread -lm -ldl

Compiler options:  -i8 -I${MKLROOT}/include/mic/ilp64 -I${MKLROOT}/include -mmic

configure command:
 ::
 milias@lxir127.gsi.de:/tmp/milias-work/software/qch/cfour/cfour-public_openmpi4_intel17_mkl_i8/.CC=icc CXX=g++ FC=ifort F77=ifort MPIFC=mpif90 MPICC=mpicc MPICXX=mpicxx ./configure --prefix=$PWD  --with-blas="${MKLROOT}/lib/mic/libmkl_blas95_ilp64.a -L${MKLROOT}/lib/mic -lmkl_scalapack_ilp64 -lmkl_cdft_core -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_ilp64 -liomp5 -lpthread -lm -ldl" --enable-mpi=openmpi  --with-mpirun="mpirun -np \$CFOUR_NUM_CORES"  --with-exenodes="mpirun -np \$CFOUR_NUM_CORES"

