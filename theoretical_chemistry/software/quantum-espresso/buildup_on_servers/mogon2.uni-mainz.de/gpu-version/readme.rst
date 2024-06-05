QE-devel with GPU
=================

Login interactively onto GPU-node
---------------------------------
mirilias@login22.mogon:~/work/software/quantum_espresso/qe-devel/.srun --pty -p m2_gpu-compile -t 1:00:00  -A m2_jgu-gpu-qe-calcs bash -i

better is longer time for compilation

mirilias@login22.mogon:~/work/software/quantum_espresso/qe-devel/.srun --pty -p m2_gpu -t 4:00:00  -A m2_jgu-gpu-qe-calcs bash -i

Loading necessary modules
-------------------------
mirilias@s0026.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu_openmpi/.ml load devel/CMake/3.21.1   mpi/OpenMPI/4.0.5-gcccuda-2020b   system/CUDA/11.4.2 compiler/PGI/20.4-GCC-8.3.0  compiler/NVHPC/21.7   numlib/imkl/2022.0.2
mirilias@s0026.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu_openmpi/.ml

Currently Loaded Modules:
  1) devel/CMake/3.21.1
  2) compiler/GCC/10.2.0
  3) toolchain/gcccuda/2020b
  4) lib/Check/0.15.2-GCCcore-10.2.0
  5) lib/GDRCopy/2.1-GCCcore-10.2.0-CUDA-11.1.1
  6) lib/UCX/1.9.0-GCCcore-10.2.0-CUDA-11.1.1
  7) lib/libfabric/1.11.0-GCCcore-10.2.0
  8) lib/PMIx/3.1.5-GCCcore-10.2.0-CUDA-11.1.1
  9) mpi/OpenMPI/4.0.5-gcccuda-2020b
 10) system/CUDA/11.4.2
 11) compiler/GCCcore/8.3.0
 12) compiler/PGI/20.4-GCC-8.3.0
 13) system/CUDAcore/11.2.2
 14) compiler/NVHPC/21.7
 15) numlib/imkl/2022.0.2


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
