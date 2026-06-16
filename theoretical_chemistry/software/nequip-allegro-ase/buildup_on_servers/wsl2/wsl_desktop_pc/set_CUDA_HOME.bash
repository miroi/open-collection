# Set CUDA_HOME to where Ubuntu installed CUDA
export CUDA_HOME=/usr/lib/cuda
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

# Verify it's set correctly
echo $CUDA_HOME
ls $CUDA_HOME
