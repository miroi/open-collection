# Set CUDA environment
export CUDA_HOME=/usr/lib/cuda
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

# Recompile for GPU
nequip-compile \
  /home/milias/.nequip/model_cache/cd7794ba9456e3aef505c69a7db8985d06641057c976c58f272c1107f37aaf77.nequip.zip \
  allegro_oam_l_gpu.nequip.pt2 \
  --mode aotinductor \
  --device cuda \
  --target ase
