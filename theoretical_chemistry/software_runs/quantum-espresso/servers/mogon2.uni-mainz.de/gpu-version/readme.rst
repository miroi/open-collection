QE-devel with GPU
=================

Login interactively onto GPU-node
---------------------------------
mirilias@login22.mogon:~/work/software/quantum_espresso/qe-devel/.srun --pty -p m2_gpu-compile -t 1:00:00  -A m2_jgu-gpu-qe-calcs bash -i

better is longer time for compilation

mirilias@login22.mogon:~/work/software/quantum_espresso/qe-devel/.srun --pty -p m2_gpu -t 4:00:00  -A m2_jgu-gpu-qe-calcs bash -i

Loading necessary modules
-------------------------
mirilias@s0026.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.ml load devel/CMake/3.21.1 mpi/OpenMPI/4.1.1-intel-compilers-2021.4.0 system/CUDA/11.4.2 compiler/PGI/20.4-GCC-8.3.0  compiler/NVHPC/21.7   numlib/imkl/2022.0.2

mirilias@s0026.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu_openmpi/.ml

Currently Loaded Modules:
  1) devel/CMake/3.21.1
  2) compiler/intel-compilers/2021.4.0
  3) system/hwloc/2.5.0-GCCcore-11.2.0
  4) lib/libfabric/1.13.2-GCCcore-11.2.0
  5) system/OpenSSL/1.1
  6) lib/libevent/2.1.12-GCCcore-11.2.0
  7) lib/PMIx/4.1.0-GCCcore-11.2.0
  8) mpi/OpenMPI/4.1.1-intel-compilers-2021.4.0
  9) system/CUDA/11.4.2
 10) compiler/GCCcore/8.3.0
 11) compiler/PGI/20.4-GCC-8.3.0
 12) system/CUDAcore/11.2.2
 13) compiler/NVHPC/21.7
 14) numlib/imkl/2022.0.2



see https://gitlab.com/QEF/q-e/-/issues/513#note_999729587

Buildup and compilation
------------------------
 mirilias@s0014.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.cmake -D QE_ENABLE_CUDA=ON -D QE_ENABLE_MPI_GPU_AWARE=ON -D CMAKE_Fortran_COMPILER=nvfortran -D CMAKE_C_COMPILER=nvc    ..
.
.
mirilias@s0021.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.ls bin/

Linked objects
---------------
mirilias@s0021.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.ldd bin/pw.x
