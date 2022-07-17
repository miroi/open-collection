Wien2k_21.1 on virgo cluster
============================

milias@lxbk0599.gsi.de:/lustre/ukt/milias/work/software/wien2k/WIEN2k_21.1/.gunzip *

Modules
-------
milias@lxbk0599.gsi.de:/lustre/ukt/milias/work/software/wien2k/WIEN2k_21.1/.spack find | grep intel
intel-mkl@2019.1.144
intel-mkl@2020.4.304
intel-parallel-studio@professional.2020.1
milias@lxbk0599.gsi.de:/lustre/ukt/milias/work/software/wien2k/WIEN2k_21.1/.spack load intel-mkl@2020.4.304 target=$(spack arch -t)
==> Error: Spec 'intel-mkl@2020.4.304 arch=linux-None-zen' matches no installed packages.


https://git.gsi.de/SDEGroup/SIR/-/issues/57


