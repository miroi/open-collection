==============
GROMACS cloned
==============

https://gitlab.com/gromacs/gromacs

https://manual.gromacs.org/documentation/2025.4/install-guide/index.html#compiler :
The Intel classic compiler (icc/icpc) is no longer supported in GROMACS. Use Intel's newer clang-based compiler from oneAPI, or gcc.


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


configure & compile & test runs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://manual.gromacs.org/documentation/2025.4/index.html

sbatch hydra_slurm_compile_gromacs.01


100% tests passed, 0 tests failed out of 95

Label Time Summary:
GTest              = 210.75 sec*proc (93 tests)
IntegrationTest    = 128.12 sec*proc (32 tests)
MpiTest            =  89.50 sec*proc (20 tests)
QuickGpuTest       =  52.72 sec*proc (23 tests)
SlowGpuTest        =  68.13 sec*proc (11 tests)
SlowTest           =  32.00 sec*proc (8 tests)
UnitTest           =  50.63 sec*proc (53 tests)


