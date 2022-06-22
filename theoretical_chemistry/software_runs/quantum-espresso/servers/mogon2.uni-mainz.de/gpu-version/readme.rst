QE-devel with GPU
=================

Login onto GPU-node
-------------------
mirilias@login22.mogon:~/work/software/quantum_espresso/qe-devel/.srun --pty -p m2_gpu-compile -t 1:00:00  -A m2_jgu-gpu-qe-calcs bash -i

Loading necessary modules
-------------------------
mirilias@s0026.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.ml load devel/CMake/3.21.1 mpi/impi/2021.5.1-intel-compilers-2022.0.2  system/CUDA/11.4.2 compiler/PGI/20.4-GCC-8.3.0  compiler/NVHPC/21.7   numlib/imkl/2022.0.2

mirilias@s0014.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.ml

Currently Loaded Modules:
  1) numlib/imkl/2022.0.2
  2) devel/CMake/3.21.1
  3) system/CUDA/11.4.2
  4) compiler/PGI/20.4-GCC-8.3.0
  5) system/CUDAcore/11.2.2
  6) compiler/NVHPC/21.7
  7) compiler/GCCcore/11.2.0
  8) compiler/intel-compilers/2022.0.2
  9) lib/UCX/1.11.2-GCCcore-11.2.0
 10) mpi/impi/2021.5.1-intel-compilers-2022.0.2


see https://gitlab.com/QEF/q-e/-/issues/513#note_999729587

Buildup and compilations
------------------------
 mirilias@s0014.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.cmake -D QE_ENABLE_CUDA=ON -D QE_ENABLE_MPI_GPU_AWARE=ON -D CMAKE_Fortran_COMPILER=nvfortran -D CMAKE_C_COMPILER=nvc    ..


