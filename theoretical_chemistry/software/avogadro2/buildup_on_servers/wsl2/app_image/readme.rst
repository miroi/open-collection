================
Run via AppImage
================

download
--------
https://github.com/OpenChemistry/avogadrolibs/releases/latest/download/Avogadro2-x86_64.AppImage

miroi@MIRO:~/work/software/avogadro2/.mv /mnt/c/Users/miroi/Downloads/Avogadro2-x86_64.AppImage .

miroi@MIRO:~/work/software/avogadro2/.ls -lt Avogadro2-x86_64.AppImage
-rwxrwxrwx 1 miroi miroi 112665792 Oct 23 22:45 Avogadro2-x86_64.AppImage*
miroi@MIRO:~/work/software/avogadro2/.ldd Avogadro2-x86_64.AppImage
        not a dynamic executable


run
---
chmod +x Avogadro2*.AppImage

miroi@MIRO:~/work/software/avogadro2/.source ~/work/software/myvenv/bin/activate
(myvenv) miroi@MIRO:~/work/software/avogadro2/../Avogadro2-x86_64.AppImage


check pip packages
~~~~~~~~~~~~~~~~~~
(myvenv) miroi@MIRO:~/.local/share/OpenChemistry/Avogadro/plugins/mace/.pip list
Package                Version    Editable project location
---------------------- ---------- ---------------------------------------------------------------
aimnet                 0.2.0
avogadro               2.1.0
avogadro-aimnet2       0.1.0      /home/miroi/.local/share/OpenChemistry/Avogadro/plugins/aimnet2
certifi                2026.10.23
charset-normalizer     3.5.2
click                  8.5.0
cuda-bindings          13.4.4
cuda-pathfinder        1.8.4
cuda-toolkit           13.0.3.0
filelock               4.2.4
fsspec                 2026.9.0
h5py                   3.16.0
idna                   3.20
Jinja2                 3.1.6
MarkupSafe             3.0.4
mpmath                 1.3.0
networkx               3.7
numpy                  2.5.4
nvalchemi-toolkit-ops  0.5.0
nvidia-cublas          13.1.1.3
nvidia-cuda-cupti      13.0.85
nvidia-cuda-nvrtc      13.0.88
nvidia-cuda-runtime    13.0.96
nvidia-cudnn-cu13      9.24.0.43
nvidia-cufft           12.0.0.61
nvidia-cufile          1.15.1.6
nvidia-curand          10.4.0.35
nvidia-cusolver        12.0.4.66
nvidia-cusparse        12.6.3.3
nvidia-cusparselt-cu13 0.8.1
nvidia-nccl-cu13       2.30.7
nvidia-nvjitlink       13.4.92
nvidia-nvshmem-cu13    3.4.5
nvidia-nvtx            13.0.85
pip                    24.0
PyYAML                 6.0.3
requests               2.34.2
setuptools             82.0.1
sympy                  1.14.0
torch                  2.14.1
triton                 3.8.0
typing_extensions      4.16.0
urllib3                2.8.0
warp-lang              1.18.0


