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

installation
------------
miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gpu/.cmake -DGMX_MPI=on  -DGMX_GPU=CUDA ..

CMake Error at /usr/share/cmake-4.2/Modules/FindPackageHandleStandardArgs.cmake:290 (message):
  Could NOT find CUDAToolkit: Found unsuitable version "12.0.140", but
  required is at least "12.1" (found /usr/include)

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/buildup_on_servers/wsl2_pc/Win11_VictusNB/gpu_build/.sudo apt-get upgrade nvidia-cu
da-toolkit
.
.
nvidia-cuda-toolkit is already the newest version (12.0.140~12.0.1-4build4).

make -j4
miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gnu/.ldd bin/gmx




