=======================
Intel ONEAPI on Govorun
=======================

Downloading
------------

https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html?packages=oneapi-toolkit&oneapi-toolkit-os=linux&oneapi-lin=offline

https://www.intel.com/content/www/us/en/developer/tools/oneapi/fortran-compiler-download.html?operatingsystem=linux&distribution-linux=offline

HPC toolkit
~~~~~~~~~~~

https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit-download.html?packages=hpc-toolkit&hpc-toolkit-os=linux&hpc-toolkit-lin=offline

install as user
---------------
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/.chmod u+x intel-oneapi-hpc-toolkit-2025.3.1.55_offline.sh
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/../intel-oneapi-hpc-toolkit-2025.3.1.55_offline.sh
[#####################################################################################################################################################################]
Extract intel-oneapi-hpc-toolkit-2025.3.1.55_offline completed!
The installer is running in graphical user interface (GUI) mode. If you expected to run the installer in command line interface (CLI) or silent mode, relaunch it with the appropriate parameters: --cli or --silent.
Remove extracted files: /lustre/projects/m/milias/work/intel_compilers/intel-oneapi-hpc-toolkit-2025.3.1.55_offline...

without GUI, silent and with destination directory change:

sh ./intel-oneapi-hpc-toolkit-2025.3.1.55_offline.sh -s -a -d /path/to/custom/dir

initialize
~~~~~~~~~~
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/.source /lustre/projects/m/milias/intel/oneapi/setvars.sh
:: initializing oneAPI environment ...
   -bash: BASH_VERSION = 5.1.8(1)-release
   args: Using "$@" for setvars.sh arguments: autologout=no
:: advisor -- latest
:: ccl -- latest
:: compiler -- latest
:: dal -- latest
:: debugger -- latest
:: dev-utilities -- latest
:: dnnl -- latest
:: dpcpp-ct -- latest
:: dpl -- latest
:: ipp -- latest
:: ippcp -- latest
:: ishmem -- latest
:: mkl -- latest
:: mpi -- latest
:: tbb -- latest
:: umf -- latest
:: vtune -- latest
:: oneAPI environment initialized ::

test
----
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/.which mpirun
/lustre/projects/m/milias/intel/oneapi/mpi/2021.17/bin/mpirun
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/.mpirun -V
Intel(R) MPI Library for Linux* OS, Version 2021.17 Build 20251215 (id: 2ac2f63)
Copyright 2003-2025, Intel Corporation.

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/.which mpiifx; mpiifx -V
/lustre/projects/m/milias/intel/oneapi/mpi/2021.17/bin/mpiifx
mpiifx for the Intel(R) MPI Library 2021.17 for Linux*
Copyright Intel Corporation.
Intel(R) Fortran Compiler for applications running on Intel(R) 64, Version 2025.3.2 Build 20260112
Copyright (C) 1985-2026 Intel Corporation. All rights reserved.

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/.which mpiicx; mpiicx -V
/lustre/projects/m/milias/intel/oneapi/mpi/2021.17/bin/mpiicx
mpiicx for the Intel(R) MPI Library 2021.17 for Linux*
Copyright Intel Corporation.
Intel(R) oneAPI DPC++/C++ Compiler for applications running on Intel(R) 64, Version 2025.3.2 Build 20260112
Copyright (C) 1985-2026 Intel Corporation. All rights reserved.

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/.which mpiicpx; mpiicpx -V
/lustre/projects/m/milias/intel/oneapi/mpi/2021.17/bin/mpiicpx
mpiicpx for the Intel(R) MPI Library 2021.17 for Linux*
Copyright Intel Corporation.
Intel(R) oneAPI DPC++/C++ Compiler for applications running on Intel(R) 64, Version 2025.3.2 Build 20260112
Copyright (C) 1985-2026 Intel Corporation. All rights reserved.

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk_cloned/.emkl
Intel MKL library ? MKLROOT=/lustre/projects/m/milias/intel/oneapi/mkl/2025.3

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk_cloned/./lustre/projects/m/milias/intel/oneapi/mkl/2025.3/bin/mkl_link_tool
