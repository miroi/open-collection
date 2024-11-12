=======
NequIP 
=======

Euclidian Equivariant neural network potentials. 

Nequip can fit neural network potentials to series of DFT calculations (using e.g. ASE trajectory files),
 and then be used to perform optimization and molecular dynamics in ASE or LAMMPS.

https://github.com/mir-group/nequip


paper
https://www.nature.com/articles/s41467-022-29939-5


installation
~~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/nequip/buildup_on_servers/wsl_desktop_pc/.pip install torch
.
.
.
Successfully installed filelock-3.16.1 fsspec-2024.10.0 mpmath-1.3.0 networkx-3.4.2 nvidia-cublas-cu12-12.4.5.8 nvidia-cuda-cupti-cu12-12.4.127 nvidia-cuda-nvrtc-cu12-12.4.127 nvidia-cuda-runtime-cu12-12.4.127 nvidia-cudnn-cu12-9.1.0.70 nvidia-cufft-cu12-11.2.1.3 nvidia-curand-cu12-10.3.5.147 nvidia-cusolver-cu12-11.6.1.9 nvidia-cusparse-cu12-12.3.1.170 nvidia-nccl-cu12-2.21.5 nvidia-nvjitlink-cu12-12.4.127 nvidia-nvtx-cu12-12.4.127 sympy-1.13.1 torch-2.5.1 triton-3.1.0

pip uninstall torch

pip install torch==1.13.*

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/nequip/buildup_on_servers/wsl_desktop_pc/.pip install nequip
.
.
Installing collected packages: tqdm, torch-runstats, torch-ema, opt-einsum-fx, e3nn, nequip
Successfully installed e3nn-0.5.4 nequip-0.6.1 opt-einsum-fx-0.1.4 torch-ema-0.3 torch-runstats-0.2.0 tqdm-4.67.0

pip uninstall nequip


milias@DESKTOP-7OTLCGO:~/work/software/.git clone https://github.com/mir-group/nequip.git
cd nequip
pip install . 


