=======
GROMACS
=======

cloning
-------
miroi@MIRO:~/work/software/gromacs/.git clone git@gitlab.com:gromacs/gromacs.git gromacs_cloned

nvidia-toolkit
--------------
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/buildup_on_servers/wsl2_pc/Win11_VictusNB/gpu_build/.wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update
sudo apt install cuda -y

sudo dpkg --configure -a
sudo apt-get upgrade
sudo apt-get autoremove

dpkg -s nvidia-cuda-toolkit | grep Version
Version: 12.0.140~12.0.1-4build4

windows are falling... try install newest cuda again ... 

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/buildup_on_servers/wsl2_pc/Win11_VictusNB/gpu_build/.sudo apt install cuda -y
cuda is already the newest version (13.1.0-1).

sudo apt-get remove nvidia-cuda-toolkit
Removing nvidia-cuda-toolkit (12.0.140~12.0.1-4build4) ...
sudo apt autoremove

installation
------------
miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gpu/.cmake -DGMX_MPI=on  -DGMX_GPU=CUDA ..  > build_gpu.log

CMake Error at /usr/share/cmake-4.2/Modules/FindPackageHandleStandardArgs.cmake:290 (message):
  Could NOT find CUDAToolkit: Found unsuitable version "12.0.140", but
  required is at least "12.1" (found /usr/include)

after fix:  -- Found CUDAToolkit: /usr/local/cuda/include (found suitable version "13.1.80", minimum required is "12.1")

make -j4
.
.
[ 39%] Building CUDA object src/gromacs/CMakeFiles/libgromacs.dir/nbnxm/cuda/nbnxm_cuda.cu.o
[ 39%] Building CUDA object src/gromacs/CMakeFiles/libgromacs.dir/nbnxm/cuda/nbnxm_cuda_data_mgmt.cu.o
[ 39%] Building CUDA object src/gromacs/CMakeFiles/libgromacs.dir/nbnxm/cuda/nbnxm_cuda_kernel_F_noprune.cu.o
[ 39%] Building CUDA object src/gromacs/CMakeFiles/libgromacs.dir/nbnxm/cuda/nbnxm_cuda_kernel_F_prune.cu.o
[ 39%] Building CUDA object src/gromacs/CMakeFiles/libgromacs.dir/nbnxm/cuda/nbnxm_cuda_kernel_VF_noprune.cu.o
[ 39%] Building CUDA object src/gromacs/CMakeFiles/libgromacs.dir/nbnxm/cuda/nbnxm_cuda_kernel_VF_prune.cu.o
[ 39%] Building CUDA object src/gromacs/CMakeFiles/libgromacs.dir/nbnxm/cuda/nbnxm_cuda_kernel_pruneonly.cu.o
ptxas error   : Value of threads per SM for entry _ZN3gmx23nbnxn_kernel_prune_cudaILb1EEEvNS_13NBAtomDataGpuENS_10NBParamGpuENS_11GpuPairlistEi is out of range. .minnctapersm will be ignored
ptxas error   : Value of threads per SM for entry _ZN3gmx23nbnxn_kernel_prune_cudaILb0EEEvNS_13NBAtomDataGpuENS_10NBParamGpuENS_11GpuPairlistEi is out of range. .minnctapersm will be ignored
ptxas fatal   : Ptx assembly aborted due to errors
make[2]: *** [src/gromacs/CMakeFiles/libgromacs.dir/build.make:3733: src/gromacs/CMakeFiles/libgromacs.dir/nbnxm/cuda/nbnxm_cuda_kernel_pruneonly.cu.o] Error 255
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:5762: src/gromacs/CMakeFiles/libgromacs.dir/all] Error 2
make: *** [Makefile:166: all] Error 2

FIX: cmake -DGMX_MPI=on  -DGMX_GPU=CUDA -DCMAKE_CUDA_ARCHITECTURES=native ..

miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gpu/.cmake -DGMX_MPI=on  -DGMX_GPU=CUDA -DCMAKE_CUDA_ARCHITECTURES=native .. > cmake_config_gpu.log

CMake Error at cmake/gmxManageNNPot.cmake:57 (message):
  Unknown CUDA architecture: native
Call Stack (most recent call first):
  CMakeLists.txt:843 (include)


try
miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gpu/.cmake -DGMX_MPI=on  -DGMX_GPU=CUDA -DCMAKE_CUDA_ARCHITECTURES=all .. > cmake_config_gpu.log
miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gpu/.make -j4
.
.

miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gnu/.ldd bin/gmx




