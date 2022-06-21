QE-devel with GPU
=================

mirilias@login22.mogon:~/work/software/quantum_espresso/qe-devel/.srun --pty -p m2_gpu-compile -t 1:00:00  -A m2_jgu-gpu-qe-calcs bash -i

mirilias@s0021.mogon:~/work/software/quantum_espresso/qe-devel/.ml load numlib/imkl/2019.3.199-iimpi-2019.03 system/CUDA/10.1.243-GCC-8.3.0 devel/CMake/3.21.1  compiler/NVHPC/22.2
mirilias@s0021.mogon:~/work/software/quantum_espresso/qe-devel/.ml list


mirilias@s0021.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.nvfortran --version

nvfortran 22.2-0 64-bit target on x86-64 Linux -tp haswell
NVIDIA Compilers and Tools
Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
mirilias@s0021.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Sun_Jul_28_19:07:16_PDT_2019
Cuda compilation tools, release 10.1, V10.1.243




