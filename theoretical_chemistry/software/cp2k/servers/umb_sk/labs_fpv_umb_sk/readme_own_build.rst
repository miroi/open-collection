========================
CP2K at @labs.fpv.umb.sk
========================

milias@labs.fpv.umb.sk:~/work/software/theoretical_chemistry/cp2k/.wget https://github.com/cp2k/cp2k/archive/refs/tags/v8.2.0.tar.gz

milias@labs.fpv.umb.sk:~/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/.install_cp2k_toolchain.sh --install-all
MPI is detected and it appears to be OpenMPI
nvcc not found, disabling CUDA by default
You have chosen to install GCC, therefore MPI libraries will have to be installed too
Compiling with 12 processes.
==================== Installing GCC ====================
gcc-10.2.0.tar.gz: OK
Checksum of gcc-10.2.0.tar.gz Ok
Installing GCC from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/gcc-10.2.0
patching file libcpp/init.c
Hunk #1 succeeded at 401 (offset 1 line).
patching file libcpp/traditional.c
Hunk #1 succeeded at 326 (offset -4 lines).
Step gcc took 2210.00 seconds.
==================== Getting proc arch info using OpenBLAS tools ====================
OpenBLAS-0.3.10.tar.gz: OK
Checksum of OpenBLAS-0.3.10.tar.gz Ok
OpenBLAS detected LIBCORE = nehalem
OpenBLAS detected ARCH    = x86_64
==================== Installing CMake ====================
cmake-3.18.5.tar.gz: OK
Checksum of cmake-3.18.5.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/cmake-3.18.5
Step cmake took 2126.00 seconds.
==================== Installing MPICH ====================
mpich-3.3.2.tar.gz: OK
Checksum of mpich-3.3.2.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/mpich-3.3.2
Step mpich took 696.00 seconds.
==================== Installing OpenBLAS ====================
OpenBLAS-0.3.10.tar.gz is found
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/openblas-0.3.10
Step openblas took 509.00 seconds.
==================== Installing FFTW ====================
fftw-3.3.8.tar.gz: OK
Checksum of fftw-3.3.8.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/fftw-3.3.8
Step fftw took 144.00 seconds.
==================== Installing LIBINT ====================
libint-v2.6.0-cp2k-lmax-5.tgz: OK
Checksum of libint-v2.6.0-cp2k-lmax-5.tgz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/libint-v2.6.0-cp2k-lmax-5
Step libint took 1830.00 seconds.
==================== Installing LIBXC ====================
libxc-5.1.4.tar.gz: OK
Checksum of libxc-5.1.4.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/libxc-5.1.4
Step libxc took 224.00 seconds.
==================== Installing libsmm ====================
Searching for an optimised libsmm binary from CP2K website
An optimized libsmm libsmm_dnn_nehalem-2015-07-02.a is available
libsmm_dnn_nehalem-2015-07-02.a: OK
Checksum of libsmm_dnn_nehalem-2015-07-02.a Ok
Step libsmm took 2.00 seconds.
==================== Installing Libxsmm ====================
libxsmm-1.16.1.tar.gz: OK
Checksum of libxsmm-1.16.1.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/libxsmm-1.16.1
Step libxsmm took 76.00 seconds.
==================== Installing ScaLAPACK ====================
scalapack-2.1.0.tgz: OK
Checksum of scalapack-2.1.0.tgz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/scalapack-2.1.0
Step scalapack took 152.00 seconds.
==================== Installing COSMA ====================
COSMA-v2.5.0.tar.gz: OK
Checksum of COSMA-v2.5.0.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/COSMA-2.5.0
Step cosma took 77.00 seconds.
==================== Installing ELPA ====================
elpa-2020.11.001.tar.gz: OK
Checksum of elpa-2020.11.001.tar.gz Ok
patching file nvcc_wrap
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/elpa-2020.11.001/cpu
Step elpa took 249.00 seconds.
==================== Installing PT-Scotch ====================
scotch_6.0.0.tar.gz: OK
Checksum of scotch_6.0.0.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/scotch-6.0.0
Step ptscotch took 40.00 seconds.
==================== Installing SuperLU_DIST ====================
superlu_dist_6.1.0.tar.gz: OK
Checksum of superlu_dist_6.1.0.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/superlu_dist-6.1.0
Step superlu took 37.00 seconds.
==================== Installing PEXSI ====================
pexsi_v1.2.0.tar.gz: OK
Checksum of pexsi_v1.2.0.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/pexsi-1.2.0
Step pexsi took 114.00 seconds.
==================== Installing QUIP ====================
QUIP-b4336484fb65b0e73211a8f920ae4361c7c353fd.tar.gz: OK
Checksum of QUIP-b4336484fb65b0e73211a8f920ae4361c7c353fd.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/quip-b4336484fb65b0e73211a8f920ae4361c7c353fd
Step quip took 445.00 seconds.
==================== Installing gsl ====================
gsl-2.6.tar.gz: OK
Checksum of gsl-2.6.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/gsl-2.6
Step gsl took 173.00 seconds.
==================== Installing PLUMED ====================
plumed-2.6.2.tgz: OK
Checksum of plumed-2.6.2.tgz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/plumed-2.6.2
Step plumed took 236.00 seconds.
==================== Installing hdf5 ====================
hdf5-1.12.0.tar.bz2: OK
Checksum of hdf5-1.12.0.tar.bz2 Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/hdf5-1.12.0
Step hdf5 took 310.00 seconds.
==================== Installing libvdwxc ====================
libvdwxc-0.4.0.tar.gz: OK
Checksum of libvdwxc-0.4.0.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/libvdwxc-0.4.0
Step libvdwxc took 22.00 seconds.
==================== Installing spglib ====================
spglib-1.16.0.tar.gz: OK
Checksum of spglib-1.16.0.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/spglib-1.16.0
Step spglib took 10.00 seconds.
==================== Installing libvori ====================
libvori-210412.tar.gz: OK
Checksum of libvori-210412.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/libvori-210412
Step libvori took 42.00 seconds.
==================== Installing spfft ====================
SpFFT-0.9.13.tar.gz: OK
Checksum of SpFFT-0.9.13.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/SpFFT-0.9.13
Step spfft took 11.00 seconds.
==================== Installing spla ====================
SpLA-1.2.1.tar.gz: OK
Checksum of SpLA-1.2.1.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/SpLA-1.2.1
Step spla took 18.00 seconds.
==================== Installing SIRIUS ====================
SIRIUS-7.0.2.tar.gz: OK
Checksum of SIRIUS-7.0.2.tar.gz Ok
Installing from scratch into /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/sirius-7.0.2
Step sirius took 1233.00 seconds.
==================== generating arch files ====================
arch files can be found in the /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/arch subdirectory
Wrote /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/arch/local.ssmp
Wrote /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/arch/local.sdbg
Wrote /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/arch/local.psmp
Wrote /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/arch/local.pdbg
Wrote /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/arch/local_warn.psmp
Wrote /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/arch/local_coverage.pdbg
========================== usage =========================
Done!
Now copy:
  cp /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/arch/* to the cp2k/arch/ directory
To use the installed tools and libraries and cp2k version
compiled with it you will first need to execute at the prompt:
  source /home/milias/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/install/setup
To build CP2K you should change directory:
  cd cp2k/
  make -j 12 ARCH=local VERSION="ssmp sdbg psmp pdbg"

arch files for GPU enabled CUDA versions are named "local_cuda.*"
arch files for coverage versions are named "local_coverage.*"

Note that these pre-built arch files are for the GNU compiler, users have to adapt them for other compilers.
It is possible to use the provided CP2K arch files as guidance.

milias@labs.fpv.umb.sk:~/work/software/theoretical_chemistry/cp2k/cp2k-8.2.0/tools/toolchain/.

