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


Files
-----
milias@lxir127.gsi.de:/data.local1/milias/scratch/wien2k.3f176.14429/LvO2onQg/.grep ':ENE' *.out*
LvO2onQg.outputm::ENE  : *INFO***** TOTAL ENERGY IN Ry =      -107975.06039312

milias@lxir127.gsi.de:/data.local1/milias/scratch/wien2k.3f176.14429/LvO2onQg/.ls -lt *.error
-rw-r--r-- 1 milias ukt 0 Jun 29 03:00 mixer.error
-rw-r--r-- 1 milias ukt 0 Jun 29 02:59 lcore.error
-rw-r--r-- 1 milias ukt 0 Jun 29 02:59 lapw2.error
-rw-r--r-- 1 milias ukt 0 Jun 29 02:59 sumpara.error
-rw-r--r-- 1 milias ukt 0 Jun 29 02:59 lapw2_1.error
-rw-r--r-- 1 milias ukt 0 Jun 29 02:59 lapw1.error
-rw-r--r-- 1 milias ukt 0 Jun 29 02:59 lapw1_1.error
-rw-r--r-- 1 milias ukt 0 Jun 29 02:49 lapw0.error
-rw-r--r-- 1 milias ukt 0 Jun 28 22:44 dstart.error


other:
milias@lxir127.gsi.de:/data.local1/milias/scratch/wien2k.cfc0c.5120/LvO2onQg/.grep ':ENE' *.out*
LvO2onQg.outputm::ENE  : ********** TOTAL ENERGY IN Ry =      -107975.12292269


