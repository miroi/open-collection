============================
GPU version of QE on MogonII
============================

module purge
#module load system/CUDAcore/11.1.1
#module load compiler/PGI
module load compiler/NVHPC/21.7

mirilias@login22.mogon:~/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8/.module list

Currently Loaded Modules:
  1) system/CUDAcore/11.2.2   2) compiler/NVHPC/21.7


mirilias@login22.mogon:~/work/software/quantum_espresso/.wget https://github.com/QEF/q-e/archive/refs/tags/qe-6.8.zip
/home/mirilias/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8

Test of loaded modules
----------------------
mirilias@login22.mogon:~/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8/.echo $CUDA_HOME
/cluster/easybuild/broadwell/software/CUDAcore/11.2.2

mirilias@login22.mogon:~/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8/.echo $LD_LIBRARY_PATH
/cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib:/cluster/easybuild/broadwell/software/CUDAcore/11.2.2/nvvm/lib64:/cluster/easybuild/broadwell/software/CUDAcore/11.2.2/extras/CUPTI/lib64:/cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib

Configure 
---------
mirilias@login22.mogon:~/work/software/quantum_espresso/gpu-qe-6.8/q-e-qe-6.8/../configure --prefix=$PWD --with-cuda=$CUDA_HOME  --with-cuda-runtime=YY --with-cuda-cc=ZZ --enable-openmp




