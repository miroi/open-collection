=========================
LvO2@smalQ-G with wien2k
=========================

No ssh on lxir127
----------------
WIENROOT=/data.local1/milias/software/wien2k/WIEN2k_23.2/intel-openmpi_mkl

https://www.mail-archive.com/wien@zeus.theochem.tuwien.ac.at/msg22588.html
In $WIENROOT/WIEN2k_parallel_options : if ( ! $?USE_REMOTE ) setenv USE_REMOTE 0 

RMT
---
O  1.05
Si 1.49 ---> 1.80 due to charge leak
H  0.57
Lv 2.20

RKMax=3.0 because of H
GMAX = 20

