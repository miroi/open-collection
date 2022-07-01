============
CP2k on ADF2
============

having Tesla M2070

milias@adf2:~/work/software/cp2k/cp2k-8.2.0/.ls
INSTALL.md  LICENSE  Makefile  README.md  REVISION  arch/  benchmarks/  data/  exts/  src/  tests/  tools/

milias@adf2:~/work/software/cp2k/cp2k-8.2.0/tools/toolchain/.module load mpi/openmpi3-x86_64

milias@adf2:~/work/software/cp2k/cp2k-8.2.0/tools/toolchain/../install_cp2k_toolchain.sh --install-all
MPI is detected and it appears to be OpenMPI
nvcc found, enabling CUDA by default
You have chosen to install GCC, therefore MPI libraries will have to be installed too
ERROR: (./install_cp2k_toolchain.sh) CUDA enabled, please choose GPU architecture to compile for with --gpu-ver

<<<<<<< HEAD:theoretical_chemistry/software_runs/cp2k/servers/adf2_at_UMB_sk/readme_adf2.rst
milias@adf2:~/work/software/cp2k/cp2k-8.2.0/tools/toolchain/../install_cp2k_toolchain.sh --install-all  --enable-cuda --gpu-ver=M2070
MPI is detected and it appears to be OpenMPI
nvcc found, enabling CUDA by default
ERROR: (./install_cp2k_toolchain.sh, line 453) --gpu-ver currently only supports K20X, K40, K80, P100, V100 and no as options
milias@adf2:~/work/software/cp2k/cp2k-8.2.0/tools/toolchain/.


  yum install patch (https://forums.centos.org/viewtopic.php?t=35112)
  Selection of GPU: see also https://en.wikipedia.org/wiki/Nvidia_Tesla  ... try K20X ??...

milias@adf2:~/work/software/cp2k/cp2k-8.2.0/tools/toolchain/../install_cp2k_toolchain.sh --install-all  --enable-cuda --gpu-ver=K20X
MPI is detected and it appears to be OpenMPI
nvcc found, enabling CUDA by default
You have chosen to install GCC, therefore MPI libraries will have to be installed too
Compiling with 12 processes.
==================== Installing GCC ====================
gcc-10.2.0.tar.gz is found
Installing GCC from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/gcc-10.2.0
patching file libcpp/init.c
Hunk #1 succeeded at 401 (offset 1 line).
patching file libcpp/traditional.c
Hunk #1 succeeded at 326 (offset -4 lines).
Step gcc took 600.00 seconds.
==================== Getting proc arch info using OpenBLAS tools ====================
OpenBLAS-0.3.10.tar.gz: OK
Checksum of OpenBLAS-0.3.10.tar.gz Ok
OpenBLAS detected LIBCORE = nehalem
OpenBLAS detected ARCH    = x86_64
==================== Installing CMake ====================
cmake-3.18.5.tar.gz: OK
Checksum of cmake-3.18.5.tar.gz Ok
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/cmake-3.18.5
Step cmake took 345.00 seconds.
==================== Installing MPICH ====================
mpich-3.3.2.tar.gz: OK
Checksum of mpich-3.3.2.tar.gz Ok
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/mpich-3.3.2
Step mpich took 436.00 seconds.
==================== Installing OpenBLAS ====================
OpenBLAS-0.3.10.tar.gz is found
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/openblas-0.3.10
Step openblas took 154.00 seconds.
==================== Installing FFTW ====================
fftw-3.3.8.tar.gz: OK
Checksum of fftw-3.3.8.tar.gz Ok
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/fftw-3.3.8
Step fftw took 59.00 seconds.
==================== Installing LIBINT ====================
libint-v2.6.0-cp2k-lmax-5.tgz: OK
Checksum of libint-v2.6.0-cp2k-lmax-5.tgz Ok
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/libint-v2.6.0-cp2k-lmax-5
Step libint took 1035.00 seconds.
==================== Installing LIBXC ====================
libxc-5.1.4.tar.gz: OK
Checksum of libxc-5.1.4.tar.gz Ok
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/libxc-5.1.4
Step libxc took 133.00 seconds.
==================== Installing libsmm ====================
Searching for an optimised libsmm binary from CP2K website
An optimized libsmm libsmm_dnn_nehalem-2015-07-02.a is available
libsmm_dnn_nehalem-2015-07-02.a: OK
Checksum of libsmm_dnn_nehalem-2015-07-02.a Ok
Step libsmm took 1.00 seconds.
==================== Installing Libxsmm ====================
libxsmm-1.16.1.tar.gz: OK
Checksum of libxsmm-1.16.1.tar.gz Ok
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/libxsmm-1.16.1
Step libxsmm took 29.00 seconds.
==================== Installing ScaLAPACK ====================
scalapack-2.1.0.tgz: OK
Checksum of scalapack-2.1.0.tgz Ok
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/scalapack-2.1.0
Step scalapack took 64.00 seconds.
==================== Installing COSMA ====================
COSMA-v2.5.0.tar.gz: OK
Checksum of COSMA-v2.5.0.tar.gz Ok
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/COSMA-2.5.0
Step cosma took 56.00 seconds.
==================== Installing ELPA ====================
elpa-2020.11.001.tar.gz: OK
Checksum of elpa-2020.11.001.tar.gz Ok
patching file nvcc_wrap
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/elpa-2020.11.001/cpu
Installing from scratch into /home/milias/work/software/cp2k/cp2k-8.2.0/tools/toolchain/install/elpa-2020.11.001/gpu
ERROR: (./scripts/stage5/install_elpa.sh, line 110) Non-zero exit code detected.


=======
see https://groups.google.com/g/cp2k/c/cAsZSOp68hQ/m/AufLyIE5AwAJ
>>>>>>> 8655c1b1a98bebb0dfd8e0cf11963658c6fed89b:theoretical_chemistry/software_runs/cp2k/servers/umb_sk/adf2_at_UMB_sk/readme_adf2.rst
