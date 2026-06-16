# Find the real location of nvcc
readlink -f /usr/bin/nvcc

# Or check where the CUDA include files are
find /usr -name "cuda.h" 2>/dev/null

# Check if CUDA is installed via apt
dpkg -l | grep cuda

# Check all possible CUDA locations
find /usr -type d -name "cuda*" 2>/dev/null
