==============================
CPU-QE on Govorun JINR cluster
==============================

wget https://github.com/QEF/q-e/archive/refs/tags/qe-6.8.zip

milias@hydra.jinr.ru:~/work/software/quantum-espresso/q-e-qe-6.8/.module list
Currently Loaded Modulefiles:
  1) intel/v2021.1   2) BASE/1.0        3) GVR/v1.0-1      4) Python/v3.6.5

milias@hydra.jinr.ru:~/work/software/quantum-espresso/q-e-qe-6.8/../configure --enable-parallel --enable-openmp --prefix=/zfs/hybrilit.jinr.ru/user/m/milias/work/software/quantum-espresso/q-e-qe-6.8/bin

milias@hydra.jinr.ru:~/work/software/quantum-espresso/q-e-qe-6.8/.module list
Currently Loaded Modulefiles:
  1) intel/v2021.1                           4) Python/v3.6.5
  2) BASE/1.0                                5) intel/v2018.1.163-9
  3) GVR/v1.0-1                              6) ELPA/v2020.05.001_intel2018_python365

milias@hydra.jinr.ru:~/work/software/quantum-espresso/q-e-qe-6.8/../configure --enable-parallel --enable-openmp --prefix=/zfs/hybrilit.jinr.ru/user/m/milias/work/software/quantum-espresso/q-e-qe-6.8/bin
.
.
.
Quantum ESPRESSO binaries are installed in /zfs/hybrilit.jinr.ru/user/m/milias/work/software/quantum-espresso/q-e-qe-6.8/bin/bin


