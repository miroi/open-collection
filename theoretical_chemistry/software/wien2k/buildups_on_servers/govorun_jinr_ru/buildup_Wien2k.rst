==================
Wienk2k on Govorun
==================

Loading modules
---------------
milias@hydra.jinr.ru:~/work/software/wien2k/.module load openmpi intel fftw
milias@hydra.jinr.ru:~/work/software/wien2k/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1               4) gcc/v11.2.0              7) fftw/v3.3.7-5
  2) BASE/1.0                 5) openmpi/v4.1.1_gcc1120
  3) Python/v3.10.2           6) intel/v2021.1

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





