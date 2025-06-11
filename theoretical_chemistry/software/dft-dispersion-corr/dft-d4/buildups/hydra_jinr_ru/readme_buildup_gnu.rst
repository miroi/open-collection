=======================================
DFTD4 on vm02.hydra.local/hydra.jinr.ru
=======================================


git clone  git@github.com:dftd4/dftd4.git
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.mkdir build_gnu

module add gcc/v12.3.0 CMake/v3.29.2 LAPACK/v3.12.0_gcc1230

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1               3) gcc/v12.3.0              5) LAPACK/v3.12.0_gcc1230
  2) BASE/1.0                 4) CMake/v3.29.2

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.which gfortran
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gfortran
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.which gcc
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gcc
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.FC=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gfortran CC=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/gcc/v12.3.0/bin/gcc   cmake -B build_gnu


