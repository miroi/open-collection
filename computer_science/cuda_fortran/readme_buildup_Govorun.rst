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


make.logfile_Govorun-dgx_SAVED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sbatch hydra_gpu-build_dgx.01:

nvfortran -O2  -o cufKernel.out cufKernel.cuf
make[1]: Leaving directory `/lustre/home/user/m/milias/work/projects/open-collection/computer_science/cuda_fortran/CUDA-Fortran-Book/chapter3/cufKernel'
make[1]: Entering directory `/lustre/home/user/m/milias/work/projects/open-collection/computer_science/cuda_fortran/CUDA-Fortran-Book/chapter3/cufKernel
'
./cufKernel.out
0: ALLOCATE: 4194304 bytes requested; not enough memory: 35(CUDA driver version is insufficient for CUDA runtime version)
make[1]: *** [run] Error 127
make[1]: Leaving directory `/lustre/home/user/m/milias/work/projects/open-collection/computer_science/cuda_fortran/CUDA-Fortran-Book/chapter3/cufKernel'

mpif90 -O2  -c ../common/mpiDeviceUtil.cuf
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/cuda/v12.1/Linux_x86_64/23.5/comm_libs/openmpi/openmpi-3.1.5/bin/.bin/mpif90: error while loading shared librarie
s: librdmacm.so.1: cannot open shared object file: No such file or directory
make[1]: *** [build] Error 127
make[1]: Leaving directory `/lustre/home/user/m/milias/work/projects/open-collection/computer_science/cuda_fortran/CUDA-Fortran-Book/chapter4/MPI/transp
oseMPI'





