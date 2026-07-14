===============================
 Get the Intel® oneAPI Toolkit 
===============================

Downloading
------------
https://www.intel.com/content/www/us/en/developer/tools/oneapi/oneapi-toolkit-download.html?packages=oneapi-toolkit&oneapi-toolkit-os=linux&oneapi-lin=offline

With the 2026.0 Release, the Intel® oneAPI Base Toolkit (Base Kit) and Intel® oneAPI HPC Toolkit have been combined into the Intel® oneAPI Toolkit. 


milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/.wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/33cb2a22-ddf1-4aa9-8d68-1f5a118acaf2/intel-oneapi-toolkit-2026.1.0.192_offline.sh
--2026-07-14 20:18:11--  https://registrationcenter-download.intel.com/akdlm/IRC_NAS/33cb2a22-ddf1-4aa9-8d68-1f5a118acaf2/intel-oneapi-toolkit-2026.1.0.192_offline.sh
Resolving registrationcenter-download.intel.com (registrationcenter-download.intel.com)... 87.245.198.155, 87.245.198.145
Connecting to registrationcenter-download.intel.com (registrationcenter-download.intel.com)|87.245.198.155|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2218010281 (2.1G) [application/octet-stream]
Saving to: ‘intel-oneapi-toolkit-2026.1.0.192_offline.sh’

intel-oneapi-toolkit-2026.1.0.192_offline.sh 100%[============================================================================================>]   2.07G  26.3MB/s    in 87s

2026-07-14 20:19:40 (24.3 MB/s) - ‘intel-oneapi-toolkit-2026.1.0.192_offline.sh’ saved [2218010281/2218010281]

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/.ls -lt
total 2158861
-rwxr--r--. 1 milias hybrilit 2218010281 Jul  1 18:40 intel-oneapi-toolkit-2026.1.0.192_offline.sh*

Install
-------
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/intel_compilers/.chmod u+x intel-oneapi-toolkit-2026.1.0.192_offline.sh

change the installation directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/lustre/projects/m/milias/work/software/intel/oneapi

check installed directory
~~~~~~~~~~~~~~~~~~~~~~~~~
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/intel/oneapi/.ls
2026.1/  common/    debugger/       dnnl/  ipp/    licensing/  mkl/                   mpi/             setvars.sh   tbb/  umf/
ccl/     compiler/  dev-utilities/  dpl/   ippcp/  logs/       modulefiles-setup.sh*  oneapi-toolkit/  support.txt  tcm/  vtune/

initialize and check
--------------------
source /lustre/projects/m/milias/work/software/intel/oneapi/setvars.sh


:: initializing oneAPI environment ...
   -bash: BASH_VERSION = 5.1.8(1)-release
   args: Using "$@" for setvars.sh arguments: autologout=no
:: ccl -- latest
:: compiler -- latest
:: debugger -- latest
:: dev-utilities -- latest
:: dnnl -- latest
:: dpl -- latest
:: ipp -- latest
:: ippcp -- latest
:: mkl -- latest
:: mpi -- latest
:: tbb -- latest
:: tcm -- latest
:: umf -- latest
:: vtune -- latest
:: oneAPI environment initialized ::

test
----
which mpirun
/lustre/projects/m/milias/work/software/intel/oneapi/mpi/2021.18/bin/mpirun

mpirun -V
Intel(R) MPI Library for Linux* OS, Version 2021.18.0 Build 20260327 (id: 821f207)
Copyright 2003-2026, Intel Corporation.

which mpiifx; mpiifx -V
/lustre/projects/m/milias/work/software/intel/oneapi/mpi/2021.18/bin/mpiifx
mpiifx for the Intel(R) MPI Library 2021.18 for Linux*
Copyright Intel Corporation.
Intel(R) Fortran Compiler for applications running on Intel(R) 64, Version 2026.1.0 Build 20260617
Copyright (C) 1985-2026 Intel Corporation. All rights reserved.

which ifx; ifx -V
/lustre/projects/m/milias/work/software/intel/oneapi/compiler/2026.1/bin/ifx
Intel(R) Fortran Compiler for applications running on Intel(R) 64, Version 2026.1.0 Build 20260617
Copyright (C) 1985-2026 Intel Corporation. All rights reserved.

which icx; icx -V
/lustre/projects/m/milias/work/software/intel/oneapi/compiler/2026.1/bin/icx
Intel(R) oneAPI DPC++/C++ Compiler for applications running on Intel(R) 64, Version 2026.1.0 Build 20260617
Copyright (C) 1985-2026 Intel Corporation. All rights reserved.

which mpiicx; mpiicx -V
/lustre/projects/m/milias/work/software/intel/oneapi/mpi/2021.18/bin/mpiicx
mpiicx for the Intel(R) MPI Library 2021.18 for Linux*
Copyright Intel Corporation.
Intel(R) oneAPI DPC++/C++ Compiler for applications running on Intel(R) 64, Version 2026.1.0 Build 20260617
Copyright (C) 1985-2026 Intel Corporation. All rights reserved.

which mpiicpx; mpiicpx -V

MKL
---
emkl
Intel MKL library ? MKLROOT=/lustre/projects/m/milias/work/software/intel/oneapi/mkl/2026.1

mkl_link_tool
~~~~~~~~~~~~~
which mkl_link_tool
/lustre/projects/m/milias/work/software/intel/oneapi/mkl/2026.1/bin/mkl_link_tool

mkl_link_tool -h

