==================
Wienk2k on Govorun
==================

Loading modules
---------------
module load openmpi intel fftw/v3.3.10_gcc1120

milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_openmpi_mkl/.module list
Currently Loaded Modulefiles:
  1) BASE/1.0                 3) openmpi/v4.1.1_gcc1120   5) fftw/v3.3.10_gcc1120
  2) gcc/v11.2.0              4) intel/v2021.1


milias@hydra.jinr.ru:~/work/software/wien2k/.which mpif90
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1/bin/mpif90
milias@hydra.jinr.ru:~/work/software/wien2k/.mpif90 --version
GNU Fortran (GCC) 11.2.0

milias@hydra.jinr.ru:~/work/software/wien2k/.emkl
Intel MKL library ? MKLROOT=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest

Wien2k unpacking
----------------
# in own directory:  tar xvf WIEN2k_23.2.tar
milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_openmpi_mkl/.
milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_openmpi_mkl/.gunzip *
milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_openmpi_mkl/.check_minimal_software_requirements.sh
milias@hydra.jinr.ru:~/work/software/wien2k/wien2k_23.2_openmpi_mkl/../expand_lapw
.
.
python found at /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/intelpython/latest/bin/python.

WIEN is now expanded. The shell-script commands were copied and links created.
To configure your Fortran-executables run:

./siteconfig_lapw



Own compilation
----------------

mpif90
mpicc
MKL

FFTW3
~~~~~
Enter the root directory of your FFTW installation!: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/fftw/v3.3.10_gcc1120
With this FFTW-ROOT choice:

  * usage of threaded FFTW IS NOT possible (NO lib_omp is present).
  * MPI parallel calculations ARE NOT possible (NO lib_mpi is present).

