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
O:1.05,Si:1.80,H:0.57,Ts:2.40

Ts:2.20 -> 2.50 -> 2.40 -> 2.30! -> 2.40

RKMax=3.0 because of H
GMAX = 20

