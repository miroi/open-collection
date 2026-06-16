==============
NequIP-Allegro
==============

installation
-------------

https://github.com/mir-group/allegro

(venv3) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/nequip-allegro-ase/buildup_on_servers/wsl2/wsl_notebookVictus/.pip install nequip-allegro

pip install nequip-allegro
.
.
Successfully installed MarkupSafe-3.0.3 aiohappyeyeballs-2.6.2 aiohttp-3.14.1 aiosignal-1.4.0 antlr4-python3-runtime-4.9.3 ase-3.28.0 attrs-26.1.0 certifi-2026.5.20 charset_normalizer-3.4.7 contourpy-1.3.3 cuda-bindings-13.3.1 cuda-pathfinder-1.5.5 cuda-toolkit-13.0.2 cycler-0.12.1 e3nn-0.6.0 filelock-3.29.4 fonttools-4.63.0 frozenlist-1.8.0 fsspec-2026.6.0 hydra-core-1.3.3 idna-3.18 jinja2-3.1.6 kiwisolver-1.5.0 lightning-2.6.5 lightning-utilities-0.15.3 lmdb-2.2.1 matplotlib-3.11.0 matscipy-1.2.0 mpmath-1.3.0 multidict-6.7.1 nequip-0.18.0 nequip-allegro-0.8.3 networkx-3.6.1 numpy-2.4.6 nvidia-cublas-13.1.1.3 nvidia-cuda-cupti-13.0.85 nvidia-cuda-nvrtc-13.0.88 nvidia-cuda-runtime-13.0.96 nvidia-cudnn-cu13-9.20.0.48 nvidia-cufft-12.0.0.61 nvidia-cufile-1.15.1.6 nvidia-curand-10.4.0.35 nvidia-cusolver-12.0.4.66 nvidia-cusparse-12.6.3.3 nvidia-cusparselt-cu13-0.8.1 nvidia-nccl-cu13-2.29.7 nvidia-nvjitlink-13.0.88 nvidia-nvshmem-cu13-3.4.5 nvidia-nvtx-13.0.85 omegaconf-2.3.1 opt-einsum-3.4.0 opt_einsum_fx-0.1.4 packaging-26.2 pillow-12.2.0 propcache-0.5.2 pyparsing-3.3.2 python-dateutil-2.9.0.post0 pytorch-lightning-2.6.5 pyyaml-6.0.3 requests-2.34.2 scipy-1.17.1 setuptools-81.0.0 six-1.17.0 sympy-1.14.0 torch-2.12.0 torchmetrics-1.9.0 tqdm-4.68.2 triton-3.7.0 typing-extensions-4.15.0 urllib3-2.7.0 yarl-1.24.2

problem
~~~~~~~
Your NVIDIA driver: 560.94 (supports CUDA 12.6)
Your PyTorch: 2.12.0+cu130 (compiled for CUDA 13.0)
The mismatch: PyTorch wants CUDA 13.0, but your driver only supports up to CUDA 12.6

pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

own CUDA installation
~~~~~~~~~~~~~~~~~~~~~

bash -f bash -f find_cuda_installation.bash

.bash -f set_CUDA_HOME.bash


obtain a model
--------------
nequip-compile   nequip.net:mir-group/Allegro-OAM-L:0.1   allegro_oam_l.nequip.pt2   --mode aotinductor   --device cuda    --target ase

nequip-compile \
  /home/milias/.nequip/model_cache/cd7794ba9456e3aef505c69a7db8985d06641057c976c58f272c1107f37aaf77.nequip.zip \
  allegro_oam_l.nequip.pt2 \
  --mode aotinductor \
  --device cuda \
  --target ase

.
.
.
[2026-06-16 14:54:50,096][nequip.scripts.compile][INFO] - [rank: 0] Exported model saved to allegro_oam_l.nequip.pt2

nequip-compile   /home/milias/.nequip/model_cache/cd7794ba9456e3aef505c69a7db8985d06641057c976c58f272c1107f37aaf77.nequip.zip   allegro_oam_l.nequip.pt2   --mode aotinductor   --device cpu   --target ase
[2026-06-16 15:06:59,961][nequip.scripts.compile][INFO] - [rank: 0] Exported model saved to allegro_oam_l.nequip.pt2

(venv3) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/nequip-allegro-ase/buildup_on_servers/wsl2/wsl_desktop_pc/.ls -lt allegro_oam_l.nequip.pt2
-rw-r--r-- 1 milias milias 40933380 Jun 16 15:06 allegro_oam_l.nequip.pt2

test run
--------
python test_nequip_cpu.py  > test_nequip_cpu.py_logfile

recompile for GPU
-----------------
(venv3) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/nequip-allegro-ase/buildup_on_servers/wsl2/wsl_desktop_pc/.bash -f recompile_for_gpu.bash
.
.
[2026-06-16 15:20:12,158][nequip.scripts.compile][INFO] - [rank: 0] Exported model saved to allegro_oam_l_gpu.nequip.pt2

(venv3) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/nequip-allegro-ase/buildup_on_servers/wsl2/wsl_desktop_pc/.python test_nequip_gpu.py  > test_nequip_gpu.py_logfile

benchmarking
------------
python benchmark_speed.py > benchmark_speed.py_logfile

recompile GPU with higher precision

# Recompile with double precision and no optimization
nequip-compile \
  /home/milias/.nequip/model_cache/cd7794ba9456e3aef505c69a7db8985d06641057c976c58f272c1107f37aaf77.nequip.zip \
  allegro_oam_l_gpu_precise.nequip.pt2 \
  --mode aotinductor \
  --device cuda \
  --target ase \
  --inductor-configs "max_autotune=False" "epilogue_fusion=False"
.
.
[2026-06-16 15:43:18,257][nequip.scripts.compile][INFO] - [rank: 0] Exported model saved to allegro_oam_l_gpu_precise.nequip.pt2

info on packages
-----------------
python packages_info_simpler.py > packages_info_simpler.py_logfile



summary of compiled models
--------------------------
(venv3) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/nequip-allegro-ase/buildup_on_servers/wsl2/wsl_desktop_pc/.ls -lt allegro_oam_l*
-rw-r--r-- 1 milias milias 41647563 Jun 16 15:43 allegro_oam_l_gpu_precise.nequip.pt2
-rw-r--r-- 1 milias milias 41631759 Jun 16 15:20 allegro_oam_l_gpu.nequip.pt2
-rw-r--r-- 1 milias milias 40933380 Jun 16 15:06 allegro_oam_l.nequip.pt2


Application - surface energy
============================

python surface_energy_working.py > surface_energy_working.py_logfile

