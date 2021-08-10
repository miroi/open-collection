GPU version of QE on MogonII
============================

module purge
module load system/CUDAcore/11.1.1
module load compiler/PGI


mirilias@login23.mogon:~/work/software/quantum_espresso/q-e-gpu-qe-gpu-6.7/.echo $CUDA_HOME
/cluster/easybuild/broadwell/software/CUDAcore/11.1.1

./configure --prefix=/home/mirilias/work/software/quantum_espresso/q-e-gpu-qe-gpu-6.7/bin 




