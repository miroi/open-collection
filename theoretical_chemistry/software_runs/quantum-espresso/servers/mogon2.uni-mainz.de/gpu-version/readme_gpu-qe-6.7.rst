============================
GPU version of QE on MogonII
============================

module purge
module load system/CUDAcore/11.1.1
module load compiler/PGI
module load module load numlib/imkl



Test of loaded modules
-----------------------
mirilias@login22.mogon:~/work/software/quantum_espresso/q-e-gpu-qe-gpu-6.7/.pgf90 -V

pgf90 20.4-0 LLVM 64-bit target on x86-64 Linux -tp haswell 
PGI Compilers and Tools
Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.

mirilias@login23.mogon:~/work/software/quantum_espresso/q-e-gpu-qe-gpu-6.7/.echo $CUDA_HOME

/cluster/easybuild/broadwell/software/CUDAcore/11.1.1

mirilias@login23.mogon:~/work/software/quantum_espresso/q-e-gpu-qe-gpu-6.7/../configure --prefix=/home/mirilias/work/software/quantum_espresso/q-e-gpu-qe-gpu-6.7/bin --with-cuda=$CUDA_HOME --with-cuda-cc=60 --with-cuda-runtime=11.1 --enable-openmp ...

ERROR in configure - reported missing stuff

he logins still don't have GPUs hence there is no system CUDA driver lib. Try again in an interactive session in m2_gpu.
