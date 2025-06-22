======================
DFTD4 on hydra.jinr.ru
======================

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/.git clone git@github.com:dftd4/dftd4.git
Cloning into 'dftd4'...
.
.
.
milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.gsu
Submodule 'assets/aur/dftd4' (https://aur.archlinux.org/dftd4.git) registered for path 'assets/aur/dftd4'
Submodule 'assets/aur/dftd4-git' (https://aur.archlinux.org/dftd4-git.git) registered for path 'assets/aur/dftd4-git'
Cloning into '/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/assets/aur/dftd4'...
Cloning into '/lustre/home/user/m/milias/work/software/dft_dispersion_corrections/dft-d4/dftd4/assets/aur/dftd4-git'...
Submodule path 'assets/aur/dftd4': checked out 'a8947fb60f1b6d192046cb91c7c0524fd4470885'
Submodule path 'assets/aur/dftd4-git': checked out '7e92bd04dea45dcba5d127938d55e85f73c6e753'


interactive buildup with Intel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module add CMake/v3.29.2  intel/oneapi

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.ifort --version
ifort (IFORT) 2021.4.0 20210910

milias@hydra.jinr.ru:~/work/software/dft_dispersion_corrections/dft-d4/dftd4/.FC=ifort CC=icc cmake -B $BUILD  -Dmctc-lib_DIR=$MCTCDIR

compilation
~~~~~~~~~~~
