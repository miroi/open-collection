==============
GROMACS cloned
==============

https://gitlab.com/gromacs/gromacs

clone
~~~~~

milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/gromacs/git_cloned/.git clone git@gitlab.com:gromacs/gromacs.git

modules
~~~~~~~
module add  intel/oneapi  CMake/v3.29.2  Python/v3.10.13

mpiicpc --version
icpc (ICC) 2021.4.0 20210910

mpiicc --version
icc (ICC) 2021.4.0 20210910
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.

mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2021.4 Build 20210831 (id: 758087adf)


configure
~~~~~~~~~
https://manual.gromacs.org/documentation/2025.4/index.html

sbatch hydra_slurm_compile_gromacs.01




