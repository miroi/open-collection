============================
GPU version of QE on MogonII
============================

module purge
module load system/CUDAcore/11.1.1
module load compiler/PGI


Test of loaded modules
-----------------------
mirilias@login22.mogon:~/work/software/quantum_espresso/q-e-gpu-qe-gpu-6.7/.pgf90 -V

pgf90 20.4-0 LLVM 64-bit target on x86-64 Linux -tp haswell 
PGI Compilers and Tools
Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.

mirilias@login23.mogon:~/work/software/quantum_espresso/q-e-gpu-qe-gpu-6.7/.echo $CUDA_HOME
/cluster/easybuild/broadwell/software/CUDAcore/11.1.1

mirilias@login23.mogon:~/work/software/quantum_espresso/q-e-gpu-qe-gpu-6.7/../configure --prefix=/home/mirilias/work/software/quantum_espresso/q-e-gpu-qe-gpu-6.7/bin 


GPU-QE 6.8
----------
mirilias@login22.mogon:~/work/software/quantum_espresso/.wget https://github.com/QEF/q-e/archive/refs/tags/qe-6.8.zip


Help:

This version requires the nvfortran (previously PGI) compiler from the
freely available NVidia HPC SDK. You are adviced to use a recent version
of NVidia software. Any version later than 17.4 should work, but many glitches
are know to exist in older versions.


