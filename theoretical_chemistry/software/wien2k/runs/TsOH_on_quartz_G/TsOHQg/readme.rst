=========================
LvO2@smalQ-G with wien2k
=========================

https://www.mail-archive.com/wien@zeus.theochem.tuwien.ac.at/msg22588.html
In $WIENROOT/WIEN2k_parallel_options : if ( ! $?USE_REMOTE ) setenv USE_REMOTE 0 

RMT
---
O:1.05,Si:1.80,H:0.57,Ts:2.40

Ts:2.20 -> 2.50 -> 2.40 -> 2.30! -> 2.40

RKMax=3.0 because of H
GMAX = 20

k points: 1 1 1 

less TsOHQg.output1_1
 MPI-parallel calculation using    24 processors
 Scalapack processors array (row,col):   6   4
 Matrix size       111610  <------- too big !!!!
see also https://www.mail-archive.com/wien@zeus.theochem.tuwien.ac.at/msg22632.html

for size 110000 .... 110000*110000*8)/(1024*1024*1024) ... cca 90.15 GB


