====================================
CUDA-Fortran-Book buildup on Govorun
====================================

The example codes included in this directory are a portion of the code samples
from the companion website to the book "CUDA Fortran for Scientists and Engineers",
both 1st and 2nd editions:

https://github.com/NVIDIA/CUDA-Fortran-2ed

make.logfile_Govorun-ampere_SAVED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sbatch hydra_gpu-build_ampere.01:

mpif90 -O2  -o mpiDevices.out mpiDevices.cuf
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/cuda/v12.1/Linux_x86_64/23.5/comm_libs/openmpi/openmpi-3.1.5/bin/.bin/mpif90: error while loading shared libraries: librdmacm.so.1: cannot open shared object file: No such file or directory

0: ALLOCATE: 80 bytes requested; status = 35(CUDA driver version is insufficient for CUDA runtime version)


make.logfile_Govorun-dgx3_PASSED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sbatch hydra_gpu-build_dgx.01:

milias@hydra.jinr.ru:~/work/projects/open-collection/computer_science/cuda_fortran/.grep libatomic.so.1  make.logfile_Govorun-dgx3_PASSED
/usr/bin/ld: warning: libatomic.so.1, needed by /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/cuda/v12.4/Linux_x86_64/24.5/comm_libs/12.4/hpcx/hpcx-2.19/ompi/lib/libmpi_usempif08.so, not found (try using -rpath or -rpath-link)
/usr/bin/ld: warning: libatomic.so.1, needed by /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/cuda/v12.4/Linux_x86_64/24.5/comm_libs/12.4/hpcx/hpcx-2.19/ompi/lib/libmpi_usempif08.so, not found (try using -rpath or -rpath-link)
/usr/bin/ld: warning: libatomic.so.1, needed by /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/cuda/v12.4/Linux_x86_64/24.5/comm_libs/12.4/hpcx/hpcx-2.19/ompi/lib/libmpi_usempif08.so, not found (try using -rpath or -rpath-link)





