Wien2k_21.1 on virgo cluster
============================

milias@lxbk0599.gsi.de:/lustre/ukt/milias/work/software/wien2k/WIEN2k_21.1/.gunzip *

Modules
-------
https://git.gsi.de/SDEGroup/SIR/-/issues/57
https://git.gsi.de/SDEGroup/SIR/-/issues/58

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack find | grep intel
intel-parallel-studio@professional.2020.1
intel-mkl@2019.1.144
intel-mkl@2020.4.304
-- linux-debian10-x86_64 / intel@19.1.1.217 ---------------------


spack load intel-parallel-studio@professional.2020.1

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack load amdfftw@3.0 target=$(spack arch -t)


milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.spack find --loaded
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
intel-parallel-studio@professional.2020.1  patchelf@0.16.1
==> 2 loaded packages

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.gunzip *

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/wien2k/Wien2k_23.2/.expand_lapw
.
.
case.win   linked to   template.win
python found at /usr/bin/python.

WIEN is now expanded. The shell-script commands were copied and links created.
To configure your Fortran-executables run:

./siteconfig_lapw


